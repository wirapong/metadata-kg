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
