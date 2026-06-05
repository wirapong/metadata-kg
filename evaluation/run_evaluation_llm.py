"""Upper-bound evaluation using LLM mode (Claude Sonnet 4).

Compares Deterministic vs LLM agent on the same gold set.
Produces:
- evaluation/results_llm.json
- evaluation/figures/fig_e1_floor_vs_ceiling.png
- evaluation/RESULTS_LLM_DELTA.md  (compact delta report)

Requires:
- ANTHROPIC_API_KEY in environment or .env
- langchain + langchain-anthropic + anthropic installed
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

# Load .env if present
try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).parent.parent / ".env")
except ImportError:
    pass

from evaluation.eval_dataset import EXTRACTION_GOLD
from metadata_kg.core.llm_agent import deterministic_extract_entities

OUT = Path(__file__).parent
FIG = OUT / "figures"
FIG.mkdir(exist_ok=True)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def prf(tp: int, fp: int, fn: int) -> tuple[float, float, float]:
    p = tp / (tp + fp) if (tp + fp) else 0.0
    r = tp / (tp + fn) if (tp + fn) else 0.0
    f1 = 2 * p * r / (p + r) if (p + r) else 0.0
    return p, r, f1


def mean(xs: list[float]) -> float:
    return statistics.fmean(xs) if xs else 0.0


# ---------------------------------------------------------------------------
# LLM-based extraction with structured output prompt
# ---------------------------------------------------------------------------
LLM_PROMPT_TEMPLATE = """You are a metadata cataloguer trained in DCAT 2 / DCMI vocabularies.

Extract structured metadata from the document below. Return STRICT JSON with these keys:
{{
  "title": str,
  "type": one of ["Dataset","Text","StillImage","MovingImage","Sound","Service","Software","Event","Collection","InteractiveResource","PhysicalObject"],
  "domain": one of ["health","environment","education","finance","government","agriculture","transport","culture","other"],
  "keywords": [str, ...],
  "license": str | null,
  "publisher": str | null,
  "language": [str, ...]
}}

Document:
\"\"\"
{text}
\"\"\"

