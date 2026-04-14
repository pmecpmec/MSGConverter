# Sprint 2 Planning – Implementation

**Sprint:** 2
**Periode:** 10 maart – 10 april 2026
**Duur:** 5 weken (15 werkdagen – Di/Wo/Do)
**Werkdagen:** Dinsdag, Woensdag, Donderdag (3 dagen/week bij Babcock)
**Project:** MSG-3 to Maximo Converter
**Student:** Pedro Eduardo Cardoso
**Opleiding:** Associate Degree Software Developer (ADSD)

---

## Sprint Goal

**"Werkende end-to-end pipeline: MSG-3 Excel → validatie → change detection → Maximo-objecten, met ≥80% test coverage en robuuste CLI."**

### Success Criteria

- `pytest` groen, ≥80% coverage
- Alle kernmodules geïmplementeerd (parser, validator, mapper, change detector, REST connector)
- CLI werkt met `--mode`, `--output`, `--previous`, `--quiet`, `--verbose`
- `ata_system` correct afgeleid uit task codes (commodity-code warning vrij)
- Minimaal 1 succesvolle demo van volledige pipeline

---

## Backlog Items Selected

### Must Have Items

#### BAC-010: MSG-3 Excel Parser
**Story Points:** 8 | **Prioriteit:** Critical

**User Story:**
> Als converter wil ik een MSG-3 Excel bestand kunnen inlezen, zodat ik de taakdata kan verwerken.

**Taken:**
- [x] `ExcelReader` klasse – sheet detectie, header mapping
- [x] `MSG3Parser` klasse – `_parse_redesign_row`, `_parse_original_row`
- [x] `MSG3Task` dataclass met alle velden (incl. `ata_system`)
- [x] `_extract_ata_from_task_code`, `_extract_ata_system_from_task_code`
- [x] Unit tests ≥90% coverage

**Acceptatiecriteria:**
- [x] Redesign-formaat parse 10 taken correct
- [x] `task_code`, `ata_chapter`, `ata_system`, `interval_value`, `interval_unit` aanwezig
- [x] Foutieve rijen worden overgeslagen met waarschuwing

---

#### BAC-011: Data Validator
**Story Points:** 5 | **Prioriteit:** Critical

**User Story:**
> Als converter wil ik data valideren vóór verwerking, zodat geen onvolledige data naar Maximo gaat.

**Taken:**
- [x] `MSG3Validator` – structuur, duplicaten, Maximo-veldlimieten
- [x] `BusinessRulesValidator` – 90 business rules geladen
- [x] Severity-niveaus: CRITICAL, ERROR, WARNING, INFO
- [x] Unit tests voor alle validators

**Acceptatiecriteria:**
- [x] 90 business rules correct geladen (6 categorieën)
- [x] CRITICAL issues blokkeren pipeline
- [x] Validatieresultaat bevat severity + message per issue

---

#### BAC-012: Change Detection
**Story Points:** 5 | **Prioriteit:** High

**User Story:**
> Als converter wil ik wijzigingen detecteren tussen twee MSG-3 versies, zodat ik alleen gewijzigde taken naar Maximo upload.

**Taken:**
- [x] `ChangeDetector.detect_changes(previous, current)`
- [x] Added, modified, deleted, unchanged categorieën
- [x] `ChangeReport` met samenvatting
- [x] Unit tests

**Acceptatiecriteria:**
- [x] Nieuwe taken als "added" gemarkeerd
- [x] Gewijzigde velden gedetecteerd
- [x] Verwijderde taken als "deleted" gemarkeerd

---

#### BAC-013: MSG-3 naar Maximo Mapper
**Story Points:** 8 | **Prioriteit:** Critical

**User Story:**
> Als converter wil ik MSG-3 taken omzetten naar Maximo-objecten, zodat ik ze kan importeren.

**Taken:**
- [x] `ItemMapper` – Item Master records
- [x] `PMMapper` – Preventive Maintenance records
- [x] `JobPlanMapper` – Job Plan records
- [x] `CommodityMapper` – Commodity codes op basis van ATA
- [x] Veld-truncatie voor Maximo-limieten

**Acceptatiecriteria:**
- [x] Elke MSG-3 taak levert PM + JobPlan + Item op
- [x] Commodity code correct op basis van `ata_chapter`+`ata_system`
- [x] Beschrijvingen truncaten correct op 100 tekens

