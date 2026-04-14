# MSG-3 → Maximo Converter

> Geautomatiseerde koppeling tussen MSG-3 Excel-onderhoudsdata en IBM Maximo voor Babcock Schiphol.

**Versie:** v0.2.0 &nbsp;|&nbsp; **Python:** 3.11+ &nbsp;|&nbsp; **Tests:** 201 &nbsp;|&nbsp; **Coverage:** 84% &nbsp;|&nbsp; **Status:** In ontwikkeling

---

## Wat doet het?

De applicatie leest een MSG-3 Excel-bestand in, valideert de data volgens 90 business rules, detecteert wijzigingen ten opzichte van een vorige versie, en genereert Maximo-objecten (Item Master, Preventive Maintenance, Job Plan, Commodity) klaar voor import via de Maximo REST API.

```
MSG-3 Excel  →  Parser  →  Validator  →  Change Detection  →  Mapper  →  Maximo REST API
```

**Tijdwinst:** Handmatig ~40 uur per MSG-3 revisie → geautomatiseerd <5 minuten.

---

## Installatie

```powershell
# Clone repository
git clone <repository-url>
cd MSGConverter

# Maak virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1          # PowerShell
# venv\Scripts\activate.bat          # cmd

# Installeer dependencies
pip install -r requirements.txt

# Configureer omgevingsvariabelen
copy .env.example .env
notepad .env                         # Vul Maximo URL en API key in
```

---

## Gebruik

### Volledig verwerken

```powershell
python -m src.main examples\msg3_redesign.xlsx
```

```
╭──────────────────────────────────────────────────────────────────╮
│  MSG-3 -> Maximo Integration  v0.2.0                             │
│  Comakership ADSD - Babcock Schiphol                             │
╰──────────────────────────────────────────────────────────────────╯

  [1/4] Excel parsing...       ████████████ 25%
  [2/4] Data validatie...      ████████████ 50%
  [3/4] Change detection...    ████████████ 75%
  [4/4] Mapping naar Maximo... ████████████ 100%

╭─────────────────────────────────╮
│ RESULTAAT: SUCCESVOL            │
╰─────────────────────────────────╯
  Formaat        redesign
  Taken          10 geparseerd, 0 parse fouten
  Validatie      OK (0 errors, 0 warnings)
  commodities    11 objecten
  items          10 objecten
  pm             10 objecten
  jobplan        10 objecten
```

### Change detection (versievergelijking)

```powershell
# Sla baseline op
python -m src.main msg3_v1.xlsx --output output\v1.json

# Vergelijk met nieuwe versie
python -m src.main msg3_v2.xlsx --output output\v2.json --previous output\v1.json
```

### Alle opties

```
python -m src.main <excel_file> [opties]

  --mode {full,validate,parse}   Verwerkingsmodus (default: full)
  --output, -o <pad>             JSON output bestand
  --previous <pad>               Vorige JSON voor change detection
  --skip-validation              Validatie overslaan
  --verbose, -v                  DEBUG logging
  --quiet, -q                    Alleen JSON output
  --log-file <pad>               Loggen naar bestand
  --version                      Toon versienummer
```

Zie [QUICKSTART.md](QUICKSTART.md) voor uitgebreide instructies.

---

## Testen

```powershell
# Alle tests
python -m pytest tests/

# Alleen unit tests
python -m pytest tests/unit/ -v

# Met coverage rapport
python -m pytest tests/ --cov=src --cov-report=html
Start-Process "htmlcov\index.html"
```

| Metric | Waarde |
|--------|--------|
| Tests | **201** (0 failed) |
| Coverage | **84%** (drempel: 80%) |
| Uitvoertijd | ~10 seconden |

---

## Projectstructuur