Return ONLY the JSON object, no prose."""


def llm_extract_one(llm: Any, text: str) -> dict[str, Any]:
    """Direct ChatAnthropic call with the structured prompt."""
    msg = llm.invoke(LLM_PROMPT_TEMPLATE.format(text=text))
    raw = msg.content if hasattr(msg, "content") else str(msg)

    # Strip code fences if present
    raw = raw.strip()
    if raw.startswith("```"):
        raw = raw.split("```", 2)[1]
        if raw.startswith("json"):
            raw = raw[4:]
        raw = raw.strip("` \n")

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        # Best-effort: find first {...} block
        start = raw.find("{")
        end = raw.rfind("}")
        if start >= 0 and end > start:
            return json.loads(raw[start:end+1])
        raise


# ---------------------------------------------------------------------------
# E1 — floor vs ceiling on extraction
# ---------------------------------------------------------------------------
def e1_floor_vs_ceiling() -> dict:
    print("=== E1 (LLM upper bound) — extraction comparison ===\n")

    api_key = os.getenv("ANTHROPIC_API_KEY")
    model = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-20250514")
    if not api_key:
        print("✗ ANTHROPIC_API_KEY not set. Set it in .env or export it before running.")
        sys.exit(1)

    from langchain_anthropic import ChatAnthropic
    llm = ChatAnthropic(
        model=model,
        api_key=api_key,
        temperature=0.1,
        max_tokens=600,
    )
    print(f"✓ LLM mode active: model={model}\n")

    # --------- Floor (deterministic) ---------
    print("--- Floor (deterministic) ---")
    floor = {"title": [0, 0], "type": [0, 0], "domain": [0, 0]}  # [tp, fn]
    for case in EXTRACTION_GOLD:
        ents = deterministic_extract_entities(case["text"])
        title = ents[0].properties.get("dct:title", "") if ents else ""
        type_ = ents[0].type if ents else ""
        # domain not produced by deterministic extractor → always fn unless keyword in text
        # (this matches the run_evaluation.py logic; reported for parity)
        exp = case["expected"]
        if exp["title"].lower() in str(title).lower(): floor["title"][0] += 1
        else: floor["title"][1] += 1
        if exp["type"] in type_ or "Dataset" in type_: floor["type"][0] += 1
        else: floor["type"][1] += 1
        # Deterministic never outputs domain → always FN for this metric
        floor["domain"][1] += 1

    # --------- Ceiling (LLM) ---------
    print("--- Ceiling (LLM) — calling Claude for each of 40 docs ---")
    ceiling = {"title": [0, 0], "type": [0, 0], "domain": [0, 0]}
    ceiling_extra = {
        "license_extracted": 0, "publisher_extracted": 0, "language_extracted": 0,
        "keyword_count_sum": 0,
    }
    per_doc_log = []
    failures = 0
    t_start = time.perf_counter()

    for i, case in enumerate(EXTRACTION_GOLD, 1):
        try:
            t0 = time.perf_counter()
            out = llm_extract_one(llm, case["text"])
            latency = time.perf_counter() - t0
        except Exception as exc:
            failures += 1
            print(f"  [{i:2d}/40] FAIL: {exc}")
            continue

        exp = case["expected"]
        title_ok = exp["title"].lower() in str(out.get("title", "")).lower()
        type_ok = out.get("type", "").lower() == exp["type"].lower() or out.get("type", "") == "Dataset" and exp["type"] == "Dataset"
        domain_ok = out.get("domain", "").lower() == exp["domain"].lower()

        if title_ok: ceiling["title"][0] += 1
        else: ceiling["title"][1] += 1
        if type_ok: ceiling["type"][0] += 1
        else: ceiling["type"][1] += 1
        if domain_ok: ceiling["domain"][0] += 1
        else: ceiling["domain"][1] += 1

        if out.get("license"): ceiling_extra["license_extracted"] += 1
        if out.get("publisher"): ceiling_extra["publisher_extracted"] += 1
        if out.get("language"): ceiling_extra["language_extracted"] += 1
        if isinstance(out.get("keywords"), list): ceiling_extra["keyword_count_sum"] += len(out["keywords"])

        per_doc_log.append({
            "i": i, "expected": exp, "predicted": {
                "title": out.get("title"), "type": out.get("type"),
                "domain": out.get("domain"), "license": out.get("license"),
            },
            "title_ok": title_ok, "type_ok": type_ok, "domain_ok": domain_ok,
            "latency_s": round(latency, 3),
        })

        ok = "✓" if (title_ok and type_ok and domain_ok) else "·"
        print(f"  [{i:2d}/40] {ok}  title={title_ok} type={type_ok} domain={domain_ok} ({latency:.1f}s)")

    total_time = time.perf_counter() - t_start
    print(f"\n  Total LLM time: {total_time:.1f}s  ({total_time/max(len(EXTRACTION_GOLD)-failures,1):.2f}s avg/doc)")
    if failures:
        print(f"  ⚠ {failures} doc(s) failed to extract")

    # --------- Metrics ---------
    floor_metrics = {k: dict(zip(["tp", "fn"], v)) | dict(zip(["precision", "recall", "f1"], prf(v[0], 0, v[1]))) for k, v in floor.items()}
    ceiling_metrics = {k: dict(zip(["tp", "fn"], v)) | dict(zip(["precision", "recall", "f1"], prf(v[0], 0, v[1]))) for k, v in ceiling.items()}

    deltas = {k: round(ceiling_metrics[k]["f1"] - floor_metrics[k]["f1"], 3) for k in floor}

    print("\n=== Floor vs Ceiling (F1) ===")
    print(f"  Field       Floor        Ceiling      Δ")
    for k in ["title", "type", "domain"]:
        print(f"  {k:10s}  {floor_metrics[k]['f1']:.3f}        {ceiling_metrics[k]['f1']:.3f}        {deltas[k]:+.3f}")

    return {
        "n_cases": len(EXTRACTION_GOLD),
        "failures": failures,
        "total_llm_time_s": round(total_time, 2),
        "avg_latency_per_doc_s": round(total_time / max(len(EXTRACTION_GOLD) - failures, 1), 3),
        "floor": floor_metrics,
        "ceiling": ceiling_metrics,
        "delta_f1": deltas,
        "ceiling_extra_fields": ceiling_extra,
        "per_doc_log": per_doc_log,
        "model": model,
    }


# ---------------------------------------------------------------------------
# Plot floor vs ceiling
# ---------------------------------------------------------------------------
def _plot(report: dict) -> None:
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        return

    fields = ["title", "type", "domain"]
    floor_f1 = [report["floor"][f]["f1"] for f in fields]
    ceil_f1 = [report["ceiling"][f]["f1"] for f in fields]

    x = np.arange(len(fields))
    fig, ax = plt.subplots(figsize=(7.5, 4.2))
    ax.bar(x - 0.2, floor_f1, 0.4, label="Floor (deterministic)", color="#7e7e7e")
    ax.bar(x + 0.2, ceil_f1, 0.4, label=f"Ceiling (LLM — {report['model']})", color="#1f77b4")
    ax.set_xticks(x)
    ax.set_xticklabels(fields)
    ax.set_ylim(0, 1.1)
    ax.set_ylabel("F1")
    ax.set_title("E1 Extraction: Floor (deterministic) vs Ceiling (LLM)")
    for i, (a, b) in enumerate(zip(floor_f1, ceil_f1)):
        ax.text(i - 0.2, a + 0.02, f"{a:.2f}", ha="center", fontsize=9)
        ax.text(i + 0.2, b + 0.02, f"{b:.2f}", ha="center", fontsize=9, weight="bold")
    ax.legend(loc="lower right")
    ax.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    out = FIG / "fig_e1_floor_vs_ceiling.png"
    plt.savefig(out, dpi=130)
    plt.close()
    print(f"\n✓ Saved plot: {out}")


# ---------------------------------------------------------------------------
# Markdown delta report
# ---------------------------------------------------------------------------
def _write_md_report(report: dict) -> None:
    md = []
    md.append("# E1 Extraction — Floor vs Ceiling Comparison\n")
    md.append(f"_Model:_ `{report['model']}`  ·  _Cases:_ {report['n_cases']}  ·  _Failures:_ {report['failures']}\n")
    md.append(f"_Total LLM time:_ {report['total_llm_time_s']} s  ·  _Avg latency/doc:_ {report['avg_latency_per_doc_s']} s\n")
    md.append("\n## Per-field F1 comparison\n")
    md.append("| Field | Floor F1 | Ceiling F1 | Δ |")
    md.append("|---|---:|---:|---:|")
    for f in ["title", "type", "domain"]:
        floor = report["floor"][f]["f1"]
        ceil = report["ceiling"][f]["f1"]
        md.append(f"| {f} | {floor:.3f} | **{ceil:.3f}** | {ceil - floor:+.3f} |")
    md.append("\n## Bonus fields extracted by LLM only\n")
    extra = report["ceiling_extra_fields"]
    md.append(f"- License values found: **{extra['license_extracted']}/{report['n_cases']}**")
    md.append(f"- Publishers identified: **{extra['publisher_extracted']}/{report['n_cases']}**")
    md.append(f"- Languages declared: **{extra['language_extracted']}/{report['n_cases']}**")
    md.append(f"- Avg keywords per doc: **{extra['keyword_count_sum'] / max(report['n_cases'] - report['failures'], 1):.1f}**")
    md.append("\n## Interpretation\n")
    md.append("The deterministic extractor provides a **safe lower bound** that runs offline and is bit-reproducible.")
    md.append("The LLM-enabled ceiling demonstrates the system's full extraction capability when a Claude API key is available.")
    md.append("Production deployments will sit between these two values depending on cost, latency, and rate-limit constraints.\n")
    out = OUT / "RESULTS_LLM_DELTA.md"
    out.write_text("\n".join(md), encoding="utf-8")
    print(f"✓ Wrote {out}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    report = e1_floor_vs_ceiling()
    out = OUT / "results_llm.json"
    out.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
    print(f"\n✓ Wrote {out}")
    _plot(report)
    _write_md_report(report)


if __name__ == "__main__":
    main()
