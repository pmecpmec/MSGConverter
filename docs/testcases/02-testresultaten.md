# Testresultaten – MSG-3 to Maximo Converter

**Project:** MSG-3 to Maximo Converter
**Auteur:** Pedro Eduardo Cardoso
**Datum:** 14 april 2026
**Versie:** 1.0
**Test run:** `pytest tests/ --tb=no -q`

---

## 1. Samenvatting

| Metric | Waarde |
|--------|--------|
| Totaal aantal tests | **201** |
| Geslaagd | **201** |
| Gefaald | **0** |
| Overgeslagen | **0** |
| Uitvoertijd | **10.81 seconden** |
| Statement coverage | **85.2%** (drempel: 80%) |
| Coverage status | **GESLAAGD** |

---

## 2. Coverage per module

Gemeten op 14 april 2026 met `pytest-cov 7.0.0` en Python 3.13.13.

```
Name                                      Stmts   Miss  Cover   Missing
-----------------------------------------------------------------------
src\__init__.py                               3      0   100%
src\change_detection\__init__.py              3      0   100%
src\change_detection\change_detector.py      69      1    99%   45
src\change_detection\diff_engine.py          10      3    70%   26, 40, 53
src\main.py                                 161     92    43%   97-98, 112-115, 168-173, 178-183, 188-219, 224-327
src\mapping\__init__.py                       4      0   100%
src\mapping\item_mapper.py                   94      2    98%   283, 377
src\mapping\jobplan_mapper.py                38      1    97%   95
src\mapping\msg3_maximo_mapper.py            96     15    84%   142-145, 153-156, 167-170, 193-195
src\mapping\pm_mapper.py                     73      4    95%   117, 238, 262, 287
src\parser\__init__.py                        3      0   100%
src\parser\excel_reader.py                   93      6    94%   94, 98-99, 108, 119, 124
src\parser\msg3_parser.py                   212     36    83%   141-144, 185, 196-207, 237, 255-257, 351-384
src\validator\__init__.py                     4      0   100%
src\validator\business_rules.py             199     12    94%   938-943, 971-976
src\validator\msg3_validator.py             143      4    97%   246, 273, 326, 386
src\validator\schema_validator.py            11      4    64%   27-28, 45-47
-----------------------------------------------------------------------
TOTAL                                      1216    180    85%
```

> **Toelichting `src/main.py` (43%):** De CLI-orchestratiecode in `main.py` is moeilijk unit-testbaar omdat deze I/O, argparse en logging combineert. De kernlogica (parsing, validatie, mapping) is volledig gedekt via integratie- en unit-tests van de afzonderlijke modules.
>
> **Toelichting `src/maximo_connector/*`:** Uitgesloten van coverage via `.coveragerc`. Connector-tests draaien volledig gemockt (39 tests).

---

## 3. Tests per module

### 3.1 Integratie tests (16 tests)

**Bestand:** `tests/integration/test_full_pipeline.py`
**Status:** Alle 16 tests geslaagd

| Test | Beschrijving | Resultaat |
|------|-------------|-----------|
| `test_parse_redesign_excel` | Redesign Excel levert 10 taken | PASSED |
| `test_parsed_task_fields` | Alle velden aanwezig incl. `ata_system` | PASSED |
| `test_validate_parsed_data` | Validatie slaagt (0 errors, 0 warnings) | PASSED |
| `test_map_validated_data` | 41 Maximo-objecten gegenereerd (10+10+10+11) | PASSED |
| `test_maximo_item_fields` | Item Master velden correct | PASSED |
| `test_maximo_pm_fields` | PM-velden correct (FREQUNIT, FREQUENCY) | PASSED |
| `test_maximo_jobplan_fields` | JobPlan-velden correct (JPNUM, JPTASKS) | PASSED |
| `test_change_detection_added` | Nieuwe taak als "added" | PASSED |
| `test_change_detection_modified` | Gewijzigde taak als "modified" | PASSED |
| `test_change_detection_deleted` | Verwijderde taak als "deleted" | PASSED |
| `test_change_detection_no_changes` | Geen wijzigingen → 0 changes | PASSED |
| `test_full_pipeline_output_structure` | Output JSON heeft verplichte sleutels | PASSED |
| `test_invalid_excel_path` | FileNotFoundError bij onbekend pad | PASSED |
| `test_validation_failure_blocks_mapping` | CRITICAL error stopt pipeline | PASSED |
| `test_commodity_codes_filled` | Commodity codes niet leeg | PASSED |
| `test_ata_system_derived_from_task_code` | ATA system correct afgeleid | PASSED |

---

### 3.2 Unit tests Parser (38 tests)

**Bestand:** `tests/unit/test_parser.py`
**Status:** Alle 38 tests geslaagd