```
MSGConverter/
├── src/
│   ├── main.py                    # CLI entry point, pipeline orchestratie
│   ├── parser/                    # Excel lezen en parsen naar MSG3Task dataclasses
│   ├── validator/                 # 90 business rules + structuurvalidatie
│   ├── mapping/                   # MSG-3 → Maximo objecten (Item, PM, JobPlan)
│   ├── change_detection/          # Versievergelijking (added/modified/deleted)
│   └── maximo_connector/          # REST client + Maximo API client
├── tests/
│   ├── unit/                      # Unit tests per module (162 tests)
│   ├── integration/               # End-to-end pipeline tests (16 tests)
│   └── fixtures/                  # Test Excel bestand
├── docs/
│   ├── scrum/sprints/             # Sprint planning, review, retrospective
│   ├── testcases/                 # Teststrategie en testresultaten
│   ├── technisch-ontwerp/         # SDD, business rules, UML, architectuur
│   ├── onderzoek/                 # Technisch onderzoeksrapport
│   └── uml/                       # PlantUML diagrammen (5 diagrammen)
├── examples/                      # Voorbeeld MSG-3 Excel bestanden
├── requirements.txt               # Dependencies
├── pytest.ini                     # Test configuratie
├── .coveragerc                    # Coverage configuratie
├── .env.example                   # Voorbeeld omgevingsvariabelen
└── QUICKSTART.md                  # Installatie- en gebruiksinstructies
```

---

## Business rules

90 gedefinieerde en geïmplementeerde business rules verdeeld over 6 categorieën:

| Categorie | Regels |
|-----------|--------|
| Structural (STR) | 15 |
| Safety (SAF) | 15 |
| Airworthiness (AIR) | 15 |
| Maintenance (MNT) | 15 |
| Logistics & Inventory (LOG) | 20 |
| Regulatory (REG) | 10 |

Zie [docs/technisch-ontwerp/business-rules.md](docs/technisch-ontwerp/business-rules.md) voor de volledige lijst.

---

## Technologie

| Doel | Library |
|------|---------|
| Excel parsing | `openpyxl`, `pandas` |
| HTTP/REST | `requests` (met retry) |
| Validatie | `pydantic`, business_rules.py |
| CLI output | `rich` (progress bar, kleur) |
| Configuratie | `python-dotenv` |
| Tests | `pytest`, `pytest-cov`, `pytest-mock` |

---

## Documentatie

| Document | Locatie |
|----------|---------|
| Software Design Document (SDD) | [docs/technisch-ontwerp/SDD-MSG3-Maximo-Converter.md](docs/technisch-ontwerp/SDD-MSG3-Maximo-Converter.md) |
| Teststrategie | [docs/testcases/01-teststrategie.md](docs/testcases/01-teststrategie.md) |
| Testresultaten | [docs/testcases/02-testresultaten.md](docs/testcases/02-testresultaten.md) |
| Business Rules | [docs/technisch-ontwerp/business-rules.md](docs/technisch-ontwerp/business-rules.md) |
| Sprint Planning / Review | [docs/scrum/sprints/](docs/scrum/sprints/) |
| Quick Start | [QUICKSTART.md](QUICKSTART.md) |
| Onderzoeksrapport | [docs/onderzoek/00-onderzoeksrapport.md](docs/onderzoek/00-onderzoeksrapport.md) |

---

## Context

**Opdrachtgever:** Babcock Schiphol (luchtvaartonderhoud)
**Student:** Pedro Eduardo Cardoso – Associate Degree Software Developer (ADSD), Windesheim
**Periode:** februari – juni 2026
**Begeleiders:** Matthijs Meijer, Rick Kramer (Babcock) · Arie Ismael (Windesheim)

### Comakership competenties

| Competentie | Bewijs |
|-------------|--------|
| Analyseren | MSG-3 structuuranalyse, 90 business rules gedefinieerd |
| Adviseren | Technologie-onderbouwing (Python vs C# vs Node.js) |
| Ontwerpen | SDD, UML-diagrammen, layered architectuur |
| Realiseren | 201 tests, 84% coverage, werkende end-to-end pipeline |
| Manage & Control | Sprint 1 + 2 planning/review/retrospective |

### AI-gebruik

Cursor AI (Claude) is gebruikt als development-assistent (AIAS niveau 3). ~75% van het werk is door Pedro (business rules, architectuur, logica, beslissingen), ~25% AI-assistentie (templates, boilerplate, refactoring). Zie [docs/ai/](docs/ai/) voor de volledige verantwoording.

---

## Licentie

Ontwikkeld in opdracht van Babcock Schiphol voor educatieve doeleinden (Comakership ADSD, Windesheim).

---

*Laatste update: 14 april 2026*
