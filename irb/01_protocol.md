# Study Protocol — Metadata KG Human Evaluation (E9 / E10 / E11)

**Version:** 1.0  ·  **Date:** 4 June 2026
**PI:** Wirapong Chansanam (KKU)
**Study site:** KKU Central Library and online (Zoom / Google Meet)

---

## 1. Background and rationale

The Metadata KG system (Chansanam, 2026) automates DCAT 2 / DCMI metadata extraction using a hybrid LLM-as-Agent and deterministic pipeline. While the system has been evaluated on automated metrics (Section 5 of the manuscript), Q1-grade venues additionally require **human-centred validation** of (a) extraction quality vs librarian judgement, (b) end-user usability, and (c) the marginal value of the Human-in-the-Loop (HITL) review loop.

This protocol covers three linked studies (E9, E10, E11) executed sequentially over **eight weeks** post-IRB approval.

---

## 2. Hypotheses and aims

### Study E9 — Inter-Annotator Agreement
**H9.1:** System–human Cohen's κ on mandatory DCAT fields ≥ 0.61 ("substantial" agreement; Landis & Koch, 1977).
**H9.2:** System–human κ is statistically indistinguishable from human–human κ for title, type, and domain fields (paired comparison, α = 0.05).

### Study E10 — Usability
**H10.1:** SUS score ≥ 68 ("above average"; Brooke, 1996).
**H10.2:** NASA-TLX overall workload ≤ 50 (moderate load) for all five core tasks.
**H10.3:** Task success rate ≥ 85 % per task, with mean completion time ≤ 90 s for the simplest task (search).

### Study E11 — HITL Effectiveness
**H11.1:** F1 lift of HITL-branch over pure-automation branch on ambiguous documents (confidence < 0.7) ≥ 0.10.
**H11.2:** Mean librarian review time per HITL document ≤ 60 s (operationally viable).

---

## 3. Participants

### E9 — Annotators (n = 2)
- **Profile:** Professional librarians or information scientists with ≥ 3 years experience in metadata cataloguing (RDA, MARC, or DCAT).
- **Recruitment:** Purposive sampling via KKU Library network + Thai Library Association (TLA) mailing list.
- **Compensation:** THB 3 000 per annotator (≈ 8 hours of work over 2 weeks).

### E10 — End users (n = 15–20)
- **Profile:** Metadata practitioners (librarians, data stewards, research data managers, repository administrators).
- **Recruitment:** TLA channels + KKU faculty/library network. Stratified by experience (5 novice / 10 intermediate / 5 expert).
- **Compensation:** THB 500 per participant + light refreshments.

### E11 — Single librarian reviewer (n = 1, independent of E9 annotators)
- **Profile:** Same as E9 but explicitly **not the same individual**, to avoid bias.
- **Compensation:** THB 5 000 (estimated 10 hours).

### Inclusion criteria (all studies)
- Age ≥ 20 (adult professional capacity)
- Thai or English proficiency at working level
- Voluntary participation with signed informed consent

### Exclusion criteria
- Direct co-author or contributor to Metadata KG codebase (conflict of interest)
- Inability to complete tasks in either Thai or English

---

## 4. Study procedures

### 4.1 E9 — Inter-Annotator Agreement (Week 1–2)

**Materials:** 120-document gold corpus (`evaluation/eval_dataset_v2.py`); annotation spreadsheet (per-document, per-field).

**Procedure:**
1. Briefing session (1 h): DCAT 2 / DCMI vocabulary refresher; annotation guidelines (`06_annotation_rubric.md`).
2. Each annotator independently labels the same 120 documents.
   - Fields: `title_span`, `dcmi_type`, `domain`, `license_present`, `pii_present`.
   - Estimated 5 min/doc × 120 = 10 h work per annotator.
3. Inter-annotator session (2 h): adjudicate disagreements; produce **consolidated gold**.
4. System output (LLM ceiling) is compared against consolidated gold and against each annotator separately.

**Outcome variables:**
- Annotator A vs B: per-field Cohen's κ.
- System vs annotator A: per-field Cohen's κ.
- System vs annotator B: per-field Cohen's κ.
- System vs consolidated: per-field Cohen's κ + percent agreement.

**Statistical analysis:** Cohen's κ with 95 % CI (bootstrap, 1 000 resamples). Bonferroni-corrected paired comparison of System–Human vs Human–Human κ.

### 4.2 E10 — Usability (Week 3–6)

**Materials:** Live Streamlit instance of Metadata KG (a private staging URL); task script (5 scenarios); SUS questionnaire; NASA-TLX form; screen-record consent.

