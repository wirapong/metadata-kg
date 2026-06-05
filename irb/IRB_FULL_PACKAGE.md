---
title: "IRB Application Package — Metadata KG Human-Centred Evaluation"
author: "Wirapong Chansanam, Khon Kaen University"
date: "4 June 2026"
geometry: margin=1in
fontsize: 11pt
---



ewpage

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


ewpage

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


ewpage

# เอกสารแสดงความยินยอม

## โครงการวิจัย: การประเมินระบบอัตโนมัติสร้างคำอธิบายข้อมูล (Metadata KG)

**หัวหน้าโครงการวิจัย:** รศ.ดร.วิระพงศ์ จันทร์สนาม
สังกัด: คณะมนุษยศาสตร์และสังคมศาสตร์ มหาวิทยาลัยขอนแก่น
อีเมล: wirach@kku.ac.th
ORCID: 0000-0001-5546-8485

---

### 1. คำเชิญ
ขอเรียนเชิญท่านเข้าร่วมโครงการวิจัยที่มีวัตถุประสงค์เพื่อประเมินประสิทธิภาพและการใช้งานของ **ระบบ Metadata KG** ซึ่งเป็นซอฟต์แวร์ช่วยจัดทำ metadata คลังข้อมูลที่สอดคล้องกับมาตรฐาน DCAT 2 / DCMI โดยใช้เทคนิคปัญญาประดิษฐ์

### 2. วัตถุประสงค์
1. วัดความสอดคล้องระหว่างผลการดึงข้อมูลของระบบกับบรรณารักษ์มืออาชีพ (Study E9)
2. ประเมินความง่ายในการใช้งานของส่วนติดต่อผู้ใช้ (Study E10)
3. วัดประโยชน์ของกระบวนการตรวจสอบโดยมนุษย์ (Human-in-the-Loop) (Study E11)

### 3. ขั้นตอนที่ท่านจะเข้าร่วม
- **กรณี E9 (ผู้ให้ฉลาก/annotator):** จดป้ายกำกับ metadata 120 เอกสาร ใช้เวลาประมาณ 10 ชั่วโมง กระจายใน 2 สัปดาห์
- **กรณี E10 (ผู้ใช้):** ทำ 5 ภารกิจบนเว็บไซต์ระบบฯ ในเซสชันเดียวประมาณ 75 นาที พร้อมตอบแบบสอบถาม SUS และ NASA-TLX
- **กรณี E11 (ผู้ตรวจสอบ HITL):** ตรวจสอบและแก้ไข metadata ของ 100 เอกสารผ่านระบบ ใช้เวลาประมาณ 10 ชั่วโมง

### 4. ความเสี่ยง
ความเสี่ยงน้อยมาก เป็นการทำงานในระดับเดียวกับงานบรรณารักษ์ปกติของท่าน ไม่มีการเก็บข้อมูลส่วนตัวที่ละเอียดอ่อน ไม่มีหัตถการทางการแพทย์ ไม่มีการเก็บตัวอย่างชีวภาพ

### 5. ผลประโยชน์ที่อาจได้รับ
- ค่าตอบแทน:
  - E9: 3,000 บาท
  - E10: 500 บาท + อาหารว่าง
  - E11: 5,000 บาท
- ได้ใช้และเรียนรู้เครื่องมือใหม่ที่อาจนำไปใช้กับงานคลังข้อมูลของท่านได้
- มีส่วนร่วมในการพัฒนาเครื่องมือด้านบรรณารักษศาสตร์ของไทย

### 6. การเก็บรักษาข้อมูล
- ข้อมูลของท่านถูกเก็บแบบไม่ระบุตัวตน
- เก็บใน Google Drive ที่เข้ารหัสของมหาวิทยาลัยขอนแก่น
- เฉพาะหัวหน้าโครงการเข้าถึงได้
- เก็บเป็นเวลา 5 ปีตามนโยบายของมหาวิทยาลัย จากนั้นทำลายทิ้ง
- บันทึกหน้าจอ (กรณี E10) เก็บไว้ 180 วันแล้วทำลาย
- ผลรวมแบบไม่ระบุตัวตนอาจเผยแพร่เป็นข้อมูลเสริมของบทความวิจัย

