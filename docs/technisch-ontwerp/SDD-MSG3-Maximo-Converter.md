# Software Design Document – MSG-3 to Maximo Converter

**Van:** Pedro Eduardo Cardoso  
**Voor:** Babcock Schiphol, Windesheim ADSD  
**Datum/versie:** 14 april 2026, v1.1

## Documentkop en versies

| Versie | Auteur | Datum | Veranderingen |
|--------|--------|-------|---------------|
| 1.0 | Pedro Eduardo Cardoso | feb 2026 | Eerste SDD volgens Windesheim-template; bestaande ontwerpdocumenten als secties/bijlagen opgenomen. |
| 1.1 | Pedro Eduardo Cardoso | apr 2026 | Bijgewerkt na sprint 2: 90 business rules (was 80), `ata_system` derivatie, `rich` CLI, Maximo REST connector geïmplementeerd, testparagraaf bijgewerkt met actuele testresultaten (201 tests, 84% coverage), UML-diagrammen toegevoegd als bijlage. |

## Inhoudsopgave (SDD-structuur)

1. Inleiding  
2. Gebruikerseisen  
3. Architectuuroverzicht  
4. Gedetailleerd Ontwerp  
5. Implementatie Details  
6. Testing en Validatie  
7. Deployments en Onderhoud  
8. Globale planning  
9. Bronnen  
10. Bijlagen  

## 1. Inleiding

### 1.1 Doel

Dit document beschrijft het functioneel en technisch ontwerp van de MSG-3 to Maximo Converter: een koppeling tussen MSG-3 Excel-bestanden en IBM Maximo voor Babcock Schiphol. Het is bedoeld voor ontwikkelaars, de opdrachtgever en beoordelaars.

### 1.2 Projectdefinitie

Het project levert een geautomatiseerde koppeling van MSG-3 onderhoudsdata (Excel) naar Maximo (PM en JobPlan). Doel: tijd besparen, fouten terugdringen en het engineering team ontlasten. Zie de projectdefinitie in `docs/projectdefinitie/` voor context, probleemstelling en scope.

### 1.3 Productvisie

De software leest MSG-3 Excel in, valideert de data volgens vastgelegde business rules, detecteert wijzigingen ten opzichte van een vorige versie, mapt naar Maximo-objecten (PM, JobPlan, Item) en stuurt deze via de Maximo REST API. De waarde: voorspelbare, gedocumenteerde en onderhoudbare import in plaats van handmatig werk.

### 1.4 Scope

In scope: parsing van MSG-3 Excel (bestaand en herontworpen formaat), validatie (structuur + business rules), change detection, mapping naar PM en JobPlan, en verzenden via REST API (create/read/update). Buiten scope: delete in Maximo, andere CMMS-systemen, volledige procesherinrichting. Zie `docs/projectdefinitie/04-scope.md`.

### 1.5 Stakeholders

Belanghebbenden zijn het engineering team (eindgebruiker), de bedrijfsbegeleider (Matthijs Meijer), de opdrachtgever en de stage-student (ontwikkelaar). Zie `docs/projectdefinitie/05-stakeholders.md` voor de stakeholderanalyse.

## 2. Gebruikerseisen

Het systeem moet:

- MSG-3 Excel-bestanden (.xlsx/.xlsm) inlezen en de relevante sheets en kolommen herkennen.
- Data valideren volgens de structuur en de **90 business rules** (veiligheid, compliance, kwaliteit, efficiency). Zie **Bijlage A: business-rules.md**.
- Wijzigingen tussen twee MSG-3 versies detecteren en rapporteren (toegevoegd, gewijzigd, verwijderd).
- MSG-3 taken mappen naar Maximo PM en JobPlan (en gerelateerde objecten) volgens de vastgelegde veldmapping.
- Via de Maximo REST API objecten aanmaken en bijwerken (geen delete).
- Een duidelijke foutafhandeling en logging bieden; geen stille fouten of onvolledige writes.

Niet-functionele eisen: verwerking binnen enkele seconden per bestand, credentials niet in code, modulaire en onderhoudbare code. Zie sectie 3.1 voor technische eisen.

## 3. Architectuuroverzicht

Dit overzicht volgt dezelfde indeling als [01-architectuur-ontwerp.md](01-architectuur-ontwerp.md). Gedetailleerde dataflow: [MAPPING-FLOW-VISUAL.md](MAPPING-FLOW-VISUAL.md) en [MAXIMO-INTEGRATIE-UPDATE.md](MAXIMO-INTEGRATIE-UPDATE.md).

