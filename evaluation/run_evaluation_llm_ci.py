"""Multi-run LLM evaluation with confidence intervals.

Runs the LLM ceiling evaluation N times on the 120-doc gold set v2,
reports mean ± stdev ± 95% bootstrap CI per metric.

Usage:
    PYTHONPATH=. .venv/bin/python evaluation/run_evaluation_llm_ci.py [N_RUNS]

Default N_RUNS = 3.
"""

from __future__ import annotations

import json
import os
import statistics
import sys
import time
from pathlib import Path
from typing import Any

import numpy as np

sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).parent.parent / ".env")
except ImportError:
    pass

from evaluation.eval_dataset_v2 import EXTRACTION_GOLD_V2
from evaluation.run_evaluation_llm import LLM_PROMPT_TEMPLATE, llm_extract_one
from metadata_kg.core.llm_agent import deterministic_extract_entities

OUT = Path(__file__).parent
FIG = OUT / "figures"
FIG.mkdir(exist_ok=True)


def prf(tp: int, fp: int, fn: int) -> tuple[float, float, float]:
    p = tp / (tp + fp) if (tp + fp) else 0.0
    r = tp / (tp + fn) if (tp + fn) else 0.0
    f1 = 2 * p * r / (p + r) if (p + r) else 0.0
    return p, r, f1


def evaluate_run(llm: Any, gold: list[dict]) -> dict:
    """Run a single evaluation pass on the gold set."""
    counts = {"title": [0, 0], "type": [0, 0], "domain": [0, 0]}
    extras = {"license_extracted": 0, "publisher_extracted": 0, "language_extracted": 0, "keyword_count_sum": 0}
    failures = 0
    latencies = []

    for i, case in enumerate(gold, 1):
        try:
            t0 = time.perf_counter()
            out = llm_extract_one(llm, case["text"])
            latencies.append(time.perf_counter() - t0)
        except Exception as exc:
            failures += 1
            print(f"  [{i:3d}/{len(gold)}] FAIL: {str(exc)[:80]}")
            continue

        exp = case["expected"]
        title_ok = exp["title"].lower() in str(out.get("title", "")).lower()
        type_ok = out.get("type", "").lower() == exp["type"].lower() or (
            out.get("type", "") == "Dataset" and exp["type"] == "Dataset"
        )
        domain_ok = out.get("domain", "").lower() == exp["domain"].lower()

        for f, ok in [("title", title_ok), ("type", type_ok), ("domain", domain_ok)]:
            if ok: counts[f][0] += 1
            else: counts[f][1] += 1

        if out.get("license"): extras["license_extracted"] += 1
        if out.get("publisher"): extras["publisher_extracted"] += 1
        if out.get("language"): extras["language_extracted"] += 1
        if isinstance(out.get("keywords"), list): extras["keyword_count_sum"] += len(out["keywords"])

        if i % 20 == 0:
            avg_lat = sum(latencies) / max(len(latencies), 1)
            print(f"  [{i:3d}/{len(gold)}] running... (avg {avg_lat:.2f}s/doc)")

    return {
        "counts": counts,
        "f1": {f: prf(c[0], 0, c[1])[2] for f, c in counts.items()},
        "extras": extras,
        "failures": failures,
        "latency_mean": statistics.fmean(latencies) if latencies else 0.0,
        "latency_p95": float(np.percentile(latencies, 95)) if latencies else 0.0,
        "total_time": sum(latencies),
    }


def deterministic_baseline(gold: list[dict]) -> dict:
    """Deterministic floor evaluation (no API)."""
    counts = {"title": [0, 0], "type": [0, 0], "domain": [0, 0]}
    for case in gold:
        ents = deterministic_extract_entities(case["text"])
        title = ents[0].properties.get("dct:title", "") if ents else ""
        type_ = ents[0].type if ents else ""
        exp = case["expected"]
        if exp["title"].lower() in str(title).lower(): counts["title"][0] += 1
        else: counts["title"][1] += 1
        if exp["type"] in type_ or "Dataset" in type_: counts["type"][0] += 1
        else: counts["type"][1] += 1
        counts["domain"][1] += 1  # deterministic never produces domain
    return {"f1": {f: prf(c[0], 0, c[1])[2] for f, c in counts.items()}}


