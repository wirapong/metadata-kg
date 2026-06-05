"""Multi-model extraction comparison on gold set v2 (120 docs).

Compares:
- Deterministic floor (no API)
- Claude Sonnet 4 (Anthropic)
- Claude Opus 4 (Anthropic)
- GPT-5.4 / GPT-4o (OpenAI, optional)

Usage:
    .venv/bin/pip install openai  # if not installed
    PYTHONPATH=. .venv/bin/python evaluation/run_evaluation_multi_model.py

Expects in .env:
    ANTHROPIC_API_KEY=...
    OPENAI_API_KEY=...      # optional
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
from evaluation.run_evaluation_llm import LLM_PROMPT_TEMPLATE
from metadata_kg.core.llm_agent import deterministic_extract_entities

OUT = Path(__file__).parent
FIG = OUT / "figures"
FIG.mkdir(exist_ok=True)


# Model registry
MODELS = [
    {"name": "Claude Sonnet 4", "provider": "anthropic", "model_id": "claude-sonnet-4-20250514"},
    {"name": "Claude Opus 4", "provider": "anthropic", "model_id": "claude-opus-4-20250514"},
    {"name": "GPT-4o", "provider": "openai", "model_id": "gpt-4o"},
]


def _call_anthropic(prompt: str, model_id: str, api_key: str) -> str:
    from langchain_anthropic import ChatAnthropic
    llm = ChatAnthropic(model=model_id, api_key=api_key, temperature=0.1, max_tokens=600)
    return llm.invoke(prompt).content


def _call_openai(prompt: str, model_id: str, api_key: str) -> str:
    try:
        from openai import OpenAI
    except ImportError:
        raise RuntimeError("openai SDK not installed: pip install openai")
    client = OpenAI(api_key=api_key)
    resp = client.chat.completions.create(
        model=model_id,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1,
        max_tokens=600,
    )
    return resp.choices[0].message.content


def _parse_json(raw: str) -> dict:
    raw = raw.strip()
    if raw.startswith("```"):
        raw = raw.split("```", 2)[1]
        if raw.startswith("json"):
            raw = raw[4:]
        raw = raw.strip("` \n")
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        s, e = raw.find("{"), raw.rfind("}")
        if s >= 0 and e > s:
            return json.loads(raw[s:e+1])
        raise


def extract_one(model: dict, text: str) -> tuple[dict, float]:
    prompt = LLM_PROMPT_TEMPLATE.format(text=text)
    t0 = time.perf_counter()
    if model["provider"] == "anthropic":
        api_key = os.getenv("ANTHROPIC_API_KEY")
        raw = _call_anthropic(prompt, model["model_id"], api_key)
    elif model["provider"] == "openai":
        api_key = os.getenv("OPENAI_API_KEY")
        raw = _call_openai(prompt, model["model_id"], api_key)
    else:
        raise ValueError(f"Unknown provider: {model['provider']}")
    latency = time.perf_counter() - t0
    return _parse_json(raw), latency


def evaluate_model(model: dict, gold: list[dict]) -> dict:
    """Evaluate one model on the gold set."""
    api_env = "ANTHROPIC_API_KEY" if model["provider"] == "anthropic" else "OPENAI_API_KEY"
    if not os.getenv(api_env):
        print(f"  ⊘ Skipping {model['name']}: {api_env} not set")
        return {"skipped": True, "reason": f"{api_env} missing"}

    counts = {"title": [0, 0], "type": [0, 0], "domain": [0, 0]}
    extras = {"license_extracted": 0, "publisher_extracted": 0, "language_extracted": 0, "keyword_count_sum": 0}
    failures = 0
    latencies = []

    print(f"\n=== {model['name']} ({model['model_id']}) ===")
    quota_exhausted = False
    for i, case in enumerate(gold, 1):
        if quota_exhausted:
            failures += 1
            continue
        try:
            out, lat = extract_one(model, case["text"])
            latencies.append(lat)
        except Exception as exc:
            failures += 1
            err_str = str(exc)[:200]
            print(f"  [{i:3d}/{len(gold)}] FAIL: {err_str[:80]}")
            if "insufficient_quota" in err_str or "429" in err_str or "quota" in err_str.lower():
                print(f"  ⚠ Quota exhausted for {model['name']} — aborting remaining " + str(len(gold) - i) + " docs")
                quota_exhausted = True
            continue
        exp = case["expected"]
        title_ok = exp["title"].lower() in str(out.get("title", "")).lower()
        type_ok = out.get("type", "").lower() == exp["type"].lower() or (
            out.get("type", "") == "Dataset" and exp["type"] == "Dataset"
        )
        domain_ok = out.get("domain", "").lower() == exp["domain"].lower()
        for f, ok in [("title", title_ok), ("type", type_ok), ("domain", domain_ok)]:
            (counts[f][0] if ok else counts[f][1])  # eval branch
            if ok: counts[f][0] += 1
            else: counts[f][1] += 1

        if out.get("license"): extras["license_extracted"] += 1
        if out.get("publisher"): extras["publisher_extracted"] += 1
        if out.get("language"): extras["language_extracted"] += 1
        if isinstance(out.get("keywords"), list): extras["keyword_count_sum"] += len(out["keywords"])

        if i % 20 == 0:
            print(f"  [{i:3d}/{len(gold)}] avg latency {statistics.fmean(latencies):.2f}s")

    def f1(c): return 2*c[0] / (2*c[0] + c[1]) if (2*c[0]+c[1]) else 0.0
    f1s = {f: f1(c) for f, c in counts.items()}
    print(f"  Final F1: title={f1s['title']:.3f}  type={f1s['type']:.3f}  domain={f1s['domain']:.3f}")
    print(f"  Latency mean: {statistics.fmean(latencies):.2f}s  failures: {failures}")

    return {
        "model_name": model["name"],
        "model_id": model["model_id"],
        "provider": model["provider"],
        "f1": f1s,
        "extras": extras,
        "failures": failures,
        "latency_mean": statistics.fmean(latencies) if latencies else 0.0,
        "latency_p95": float(np.percentile(latencies, 95)) if latencies else 0.0,
        "total_time": sum(latencies),
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
    def f1(c): return 2*c[0] / (2*c[0] + c[1]) if (2*c[0]+c[1]) else 0.0
    return {
        "model_name": "Deterministic (Floor)",
        "provider": "none",
        "f1": {f: f1(c) for f, c in counts.items()},
        "latency_mean": 0.0, "failures": 0,
    }


def main() -> None:
    print(f"Multi-model comparison on {len(EXTRACTION_GOLD_V2)} docs\n")
    results = [floor_baseline()]
    for m in MODELS:
        results.append(evaluate_model(m, EXTRACTION_GOLD_V2))

    # Summary table
    print("\n" + "=" * 80)
    print(f"{'Model':<25} {'Title F1':>10} {'Type F1':>10} {'Domain F1':>10} {'Latency (s)':>12}")
    print("-" * 80)
    for r in results:
        if r.get("skipped"):
            print(f"{r.get('model_name', '?'):<25}  SKIPPED — {r.get('reason')}")
            continue
        f1s = r["f1"]
        print(f"{r['model_name']:<25} {f1s['title']:>10.3f} {f1s['type']:>10.3f} {f1s['domain']:>10.3f} {r['latency_mean']:>12.2f}")

    # Save
    out = OUT / "results_multi_model.json"
    out.write_text(json.dumps(results, indent=2, default=str), encoding="utf-8")
    print(f"\n✓ Wrote {out}")
    _plot(results)


def _plot(results: list[dict]) -> None:
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        return
    valid = [r for r in results if not r.get("skipped")]
    names = [r["model_name"] for r in valid]
    fields = ["title", "type", "domain"]
    x = np.arange(len(names))
    width = 0.27

    fig, ax = plt.subplots(figsize=(10, 5))
    colors = ["#888888", "#1f77b4", "#ff7f0e", "#2ca02c"]
    for i, f in enumerate(fields):
        vals = [r["f1"][f] for r in valid]
        ax.bar(x + (i - 1) * width, vals, width, label=f"{f} F1", color=colors[i+1] if i+1 < len(colors) else f"C{i}")
        for j, v in enumerate(vals):
            ax.text(x[j] + (i - 1) * width, v + 0.02, f"{v:.2f}", ha="center", fontsize=8)

    ax.set_xticks(x)
    ax.set_xticklabels(names, rotation=15, ha="right")
    ax.set_ylim(0, 1.15); ax.set_ylabel("F1")
    ax.set_title(f"Multi-model extraction comparison (n={len(EXTRACTION_GOLD_V2)} docs)")
    ax.legend(loc="lower right"); ax.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    out = FIG / "fig_multi_model.png"
    plt.savefig(out, dpi=130)
    plt.close()
    print(f"✓ Saved {out}")


if __name__ == "__main__":
    main()