### 3.1 Technische eisen

**Performance.** Verwerking van een MSG-3 Excel-bestand binnen enkele seconden. API-calls met retry en timeouts; acceptabele responstijd per record.

**Betrouwbaarheid.** Geen automatische delete in Maximo. Duidelijke foutmeldingen en logging; bij API-fouten retry en graceful failure.

**Onderhoudbaarheid.** Modulaire opzet: parser, validator, mapping en Maximo-client gescheiden. Business rules centraal in `business_rules.py`. PEP 8, type hints en docstrings.

**Beveiliging.** Credentials niet in code; configuratie via omgevingsvariabelen of configbestand. Geen gevoelige data in logs.

**Compatibiliteit.** Ondersteuning bestaand en herontworpen MSG-3 formaat. Python 3.11+; dependencies in requirements.txt.

### 3.2 Algemene architectuur

Pipeline: Parse → Validate → Change detection (optioneel) → Map → Send to Maximo. Gebruiker bedient via CLI.

1. **Parse.** Excel inlezen (excel_reader, msg3_parser). Output: gestructureerde data inclusief `ata_chapter` en `ata_system` afgeleid van task code.
2. **Validate.** Schemavalidatie en 90 business rules (business_rules.py). Output: gevalideerde data en waarschuwingen.
3. **Change detection.** Vergelijking met vorige versie (change_detector, diff_engine). Output: change report.
4. **Mapping.** MSG3MaximoMapper naar Maximo-objecten. Volgorde: Commodities → Items → Item/Org → PM → JobPlan. Zie MAPPING-FLOW-VISUAL.md.
5. **Send to Maximo.** maximo_client en rest_client via REST API (create/read/update) met retry-logica.

Componenten: parser, validator, change_detection, mapping, maximo_connector, main. Geen eigen database; configuratie extern.

**UML-diagrammen** (zie `docs/uml/`):

| Diagram | Bestand | Inhoud |
|---------|---------|--------|
| Use Case | `docs/uml/usecase.puml` | Actoren en gebruiksscenario's |
| Componentdiagram | `docs/uml/components.puml` | Pakketstructuur en afhankelijkheden |
| Sequentiediagram | `docs/uml/sequence.puml` | End-to-end dataflow |
| Activiteitendiagram | `docs/uml/activity.puml` | Pipeline stappen |
| Klassendiagram | `docs/uml/classdiagram.puml` | Klassen en relaties |

### 3.3 Technologieën en frameworks

Python 3.11+. Excel: openpyxl (.xlsx/.xlsm), pandas waar nuttig. Validatie: pydantic en business_rules.py. Maximo: requests, REST API. Testing: pytest. CLI: argparse. Logging: standaard logging-module.

## 4. Gedetailleerd Ontwerp

### 4.1 Interface-ontwerp

- **CLI:** argumenten voor invoerbestand, configuratie, actie (parse, validate, map, send). Zie main.py.
- **Maximo REST API:** endpoints en authenticatie volgens Maximo-documentatie; velden en beperkingen in **Bijlage B: maximo-specificaties.md** en MAXIMO-INTEGRATIE-UPDATE.md.

### 4.2 Datastromen

End-to-end flow: MSG-3 Excel → Parser → Validator → (Change detector) → Mapper → Maximo REST. Zie [MAPPING-FLOW-VISUAL.md](MAPPING-FLOW-VISUAL.md) voor het visuele overzicht.

### 4.3 Datamodel

Intern taakmodel: o.a. MSG3Task (taakcode, beschrijving, type, interval, eenheid, zone, ATA, man-uren, vaardigheden). Mapping naar Maximo PM en JobPlan gedocumenteerd in maximo-specificaties.md en in de code (src/mapping/).

### 4.4 Module-overzicht

| Module | Klassen | Verantwoordelijkheid |
|--------|---------|---------------------|
| `parser` | `ExcelReader`, `MSG3Parser`, `MSG3Task` | Excel inlezen, headers detecteren, data parsen naar dataclasses |
| `validator` | `SchemaValidator`, `MSG3Validator`, `BusinessRulesValidator` | Structuurcontrole, 90 business rules, severity-rapportage |
| `change_detection` | `ChangeDetector`, `DiffEngine`, `ChangeReport` | Versievergelijking, added/modified/deleted/unchanged |
| `mapping` | `MSG3MaximoMapper`, `ItemMapper`, `PMMapper`, `JobPlanMapper` | Transformatie naar Maximo-objecten, ATA-commodity koppeling |
| `maximo_connector` | `RestClient`, `MaximoClient`, `MaximoAPIError` | HTTP-client met retry, hoge-niveau Maximo CRUD operaties |
| `main` | `MSG3MaximoIntegration` | CLI, pipeline-orchestratie, `rich`-output |