### 7. สิทธิ์ของท่าน
- **เข้าร่วมโดยสมัครใจ** ปฏิเสธได้ ถอนตัวได้ทุกเมื่อโดยไม่ต้องให้เหตุผล
- **ค่าตอบแทน:** จ่ายตามสัดส่วนการเข้าร่วมแม้ถอนตัวก่อนเสร็จสิ้น
- **ติดต่อกลับ:** สามารถขอลบข้อมูลของท่านได้ภายใน 30 วันหลังเข้าร่วม
- **สอบถามได้ที่:** wirach@kku.ac.th โทร [PI phone]
- **ร้องเรียนได้ที่:** คณะกรรมการจริยธรรมการวิจัยในมนุษย์ มหาวิทยาลัยขอนแก่น
  - อีเมล: hec@kku.ac.th
  - โทร: 043 203 178

### 8. คำยินยอม

ข้าพเจ้าได้อ่านและเข้าใจเอกสารฉบับนี้แล้ว มีโอกาสซักถามและได้รับคำตอบเป็นที่พอใจ และยินยอมเข้าร่วมโครงการวิจัยด้วยความสมัครใจ

ข้าพเจ้ายินยอม (เลือกข้อใดข้อหนึ่ง):

- [ ] ให้เก็บข้อมูลและบันทึกหน้าจอ (เฉพาะกรณี E10)
- [ ] ให้เก็บเฉพาะข้อมูลตัวเลข ไม่บันทึกหน้าจอ
- [ ] ให้ใช้ข้อความบางส่วนของข้าพเจ้า (โดยไม่ระบุตัวตน) เพื่อประกอบบทความวิจัย

---

ชื่อ-สกุล ผู้เข้าร่วม:  ________________________________________

ลายเซ็น:  ________________________________________  วันที่:  __________

ลายเซ็นหัวหน้าโครงการ:  ____________________________  วันที่:  __________


ewpage

# Informed Consent Form

## Research project: Evaluation of an AI-powered Metadata Cataloguing System (Metadata KG)

**Principal Investigator:** Assoc. Prof. Dr. Wirapong Chansanam
Affiliation: Faculty of Humanities and Social Sciences, Khon Kaen University
Email: wirach@kku.ac.th  ·  ORCID: 0000-0001-5546-8485

---

### 1. Invitation
You are invited to take part in a research study evaluating the performance and usability of **Metadata KG**, an AI-assisted system that produces metadata records aligned with the DCAT 2 / DCMI standards.

### 2. Purpose
1. Measure agreement between the system and professional librarians (Study E9).
2. Evaluate user interface usability (Study E10).
3. Quantify the benefit of the Human-in-the-Loop review process (Study E11).

### 3. What participation involves
- **E9 (annotator):** Label 120 documents (~10 hours over 2 weeks).
- **E10 (end user):** Complete five scripted tasks during a ~75-minute session + SUS and NASA-TLX questionnaires.
- **E11 (HITL reviewer):** Review and correct metadata for 100 documents (~10 hours).

### 4. Risks
Minimal — comparable to your routine professional cataloguing work. No sensitive personal data, no medical procedures, no biological samples.

### 5. Benefits
- Honorarium:
  - E9: THB 3,000
  - E10: THB 500 + light refreshments
  - E11: THB 5,000
- Opportunity to learn a new cataloguing tool potentially useful for your work.
- Contribute to the development of Thai library and metadata tools.

### 6. Data management
- All data are stored in an anonymised form.
- Stored on encrypted KKU Google Drive accessible only by the PI.
- Retained 5 years per KKU Research Data Management policy, then destroyed.
- Screen recordings (E10 only) retained 180 days, then destroyed.
- De-identified aggregate data may be published as supplementary materials.

### 7. Your rights
- **Voluntary participation:** You may decline or withdraw at any time without consequence.
- **Pro-rated compensation** even if you withdraw before completion.
- **Right to deletion:** You may request deletion of your data within 30 days of participation.
- **Contact:** wirach@kku.ac.th  ·  Tel. [PI phone]
- **Complaints:** KKU Human Research Ethics Committee  ·  hec@kku.ac.th  ·  Tel. 043 203 178

### 8. Consent

I have read and understood this document, had the opportunity to ask questions, and voluntarily agree to participate.

