# IRB Application Package — Metadata KG Human-Centred Evaluation

**Principal Investigator (PI):** Assoc. Prof. Dr. Wirapong Chansanam
**Affiliation:** Faculty of Humanities and Social Sciences, Khon Kaen University
**ORCID:** 0000-0001-5546-8485
**Email:** wirach@kku.ac.th
**Funding:** Faculty of Humanities Research Grant 2026 (ทุนวิจัยคณะมนุษย์ 2569)

---

## 1. Studies covered

| ID | Study | Participants | Status |
|----|-------|-------------|--------|
| E9 | Inter-Annotator Agreement (IAA) | 2 academic librarians | Document package ready |
| E10 | System Usability + Cognitive Load | 15–20 metadata practitioners | Document package ready |
| E11 | HITL Effectiveness A/B Trial | 100 ambiguous documents reviewed by 1 librarian | Document package ready |

All three studies use **publicly observable behaviour** (annotation logs, task completion times, validated questionnaires) and **anonymous/aggregate analysis**. No clinical data, no minors, no vulnerable populations.

---

## 2. Risk classification (per Thai NRCT human-research-ethics framework)

- **Category:** Minimal risk (exempted / expedited review pathway)
- **Justification:**
  - Adult professional participants only (librarians and metadata stewards, recruited via professional channels).
  - Tasks involve cataloguing software interaction — comparable to routine professional work.
  - No invasive procedures, no biospecimens, no sensitive personal data.
  - Participants may withdraw at any time without consequence.

---

## 3. Package contents

```
irb/
├── 00_README.md                       ← this file
├── 01_protocol.md                     ← full study protocol (all 3 studies)
├── 02_consent_form_TH.md              ← Thai participant consent form
├── 02_consent_form_EN.md              ← English participant consent form
├── 03_recruitment_email_TH.md         ← Thai recruitment template
├── 03_recruitment_email_EN.md         ← English recruitment template
├── 04_sus_questionnaire.md            ← System Usability Scale (10-item)
├── 05_nasa_tlx.md                     ← NASA-TLX cognitive-load rubric
├── 06_annotation_rubric.md            ← Librarian annotation guidelines for E9
├── 07_hitl_grading_rubric.md          ← Gold-standard scoring rubric for E11
├── 08_data_management_plan.md         ← DMP (storage, retention, sharing)
├── 09_risk_assessment.md              ← Detailed risk-benefit analysis
└── 10_timeline_budget.md              ← Study timeline & budget breakdown
```

---

## 4. Submission pathway

1. Compile this package as a single PDF using `pandoc` or Word.
2. Submit to **KKU Research Ethics Committee for Human Research** (`hec.kku.ac.th`).
3. Recommended review pathway: **Expedited** (Category 7 — research employing survey, interview, observational procedures).
4. Expected turnaround: **4–6 weeks**.

---

## 5. Pre-submission checklist

- [ ] PI signs cover letter
- [ ] Co-PI consent obtained (if applicable)
- [ ] All instruments translated TH/EN
- [ ] Consent forms reviewed by KKU OHRP liaison
- [ ] Data Management Plan (DMP) aligned with FAIR principles
- [ ] Budget approval letter from Faculty
- [ ] Conflict-of-interest disclosure attached
- [ ] Pilot test (n=2) completed before main recruitment

---

## 6. Manuscript linkage

This IRB package directly enables the human-study Guidelines (E9–E11) described in **Section 5.10 of the manuscript** (`manuscript/methodology_and_results.md`). Upon ethics approval, the studies can be executed to upgrade those Guidelines into reported empirical results.

**Manuscript update plan after IRB completion:**
1. Section 5.10 (Guidelines) → moved to Section 5.5–5.7 (Results).
2. Table 11 (consolidated results) extended with three new rows (κ_system, SUS score, HITL F1 lift).
3. Discussion section adds qualitative findings from think-aloud sessions.