---

#### BAC-014: Maximo REST Connector
**Story Points:** 8 | **Prioriteit:** High

**User Story:**
> Als converter wil ik Maximo-objecten via REST API aanmaken, zodat het proces geautomatiseerd is.

**Taken:**
- [x] `RestClient` – GET, POST, PATCH, DELETE, retry-logica
- [x] `MaximoClient` – `create_item`, `create_pm`, `create_jobplan`, `create_commodity`
- [x] API Key + Basic Auth ondersteuning
- [x] `batch_create` en `upload_maximo_objects`
- [x] 39 gemockte unit tests

**Acceptatiecriteria:**
- [x] Retry bij 500/429 (max 3 pogingen)
- [x] `MaximoAPIError` bevat status code + response body
- [x] Alle methodes getest met mocks

---

#### BAC-015: CLI Applicatie
**Story Points:** 5 | **Prioriteit:** Critical

**User Story:**
> Als gebruiker wil ik de converter via command line uitvoeren, zodat ik het in workflows kan inbedden.

**Taken:**
- [x] `argparse` CLI met `--mode`, `--output`, `--previous`, `--skip-validation`, `--verbose`, `--quiet`, `--log-file`, `--version`
- [x] Pipeline orchestratie in `MSGConverterApp`
- [x] Logging naar stdout + optioneel bestand
- [x] Samenvatting output

**Acceptatiecriteria:**
- [x] `python -m src.main --help` toont alle opties
- [x] `--output` schrijft JSON naar bestand
- [x] `--previous` activeert change detection
- [x] `--quiet` onderdrukt banner/samenvatting

---

#### BAC-050: Sprint 2 Documentatie
**Story Points:** 3 | **Prioriteit:** Must Have

**User Story:**
> Als student wil ik Sprint 2 documenteren voor Manage & Control competentie.

**Taken:**
- [x] Sprint planning (dit document)
- [ ] Daily progress (bijhouden per werkdag)
- [ ] Sprint review (eind sprint)
- [ ] Sprint retrospective (eind sprint)

---

### Should Have Items

#### BAC-016: `rich` CLI Output
**Story Points:** 3 | **Prioriteit:** Should Have

**Beschrijving:** Progress bar en gekleurde output met `rich`-bibliotheek. Verhoogt de "wow factor" van de applicatie.

**Taken:**
- [ ] Progress bar tijdens 4 pipeline-stappen
- [ ] Gekleurde samenvatting (groen/rood)
- [ ] `rich.panel` voor banner

---

## Sprint Capacity

**Beschikbare tijd:**
- 15 werkdagen × 8 uur = 120 uur theoretisch
- Meetings/overhead/documenten: -15 uur
- **Netto capaciteit: ~105 uur**

**Gepland:**
- Must Have items: 42 story points ≈ 42 uur
- Should Have items: 3 story points ≈ 3 uur
- **Totaal: 45 story points**

**Buffer:** ~60 uur voor documentatie, testen, bugs en polish

---

## Definition of Done – Sprint 2

**Een item is "done" als:**
- [ ] Geïmplementeerd en werkend
- [ ] Unit tests aanwezig (≥80% coverage voor module)
- [ ] `pytest` groen (geen failures)
- [ ] Geen linter errors (flake8)
- [ ] Docstrings aanwezig op publieke methods
- [ ] `ZELFEVALUATIE-TRACKING.md` bijgewerkt

---

## Sprint 2 Retrospective Preview (te vullen eind sprint)

*Dit gedeelte wordt ingevuld na afloop van sprint 2.*

---

## Authenticiteitsverklaring AI-gebruik

**Auteur:** Pedro Eduardo Cardoso
**AI-assistentie:** Cursor AI (Claude)

**AI-gebruik:**
- Sprint planning structuur voorgesteld door AI
- Backlog items en acceptatiecriteria gereviewed met AI-assistent

**Mijn bijdrage:**
- Alle technische beslissingen en prioritering zijn mijn eigen keuzes
- Dagelijkse voortgang en reflectie zijn 100% mijn eigen werk

---

**Datum aangemaakt:** 10 maart 2026
**Laatste update:** 14 april 2026
**Status:** IN UITVOERING