I consent to (tick all that apply):

- [ ] Collection of behavioural and screen recordings (E10 only)
- [ ] Collection of numerical data only (no screen recording)
- [ ] Use of anonymous quotes from my think-aloud or interview in the resulting publication

---

Participant name: ________________________________________

Signature: ________________________________________  Date:  __________

PI signature: ____________________________  Date:  __________


ewpage

# เทมเพลตอีเมลเชิญเข้าร่วมโครงการวิจัย

**หัวเรื่อง:** ขอเชิญเข้าร่วมโครงการวิจัยประเมินระบบ AI สำหรับงาน Metadata คลังข้อมูล — ค่าตอบแทน 500–5,000 บาท

---

เรียน คุณ [ชื่อผู้รับ]

ผม รศ.ดร.วิระพงศ์ จันทร์สนาม อาจารย์ประจำคณะมนุษยศาสตร์และสังคมศาสตร์ มหาวิทยาลัยขอนแก่น

ผมและทีมวิจัยกำลังพัฒนาเครื่องมือ AI ชื่อ **Metadata KG** สำหรับช่วยจัดทำ metadata ของคลังข้อมูลแบบอัตโนมัติตามมาตรฐาน DCAT 2 / DCMI ขณะนี้เรากำลังประเมินคุณภาพและความเหมาะสมของเครื่องมือก่อนเผยแพร่เป็น open source

จึงขอเรียนเชิญท่านในฐานะ [บรรณารักษ์/data steward/นักจัดการข้อมูลวิจัย] เข้าร่วมโครงการวิจัยซึ่งผ่านการอนุมัติจริยธรรมการวิจัย (เลขที่อ้างอิง: [HEC-KKU-XXX]) เรียบร้อยแล้ว

**ภารกิจที่จะให้ความช่วยเหลือ:** _[เลือกหนึ่งจาก:]_
- 🔖 **E9** จดป้ายกำกับ metadata 120 เอกสาร (~10 ชม. กระจาย 2 สัปดาห์ ค่าตอบแทน 3,000 บาท)
- 🖥️ **E10** ทดลองใช้ระบบ + ตอบแบบสอบถาม (75 นาที ค่าตอบแทน 500 บาท)
- ✅ **E11** ตรวจสอบและแก้ไข metadata 100 เอกสาร (~10 ชม. ค่าตอบแทน 5,000 บาท)

**ผู้ได้รับการพิจารณา:** ผู้ที่มีประสบการณ์ ≥ 3 ปีในการจัดทำ metadata (เน้น RDA / MARC / DCAT)

**สถานที่:** ที่ห้องสมุดกลาง มข. หรือผ่าน Zoom ก็ได้

หากท่านสนใจ กรุณาตอบกลับอีเมลฉบับนี้ภายในวันที่ [DATE] เพื่อรับข้อมูลเพิ่มเติมและกำหนดเวลาที่สะดวกครับ

ขอบคุณท่านเป็นอย่างสูง

ด้วยความเคารพ
รศ.ดร.วิระพงศ์ จันทร์สนาม
อีเมล: wirach@kku.ac.th
ORCID: 0000-0001-5546-8485


ewpage

# Recruitment Email Template (English)

**Subject:** Invitation to evaluate an AI-powered metadata cataloguing tool — Honorarium THB 500–5,000

---

Dear [Recipient name],

I am Assoc. Prof. Dr. Wirapong Chansanam, Faculty of Humanities and Social Sciences, Khon Kaen University.

My research team is developing **Metadata KG**, an AI-powered tool that helps catalogue digital collections according to the DCAT 2 / DCMI standards. We are now evaluating the system before releasing it as open-source.

I would like to invite you, as an experienced [librarian / data steward / research data manager], to participate in our research study, which has received KKU Human Research Ethics Committee approval (Ref.: [HEC-KKU-XXX]).

**Role options:** _[select one]_
- 🔖 **E9** Annotate 120 metadata documents (~10 h over 2 weeks; honorarium THB 3,000)
- 🖥️ **E10** Try the system + complete questionnaires (75 min; honorarium THB 500)
- ✅ **E11** Review and correct metadata for 100 documents (~10 h; honorarium THB 5,000)

**Eligibility:** ≥ 3 years of metadata cataloguing experience (RDA / MARC / DCAT preferred).

