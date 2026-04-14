# Quick Start – MSG-3 to Maximo Converter

**Versie:** 0.2.0 | **Python:** 3.11+

---

## 1. Installatie

```powershell
# Navigeer naar de project directory
cd "C:\Users\pmec\Documents\Stage Babcock\MSGConverter"

# Controleer Python versie (moet 3.11+ zijn)
python --version

# Maak virtual environment (eenmalig)
python -m venv venv

# Activeer virtual environment
.\venv\Scripts\Activate.ps1        # PowerShell
# of: venv\Scripts\activate.bat    # cmd

# Installeer dependencies
pip install -r requirements.txt

# Verify installatie
python -c "import openpyxl, pandas, rich, requests; print('OK – alle dependencies aanwezig')"
```

---

## 2. Omgevingsvariabelen instellen

```powershell
# Kopieer het voorbeeld-configuratiebestand
copy .env.example .env

# Open en vul de waarden in (Maximo URL, API key, org ID)
notepad .env
```

Vereiste variabelen:

| Variabele | Beschrijving | Voorbeeld |
|-----------|-------------|---------|
| `MAXIMO_BASE_URL` | Maximo basis-URL | `https://maximo.babcock.local` |
| `MAXIMO_API_KEY` | API sleutel (of gebruik MAXIMO_USERNAME/PASSWORD) | `abc123xyz` |
| `MAXIMO_ORG_ID` | Organisatie ID in Maximo | `SCHIPHOL` |
| `MAXIMO_ITEM_SET` | Item Set | `MSG3-MAINT` |

---

## 3. Gebruik – CLI

### Volledig verwerken (standaard)

```powershell
# Verwerk een MSG-3 Excel bestand (parse + valideer + map)
python -m src.main examples\msg3_example.xlsx

# Met JSON output naar bestand
python -m src.main examples\msg3_example.xlsx --output output\result.json

# Uitgebreide logging
python -m src.main examples\msg3_example.xlsx --verbose
```

### Change detection (vergelijk met vorige versie)

```powershell
# Sla eerste run op als baseline
python -m src.main msg3_v1.xlsx --output output\v1.json

# Vergelijk tweede run met baseline
python -m src.main msg3_v2.xlsx --output output\v2.json --previous output\v1.json
```

### Validatie only

```powershell
# Alleen valideren (geen mapping)
python -m src.main examples\msg3_example.xlsx --mode validate
```

### Parse only (JSON structuur bekijken)

```powershell
# Alleen parsen naar JSON (geen validatie, geen mapping)
python -m src.main examples\msg3_example.xlsx --mode parse --output output\parsed.json
```

### Quiet mode (alleen JSON, geen banner/samenvatting)

```powershell
# Geschikt voor scripting / pipen
python -m src.main examples\msg3_example.xlsx --quiet --output output\result.json
```

### Logging naar bestand

```powershell
python -m src.main examples\msg3_example.xlsx --log-file logs\run.log
```

---

## 4. Alle CLI opties

```
usage: python -m src.main [-h] [--mode {full,validate,parse}]
                           [--output OUTPUT] [--previous PREVIOUS]
                           [--skip-validation] [--verbose] [--quiet]
                           [--log-file LOG_FILE] [--version]
                           excel_file

Positional arguments:
  excel_file            Pad naar MSG-3 Excel bestand

Options:
  -h, --help            Toon help bericht en sluit af
  --mode {full,validate,parse}
                        Verwerkingsmodus (default: full)
  --output, -o          Pad voor JSON output bestand (default: stdout)
  --previous            Pad naar vorige JSON output voor change detection
  --skip-validation     Sla validatie over (niet aanbevolen)
  --verbose, -v         Uitgebreide logging (DEBUG niveau)
  --quiet, -q           Alleen JSON output, geen banner/samenvatting
  --log-file LOG_FILE   Schrijf logs naar bestand
  --version             Toon versienummer
```

---

## 5. Testen

```powershell
# Alle tests draaien
python -m pytest tests/

# Alleen unit tests
python -m pytest tests/unit/ -v

# Alleen integratie tests
python -m pytest tests/integration/ -v

# Met coverage rapport (HTML)
python -m pytest tests/ --cov=src --cov-report=html

# Coverage rapport openen
Start-Process "htmlcov\index.html"
```

Huidige status: **201 tests**, **84% coverage**, alle tests groen.

---

## 6. Project structuur

```
MSGConverter/
├── src/
│   ├── main.py                    # CLI entry point
│   ├── parser/
│   │   ├── excel_reader.py        # Excel lezen
│   │   └── msg3_parser.py         # MSG-3 data parsen
│   ├── validator/
│   │   ├── msg3_validator.py      # Structuur- en veldvalidatie
│   │   └── business_rules.py      # 90 business rules
│   ├── mapping/
│   │   ├── msg3_maximo_mapper.py  # Orchestratie mapper
│   │   ├── item_mapper.py         # Item Master records
│   │   ├── pm_mapper.py           # Preventive Maintenance records
│   │   └── jobplan_mapper.py      # Job Plan records
│   ├── change_detection/
│   │   └── change_detector.py     # Versievergelijking
│   └── maximo_connector/
│       ├── rest_client.py         # Lage-niveau HTTP client
│       └── maximo_client.py       # Hoge-niveau Maximo API client
├── tests/
│   ├── unit/                      # Unit tests per module
│   ├── integration/               # End-to-end pipeline tests
│   └── fixtures/                  # Test Excel bestand
├── docs/
│   ├── scrum/sprints/             # Sprint planning, review, retrospective
│   ├── testcases/                 # Teststrategie en testresultaten
│   └── technisch-ontwerp/         # SDD, business rules, UML
├── requirements.txt               # Productie- en dev-dependencies
├── pytest.ini                     # Test configuratie
├── .coveragerc                    # Coverage configuratie
├── .env.example                   # Voorbeeld omgevingsvariabelen
└── QUICKSTART.md                  # Dit bestand
```

---

## 7. Veelgestelde problemen

### ModuleNotFoundError bij `python -m src.main`

Zorg dat je de opdracht uitvoert vanuit de `MSGConverter/` map en dat de venv actief is:

```powershell
cd "C:\Users\pmec\Documents\Stage Babcock\MSGConverter"
.\venv\Scripts\Activate.ps1
python -m src.main --help
```

### Validatie gefaald – CRITICAL errors

Controleer de task codes in het Excel bestand. Verplicht formaat: `{chapter}-{system}-{subsystem}-{sequence}` (bijv. `32-11-01-001`).

### `rich` niet gevonden

```powershell
pip install rich
```

### UnicodeDecodeError in Windows console

Stel de console encoding in:

```powershell
$env:PYTHONIOENCODING = "utf-8"
python -m src.main examples\msg3_example.xlsx
```

---

## 8. Business rules

De applicatie valideert 90 business rules verdeeld over 6 categorieën:

| Categorie | Regels | Voorbeelden |
|-----------|--------|-------------|
| Structural (STR) | 15 | Verplichte velden, bestandsformaat |
| Safety (SAF) | 15 | Veiligheidskritische taken |
| Airworthiness (AIR) | 15 | Luchwaardigheidsregels |
| Maintenance (MNT) | 15 | Onderhoudsinterval-regels |
| Logistics & Inventory (LOG) | 20 | Commodity codes, Maximo veldlimieten |
| Regulatory (REG) | 10 | Complianceregels |

Zie `docs/technisch-ontwerp/business-rules.md` voor de volledige lijst.

---

**Vragen of problemen?** Zie `docs/` voor gedetailleerde documentatie of raadpleeg de testcases in `tests/`.