**Procedure:**
1. Participants attend a single ~75-minute session (in person at KKU Library or remote via Zoom).
2. Brief orientation (5 min) covering interface tabs.
3. Five scripted tasks (Section 4.4 of usability script):
   - T1. **Ingest** a sample document (target ≤ 90 s)
   - T2. **Search** for a metadata record (target ≤ 90 s)
   - T3. **Explain** an entity's lineage (target ≤ 120 s)
   - T4. **Validate** a record against DCAT 2 (target ≤ 120 s)
   - T5. **HITL review** a flagged entity (target ≤ 180 s)
4. Think-aloud protocol during tasks; screen-record with consent.
5. Post-session: SUS (10 items, 5-point Likert) + NASA-TLX (6 sub-scales × 0–100).
6. Optional 5-minute open interview for qualitative feedback.

**Outcome variables:**
- SUS total score (0–100).
- NASA-TLX raw and weighted overall.
- Per-task completion time, success rate, error count, help requests.
- Thematic codes from think-aloud transcripts (qualitative).

**Statistical analysis:** Descriptive statistics (mean, SD, 95 % CI). Stratified analysis by experience level. Mann–Whitney U test for novice vs expert SUS comparison.

### 4.3 E11 — HITL Effectiveness (Week 7–8)

**Materials:** 100 ambiguous documents sampled from production logs (where system confidence < 0.7); two parallel processing branches.

**Procedure:**
1. **Branch A (automation only):** The agent's first output is accepted as final.
2. **Branch B (HITL):** The librarian (E11 reviewer) opens each flagged document via `/hitl/review` and either approves or corrects it. All corrections logged with timestamp.
3. Both branches' outputs are graded against a held-out **third-party gold standard** (independent annotator from the E10 expert pool, blinded to which branch produced the output).
4. Metrics: per-document F1, overall lift (B − A), librarian time-per-doc.

**Outcome variables:**
- F1 lift (Branch B − Branch A) with 95 % CI.
- Mean review time per document.
- Confusion matrix of librarian decisions (approve / correct title / correct type / correct domain).

**Statistical analysis:** Paired Wilcoxon signed-rank test on per-document F1 (n = 100). Effect size (Cohen's d). Report median review time + IQR.

---

## 5. Data handling and privacy

- All annotator/participant identifiers stored only on a master key file held by PI, separate from analysis data.
- Screen recordings retained for **180 days**, then destroyed.
- Aggregated, de-identified data published with manuscript supplementary materials (Zenodo / Figshare).
- Raw data retained for **5 years** per KKU Research Data Management policy.
- Storage: encrypted KKU Google Drive (university account) with PI access only.

---

## 6. Ethical considerations

- **Voluntary participation** with explicit informed consent (Section `02_consent_form_*.md`).
- **Right to withdraw** at any time without penalty; data deleted on request.
- **No deception**; participants are told the study evaluates an AI metadata tool.
- **Minimal-risk** classification: task burden < 90 minutes per participant for E10; up to 10 h spread over 2 weeks for E9 annotators (with regular breaks).
- **Compensation**: not contingent on completion (pro-rated for partial participation).
- **Conflict of interest:** PI is the system designer; mitigated by using **independent annotators** for ground truth and **blinded gold-standard grading** for E11.

---

## 7. Timeline

| Week | Activity |
|------|----------|
| Pre-week 0 | IRB approval, pilot test (n = 2) |
| Week 1–2 | E9 — IAA annotation + adjudication |
| Week 3–6 | E10 — Usability sessions (3–5 per week) |
| Week 7–8 | E11 — HITL A/B trial + grading |
| Week 9–10 | Analysis, write-up, manuscript revision |

---

## 8. Statistical power and sample size justification

- **E9 (κ):** Two-rater κ is sufficient when paired with a 120-doc corpus to detect κ ≥ 0.61 with α = 0.05, power = 0.80 (Sim & Wright, 2005).
- **E10 (usability):** Nielsen (1993) shows that 80 % of usability problems are detected with 5 evaluators; n = 15–20 ensures statistical reliability for SUS (Sauro & Lewis, 2016).
- **E11 (HITL):** Paired comparison on n = 100 docs gives power = 0.83 for detecting d = 0.30 with α = 0.05 (two-sided Wilcoxon).

---

## 9. References

- Brooke, J. (1996). SUS: A "quick and dirty" usability scale.
- Hart, S. G., & Staveland, L. E. (1988). Development of NASA-TLX.
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement.
- Nielsen, J. (1993). *Usability Engineering*.
- Sauro, J., & Lewis, J. R. (2016). *Quantifying the User Experience* (2nd ed.).
- Sim, J., & Wright, C. C. (2005). The kappa statistic in reliability studies. *Physical Therapy*, 85(3), 257–268.