**Location:** KKU Central Library or remote via Zoom.

If you are interested, please reply by [DATE] for further information and scheduling.

Thank you for considering this invitation.

With kind regards,
Assoc. Prof. Dr. Wirapong Chansanam
Email: wirach@kku.ac.th
ORCID: 0000-0001-5546-8485


ewpage

# System Usability Scale (SUS) Questionnaire

**Reference:** Brooke, J. (1996). SUS: A "quick and dirty" usability scale.

**Instructions:** Please rate your level of agreement with each statement after using Metadata KG.
**Scale:** 1 = Strongly disagree · 2 = Disagree · 3 = Neutral · 4 = Agree · 5 = Strongly agree

---

| # | Statement | Rating (1–5) |
|---|-----------|:---:|
| 1 | I think that I would like to use this system frequently. |   |
| 2 | I found the system unnecessarily complex. |   |
| 3 | I thought the system was easy to use. |   |
| 4 | I think that I would need the support of a technical person to use this system. |   |
| 5 | I found the various functions in this system were well integrated. |   |
| 6 | I thought there was too much inconsistency in this system. |   |
| 7 | I imagine that most people would learn to use this system very quickly. |   |
| 8 | I found the system very cumbersome to use. |   |
| 9 | I felt very confident using the system. |   |
| 10 | I needed to learn a lot of things before I could get going with this system. |   |

---

## Scoring formula

For odd-numbered items (1, 3, 5, 7, 9): subtract 1 from the user's rating.
For even-numbered items (2, 4, 6, 8, 10): subtract the user's rating from 5.
Sum the adjusted scores and multiply by 2.5.

$$\text{SUS} = 2.5 \times \left[ \sum_{i \in O} (x_i - 1) + \sum_{i \in E} (5 - x_i) \right]$$

where $O = \{1, 3, 5, 7, 9\}$ and $E = \{2, 4, 6, 8, 10\}$.

**Interpretation (Sauro & Lewis, 2016):**
- < 50: Unacceptable
- 50–67: Marginal
- 68: Average (boundary of acceptable usability)
- ≥ 80: Excellent

---

## Optional Thai translation

| # | คำกล่าว | คะแนน |
|---|--------|:---:|
| 1 | ฉันคิดว่าฉันจะอยากใช้ระบบนี้บ่อย ๆ |   |
| 2 | ฉันรู้สึกว่าระบบนี้ซับซ้อนเกินความจำเป็น |   |
| 3 | ฉันคิดว่าระบบนี้ใช้งานง่าย |   |
| 4 | ฉันคิดว่าฉันคงต้องการความช่วยเหลือจากเจ้าหน้าที่ด้านเทคนิคเพื่อใช้งานระบบนี้ |   |
| 5 | ฉันพบว่าฟังก์ชันต่าง ๆ ในระบบทำงานเชื่อมโยงกันได้ดี |   |
| 6 | ฉันคิดว่าระบบมีความไม่สอดคล้องกันมากเกินไป |   |
| 7 | ฉันคิดว่าคนส่วนใหญ่จะเรียนรู้ที่จะใช้ระบบนี้ได้อย่างรวดเร็ว |   |
| 8 | ฉันพบว่าระบบนี้ใช้ลำบาก |   |
| 9 | ฉันรู้สึกมั่นใจในการใช้ระบบนี้ |   |
| 10 | ฉันต้องเรียนรู้หลายสิ่งหลายอย่างก่อนจึงจะใช้ระบบนี้ได้ |   |


ewpage

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


ewpage

# Librarian Annotation Rubric (Study E9)

Use this rubric when labelling the 120-document gold corpus.

---

## 1. Fields to annotate (per document)

| Field | Definition | Allowed values |
|-------|-----------|----------------|
| `title_span` | The most precise title that uniquely identifies the resource (Cutter-style if applicable). | Free-text span from the document |
| `dcmi_type` | The single most appropriate DCMI Type Vocabulary term. | One of: **Dataset · Text · StillImage · MovingImage · Sound · Software · Service · Event · Collection · InteractiveResource · PhysicalObject** |
| `domain` | The thematic / subject domain best describing the resource. | One of: **health · environment · education · finance · government · agriculture · transport · culture · other** |
| `license_present` | Is a license explicitly stated in the document? | yes / no / unclear |
| `pii_present` | Does the document text contain personally identifiable information? | yes / no / unclear |

