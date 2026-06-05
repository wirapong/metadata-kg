"""Multi-model × multi-run evaluation with CI (Option B).

Runs 3 models × N runs × 120 docs:
  - Claude Sonnet 4
  - Claude Opus 4
  - GPT-4o

Reports mean ± stdev ± 95% bootstrap CI per (model, field).
Outputs:
  - evaluation/results_multi_ci.json
  - evaluation/figures/fig_multi_ci.png
  - evaluation/RESULTS_MULTI_CI.md
"""
from __future__ import annotations
import json, os, statistics, sys, time
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).parent.parent))
try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).parent.parent / ".env")
except ImportError:
    pass

from evaluation.eval_dataset_v2 import EXTRACTION_GOLD_V2
from evaluation.run_evaluation_llm import LLM_PROMPT_TEMPLATE
from metadata_kg.core.llm_agent import deterministic_extract_entities

OUT = Path(__file__).parent
FIG = OUT / "figures"
FIG.mkdir(exist_ok=True)
N_RUNS = int(sys.argv[1]) if len(sys.argv) > 1 else 3

MODELS = [
    {"name": "Claude Sonnet 4", "provider": "anthropic", "model_id": "claude-sonnet-4-20250514"},
    {"name": "Claude Opus 4",   "provider": "anthropic", "model_id": "claude-opus-4-20250514"},
    {"name": "GPT-4o",          "provider": "openai",    "model_id": "gpt-4o"},
]


def parse_json(raw: str) -> dict:
    raw = raw.strip()
    if raw.startswith("```"):
        raw = raw.split("```", 2)[1]
        if raw.startswith("json"): raw = raw[4:]
        raw = raw.strip("` \n")
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        s, e = raw.find("{"), raw.rfind("}")
        if s >= 0 and e > s: return json.loads(raw[s:e+1])
        raise


def call_model(model: dict, prompt: str) -> str:
    if model["provider"] == "anthropic":
        from langchain_anthropic import ChatAnthropic
        llm = ChatAnthropic(model=model["model_id"], api_key=os.getenv("ANTHROPIC_API_KEY"),
                            temperature=0.1, max_tokens=600)
        return llm.invoke(prompt).content
    elif model["provider"] == "openai":
        from openai import OpenAI
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        r = client.chat.completions.create(
            model=model["model_id"], temperature=0.1, max_tokens=600,
            messages=[{"role": "user", "content": prompt}])
        return r.choices[0].message.content


def evaluate_run(model: dict, gold: list[dict]) -> dict:
    counts = {"title": [0, 0], "type": [0, 0], "domain": [0, 0]}
    failures = 0
    latencies = []
    quota_dead = False
    for i, case in enumerate(gold, 1):
        if quota_dead:
            failures += 1
            continue
        try:
            t0 = time.perf_counter()
            raw = call_model(model, LLM_PROMPT_TEMPLATE.format(text=case["text"]))
            latencies.append(time.perf_counter() - t0)
            out = parse_json(raw)
        except Exception as exc:
            failures += 1
            es = str(exc)[:200]
            if "quota" in es.lower() or "429" in es or "insufficient" in es.lower():
                print(f"  [{i:3d}/{len(gold)}] QUOTA DEAD — aborting")
                quota_dead = True
            continue
        exp = case["expected"]
        title_ok = exp["title"].lower() in str(out.get("title", "")).lower()
        type_ok = out.get("type", "").lower() == exp["type"].lower() or (
            out.get("type", "") == "Dataset" and exp["type"] == "Dataset")
        domain_ok = out.get("domain", "").lower() == exp["domain"].lower()
        for f, ok in [("title", title_ok), ("type", type_ok), ("domain", domain_ok)]:
            if ok: counts[f][0] += 1
            else: counts[f][1] += 1
        if i % 30 == 0:
            print(f"  [{i:3d}/{len(gold)}] avg {statistics.fmean(latencies):.2f}s/doc")
    def f1(c): return 2*c[0] / (2*c[0] + c[1]) if (2*c[0] + c[1]) else 0.0
    return {
        "f1": {f: f1(c) for f, c in counts.items()},
        "counts": counts,
        "failures": failures,
        "latency_mean": statistics.fmean(latencies) if latencies else 0.0,
    }


def floor_baseline() -> dict:
    counts = {"title": [0, 0], "type": [0, 0], "domain": [0, 0]}
    for case in EXTRACTION_GOLD_V2:
        ents = deterministic_extract_entities(case["text"])
        title = ents[0].properties.get("dct:title", "") if ents else ""
        type_ = ents[0].type if ents else ""
        exp = case["expected"]
        if exp["title"].lower() in str(title).lower(): counts["title"][0] += 1
        else: counts["title"][1] += 1
        if exp["type"] in type_ or "Dataset" in type_: counts["type"][0] += 1
        else: counts["type"][1] += 1
        counts["domain"][1] += 1
    def f1(c): return 2*c[0] / (2*c[0] + c[1]) if (2*c[0] + c[1]) else 0.0
    return {f: f1(c) for f, c in counts.items()}


def aggregate(runs: list[dict]) -> dict:
    fields = ["title", "type", "domain"]
    agg = {}
    rng = np.random.default_rng(42)
    for f in fields:
        vals = [r["f1"][f] for r in runs]
        m = statistics.fmean(vals)
        s = statistics.pstdev(vals) if len(vals) > 1 else 0.0
        boot = [np.mean(rng.choice(vals, size=len(vals), replace=True)) for _ in range(1000)]
        agg[f] = {
            "mean": m, "stdev": s,
            "ci_low": float(np.percentile(boot, 2.5)),
            "ci_high": float(np.percentile(boot, 97.5)),
            "raw": vals,
        }
    return agg