Getest: `MSG3Parser`, `ExcelReader`, helper-methoden, `_extract_ata_system_from_task_code`.

Kernscenario's:
- Redesign-formaat parsing (10 taken correct)
- Ontbrekende verplichte headers → `ValueError`
- Ongeldige interval-eenheid → overgeslagen
- `ata_chapter` en `ata_system` afgeleid uit task code `"32-11-01-001"` → `"32"`, `"11"`
- `to_dict()` inclusief `ata_system`

---

### 3.3 Unit tests Validator (52 tests)

**Bestand:** `tests/unit/test_validator.py`
**Status:** Alle 52 tests geslaagd

Getest: `MSG3Validator`, `BusinessRulesValidator`.

Kernscenario's:
- Structuurvalidatie op verplichte sleutels
- Duplicate task codes → ERROR
- Maximo veldlimieten (PMNUM max 12, DESCRIPTION max 100)
- 90 business rules correct geladen
- 6 categorieën: STR(15), SAF(15), AIR(15), MNT(15), LOG(20), REG(10)
- CRITICAL severity blokkeert verdere verwerking

---

### 3.4 Unit tests Mapper (56 tests)

**Bestand:** `tests/unit/test_mapping.py`
**Status:** Alle 56 tests geslaagd

Getest: `PMMapper`, `JobPlanMapper`, `ItemMapper`, `MSG3MaximoMapper`.

Kernscenario's:
- PM-velden correct gegenereerd
- JobPlan-velden correct gegenereerd
- Item Master inclusief commodity code
- Beschrijving-truncatie op 100 tekens
- Commodity code op basis van `ata_chapter` + `ata_system`
- Lege input → lege output

---

### 3.5 Unit tests Maximo Connector (39 tests)

**Bestand:** `tests/unit/test_maximo_connector.py`
**Status:** Alle 39 tests geslaagd

Getest: `RestClient`, `MaximoClient` (volledig gemockt).

Kernscenario's:
- GET/POST/PATCH/DELETE succes en fout
- Retry-logica bij 500-responses
- `MaximoAPIError` bevat status code + body
- API Key authenticatie
- Basic Auth authenticatie
- `create_item`, `create_pm`, `create_jobplan`, `create_commodity`
- `item_exists` True en False
- `batch_create` sequentieel
- `upload_maximo_objects` volledige flow

---

## 4. Niet gedekte code (Missing lines analyse)

| Module | Niet-gedekte regels | Reden |
|--------|-------------------|-------|
| `main.py` | 97-327 (CLI-code) | Moeilijk unit-testbaar (argparse + I/O) |
| `diff_engine.py` | 26, 40, 53 | Edge cases in diff-algoritme niet in huidige fixture |
| `schema_validator.py` | 27-28, 45-47 | Schema-validatie pad zelden actief in normale flow |
| `msg3_parser.py` | 351-384 | Origineel-formaat parsing (geen fixture beschikbaar) |
| `msg3_maximo_mapper.py` | 142-195 | Org-specifieke mapping zonder `org_id` |

**Conclusie:** De niet-gedekte regels zijn ofwel CLI-wrappercode, edge-case paths, of legacy-format ondersteuning. De kernbusiness-logica (parsing, validatie, mapping, change detection) heeft >83% coverage.

---

## 5. Test-omgeving

| Component | Versie |
|-----------|--------|
| Python | 3.13.13 |
| pytest | 8.4.2 |
| pytest-cov | 7.0.0 |
| pytest-mock | 3.15.1 |
| openpyxl | (productiedependency) |
| OS | Windows 10 (win32) |

---

## 6. HTML Coverage Rapport

Het HTML-rapport is gegenereerd naar `htmlcov/index.html`.

Om te bekijken (lokaal):

```powershell
# Genereer HTML rapport
python -m pytest tests/ --cov=src --cov-report=html

# Open rapport (Windows)
Start-Process "htmlcov\index.html"
```

---

## 7. Pytest commando's

```powershell
# Alle tests draaien
python -m pytest tests/

# Alleen unit tests
python -m pytest tests/unit/ -v

# Alleen integratie tests
python -m pytest tests/integration/ -v

# Met coverage (console)
python -m pytest tests/ --cov=src --cov-report=term-missing

# Met coverage (HTML)
python -m pytest tests/ --cov=src --cov-report=html

# Specifieke module
python -m pytest tests/unit/test_parser.py -v

# Met keyword filter
python -m pytest tests/ -k "ata_system" -v
```

---

## 8. Authenticiteitsverklaring

**Auteur:** Pedro Eduardo Cardoso
De testresultaten in dit document zijn gegenereerd op 14 april 2026 op mijn lokale ontwikkelmachine. Alle 201 tests zijn door mij zelf geschreven en/of gereviewed. De coverage-cijfers zijn direct gekopieerd uit de `pytest` output.