---

## 2. Decision rules (apply in order)

### 2.1 Title
- Prefer the literal span following "Title:" if present.
- Otherwise, take the most concise noun phrase that identifies the resource.
- Trim trailing year unless the year is part of the work's official name.

### 2.2 DCMI Type
- **Dataset** = numerical, tabular, or structured records (CSV, RDB, JSON arrays).
- **Text** = narrative or policy documents, articles, books, reports, manuscripts.
- **StillImage** = photographs, scans, satellite imagery, drawings (single frames).
- **MovingImage** = video, film, animation, footage.
- **Sound** = audio recordings, soundscapes, voice archives.
- **Software** = executable code, libraries, applications, mobile apps.
- **Service** = APIs, web services, SOAP/REST/WebSocket endpoints.
- **Event** = a happening at a specific time (festivals, conferences, ceremonies).
- **Collection** = an aggregation of resources (digital libraries, archives, manuscript groups).
- **InteractiveResource** = web dashboards, simulators, virtual labs.

**Disambiguation guidance:**
- "X-Ray Image Set" → StillImage (not Dataset) even though it has labels.
- "Map Collection" → Collection (not StillImage) when described as a curated aggregation.
- "API delivering data" → Service (not Dataset); the data is the payload, not the resource.
- "Mobile app for X" → Software (not Service) when the user installs it.

### 2.3 Domain
- Use the most specific applicable label.
- For multi-domain resources, choose the **primary** stated domain.
- If no clear domain match, choose `other` (do not force-fit).

### 2.4 License presence
- "CC-BY-4.0", "MIT", "GPL", "proprietary" → yes.
- "Open data", "publicly available" → unclear (no explicit license).
- No statement → no.

### 2.5 PII presence
- Email addresses, phone numbers, national-ID numbers, credit-card numbers → yes.
- Aggregate counts (e.g., "5,000 patients") → no.
- "Anonymized" / "de-identified" → no (unless something specific persists).

---

## 3. Edge cases & adjudication

When two annotators disagree, the senior annotator + PI meet to resolve. Document the final decision and the reasoning in the adjudication log (template in `irb/adjudication_log_template.xlsx`, to be supplied at study start).

---

## 4. Quality check

After every 30 documents, take a 10-minute break. After the first 30, the team holds a calibration call (15 min) to discuss any systematic discrepancies before continuing.

---

## 5. Inter-annotator reliability targets

| Field | Target κ (post-calibration) |
|-------|:---:|
| Title span | ≥ 0.80 (exact match) |
| DCMI type | ≥ 0.70 |
| Domain | ≥ 0.65 |
| License presence | ≥ 0.80 (categorical) |
| PII presence | ≥ 0.85 (categorical) |


ewpage

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


ewpage

# Data Management Plan (DMP)

**Project:** Metadata KG Human Evaluation (E9 / E10 / E11)
**PI:** Wirapong Chansanam (KKU)
**Standard:** Aligned with FAIR principles and KKU Research Data Management policy.

---

## 1. Data sources

| Data | Source | Volume (est.) | Sensitivity |
|------|--------|:---:|:---:|
| Annotation spreadsheets (E9) | 2 annotators × 120 docs | ~ 240 rows | Low |
| Adjudication notes (E9) | Joint annotator meeting | ~ 20 entries | Low |
| Task interaction logs (E10) | Streamlit instrumentation | ~ 100 rows × 20 users | Low |
| Screen recordings (E10) | Zoom / OBS | ~ 90 min × 20 = 30 h | Medium (face/voice) |
| SUS + NASA-TLX scores (E10) | Paper or Google Form | ~ 20 forms | Low |
| HITL review logs (E11) | System endpoint `/hitl/review` | ~ 100 records | Low |
| Gold-standard scoring (E11) | Blinded grader | ~ 200 rows | Low |

---

## 2. Storage and security

