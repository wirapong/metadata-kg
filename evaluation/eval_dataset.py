"""Extended evaluation dataset (gold standard) for Metadata KG.

40 metadata documents across 8 domains. Designed for Q1-grade evaluation:
- precision/recall on metadata extraction
- P@k / MRR / nDCG on search
- PII detection F1
- consistency validation coverage
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# EXTRACTION GOLD SET (40 documents, balanced across 8 DCMI types)
# ---------------------------------------------------------------------------
EXTRACTION_GOLD: list[dict] = [
    # ---- Dataset (10) ----
    {"text": "Title: Thailand COVID-19 Daily Cases 2024\nDescription: Provincial daily case counts and deaths from the Ministry of Public Health.\nTags: covid, health, Thailand, epidemiology", "expected": {"title": "COVID-19", "type": "Dataset", "domain": "health"}},
    {"text": "Title: Bangkok PM2.5 Hourly Monitoring\nDescription: Particulate matter readings from 80 air quality stations.\nKeywords: air-quality, PM25, Bangkok", "expected": {"title": "PM2.5", "type": "Dataset", "domain": "environment"}},
    {"text": "Title: Thai Stock Exchange Daily Close 2024\nDescription: SET index daily closing values and volume.", "expected": {"title": "Stock Exchange", "type": "Dataset", "domain": "finance"}},
    {"text": "Title: KKU Library Loan Records 2024\nDescription: Anonymized book circulation data from the central library.", "expected": {"title": "Library Loan", "type": "Dataset", "domain": "education"}},
    {"text": "Title: Chao Phraya River Water Quality\nDescription: Monthly DO, pH, and turbidity measurements.", "expected": {"title": "Water Quality", "type": "Dataset", "domain": "environment"}},
    {"text": "Title: Thailand National Election Results 2023\nDescription: Constituency-level vote counts.", "expected": {"title": "Election Results", "type": "Dataset", "domain": "government"}},
    {"text": "Title: Khon Kaen Hospital Admissions\nDescription: De-identified inpatient records with ICD-10 diagnoses.", "expected": {"title": "Hospital Admissions", "type": "Dataset", "domain": "health"}},
    {"text": "Title: Iris Flower Classification Set\nDescription: 150 samples, 4 features, 3 species.", "expected": {"title": "Iris", "type": "Dataset", "domain": "education"}},
    {"text": "Title: Thailand Rice Production by Province\nDescription: Yearly tonnage 2010-2024 from the Department of Agriculture.", "expected": {"title": "Rice Production", "type": "Dataset", "domain": "agriculture"}},
    {"text": "Title: Bangkok BTS Ridership 2024\nDescription: Hourly passenger counts at all 62 stations.", "expected": {"title": "BTS Ridership", "type": "Dataset", "domain": "transport"}},

    # ---- Text/Articles (10) ----
    {"text": "Title: Climate Adaptation Policy Brief 2024\nDescription: An overview of Thailand's national climate adaptation framework.", "expected": {"title": "Climate Adaptation", "type": "Text", "domain": "government"}},
    {"text": "Title: Annual Report KKU 2024\nDescription: Academic and research achievements for fiscal year 2024.", "expected": {"title": "Annual Report", "type": "Text", "domain": "education"}},
    {"text": "Title: SARS-CoV-2 Genomic Surveillance Manuscript\nDescription: Peer-reviewed paper on viral variants in Southeast Asia.", "expected": {"title": "Genomic Surveillance", "type": "Text", "domain": "health"}},
    {"text": "Title: Thai Penal Code Amendments 2024\nDescription: Full text of statutory changes.", "expected": {"title": "Penal Code", "type": "Text", "domain": "government"}},
    {"text": "Title: Open Banking Whitepaper Thailand\nDescription: Industry consultation paper on API standards.", "expected": {"title": "Open Banking", "type": "Text", "domain": "finance"}},
    {"text": "Title: PM2.5 Mortality Meta-Analysis\nDescription: Systematic review of 47 cohort studies.", "expected": {"title": "Mortality Meta-Analysis", "type": "Text", "domain": "health"}},
    {"text": "Title: Rice Genome Sequencing Report\nDescription: Technical bulletin on Hom Mali genome.", "expected": {"title": "Rice Genome", "type": "Text", "domain": "agriculture"}},
    {"text": "Title: Smart City Master Plan Khon Kaen\nDescription: 10-year urban development strategy.", "expected": {"title": "Smart City", "type": "Text", "domain": "government"}},
    {"text": "Title: AI Ethics Guidelines NSTDA\nDescription: National framework for trustworthy AI.", "expected": {"title": "AI Ethics", "type": "Text", "domain": "government"}},
    {"text": "Title: Open Government Data Best Practices\nDescription: Curated catalogue guidelines following DCAT 2.", "expected": {"title": "Open Government", "type": "Text", "domain": "government"}},

    # ---- Image / StillImage (5) ----
    {"text": "Title: Satellite Image Set Bangkok Floods 2011\nDescription: Sentinel-2 RGB tiles covering the 2011 flood.", "expected": {"title": "Satellite Image", "type": "StillImage", "domain": "environment"}},
    {"text": "Title: Thai Folk Art Photograph Archive\nDescription: 500 high-resolution images of regional crafts.", "expected": {"title": "Folk Art", "type": "StillImage", "domain": "culture"}},
    {"text": "Title: Medical X-Ray Pneumonia Dataset\nDescription: 5,000 chest radiographs labeled normal vs pneumonia.", "expected": {"title": "X-Ray", "type": "StillImage", "domain": "health"}},
    {"text": "Title: Rice Disease Leaf Image Set\nDescription: 3,000 photos labeled by 4 disease classes.", "expected": {"title": "Rice Disease", "type": "StillImage", "domain": "agriculture"}},
    {"text": "Title: Historical Map Collection Siam 1880-1932\nDescription: Scanned cartographic archive.", "expected": {"title": "Historical Map", "type": "StillImage", "domain": "culture"}},

    # ---- Software (5) ----
    {"text": "Title: PyKKU NLP Toolkit\nDescription: Open-source Thai NLP utilities; Python 3.11.", "expected": {"title": "PyKKU", "type": "Software", "domain": "education"}},
    {"text": "Title: ThaiGov-DCAT Validator\nDescription: CLI tool for DCAT 2 compliance.", "expected": {"title": "DCAT Validator", "type": "Software", "domain": "government"}},
    {"text": "Title: SmartFarm Decision App\nDescription: Mobile decision-support for paddy growers.", "expected": {"title": "SmartFarm", "type": "Software", "domain": "agriculture"}},
    {"text": "Title: Air Quality Forecast Service\nDescription: REST API delivering 24h PM2.5 forecasts.", "expected": {"title": "Air Quality Forecast", "type": "Software", "domain": "environment"}},
    {"text": "Title: KKU Library OPAC Source Code\nDescription: Open-source online catalogue.", "expected": {"title": "OPAC", "type": "Software", "domain": "education"}},

    # ---- Service (5) ----
    {"text": "Title: KKU SPARQL Endpoint\nDescription: Public RDF query service for university bibliographic graphs.", "expected": {"title": "SPARQL", "type": "Service", "domain": "education"}},
    {"text": "Title: NSTDA Open Data Portal API\nDescription: REST API for catalogue search.", "expected": {"title": "Open Data Portal", "type": "Service", "domain": "government"}},
    {"text": "Title: Thai Citation Index Web Service\nDescription: SOAP and REST endpoints for scholarly metadata.", "expected": {"title": "Citation Index", "type": "Service", "domain": "education"}},
    {"text": "Title: BAAC Loan Calculator Service\nDescription: Online calculator for agricultural loan estimates.", "expected": {"title": "Loan Calculator", "type": "Service", "domain": "finance"}},
    {"text": "Title: National Election Live Tally API\nDescription: WebSocket service streaming vote counts.", "expected": {"title": "Election Live Tally", "type": "Service", "domain": "government"}},

    # ---- Event (3) ----
    {"text": "Title: KKU Annual Research Forum 2024\nDescription: 3-day conference with 200 papers.", "expected": {"title": "Research Forum", "type": "Event", "domain": "education"}},
    {"text": "Title: Bangkok Music Festival 2024\nDescription: 2-week cultural event with 80 artists.", "expected": {"title": "Music Festival", "type": "Event", "domain": "culture"}},
    {"text": "Title: International AI Symposium Thailand\nDescription: Hybrid conference on responsible AI.", "expected": {"title": "AI Symposium", "type": "Event", "domain": "education"}},

    # ---- Sound (2) ----
    {"text": "Title: Thai Court Music Audio Archive\nDescription: 200 lossless recordings of Piphat ensembles.", "expected": {"title": "Court Music", "type": "Sound", "domain": "culture"}},
    {"text": "Title: Wildlife Bioacoustics Khao Yai\nDescription: 1,000 hours of forest sound recordings.", "expected": {"title": "Bioacoustics", "type": "Sound", "domain": "environment"}},
]

# ---------------------------------------------------------------------------
# SEARCH BENCHMARK (corpus 40 docs + 20 queries with rank-relevance)
# ---------------------------------------------------------------------------
SEARCH_CORPUS = [
    (f"ds:{i:03d}", d["expected"]["title"], d["text"].split("\n", 1)[-1][:200], d["expected"]["domain"])
    for i, d in enumerate(EXTRACTION_GOLD, 1)
]

# Each query maps to a list of relevant entity IDs (binary relevance; for nDCG we score by position)
SEARCH_QUERIES = [
    ("covid health Thailand", ["ds:001", "ds:013", "ds:016"]),
    ("PM2.5 air quality Bangkok", ["ds:002", "ds:029"]),
    ("stock market finance", ["ds:003", "ds:015", "ds:034"]),
    ("library bibliographic records", ["ds:004", "ds:031", "ds:033"]),
    ("water environment river", ["ds:005"]),
    ("election government Thailand", ["ds:006", "ds:035"]),
    ("hospital medical ICD", ["ds:007"]),
    ("iris flower classification", ["ds:008"]),
    ("rice agriculture production", ["ds:009", "ds:017", "ds:024", "ds:028"]),
    ("transport ridership BTS", ["ds:010"]),
    ("climate policy adaptation", ["ds:011"]),
    ("genome SARS-CoV-2 virus", ["ds:013"]),
    ("smart city urban planning", ["ds:018"]),
    ("AI ethics guidelines", ["ds:019"]),
    ("satellite flood image", ["ds:021"]),
    ("X-ray pneumonia medical image", ["ds:023"]),
    ("NLP Thai toolkit software", ["ds:026"]),
    ("SPARQL endpoint service", ["ds:031"]),
    ("research forum conference", ["ds:036", "ds:038"]),
    ("music audio Thai culture", ["ds:022", "ds:039"]),
]

# ---------------------------------------------------------------------------
# PII DETECTION TEST SET (positive = contains PII, negative = clean)
# ---------------------------------------------------------------------------
PII_TEST_SET = [
    # Positives — should be flagged
    ("Contact me at wirach@kku.ac.th for details", True, "email"),
    ("Reach out: alice.smith+test@example.co.th", True, "email"),
    ("Phone: 081-234-5678", True, "phone"),
    ("Call (02) 123-4567 anytime", True, "phone"),
    ("My credit card 4111 1111 1111 1111 is expired", True, "credit_card"),
    ("SSN 123-45-6789 for verification", True, "us_ssn"),
    ("Thai ID 1 2345 67890 12 3", True, "thai_national_id"),
    ("Mixed: email a@b.co and phone 089-111-2222", True, "email_phone"),
    ("Email: support@gov.th, urgent matter", True, "email"),
    ("Patient phone 02-555-1234 confirmed", True, "phone"),
    # Negatives — should pass
    ("Open dataset of air quality measurements", False, "clean"),
    ("Annual report from Department of Agriculture", False, "clean"),
    ("Iris flower dataset 150 samples 4 features", False, "clean"),
    ("Bangkok rainfall hourly measurements", False, "clean"),
    ("Thai folk art photograph archive", False, "clean"),
    ("Open source NLP toolkit for Thai language", False, "clean"),
    ("Satellite imagery from Sentinel-2 mission", False, "clean"),
    ("DCAT 2 metadata catalogue endpoint", False, "clean"),
    ("Vote tally for general election 2024", False, "clean"),
    ("Wildlife bioacoustics recordings Khao Yai", False, "clean"),
]