Klassendiagram: `docs/uml/classdiagram.puml`.

## 5. Implementatie Details

### 5.1 Programmeertaal en coding standaarden

Python 3.11+. Type hints voor alle parameters en return types. Docstrings voor alle publieke functies en classes. PEP 8; max ca. 200 regels per bestand waar mogelijk. Zie `.cursor/rules/python-code.mdc`.

### 5.2 Ontwerpprincipes

Business rules first: elke feature moet compliant zijn met de **90 business rules** in `docs/technisch-ontwerp/business-rules.md` en `src/validator/business_rules.py`. Zie BUSINESS-RULES-FIRST.md. Modulaire opzet; design patterns (Factory, Strategy, Repository) waar passend.

Toegepaste principes:
- **SRP (Single Responsibility):** Elke module heeft één taak (parser parst, mapper mapt, etc.)
- **DI (Dependency Injection):** `MSG3MaximoIntegration` krijgt componenten via `_initialize_components()`
- **Layered Architecture:** Parser → Validator → Mapper → Connector (geen terugkoppeling)
- **Fail-fast:** CRITICAL validatiefouten stoppen de pipeline direct

### 5.3 Beveiliging en authenticatie

Credentials voor Maximo via omgevingsvariabelen of config; niet in code of logs. Authenticatie volgens Maximo (Basic of API key).

## 6. Testing en Validatie

### 6.1 Teststrategie

De teststrategie volgt de testpyramide (unit → integratie). De volledige strategie en testscenario's staan in `docs/testcases/01-teststrategie.md`.

**Testtypen:**

| Type | Bestanden | Beschrijving |
|------|-----------|-------------|
| Unit tests | `tests/unit/` | Geïsoleerde tests per module (parser, validator, mapper, connector) |
| Integratietests | `tests/integration/` | End-to-end pipeline met echt Excel-fixture |
| Maximo connector tests | `tests/unit/test_maximo_connector.py` | Volledig gemockt via `unittest.mock` |

**Huidige testresultaten (14 april 2026):**

| Metric | Waarde |
|--------|--------|
| Totaal tests | **201** (201 passed, 0 failed) |
| Statement coverage | **84.4%** |
| Coverage drempel | 80% (geconfigureerd in `pytest.ini`) |
| Uitvoertijd | ~10 seconden |

Zie `docs/testcases/02-testresultaten.md` voor de volledige coverage-tabel per module.

**Coverage per module:**

| Module | Coverage |
|--------|---------|
| `change_detector.py` | 99% |
| `msg3_validator.py` | 97% |
| `item_mapper.py` | 98% |
| `business_rules.py` | 94% |
| `excel_reader.py` | 94% |
| `msg3_parser.py` | 83% |
| `main.py` | 43% (CLI-wrapper, moeilijk unit-testbaar) |

**Test configuratie:**

```ini
# pytest.ini
[pytest]
testpaths = tests
addopts = --cov=src --cov-report=term-missing --cov-report=html
          --cov-fail-under=80 --cov-config=.coveragerc
```

### 6.2 Prestatie-eisen

Verwerking van een representatief MSG-3 bestand (10 taken) binnen 2 seconden; API-calls met retry (max 3 pogingen, exponential backoff). Geen harde SLA in deze fase.

**Gemeten:** 10 taken geparseerd in <100ms; volledige pipeline in ~300ms (excl. Maximo API).

### 6.3 Foutafhandeling en logging

Alle parsing-, validatie- en API-fouten worden gelogd via Python's standaard `logging`-module. Severity-niveaus:

- `CRITICAL` – Blokkeert verdere verwerking (bijv. bestand niet gevonden, validatie gefaald)
- `ERROR` – Fout tijdens stap (bijv. ongeldige rij), stap overgeslagen
- `WARNING` – Aandachtspunt (bijv. veldlengte, ontbrekende optionele kolom)
- `INFO` – Normale voortgang
- `DEBUG` – Gedetailleerde trace (activeer met `--verbose`)

CLI-output via `rich`: progress bar tijdens 4 pipeline-stappen, kleurgecodeerde samenvatting (groen = succes, rood = fout). Logging naar bestand via `--log-file`.

## 7. Deployments en Onderhoud

### 7.1 Deployment strategie