def aggregate(runs: list[dict]) -> dict:
    """Compute mean, stdev, 95% bootstrap CI across runs."""
    agg = {"per_field": {}}
    fields = list(runs[0]["f1"].keys())
    for f in fields:
        vals = [r["f1"][f] for r in runs]
        mean = statistics.fmean(vals)
        stdev = statistics.pstdev(vals) if len(vals) > 1 else 0.0
        # Bootstrap 95% CI
        boot = []
        rng = np.random.default_rng(42)
        for _ in range(1000):
            sample = rng.choice(vals, size=len(vals), replace=True)
            boot.append(np.mean(sample))
        ci_lo = float(np.percentile(boot, 2.5))
        ci_hi = float(np.percentile(boot, 97.5))
        agg["per_field"][f] = {
            "mean": mean, "stdev": stdev,
            "ci_95_low": ci_lo, "ci_95_high": ci_hi,
            "raw": vals,
        }

    agg["latency_mean_across_runs"] = statistics.fmean(r["latency_mean"] for r in runs)
    agg["failures_total"] = sum(r["failures"] for r in runs)
    return agg


def main(n_runs: int = 3) -> None:
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("✗ ANTHROPIC_API_KEY not set in .env")
        sys.exit(1)

    from langchain_anthropic import ChatAnthropic
    model = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-20250514")
    llm = ChatAnthropic(
        model=model,
        api_key=os.getenv("ANTHROPIC_API_KEY"),
        temperature=0.1,
        max_tokens=600,
    )
    print(f"✓ LLM mode: model={model}")
    print(f"✓ Gold set: {len(EXTRACTION_GOLD_V2)} docs (v2)")
    print(f"✓ Runs: {n_runs}\n")

    # Floor
    print("=== Floor (deterministic, 1 pass) ===")
    floor = deterministic_baseline(EXTRACTION_GOLD_V2)
    for f, v in floor["f1"].items():
        print(f"  {f:10s}  F1 = {v:.3f}")

    # Ceiling × N runs
    runs = []
    for r in range(1, n_runs + 1):
        print(f"\n=== Ceiling Run {r}/{n_runs} ===")
        run_result = evaluate_run(llm, EXTRACTION_GOLD_V2)
        runs.append(run_result)
        print(f"  Run {r} F1: title={run_result['f1']['title']:.3f}  type={run_result['f1']['type']:.3f}  domain={run_result['f1']['domain']:.3f}")
        print(f"  Failures: {run_result['failures']}  Avg latency: {run_result['latency_mean']:.2f}s")

    # Aggregate
    agg = aggregate(runs)
    print("\n=== Aggregate (across runs) ===")
    print(f"  Field       Mean F1     ± Stdev    95% CI")
    for f, stats_ in agg["per_field"].items():
        print(f"  {f:10s}  {stats_['mean']:.3f}     ± {stats_['stdev']:.3f}    [{stats_['ci_95_low']:.3f}, {stats_['ci_95_high']:.3f}]")

    # Save
    report = {
        "n_runs": n_runs,
        "gold_size": len(EXTRACTION_GOLD_V2),
        "model": model,
        "floor": floor,
        "runs": runs,
        "aggregate": agg,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S %Z"),
    }
    out = OUT / "results_llm_ci.json"
    out.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
    print(f"\n✓ Wrote {out}")

    # Plot
    _plot_ci(floor, agg)


def _plot_ci(floor: dict, agg: dict) -> None:
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        return
    fields = ["title", "type", "domain"]
    floor_f1 = [floor["f1"][f] for f in fields]
    mean_f1 = [agg["per_field"][f]["mean"] for f in fields]
    err_low = [agg["per_field"][f]["mean"] - agg["per_field"][f]["ci_95_low"] for f in fields]
    err_high = [agg["per_field"][f]["ci_95_high"] - agg["per_field"][f]["mean"] for f in fields]

    x = np.arange(len(fields))
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.bar(x - 0.2, floor_f1, 0.4, label="Floor (deterministic)", color="#7e7e7e")
    ax.bar(x + 0.2, mean_f1, 0.4, label="Ceiling (LLM, mean)", color="#1f77b4",
           yerr=[err_low, err_high], capsize=5, error_kw={"color": "black"})
    ax.set_xticks(x); ax.set_xticklabels(fields)
    ax.set_ylim(0, 1.1); ax.set_ylabel("F1")
    ax.set_title(f"E1 Extraction (n={agg.get('runs_n', 'N')} runs, gold=120, error bars = 95% CI)")
    for i, (a, b) in enumerate(zip(floor_f1, mean_f1)):
        ax.text(i - 0.2, a + 0.02, f"{a:.2f}", ha="center", fontsize=9)
        ax.text(i + 0.2, b + 0.04, f"{b:.2f}", ha="center", fontsize=9, weight="bold")
    ax.legend(loc="lower right"); ax.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    out = FIG / "fig_e1_ci.png"
    plt.savefig(out, dpi=130)
    plt.close()
    print(f"✓ Saved {out}")


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    main(n)
