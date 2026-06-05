# HITL A/B Grading Rubric (Study E11)

A blinded gold-standard grader scores both branches (Automation-only vs HITL) on each of 100 ambiguous documents.

---

## 1. Per-document scoring (per branch)

| Field | Scoring | Weight |
|-------|---------|:---:|
| `title` | Exact substring match (case-insensitive) | 0.25 |
| `dcmi_type` | Exact match against DCMI Type Vocabulary | 0.25 |
| `domain` | Exact match against domain enum | 0.20 |
| `keywords` | Set IoU between predicted and gold | 0.15 |
| `license` | Match (or both null) | 0.05 |
| `publisher` | Substring of gold publisher | 0.10 |

**Composite F1 (per document):**
$$F1_{doc} = \sum_{f \in \text{fields}} w_f \cdot s_f$$

where $s_f \in [0, 1]$ is the field score.

---

## 2. Branch-level comparison

For each document $d_i$ in the 100-document set, compute $F1_A(d_i)$ and $F1_B(d_i)$.

### 2.1 Aggregate metrics

- **Branch A mean F1:** $\bar{F1}_A = \frac{1}{100} \sum_i F1_A(d_i)$
- **Branch B mean F1:** $\bar{F1}_B = \frac{1}{100} \sum_i F1_B(d_i)$
- **Lift:** $\Delta = \bar{F1}_B - \bar{F1}_A$
- **95 % CI of lift** via bootstrap (1,000 resamples)

### 2.2 Statistical test

- Paired Wilcoxon signed-rank test on $\{F1_A(d_i) - F1_B(d_i)\}_{i=1}^{100}$
- Cohen's $d_z$ for effect size

### 2.3 Acceptance

- **H11.1** accepted if $\Delta \geq 0.10$ with $p < 0.05$.
- **H11.2** accepted if median review time $\leq 60$ s per document.

---

## 3. Time logging

The HITL branch system logs `t_open`, `t_first_edit`, `t_submit` for each document. Compute:

- **Review latency** = $t_{submit} - t_{open}$
- **Edit fraction** = number of documents where any field was corrected / 100

---

## 4. Disagreement log

If the gold-standard grader disagrees with **both** branches on the same field, log the disagreement with rationale. These cases inform a future Q1 revision of the gold corpus.

---

## 5. Blinding protocol

- The grader receives an interleaved CSV containing 200 rows (100 docs × 2 branches), with `branch_id` masked (`X1`, `X2`).
- The grader scores each row independently.
- Branch identities are revealed only after all 200 rows are scored.
- The original PI sets up the masking pipeline; the grader never sees the mapping.