- **Live working storage:** KKU Google Workspace Drive (institutional account, two-factor authentication enabled).
- **Folder:** `/My Drive/OpenClawMacMini/graph_rag-V4/irb/raw_data/` (created post-IRB approval).
- **Permissions:** Restricted to PI only; co-investigators are added on need-to-know basis with explicit logging.
- **Backups:** Daily automated snapshot to a secondary KKU file server.
- **Encryption:** At-rest encryption via Google Workspace; PI laptop disk encryption (FileVault).

---

## 3. De-identification

- Participants receive pseudonymous IDs `E9-A01` (annotator), `E10-U01..U20`, `E11-R01`.
- The mapping table (real name ↔ ID) is stored in a **separate** spreadsheet (`master_key.xlsx`) accessible only to PI.
- All analysis files reference IDs only.

---

## 4. Retention and destruction

| Asset | Retention | Destruction method |
|-------|----------|--------------------|
| Master key file | 5 years | Secure shredding (file overwrite + drive empty) |
| Annotation data | 5 years | Same |
| Interaction logs | 5 years | Same |
| Screen recordings | **180 days** | File overwrite |
| SUS / NASA-TLX | 5 years | Same |
| Adjudication notes | 5 years | Same |

Schedule a calendar reminder to destroy short-retention assets on **Day 180** after each participant's session.

---

## 5. Sharing and publication

- **Aggregate / anonymous data** will accompany the manuscript on **Zenodo** (DOI minted) with a CC-BY-4.0 licence.
- **Raw participant-level data** will **not** be shared.
- **Code and notebooks** for the human-study analysis will be released on the project's GitHub repository under MIT.
- **Quotes** used in the manuscript will be paraphrased or fully anonymised, and only if the participant ticked the appropriate consent option.

---

## 6. Risk register

| Risk | Likelihood | Impact | Mitigation |
|------|:---:|:---:|------------|
| Re-identification via screen capture | Low | Medium | Limit access; blur identifiable backgrounds; 180-day cap |
| Master key leak | Very low | High | Single PI access; offline backup; password manager |
| Loss of consent forms | Low | Medium | Paper + scanned copy; both stored separately |
| Cloud provider outage | Low | Low | Local + secondary KKU server backup |

---

## 7. Roles and responsibilities

| Role | Person | Responsibility |
|------|--------|---------------|
| PI | Wirapong Chansanam | Overall data governance, ethics liaison |
| Research assistant (optional) | TBD | Daily data ingest, quality checks |
| KKU OHRP liaison | TBD | Ethics queries from participants |
| IT support | KKU Library tech team | Backup verification |

---

## 8. FAIR compliance summary

- **Findable:** Manuscript supplementary materials registered on Zenodo with DOI.
- **Accessible:** Open licence on aggregate data; raw data on justified request.
- **Interoperable:** CSV + JSON + DCAT 2 / DCMI metadata schema.
- **Reusable:** Documentation includes rubrics, scripts, and a clear data dictionary.


ewpage

# Risk–Benefit Assessment

## 1. Summary

**Overall risk classification:** Minimal (exempted / expedited review).
**Justification:** All participants are adult professionals performing tasks similar in scope and complexity to their everyday work. No physical, psychological, social, or legal risks beyond those of routine library employment.

---

## 2. Risk inventory

### 2.1 Physical risks
None. All tasks are computer-based and seated.

### 2.2 Psychological risks
- **Fatigue** during E9 (10-hour annotation task across 2 weeks).
  - **Mitigation:** Mandatory breaks every 30 documents; recommended cap of 2 hours/day; mid-task calibration call.
- **Performance anxiety** in E10 (think-aloud while observed).
  - **Mitigation:** Emphasise that the *system* is being evaluated, not the participant; no time pressure; right to stop any task without consequence.

### 2.3 Social risks
- **Professional embarrassment** if usability scores are unexpectedly low.
  - **Mitigation:** Individual-level data are never shared. Manuscript reports only aggregate statistics.
- **Privacy** if screen-recording captures unrelated content.
  - **Mitigation:** Participants are instructed to close personal applications; screen is recorded only during the scripted tasks; recordings retained 180 days then destroyed.

### 2.4 Legal / employment risks
None. Participation is outside the participants' employment relationship; no employer reporting.

### 2.5 Data privacy risks
- **PII in screen recordings:** Faces, voices, possibly visible window titles.
  - **Mitigation:** See DMP; consent-tiered recording option; 180-day retention.
