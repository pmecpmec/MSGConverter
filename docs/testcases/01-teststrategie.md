# Teststrategie – MSG-3 to Maximo Converter

**Project:** MSG-3 to Maximo Converter
**Auteur:** Pedro Eduardo Cardoso
**Datum:** 14 april 2026
**Versie:** 1.0

---

## 1. Inleiding

Dit document beschrijft de teststrategie voor de MSG-3 to Maximo Converter applicatie. Het geeft inzicht in de testdoelen, testmethoden, tools, coverage-targets en de verantwoording van testkeuzes.

---

## 2. Testdoelstellingen

| Doel | Omschrijving |
|------|-------------|
| Correctheid | Elke module produceert de verwachte output voor gegeven input |
| Robuustheid | De pipeline faalt graceful bij ontbrekende/foutieve data |
| Regressionsveiligheid | Nieuwe wijzigingen breken bestaande functionaliteit niet |
| Maximo-compliance | Gegenereerde objecten voldoen aan Maximo-veldlimieten en -structuur |
| Coverage | Minimaal 80% statement coverage op alle productie-modules |

---

## 3. Scope

### In scope

- `src/parser/` – Excel lezen en parsen naar `MSG3Task`-dataclasses
- `src/validator/` – Business rules validatie en structuurcontrole
- `src/mapping/` – Transformatie naar Maximo-objecten (Item, PM, JobPlan, Commodity)
- `src/change_detection/` – Detectie van toegevoegde, gewijzigde en verwijderde taken
- `src/maximo_connector/` – REST client en Maximo API client (gemockt)
- `src/main.py` – CLI en pipeline-orchestratie (gedeeltelijk)

### Buiten scope

- Live Maximo API calls (geen testomgeving beschikbaar)
- Performance-benchmarks (niet vereist voor beoordeling)
- UI-testen (CLI-only applicatie)

---

## 4. Testpyramide

De testaanpak volgt de klassieke testpyramide:

```
        /\
       /  \
      / E2E\        (niet van toepassing – geen live Maximo)
     /------\
    / Integ  \      tests/integration/   (16 tests)
   /----------\
  /  Unit Tests \   tests/unit/          (185 tests)
 /--------------\
```

**Unit tests (91%):** Klein, snel, geïsoleerd. Testen één klasse of methode tegelijk. Externe afhankelijkheden (bestanden, HTTP) worden gemockt.

**Integratietests (9%):** Testen de volledige pipeline van Excel-bestand naar Maximo-objecten. Gebruik maken van een voorbereid test-fixture (`tests/fixtures/test_msg3_redesign.xlsx`).

---

## 5. Testaanpak per module

### 5.1 Parser (`src/parser/`)

**Aanpak:** Unit tests op `MSG3Parser` en `ExcelReader`.

**Testscenario's:**
- Succesvol parsen van redesign-formaat (10 taken)
- Parsen van origineel-formaat
- Ontbrekende verplichte kolommen → `ValueError`
- Ongeldige interval-eenheid → taak overgeslagen + waarschuwing
- `ata_chapter` en `ata_system` correct afgeleid uit `task_code`
- Helper-methoden: `_clean_str`, `_parse_int`, `_parse_float`, `_parse_skills`
- Duplicate task codes worden gedetecteerd

**Mock-strategie:** `openpyxl.load_workbook` wordt niet gemockt; tests gebruiken het echte fixture-bestand.

---

### 5.2 Validator (`src/validator/`)

**Aanpak:** Unit tests op `MSG3Validator` en `BusinessRulesValidator`.

**Testscenario's:**
- Validatie slaagt voor correcte data
- Ontbrekende velden (task_code, description, interval) → ERROR
- Duplicate task codes → ERROR
- Beschrijving te lang voor Maximo (>100 tekens) → WARNING
- 90 business rules correct geladen (6 categorieën)
- CRITICAL rules blokkeren verdere verwerking
- Validatierapport bevat correcte severity, code en bericht

**Business rule-categorieën:**

| Categorie | Prefix | Aantal |
|-----------|--------|--------|
| Structural | STR | 15 |
| Safety | SAF | 15 |
| Airworthiness | AIR | 15 |
| Maintenance | MNT | 15 |
| Logistics & Inventory | LOG | 20 |
| Regulatory | REG | 10 |
| **Totaal** | | **90** |

---

### 5.3 Mapper (`src/mapping/`)

**Aanpak:** Unit tests per mapper + integratietest op `MSG3MaximoMapper`.

**Testscenario's:**
- `PMMapper`: PM-velden correct (PMNUM, DESCRIPTION, FREQUNIT, FREQUENCY, CRAFTSKILL)
- `JobPlanMapper`: JobPlan-velden correct (JPNUM, DESCRIPTION, JPTASKS)
- `ItemMapper`: Item-velden correct (ITEMNUM, DESCRIPTION, COMMODITY, COMMODITYGROUP)
- Beschrijving-truncatie op 100 tekens
- Commodity code correct afgeleid van `ata_chapter` + `ata_system`
- Lege takenlijst → lege outputlijst (geen crash)
- Foutieve taak (ontbrekend field) → overgeslagen + gelogd

---

### 5.4 Change Detector (`src/change_detection/`)

**Aanpak:** Unit tests op `ChangeDetector`.

**Testscenario's:**
- Nieuwe taak → `added`
- Gewijzigd veld (interval, description) → `modified`
- Verwijderde taak → `deleted`
- Ongewijzigde taak → `unchanged`
- Lege datasets → geen crash
- `ChangeReport` samenvatting bevat correcte tellingen

---

### 5.5 Maximo Connector (`src/maximo_connector/`)

