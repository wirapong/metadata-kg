"""Quick-start script demonstrating the end-to-end pipeline.

Run: `python examples/quickstart.py`
"""

from __future__ import annotations

import json
from pathlib import Path

from metadata_kg.governance.policy import PolicyEngine
from metadata_kg.governance.xai import ExplainabilityLayer
from metadata_kg.pipeline.lifecycle import MetadataLifecycle
from metadata_kg.search.semantic_search import SemanticMetadataSearch


def main() -> None:
    print("=== Metadata KG quickstart ===\n")
    lc = MetadataLifecycle()

    # 1. Ingest a JSON file (pass the Path so ingest_any reads it)
    sample = Path(__file__).parent / "sample_dataset.json"
    results = lc.run_full(sample, source=str(sample))
    eid = results["creation"].entity_ids[0]
    print(f"✅ Created entity: {eid}\n")

    # 2. Search
    search = SemanticMetadataSearch()
    search.index_kg(lc.kg)
    print("🔎 Search 'air quality':")
    for r in search.hybrid_search("air quality", top_k=3):
        print(f"   {r.score:.3f}  {r.entity_id[-30:]}  {r.snippet[:60]}...")
    print()

    # 3. Policy check
    pe = PolicyEngine()
    rules_yaml = Path(__file__).parent / "custom_policy.yaml"
    pe.load_rules(rules_yaml)
    compliance = pe.check_compliance(lc.kg.get_entity(eid))
    print(f"🛡️ Policy: pass={compliance['pass']}, errors={compliance['summary']['error']}")
    for v in compliance["violated_rules"][:3]:
        print(f"   - [{v['severity']}] {v['rule_id']}: {v['message']}")
    print()

    # 4. XAI
    xai = ExplainabilityLayer(lc.kg, lc.lineage)
    print("🧠 XAI explanation (first 400 chars):")
    print(xai.explain_decision(eid)[:400], "...\n")

    # 5. Persist
    out_dir = Path(__file__).parent.parent / "data"
    out_dir.mkdir(exist_ok=True)
    lc.kg.export_to_turtle(out_dir / "quickstart.ttl")
    lc.lineage.export_lineage_graph(out_dir / "quickstart_lineage.jsonld")
    print(f"💾 Saved: {out_dir}/quickstart.ttl + quickstart_lineage.jsonld")


if __name__ == "__main__":
    main()
