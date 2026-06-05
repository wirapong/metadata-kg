"""Extended evaluation dataset v2 (120 documents).

Expansion from v1 (40 docs) → v2 (120 docs):
- Original 40 documents retained verbatim
- 80 new documents added across 11 DCMI types and 10+ domains
- Includes adversarial cases (ambiguous types, multi-domain, noisy text)
- Designed for Q1 evaluation with statistical power (n=120)

Stratification (v2):
- Dataset:           35 (29.2%)
- Text:              25 (20.8%)
- StillImage:        15 (12.5%)
- MovingImage:        5 ( 4.2%)
- Software:          12 (10.0%)
- Service:           12 (10.0%)
- Event:              8 ( 6.7%)
- Sound:              4 ( 3.3%)
- Collection:         2 ( 1.7%)
- InteractiveResource:2 ( 1.7%)
"""

from __future__ import annotations

from evaluation.eval_dataset import EXTRACTION_GOLD as _V1_GOLD


# ---------------------------------------------------------------------------
# v2 expansion (80 additional documents)
# ---------------------------------------------------------------------------
_V2_ADDITIONS: list[dict] = [
    # ---- Dataset additions (25 more, total 35) ----
    {"text": "Title: NSO Population Census 2024\nDescription: Provincial population, age, and household statistics from the National Statistical Office.", "expected": {"title": "Population Census", "type": "Dataset", "domain": "government"}},
    {"text": "Title: GISTDA Sentinel-2 Surface Reflectance\nDescription: Atmospherically corrected satellite imagery over Thailand 2020-2024.", "expected": {"title": "Sentinel-2", "type": "Dataset", "domain": "environment"}},
    {"text": "Title: Thai Bond Market Daily Prices\nDescription: Daily yield curves and clean prices for government and corporate bonds.", "expected": {"title": "Bond Market", "type": "Dataset", "domain": "finance"}},
    {"text": "Title: Bangkok Taxi Trajectory Dataset\nDescription: Anonymized GPS traces of 5,000 taxis over one month.", "expected": {"title": "Taxi Trajectory", "type": "Dataset", "domain": "transport"}},
    {"text": "Title: Wheat Yield Prediction Features\nDescription: Multispectral and weather features for yield modeling.", "expected": {"title": "Wheat Yield", "type": "Dataset", "domain": "agriculture"}},
    {"text": "Title: KKU MOOC Learning Logs\nDescription: De-identified clickstream data from 12 online courses.", "expected": {"title": "MOOC Learning", "type": "Dataset", "domain": "education"}},
    {"text": "Title: ASEAN Energy Consumption 2020-2024\nDescription: Annual electricity and fossil-fuel consumption by member state.", "expected": {"title": "Energy Consumption", "type": "Dataset", "domain": "environment"}},
    {"text": "Title: Thai Restaurant Reviews Sentiment\nDescription: 50,000 Wongnai reviews labeled positive/neutral/negative.", "expected": {"title": "Restaurant Reviews", "type": "Dataset", "domain": "culture"}},
    {"text": "Title: Bangkok Crime Incident Report 2023\nDescription: Geo-coded incidents from the Royal Thai Police.", "expected": {"title": "Crime Incident", "type": "Dataset", "domain": "government"}},
    {"text": "Title: Mekong River Discharge\nDescription: Daily flow measurements at 12 gauging stations.", "expected": {"title": "Mekong Discharge", "type": "Dataset", "domain": "environment"}},
    {"text": "Title: Customs Import-Export Records 2024\nDescription: HS-code level trade statistics from Thai Customs.", "expected": {"title": "Import-Export", "type": "Dataset", "domain": "government"}},
    {"text": "Title: Thai Hospital Bed Capacity\nDescription: ICU and ward bed counts by province during COVID surges.", "expected": {"title": "Hospital Bed", "type": "Dataset", "domain": "health"}},
    {"text": "Title: Drone-captured Rice Field Imagery\nDescription: 12,000 georeferenced UAV photos with growth-stage labels.", "expected": {"title": "Drone Rice", "type": "Dataset", "domain": "agriculture"}},
    {"text": "Title: Thai Court Case Citation Network\nDescription: Citation graph of Supreme Court rulings 1995-2024.", "expected": {"title": "Court Case", "type": "Dataset", "domain": "government"}},
    {"text": "Title: Bangkok Urban Tree Inventory\nDescription: GPS-tagged tree species, DBH, and health status.", "expected": {"title": "Urban Tree", "type": "Dataset", "domain": "environment"}},
    {"text": "Title: KKU Research Publication Bibliography\nDescription: Scopus-indexed records of all KKU outputs 2010-2024.", "expected": {"title": "Research Publication", "type": "Dataset", "domain": "education"}},
    {"text": "Title: Thai Banking Mobile Transactions\nDescription: Aggregated PromptPay daily volume by region.", "expected": {"title": "Mobile Transactions", "type": "Dataset", "domain": "finance"}},
    {"text": "Title: Songkran Travel Mobility Data\nDescription: Anonymized phone-tower movement during 2024 holidays.", "expected": {"title": "Songkran Mobility", "type": "Dataset", "domain": "transport"}},
    {"text": "Title: Thai Cancer Registry 2020-2024\nDescription: De-identified diagnosis and survival statistics.", "expected": {"title": "Cancer Registry", "type": "Dataset", "domain": "health"}},
    {"text": "Title: PEA Smart Meter Energy Profiles\nDescription: Hourly residential consumption from 10,000 households.", "expected": {"title": "Smart Meter", "type": "Dataset", "domain": "environment"}},
    {"text": "Title: Bangkok Property Transaction Prices\nDescription: Quarterly condo and house sales 2018-2024.", "expected": {"title": "Property Transaction", "type": "Dataset", "domain": "finance"}},
    {"text": "Title: Thai Tourist Arrivals by Nationality\nDescription: Monthly visitor counts from immigration data.", "expected": {"title": "Tourist Arrivals", "type": "Dataset", "domain": "transport"}},
    {"text": "Title: Mekong Fish Species Survey\nDescription: Multi-year biodiversity census from 30 sampling sites.", "expected": {"title": "Fish Species", "type": "Dataset", "domain": "environment"}},
    {"text": "Title: KKU Student Course Enrolment 2023\nDescription: Aggregated, anonymized registrations by faculty.", "expected": {"title": "Course Enrolment", "type": "Dataset", "domain": "education"}},
    {"text": "Title: Thai Inflation Index Components\nDescription: Monthly CPI sub-indices from Bank of Thailand.", "expected": {"title": "Inflation Index", "type": "Dataset", "domain": "finance"}},

    # ---- Text/Articles additions (15 more, total 25) ----
    {"text": "Title: Universal Health Coverage Whitepaper\nDescription: Position paper from the National Health Security Office on UHC reform.", "expected": {"title": "Universal Health Coverage", "type": "Text", "domain": "health"}},
    {"text": "Title: Smart Agriculture Roadmap 2030\nDescription: Ministry of Agriculture strategy document for precision farming.", "expected": {"title": "Smart Agriculture", "type": "Text", "domain": "agriculture"}},
    {"text": "Title: Bangkok BMA Annual Budget Report\nDescription: Fiscal year 2024 budget allocations and outturn.", "expected": {"title": "BMA Annual Budget", "type": "Text", "domain": "government"}},
    {"text": "Title: Thai Buddhist Studies Journal Vol 24\nDescription: Peer-reviewed articles on Pali canon scholarship.", "expected": {"title": "Buddhist Studies", "type": "Text", "domain": "culture"}},
    {"text": "Title: National Cyber Security Strategy\nDescription: Five-year plan from the NCSA.", "expected": {"title": "Cyber Security Strategy", "type": "Text", "domain": "government"}},
    {"text": "Title: Tropical Medicine Research Bulletin\nDescription: Mahidol research compilation on dengue and malaria.", "expected": {"title": "Tropical Medicine", "type": "Text", "domain": "health"}},
    {"text": "Title: Thai Cuisine Heritage Inventory\nDescription: UNESCO submission documenting regional dishes.", "expected": {"title": "Cuisine Heritage", "type": "Text", "domain": "culture"}},
    {"text": "Title: Bond Market Development Plan 2024\nDescription: SEC Thailand consultation paper on retail bonds.", "expected": {"title": "Bond Market Development", "type": "Text", "domain": "finance"}},
    {"text": "Title: KKU Strategic Plan 2025-2030\nDescription: University-wide research and education roadmap.", "expected": {"title": "KKU Strategic Plan", "type": "Text", "domain": "education"}},
    {"text": "Title: Mekong Basin Sustainable Development\nDescription: MRC technical brief on hydropower trade-offs.", "expected": {"title": "Mekong Basin", "type": "Text", "domain": "environment"}},
    {"text": "Title: Thai Industry 4.0 Adoption Survey\nDescription: NSTDA report on manufacturing digitalization.", "expected": {"title": "Industry 4.0", "type": "Text", "domain": "government"}},
    {"text": "Title: ASEAN Connectivity Master Plan 2025\nDescription: Regional infrastructure and transport blueprint.", "expected": {"title": "ASEAN Connectivity", "type": "Text", "domain": "transport"}},
    {"text": "Title: Soft Power Diplomacy Policy Brief\nDescription: Ministry of Foreign Affairs paper on cultural exports.", "expected": {"title": "Soft Power", "type": "Text", "domain": "culture"}},
    {"text": "Title: Climate Disclosure Framework Thailand\nDescription: TCFD-aligned reporting guidance for listed firms.", "expected": {"title": "Climate Disclosure", "type": "Text", "domain": "finance"}},
    {"text": "Title: National Open Data Action Plan\nDescription: DGA roadmap for government data publication.", "expected": {"title": "Open Data Action", "type": "Text", "domain": "government"}},

    # ---- StillImage additions (10 more, total 15) ----
    {"text": "Title: Wat Phra Kaew Architecture Photography\nDescription: 300 high-resolution architectural photos of the Grand Palace.", "expected": {"title": "Wat Phra Kaew", "type": "StillImage", "domain": "culture"}},
    {"text": "Title: Thai Beetle Species Photo Atlas\nDescription: Macro photographs of 450 coleoptera species.", "expected": {"title": "Beetle Species", "type": "StillImage", "domain": "environment"}},
    {"text": "Title: Songkhla Lake Aerial Photography\nDescription: Aerial survey imagery of lake ecosystem 2024.", "expected": {"title": "Songkhla Lake", "type": "StillImage", "domain": "environment"}},
    {"text": "Title: Thai Royal Coronation Photo Archive\nDescription: Official photographs of the 2019 coronation ceremony.", "expected": {"title": "Royal Coronation", "type": "StillImage", "domain": "culture"}},
    {"text": "Title: Diabetic Retinopathy Fundus Images\nDescription: 8,000 retinal photographs graded by ophthalmologists.", "expected": {"title": "Diabetic Retinopathy", "type": "StillImage", "domain": "health"}},
    {"text": "Title: Mango Disease Symptom Photographs\nDescription: 2,500 labeled images of fungal and bacterial infections.", "expected": {"title": "Mango Disease", "type": "StillImage", "domain": "agriculture"}},
    {"text": "Title: Bangkok Streetscape Photography Project\nDescription: 1,200 urban scenes documenting neighborhood change.", "expected": {"title": "Streetscape", "type": "StillImage", "domain": "culture"}},
    {"text": "Title: NASA MODIS Cloud Cover Snapshots\nDescription: Daily cloud-cover imagery over Southeast Asia.", "expected": {"title": "MODIS Cloud", "type": "StillImage", "domain": "environment"}},
    {"text": "Title: Thai Handicraft Product Photography\nDescription: Studio photos of OTOP textile and silverware products.", "expected": {"title": "Handicraft Product", "type": "StillImage", "domain": "culture"}},
    {"text": "Title: KKU Campus Drone Mapping Imagery\nDescription: Orthorectified UAV photos of all 8 campuses.", "expected": {"title": "Campus Drone", "type": "StillImage", "domain": "education"}},

    # ---- MovingImage (5 new) ----
    {"text": "Title: Thai Folk Dance Performance Videos\nDescription: HD recordings of 50 traditional dances across regions.", "expected": {"title": "Folk Dance", "type": "MovingImage", "domain": "culture"}},
    {"text": "Title: Surgery Training Video Library\nDescription: 200 laparoscopic procedures with expert commentary.", "expected": {"title": "Surgery Training", "type": "MovingImage", "domain": "health"}},
    {"text": "Title: Bangkok Traffic Camera Footage\nDescription: 24-hour CCTV feeds from 80 intersections, anonymized.", "expected": {"title": "Traffic Camera", "type": "MovingImage", "domain": "transport"}},
    {"text": "Title: Wildlife Camera-Trap Video Collection\nDescription: 5,000 motion-triggered clips from Khao Yai National Park.", "expected": {"title": "Camera-Trap", "type": "MovingImage", "domain": "environment"}},
    {"text": "Title: Thai Educational Lecture Recording Archive\nDescription: 1,500 recorded lectures across STEM disciplines.", "expected": {"title": "Educational Lecture", "type": "MovingImage", "domain": "education"}},

    # ---- Software additions (7 more, total 12) ----
    {"text": "Title: TLite Thai Text Normalizer\nDescription: Lightweight library for tokenizing and normalizing Thai script.", "expected": {"title": "TLite", "type": "Software", "domain": "education"}},
    {"text": "Title: SEAClimate Downscaling Toolkit\nDescription: Python package for regional climate model downscaling.", "expected": {"title": "SEAClimate", "type": "Software", "domain": "environment"}},
    {"text": "Title: ThaiOCR Document Reader\nDescription: Open-source CTC-based OCR engine optimized for Thai script.", "expected": {"title": "ThaiOCR", "type": "Software", "domain": "education"}},
    {"text": "Title: HealthRisk Mobile App\nDescription: Risk-stratification application for chronic disease screening.", "expected": {"title": "HealthRisk", "type": "Software", "domain": "health"}},
    {"text": "Title: SmartHarvest Computer Vision Kit\nDescription: Edge ML toolkit for tropical fruit ripeness detection.", "expected": {"title": "SmartHarvest", "type": "Software", "domain": "agriculture"}},
    {"text": "Title: BangkokGo Routing Engine\nDescription: Open-source multimodal routing for Bangkok public transit.", "expected": {"title": "BangkokGo", "type": "Software", "domain": "transport"}},
    {"text": "Title: KKU Identity SSO Library\nDescription: SAML 2.0 single-sign-on integration toolkit.", "expected": {"title": "KKU Identity SSO", "type": "Software", "domain": "education"}},

    # ---- Service additions (7 more, total 12) ----
    {"text": "Title: Thailand National DOI Registration Service\nDescription: REST API for minting DOIs for Thai research outputs.", "expected": {"title": "DOI Registration", "type": "Service", "domain": "education"}},
    {"text": "Title: Air4Thai Real-time AQI Web Service\nDescription: SOAP and REST endpoints serving Pollution Control Department air-quality data.", "expected": {"title": "Air4Thai", "type": "Service", "domain": "environment"}},
    {"text": "Title: ThaiID Verification API\nDescription: Government identity verification service for KYC integration.", "expected": {"title": "ThaiID Verification", "type": "Service", "domain": "government"}},
    {"text": "Title: SET Realtime Quote Streaming\nDescription: WebSocket feed of Stock Exchange of Thailand tick data.", "expected": {"title": "SET Realtime", "type": "Service", "domain": "finance"}},
    {"text": "Title: Telemedicine Consultation Platform\nDescription: HIPAA-compliant video consultation service for rural clinics.", "expected": {"title": "Telemedicine", "type": "Service", "domain": "health"}},
    {"text": "Title: AgriMarket Price Lookup Service\nDescription: REST API delivering daily wholesale produce prices.", "expected": {"title": "AgriMarket", "type": "Service", "domain": "agriculture"}},
    {"text": "Title: TM30 Foreign Resident Reporting Service\nDescription: Immigration Bureau API for landlord reporting requirements.", "expected": {"title": "TM30 Reporting", "type": "Service", "domain": "government"}},

    # ---- Event (5 more, total 8) ----
    {"text": "Title: Royal Ploughing Ceremony 2024\nDescription: Annual government ceremony marking the rice planting season.", "expected": {"title": "Ploughing Ceremony", "type": "Event", "domain": "culture"}},
    {"text": "Title: Thailand National Software Contest 2024\nDescription: Three-month nationwide coding competition with 2,000 teams.", "expected": {"title": "Software Contest", "type": "Event", "domain": "education"}},
    {"text": "Title: Loy Krathong Festival Bangkok\nDescription: City-wide cultural festival on the night of the full moon.", "expected": {"title": "Loy Krathong", "type": "Event", "domain": "culture"}},
    {"text": "Title: Bangkok International Film Festival\nDescription: Two-week film showcase with 150 international titles.", "expected": {"title": "International Film Festival", "type": "Event", "domain": "culture"}},
    {"text": "Title: Asia Bio Innovation Summit Bangkok\nDescription: Industry-academic conference on biotech commercialization.", "expected": {"title": "Bio Innovation Summit", "type": "Event", "domain": "education"}},

    # ---- Sound (2 more, total 4) ----
    {"text": "Title: Thai Language Pronunciation Audio Reference\nDescription: 5,000 native-speaker recordings for phonetics research.", "expected": {"title": "Pronunciation Audio", "type": "Sound", "domain": "education"}},
    {"text": "Title: ASEAN Underwater Acoustics Recordings\nDescription: Reef soundscape recordings from 12 dive sites.", "expected": {"title": "Underwater Acoustics", "type": "Sound", "domain": "environment"}},

    # ---- Collection (2 new — tests "Dataset vs Collection" ambiguity) ----
    {"text": "Title: KKU Special Collections Manuscripts\nDescription: A curated collection of palm-leaf manuscripts and rare books.", "expected": {"title": "Special Collections", "type": "Collection", "domain": "culture"}},
    {"text": "Title: National Archives Digital Collection 2024\nDescription: Aggregated digitized records from royal archives, military files, and cabinet papers.", "expected": {"title": "Archives Digital Collection", "type": "Collection", "domain": "government"}},

    # ---- InteractiveResource (2 new) ----
    {"text": "Title: Thailand National Statistics Dashboard\nDescription: Interactive web dashboard for exploring NSO indicators.", "expected": {"title": "Statistics Dashboard", "type": "InteractiveResource", "domain": "government"}},
    {"text": "Title: KKU Virtual Anatomy Lab\nDescription: WebGL-based interactive 3D anatomy learning platform.", "expected": {"title": "Virtual Anatomy", "type": "InteractiveResource", "domain": "education"}},
]


# Final v2 gold set
EXTRACTION_GOLD_V2: list[dict] = _V1_GOLD + _V2_ADDITIONS

assert len(EXTRACTION_GOLD_V2) == 120, f"Expected 120 docs, got {len(EXTRACTION_GOLD_V2)}"


# ---------------------------------------------------------------------------
# Quality check helper
# ---------------------------------------------------------------------------
def summarize_distribution() -> dict:
    from collections import Counter
    types = Counter(c["expected"]["type"] for c in EXTRACTION_GOLD_V2)
    domains = Counter(c["expected"]["domain"] for c in EXTRACTION_GOLD_V2)
    return {"total": len(EXTRACTION_GOLD_V2), "types": dict(types), "domains": dict(domains)}


if __name__ == "__main__":
    import json
    print(json.dumps(summarize_distribution(), indent=2))