**Aanpak:** Unit tests met `unittest.mock.patch` op `requests.Session`.

**Testscenario's:**
- `RestClient`: GET, POST, PATCH, DELETE – succes (2xx)
- `RestClient`: Retry bij 500-response (max 3 pogingen)
- `RestClient`: `MaximoAPIError` bij 4xx
- `MaximoClient`: API Key authenticatie
- `MaximoClient`: Basic Auth authenticatie
- `MaximoClient`: `create_item`, `create_pm`, `create_jobplan`, `create_commodity`
- `MaximoClient`: `item_exists` – True/False
- `MaximoClient`: `batch_create` – sequentieel per object
- `MaximoClient`: `upload_maximo_objects` – volledige upload-flow

**Reden voor mocking:** Er is geen live Maximo-testomgeving beschikbaar. Alle HTTP-calls worden gemockt met `unittest.mock.MagicMock`. Dit garandeert deterministische en snelle tests.

---

### 5.6 Integratie (`tests/integration/`)

**Aanpak:** End-to-end pipeline tests met echt Excel-fixture.

**Testscenario's (16 tests):**

| Test | Beschrijving |
|------|-------------|
| `test_parse_redesign_excel` | Redesign Excel levert 10 taken op |
| `test_parsed_task_fields` | Alle verplichte velden aanwezig incl. `ata_system` |
| `test_validate_parsed_data` | Validatie slaagt voor fixture-data |
| `test_map_validated_data` | 41 Maximo-objecten gegenereerd |
| `test_maximo_item_fields` | Item Master velden correct |
| `test_maximo_pm_fields` | PM-velden correct |
| `test_maximo_jobplan_fields` | JobPlan-velden correct |
| `test_change_detection_added` | Nieuwe taak correct als "added" gemarkeerd |
| `test_change_detection_modified` | Gewijzigde taak correct als "modified" |
| `test_change_detection_deleted` | Verwijderde taak correct als "deleted" |
| `test_change_detection_no_changes` | Ongewijzigde data → 0 wijzigingen |
| `test_full_pipeline_output_structure` | Output JSON heeft verplichte sleutels |
| `test_invalid_excel_path` | `FileNotFoundError` bij niet-bestaand pad |
| `test_validation_failure_blocks_mapping` | CRITICAL error stopt de pipeline |
| `test_commodity_codes_filled` | Commodity codes niet leeg |
| `test_ata_system_derived_from_task_code` | `ata_system` correct afgeleid |

---

## 6. Tools en configuratie

| Tool | Versie | Doel |
|------|--------|------|
| `pytest` | 8.4.2 | Test runner |
| `pytest-cov` | 7.0.0 | Coverage meting |
| `pytest-mock` | 3.15.1 | Mock utilities |
| `coverage.py` | (via pytest-cov) | HTML coverage rapport |
| `unittest.mock` | stdlib | Mocking HTTP calls |

### pytest.ini configuratie

```ini
[pytest]
testpaths = tests
addopts = --cov=src --cov-report=term-missing --cov-report=html --cov-fail-under=80 --cov-config=.coveragerc
log_cli = true
log_cli_level = INFO
```

### .coveragerc

```ini
[run]
omit =
    src/maximo_connector/*

[report]
exclude_lines =
    if __name__ == .__main__.:
    pass
    raise NotImplementedError
```

> **Toelichting omit:** `src/maximo_connector/*` is uitgesloten van coverage omdat alle HTTP-calls worden gemockt. De connector-module zelf wordt via een aparte test-suite getest, maar telt niet mee in de coverage-drempel omdat live tests niet mogelijk zijn zonder Maximo-testomgeving.

---

## 7. Coverage target

| Scope | Target | Behaald (14 april 2026) |
|-------|--------|------------------------|
| Totaal (excl. connector) | ≥80% | **85.2%** |
| Parser | ≥85% | 88% |
| Validator | ≥90% | 95% |
| Mapper | ≥85% | 93% |
| Change Detection | ≥85% | 96% |

---

## 8. Test naming convention

```
tests/
├── unit/
│   ├── test_parser.py          # MSG3Parser, ExcelReader
│   ├── test_validator.py       # MSG3Validator, BusinessRulesValidator
│   ├── test_mapping.py         # PMMapper, ItemMapper, JobPlanMapper
│   └── test_maximo_connector.py # RestClient, MaximoClient (gemockt)
└── integration/
    └── test_full_pipeline.py   # End-to-end pipeline tests
```

Testnamen volgen het patroon `test_<wat_getest_wordt>_<verwacht_resultaat>`.

---

## 9. Teststrategie-beslissingen

| Beslissing | Motivering |
|-----------|-----------|
| Geen live Maximo calls | Testomgeving niet beschikbaar; mocking is deterministisch en sneller |
| Fixture-bestand in `tests/fixtures/` | Reproduceerbaar, geen afhankelijkheid van externe bestanden |
| Coverage-drempel 80% | Industriestandaard voor Python-projecten; hoger is beter maar niet realistisch zonder E2E-omgeving |
| `BusinessRulesValidator` 90 regels | Logistiek/Inventory heeft 20 regels (10 standaard + 10 Maximo-specifiek) |
| TDD-aanpak sprint 2 | Tests eerst schrijven dwingt tot helder interface-ontwerp |

---

## 10. Authenticiteitsverklaring

**Auteur:** Pedro Eduardo Cardoso
**AI-assistentie:** Cursor AI (Claude) heeft de structuur en secties voorgesteld. Alle inhoudelijke beslissingen, testscenario's en motivaties zijn door mij zelf bepaald op basis van de daadwerkelijk geïmplementeerde code en testresultaten.
