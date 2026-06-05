# NASA Task Load Index (NASA-TLX)

**Reference:** Hart, S. G., & Staveland, L. E. (1988). Development of NASA-TLX.

Use after each task (T1–T5) in Study E10. Rate each sub-scale on a 21-step bipolar scale (0–100, lower numbers = lower load).

---

## Sub-scales

| Sub-scale | Endpoints (Low → High) | Rating (0–100) |
|-----------|------------------------|:---:|
| **Mental demand** | How much mental and perceptual activity was required? (Low → High) |   |
| **Physical demand** | How much physical activity was required? (Low → High) |   |
| **Temporal demand** | How much time pressure did you feel? (Low → High) |   |
| **Performance** | How successful were you in accomplishing the task? (Perfect → Failure) |   |
| **Effort** | How hard did you have to work to accomplish your performance? (Low → High) |   |
| **Frustration** | How insecure, discouraged, irritated, stressed, or annoyed were you? (Low → High) |   |

---

## Scoring (raw NASA-TLX)

Average the six raw scores. Lower is better.

$$\text{NASA-TLX}_{\text{raw}} = \frac{1}{6} \sum_{i=1}^{6} r_i$$

For the **weighted** version, conduct 15 pairwise comparisons of sub-scales (which contributed more to workload?). The weight of each sub-scale is the number of times it was chosen, divided by 15.

$$\text{NASA-TLX}_{\text{weighted}} = \frac{\sum_{i=1}^{6} w_i r_i}{15}$$

---

## Acceptance thresholds (Section 2 of protocol)

- ≤ 30: **Low** workload (target for routine tasks)
- 31–50: **Moderate** workload (acceptance criterion for H10.2)
- 51–70: **High** workload (warrants UI redesign)
- > 70: **Very high** workload (system not deployable as-is)

---

## Per-task recording sheet

|       | Mental | Physical | Temporal | Performance | Effort | Frustration | **Raw mean** |
|-------|:------:|:--------:|:--------:|:-----------:|:------:|:-----------:|:------------:|
| T1 Ingest |  |  |  |  |  |  |  |
| T2 Search |  |  |  |  |  |  |  |
| T3 Explain |  |  |  |  |  |  |  |
| T4 Validate |  |  |  |  |  |  |  |
| T5 HITL Review |  |  |  |  |  |  |  |
