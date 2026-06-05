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
