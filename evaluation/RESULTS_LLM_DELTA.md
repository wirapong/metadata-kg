# E1 Extraction — Floor vs Ceiling Comparison

_Model:_ `claude-sonnet-4-20250514`  ·  _Cases:_ 40  ·  _Failures:_ 0

_Total LLM time:_ 91.74 s  ·  _Avg latency/doc:_ 2.293 s


## Per-field F1 comparison

| Field | Floor F1 | Ceiling F1 | Δ |
|---|---:|---:|---:|
| title | 1.000 | **1.000** | +0.000 |
| type | 1.000 | **0.947** | -0.053 |
| domain | 0.000 | **0.919** | +0.919 |

## Bonus fields extracted by LLM only

- License values found: **0/40**
- Publishers identified: **4/40**
- Languages declared: **37/40**
- Avg keywords per doc: **5.8**

## Interpretation

The deterministic extractor provides a **safe lower bound** that runs offline and is bit-reproducible.
The LLM-enabled ceiling demonstrates the system's full extraction capability when a Claude API key is available.
Production deployments will sit between these two values depending on cost, latency, and rate-limit constraints.