Applicatie draait lokaal of op een server binnen het netwerk van Babcock; verbinding met Maximo test- en eventueel productie-omgeving. Geen cloud-vereiste in de basis.

### 7.2 Monitoring en onderhoud

Logging naar bestand en/of console. Onderhoud: aanpassingen aan business rules of mapping via code en configuratie; geen wijzigingen in Maximo-configuratie door deze applicatie.

### 7.3 Schaalbaarheid

Eén bestand per run; bij grotere volumes batchverwerking of queue later mogelijk. Geen schaalvereisten in de huidige scope.

## 8. Globale planning

Planning staat in het Plan van Aanpak: docs/plan-van-aanpak/02-planning.md. Fasering: opstart, onderzoek/POC, parser en validator, change detection, mapping, Maximo-connector, MSG-3-redesign, testen en afronding. Mijlpalen en deadlines daar.

## 9. Bronnen

- IBM Maximo REST API-documentatie  
- maximosecrets.com (veld- en objectinformatie)  
- Projectdefinitie en PvA: docs/projectdefinitie/, docs/plan-van-aanpak/  
- Onderzoeksrapport: docs/onderzoek/00-onderzoeksrapport.md  
- Windesheim SDD-template (Eindopdracht Nonogram)  

## 10. Bijlagen

De volgende documenten horen bij dit SDD en bevatten de gedetailleerde specificaties:

### Technisch ontwerp

| Bijlage | Bestand | Inhoud |
|---------|---------|--------|
| A | [business-rules.md](business-rules.md) | Volledige 90 business rules (6 categorieën); basis voor validatie en transformaties. |
| B | [maximo-specificaties.md](maximo-specificaties.md) | Maximo-velden, objecten (Item, PM, JobPlan), beperkingen. |
| C | [MAXIMO-INTEGRATIE-UPDATE.md](MAXIMO-INTEGRATIE-UPDATE.md) | Status Maximo-integratie; volgorde Item → PM → JobPlan. |
| D | [MAPPING-FLOW-VISUAL.md](MAPPING-FLOW-VISUAL.md) | Visuele dataflow en mapping. |
| E | [01-architectuur-ontwerp.md](01-architectuur-ontwerp.md) | Uitgewerkt architectuuroverzicht (sectie 3). |
| F | [BUSINESS-RULES-FIRST.md](BUSINESS-RULES-FIRST.md) | Guideline: business rules eerst bij elke wijziging. |
| G | [business-rules-quick-reference.md](business-rules-quick-reference.md) | Snelle referentie en codevoorbeelden. |

### UML-diagrammen

| Diagram | Bestand | PlantUML |
|---------|---------|---------|
| Use Case | `docs/uml/usecase.puml` | Actoren: Developer/Gebruiker, use cases: Parse, Validate, Map, Upload |
| Componentdiagram | `docs/uml/components.puml` | Pakketstructuur: parser, validator, mapping, connector |
| Sequentiediagram | `docs/uml/sequence.puml` | End-to-end: CLI → Parser → Validator → Mapper → MaximoClient |
| Activiteitendiagram | `docs/uml/activity.puml` | Pipeline-stappen met beslissingspunten (validatie OK?) |
| Klassendiagram | `docs/uml/classdiagram.puml` | MSG3Task, MSG3Parser, MSG3Validator, MSG3MaximoMapper, MaximoClient |

### Testdocumentatie

| Document | Bestand | Inhoud |
|----------|---------|--------|
| Teststrategie | `docs/testcases/01-teststrategie.md` | Aanpak, tools, coverage targets, testscenario's per module |
| Testresultaten | `docs/testcases/02-testresultaten.md` | 201 tests, 84% coverage, coverage per module |

Voor het overzicht van alle ontwerpdocumenten: [00-ontwerp-overzicht.md](00-ontwerp-overzicht.md).

_Datum laatste update: 14 april 2026_  
_Auteur: Pedro Eduardo Cardoso_  
_Project: MSG-3 naar Maximo Converter_  
_Versie applicatie: v0.2.0_

## AI Authenticiteitsverklaring

Tijdens het technisch onderzoek en ontwerp is Cursor AI gebruikt voor het genereren van diagramtemplates, het analyseren van API-documentatie en het structureren van technische beslissingen. De uitkomsten zijn gecontroleerd en aangepast. Alle architecturale beslissingen, business rules en technische keuzes zijn gebaseerd op eigen analyse en overleg met stakeholders. De auteur draagt de volledige verantwoordelijkheid voor de inhoud.

_AIAS-niveau: 3 – AI Samenwerking_