def main():
    print(f"=== Multi-model × {N_RUNS}-run CI evaluation ===")
    print(f"Gold set: {len(EXTRACTION_GOLD_V2)} docs (v2)\n")
    print("Floor baseline (1 pass):")
    floor = floor_baseline()
    for f, v in floor.items(): print(f"  {f:10s} F1 = {v:.3f}")

    report = {
        "n_runs": N_RUNS, "gold_size": len(EXTRACTION_GOLD_V2),
        "floor": floor, "models": {},
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S %Z"),
    }
    for m in MODELS:
        env_key = "ANTHROPIC_API_KEY" if m["provider"] == "anthropic" else "OPENAI_API_KEY"
        if not os.getenv(env_key):
            print(f"\n⊘ Skipping {m['name']}: {env_key} not set")
            continue
        print(f"\n=== {m['name']} ({m['model_id']}) — {N_RUNS} runs ===")
        runs = []
        for r in range(1, N_RUNS + 1):
            print(f"\nRun {r}/{N_RUNS}:")
            t0 = time.perf_counter()
            res = evaluate_run(m, EXTRACTION_GOLD_V2)
            wall = time.perf_counter() - t0
            print(f"  → title={res['f1']['title']:.3f}  type={res['f1']['type']:.3f}  domain={res['f1']['domain']:.3f}  failures={res['failures']}  wall={wall:.0f}s")
            runs.append(res)
        agg = aggregate(runs)
        report["models"][m["name"]] = {
            "model_id": m["model_id"], "provider": m["provider"],
            "runs": runs, "aggregate": agg,
        }
        print(f"\n  Aggregate (n={N_RUNS}):")
        for f, st in agg.items():
            print(f"    {f:10s} mean={st['mean']:.3f} ±{st['stdev']:.3f}  95%CI=[{st['ci_low']:.3f}, {st['ci_high']:.3f}]")
        out = OUT / "results_multi_ci.json"
        out.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
        print(f"  ✓ Intermediate save: {out}")

    # Final plot
    plot(report)
    write_md(report)
    print(f"\n✓ Done — wrote {OUT}/results_multi_ci.json")


def plot(report):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError: return
    models = ["Floor"] + list(report["models"].keys())
    fields = ["title", "type", "domain"]
    means = {f: [report["floor"][f]] + [report["models"][m]["aggregate"][f]["mean"] for m in report["models"]] for f in fields}
    err_lo = {f: [0] + [report["models"][m]["aggregate"][f]["mean"] - report["models"][m]["aggregate"][f]["ci_low"] for m in report["models"]] for f in fields}
    err_hi = {f: [0] + [report["models"][m]["aggregate"][f]["ci_high"] - report["models"][m]["aggregate"][f]["mean"] for m in report["models"]] for f in fields}

    x = np.arange(len(models))
    w = 0.27
    fig, ax = plt.subplots(figsize=(11, 5.5))
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]
    for i, f in enumerate(fields):
        ax.bar(x + (i-1)*w, means[f], w, label=f"{f} F1", color=colors[i],
               yerr=[err_lo[f], err_hi[f]], capsize=4, error_kw={"color": "black", "lw": 1})
        for j, v in enumerate(means[f]):
            ax.text(x[j] + (i-1)*w, v + 0.04, f"{v:.3f}", ha="center", fontsize=8, weight="bold" if i==2 else "normal")
    ax.set_xticks(x); ax.set_xticklabels(models, rotation=10, ha="right")
    ax.set_ylim(0, 1.15); ax.set_ylabel("F1")
    ax.set_title(f"Multi-model extraction × {report['n_runs']} runs (n={report['gold_size']} docs, error bars = 95% CI)")
    ax.legend(loc="lower right"); ax.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    out = FIG / "fig_multi_ci.png"
    plt.savefig(out, dpi=130)
    plt.close()
    print(f"  ✓ Plot: {out}")


def write_md(report):
    md = ["# Multi-model CI evaluation results", ""]
    md.append(f"_Generated:_ {report['timestamp']}  ·  _Runs per model:_ {report['n_runs']}  ·  _Gold:_ {report['gold_size']} docs\n")
    md.append("## Mean F1 (with 95% bootstrap CI from N runs)\n")
    md.append("| Model | Title F1 (95% CI) | Type F1 (95% CI) | Domain F1 (95% CI) |")
    md.append("|-------|------------------:|----------------:|------------------:|")
    md.append(f"| Floor (deterministic) | {report['floor']['title']:.3f} | {report['floor']['type']:.3f} | {report['floor']['domain']:.3f} |")
    for name, data in report["models"].items():
        a = data["aggregate"]
        def s(f): return f"{a[f]['mean']:.3f} ({a[f]['ci_low']:.3f}–{a[f]['ci_high']:.3f})"
        md.append(f"| {name} | {s('title')} | {s('type')} | {s('domain')} |")
    OUT_MD = OUT / "RESULTS_MULTI_CI.md"
    OUT_MD.write_text("\n".join(md), encoding="utf-8")
    print(f"  ✓ Markdown: {OUT_MD}")


if __name__ == "__main__":
    main()