- **Master key leak:** Could re-identify participants.
  - **Mitigation:** PI-only access; separate storage from analysis data.

---

## 3. Benefits

### 3.1 Direct benefits
- **Honorarium** (THB 500–5,000) commensurate with effort.
- **Skill development:** Hands-on experience with state-of-the-art AI metadata tools.
- **Network:** Connection to KKU research and the broader Thai library community.

### 3.2 Societal benefits
- Validated, openly released metadata-automation tool for the Thai cultural-heritage and academic-data sectors.
- Documented best practices for combining LLMs with classical cataloguing workflows.
- Contribution to FAIR / DCAT 2 adoption in Southeast Asia.

---

## 4. Risk–benefit balance

The combined risks are minimal and adequately mitigated. The professional, societal, and direct benefits substantially outweigh residual risks. We therefore consider the study **ethically justified** at the minimal-risk level and request **expedited review**.

---

## 5. Adverse-event reporting protocol

In the unlikely event of any participant complaint or distress:

1. The session is paused immediately.
2. PI documents the incident in the adverse-event log within 24 hours.
3. Incident report submitted to KKU Human Research Ethics Committee within 7 days.
4. If the event is deemed serious, the study is paused pending HREC review.


ewpage

# Timeline and Budget

## 1. Master timeline (post-IRB approval, 10 weeks total)

| Week | Phase | Activities | Deliverables |
|:---:|------|------------|--------------|
| -2 | Pre-launch | IRB approval; pilot test (n = 2) | Pilot report; refined materials |
| 1–2 | E9 IAA | Annotator briefing; independent labelling; adjudication | Consolidated gold set; per-field κ |
| 3 | E10 prep | Streamlit staging URL; recruit 20 users | Recruitment confirmed |
| 4–6 | E10 sessions | 6–8 sessions per week | All SUS / NASA-TLX data; recordings |
| 7 | E11 prep | Sample 100 ambiguous docs from production; brief reviewer | A/B branch outputs |
| 7–8 | E11 grading | Branch A automation; Branch B HITL; blinded gold scoring | Per-doc F1; review times |
| 9 | Analysis | All statistical analyses; figures | Stats tables; figures |
| 10 | Write-up | Manuscript revision (Sections 5.5–5.7 → empirical results) | Updated manuscript draft |

---

## 2. Budget (THB)

| Item | Quantity | Unit cost | Subtotal |
|------|:---:|:---:|---:|
| **Honoraria** | | | |
| E9 annotators | 2 | 3,000 | 6,000 |
| E10 participants | 20 | 500 | 10,000 |
| E11 HITL reviewer | 1 | 5,000 | 5,000 |
| E11 gold-standard grader | 1 | 3,000 | 3,000 |
| Pilot participants | 2 | 500 | 1,000 |
| **Materials & refreshments** | | | |
| Refreshments (E10 sessions) | 20 | 150 | 3,000 |
| Stationery, printing | — | — | 1,500 |
| **Tools & infrastructure** | | | |
| Anthropic API (further evaluation rounds) | 1 | 1,000 | 1,000 |
| Zoom Pro (1 month) | 1 | 500 | 500 |
| Cloud storage overflow (Streamlit Cloud premium) | 1 | 1,500 | 1,500 |
| **Personnel** | | | |
| Research assistant (optional, 40 hours) | 1 | 250 | 10,000 |
| **Contingency (10 %)** | | | 4,250 |
| **TOTAL** | | | **46,750** |

(≈ USD 1,300 at THB 36 = USD 1)

---

## 3. Funding source

- **Primary:** Faculty of Humanities Research Grant 2026 (ทุนวิจัยคณะมนุษย์ 2569)
- **Secondary (optional):** KKU Research Promotion Fund

---

## 4. Cost-saving alternatives

If full budget is not approved:

| Option | Cost saving |
|--------|:---:|
| Skip optional research assistant | -10,000 |
| Drop second annotator (E9 with n = 1) — **not recommended** (no κ possible) | -3,000 |
| Use volunteer KKU library staff (n = 10 instead of 20 for E10) | -5,000 |
| Conduct all sessions remotely (no refreshments) | -3,000 |

**Minimum viable budget:** ≈ THB 23,750 (omits RA, halves E10 sample, remote-only).
