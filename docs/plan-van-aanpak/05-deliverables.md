# Deliverables

## Inleiding

Dit document beschrijft alle **op te leveren producten** (deliverables) van het MSG-3 to Maximo project. Elk deliverable is gekoppeld aan een fase en heeft duidelijke acceptatiecriteria.

---

## Overzicht Deliverables

| # | Deliverable | Type | Fase | Status |
|---|-------------|------|------|--------|
| 1 | Projectdefinitie | Documentatie | 0 | ✅ Compleet |
| 2 | Plan van Aanpak | Documentatie | 0 | ✅ Compleet |
| 3 | Onderzoek Documenten | Documentatie | 1 | ⏳ TODO |
| 4 | POC Code | Code | 1 | ⏳ TODO |
| 5 | Technisch Ontwerp | Documentatie | 1 | ⏳ TODO |
| 6 | MSG-3 Parser Module | Code | 2 | ⏳ TODO |
| 7 | Data Validator | Code | 2 | ⏳ TODO |
| 8 | Change Detection Engine | Code | 3 | ⏳ TODO |
| 9 | Mapping Engine | Code | 4 | ⏳ TODO |
| 10 | Maximo REST Connector | Code | 5 | ⏳ TODO |
| 11 | Herontworpen MSG-3 Template | Template | 6 | ⏳ TODO |
| 12 | Integration Tests | Code | 7 | ⏳ TODO |
| 13 | Gebruikershandleiding | Documentatie | 8 | ⏳ TODO |
| 14 | Technische Documentatie | Documentatie | 8 | ⏳ TODO |
| 15 | Reflectie & Presentatie | Documentatie | 8 | ⏳ TODO |

---

## 1. Documentatie Deliverables

### 1.1 Projectdefinitie ✅
**Status:** Compleet  
**Datum:** 4 februari 2026

**Inhoud:**
- Context analyse (Babcock, MSG-3, Maximo)
- Probleemstelling (pijnpunten, impact)
- Doelstellingen (SMART subdoelen)
- Scope (in/out of scope)
- Stakeholders (rollen, verantwoordelijkheden)

**Locatie:** `docs/projectdefinitie/`

**Acceptatiecriteria:**
- [x] Context is duidelijk beschreven
- [x] Probleemstelling is geïdentificeerd
- [x] Doelen zijn SMART geformuleerd
- [x] Scope is duidelijk afgebakend
- [x] Stakeholders zijn geïdentificeerd
- [x] Goedgekeurd door begeleider

---

### 1.2 Plan van Aanpak ✅
**Status:** Compleet  
**Datum:** 4 februari 2026

**Inhoud:**
- Projectaanpak (Agile/iteratief)
- Planning (18 weken, fasen, sprints)
- Risicoanalyse (identificatie + mitigatie)
- Randvoorwaarden (vereisten voor succes)
- Deliverables lijst (dit document)

**Locatie:** `docs/plan-van-aanpak/`

**Acceptatiecriteria:**
- [x] Methodiek is gedefinieerd en verantwoord
- [x] Planning is gedetailleerd met milestones
- [x] Risico's zijn geïdentificeerd met mitigaties
- [x] Randvoorwaarden zijn gedocumenteerd
- [x] Deliverables zijn duidelijk
- [x] Goedgekeurd door begeleider

---

### 1.3 Onderzoek Documenten
**Status:** TODO  
**Deadline:** Week 4 (3 maart 2026)

**Inhoud:**
- **MSG-3 Excel Analyse**
  - Structuur en format analyse
  - Velden en data types
  - Edge cases en complexiteiten
  - Voorbeelden
  
- **Maximo API Onderzoek**
  - REST API capabilities
  - PM en JobPlan objecten
  - Authentication methoden
  - Rate limiting en best practices
  
- **Technologie Selectie**
  - Library keuzes (openpyxl vs pandas)
  - Argumentatie voor keuzes
  - Trade-offs

**Locatie:** `docs/onderzoek/`

**Acceptatiecriteria:**
- [ ] MSG-3 structuur volledig gedocumenteerd
- [ ] Maximo API capabilities in kaart gebracht
- [ ] Technologie keuzes zijn verantwoord
- [ ] Minimaal 2 voorbeeld MSG-3 bestanden geanalyseerd
- [ ] Review door stakeholders

---

### 1.4 Technisch Ontwerp
**Status:** TODO  
**Deadline:** Week 4 (3 maart 2026)

**Inhoud:**
- Architectuur diagram (high-level componenten)
- Component design (modules en interfaces)
- Data flow diagram (MSG-3 → Parser → Mapper → Maximo)
- Class diagram (belangrijkste klassen)
- Sequence diagram (belangrijkste flows)
- Technology stack
- Design decisions en trade-offs

**Locatie:** `docs/technisch-ontwerp/`

**Acceptatiecriteria:**
- [ ] Architectuur is duidelijk en modulair
- [ ] UML diagrammen zijn compleet en begrijpelijk
- [ ] Component interfaces zijn gedefinieerd
- [ ] Design decisions zijn gedocumenteerd
- [ ] Review door technische stakeholders
- [ ] Approved voor implementatie

---

### 1.5 Gebruikershandleiding
**Status:** TODO  
**Deadline:** Week 18 (15 juni 2026)

**Inhoud:**
- **Inleiding**: Wat doet de tool?
- **Installatie**: Stap-voor-stap installatie instructies
- **Configuratie**: Setup van credentials, config files
- **Gebruik**: Hoe MSG-3 bestanden verwerken
- **Workflows**: 
  - Nieuwe MSG-3 importeren
  - MSG-3 update verwerken
  - Change detection uitvoeren
- **Troubleshooting**: Veelvoorkomende problemen en oplossingen
- **FAQ**: Frequently asked questions
- **Voorbeelden**: Screenshots en voorbeeldcommando's

**Locatie:** `docs/gebruikershandleiding.md`

**Acceptatiecriteria:**
- [ ] Stap-voor-stap instructies voor alle use cases
- [ ] Screenshots of voorbeelden
- [ ] Troubleshooting sectie
- [ ] Review door eindgebruikers
- [ ] Minimaal 1 persoon kan tool gebruiken na lezen handleiding

---

### 1.6 Technische Documentatie
**Status:** TODO  
**Deadline:** Week 18 (15 juni 2026)

**Inhoud:**
- **Architectuur**: High-level system design
- **Component Documentatie**: Elke module uitgelegd
- **API Documentatie**: Maximo API integratie details
- **Data Mapping**: MSG-3 → Maximo field mapping
- **Configuration**: Config files en environment variables
- **Deployment**: Hoe te deployen en onderhouden
- **Development Setup**: Hoe development environment opzetten
- **Testing**: Hoe tests te runnen
- **Known Issues**: Bekende limitaties en workarounds

**Locatie:** `docs/technisch-ontwerp/` en `README.md`

**Acceptatiecriteria:**
- [ ] Volledige architectuur gedocumenteerd
- [ ] Alle modules hebben documentatie
- [ ] Code comments en docstrings aanwezig
- [ ] API integratie volledig uitgelegd
- [ ] Deployment proces gedocumenteerd
- [ ] Review door technische stakeholders

---

### 1.7 Overdracht Documentatie
**Status:** TODO  
**Deadline:** Week 18 (15 juni 2026)

**Inhoud:**
- **Oplevering Checklist**: Wat is opgeleverd
- **Known Issues**: Bekende bugs of limitaties
- **Future Enhancements**: Suggesties voor uitbreidingen
- **Maintenance Guide**: Hoe systeem te onderhouden
- **Contact Informatie**: Voor vragen na oplevering
- **Handover Notes**: Belangrijke informatie voor overdracht

**Locatie:** `docs/overdracht/`

**Acceptatiecriteria:**
- [ ] Volledige oplevering checklist
- [ ] Known issues gedocumenteerd
- [ ] Future enhancements lijst
- [ ] Maintenance instructies
- [ ] Overdracht sessie gehouden met team

---

### 1.8 Reflectie Document (Comakership)
**Status:** TODO  
**Deadline:** Week 18 (15 juni 2026)

**Inhoud:**
- **Inleiding**: Project context
- **Competentie Ontwikkeling**: 
  - Technische competenties
  - Professionele vaardigheden
  - Persoonlijke groei
- **Uitdagingen & Learnings**: Wat was moeilijk en wat heb ik geleerd
- **Successen**: Wat ging goed
- **Reflectie op Proces**: Aanpak, planning, samenwerking
- **Toekomst**: Wat neem ik mee naar volgende projecten

**Locatie:** Comakership portfolio

**Acceptatiecriteria:**
- [ ] Competenties gedocumenteerd en gereflecteerd
- [ ] Learnings beschreven
- [ ] Concrete voorbeelden gebruikt
- [ ] Reflectie op proces en aanpak
- [ ] Review door schoolbegeleider

---

## 2. Code Deliverables

### 2.1 POC Code
**Status:** TODO  
**Deadline:** Week 4 (3 maart 2026)

**Inhoud:**
- Excel parsing POC (test met openpyxl en pandas)
- Maximo API connection POC (test REST calls)
- Minimale working prototype

**Locatie:** `examples/poc/`

**Acceptatiecriteria:**
- [ ] Excel kan ingelezen worden
- [ ] Maximo API call succesvol
- [ ] Proof of concept voor haalbaarheid
- [ ] Code is gedocumenteerd

---

### 2.2 MSG-3 Parser Module
**Status:** TODO  
**Deadline:** Week 7 (24 maart 2026)

**Inhoud:**
- `excel_reader.py`: Excel parsing logica
- `msg3_parser.py`: MSG-3 specifieke parsing
- JSON schema definities
- Error handling

**Locatie:** `src/parser/`

**Acceptatiecriteria:**
- [ ] Excel bestanden worden correct geparseerd
- [ ] Data wordt geconverteerd naar JSON
- [ ] Alle MSG-3 velden worden geëxtraheerd
- [ ] Error handling voor invalide bestanden
- [ ] Unit tests met 80%+ coverage
- [ ] Documentatie (docstrings)

---

### 2.3 Data Validator
**Status:** TODO  
**Deadline:** Week 7 (24 maart 2026)

**Inhoud:**
- `schema_validator.py`: Structuur validatie
- `business_rules.py`: Business logic validatie
- `msg3_validator.py`: MSG-3 specifieke regels
- Validatie rapportage

**Locatie:** `src/validator/`

**Acceptatiecriteria:**
- [ ] Schema validatie werkt (verplichte velden)
- [ ] Business rules zijn geïmplementeerd
- [ ] Validatie errors zijn duidelijk
- [ ] Validatie rapport wordt gegenereerd
- [ ] Unit tests
- [ ] Documentatie

---

### 2.4 Change Detection Engine
**Status:** TODO  
**Deadline:** Week 9 (7 april 2026)

**Inhoud:**
- `change_detector.py`: Versie vergelijking
- `diff_engine.py`: Diff algoritme
- Change report generator
- Delta calculatie

**Locatie:** `src/change_detection/`

**Acceptatiecriteria:**
- [ ] Toegevoegde taken worden gedetecteerd
- [ ] Gewijzigde taken worden gedetecteerd (field-level)
- [ ] Verwijderde taken worden gedetecteerd
- [ ] Change report is leesbaar en accuraat
- [ ] Unit tests met verschillende scenario's
- [ ] Documentatie

---

### 2.5 Mapping Engine
**Status:** TODO  
**Deadline:** Week 11 (21 april 2026)

**Inhoud:**
- `msg3_maximo_mapper.py`: Generic mapping logica
- `pm_mapper.py`: Preventive Maintenance mapping
- `jobplan_mapper.py`: JobPlan mapping
- Mapping configuratie
- Transformatie regels

**Locatie:** `src/mapping/`

**Acceptatiecriteria:**
- [ ] MSG-3 data wordt correct gemapped naar PM objecten
- [ ] MSG-3 data wordt correct gemapped naar JobPlan objecten
- [ ] Relaties tussen PM en JobPlan zijn correct
- [ ] Transformatie regels werken (data conversies)
- [ ] Mapping configuratie is flexibel
- [ ] Unit tests
- [ ] Mapping documentatie

---

### 2.6 Maximo REST Connector
**Status:** TODO  
**Deadline:** Week 13 (5 mei 2026)

**Inhoud:**
- `rest_client.py`: Generic REST client
- `maximo_client.py`: Maximo specifieke logica
- Authentication handling
- CRUD operaties (Create, Read, Update)
- Batch processing
- Error handling & retry logic
- Rate limiting

**Locatie:** `src/maximo_connector/`

**Acceptatiecriteria:**
- [ ] Connectie met Maximo werkt
- [ ] Authentication is geïmplementeerd en veilig
- [ ] PM objecten kunnen worden aangemaakt en geüpdatet
- [ ] JobPlan objecten kunnen worden aangemaakt en geüpdatet
- [ ] Batch processing werkt efficiënt
- [ ] Error handling en retry logic aanwezig
- [ ] Integration tests met Maximo test environment
- [ ] Logging van alle API calls
- [ ] Documentatie

---

### 2.7 Main Application
**Status:** TODO  
**Deadline:** Week 15 (19 mei 2026)

**Inhoud:**
- `main.py`: Main entry point en CLI
- Command-line interface (argparse)
- Workflow orchestration
- Progress indicators
- Configuration loading

**Locatie:** `src/main.py`

**Acceptatiecriteria:**
- [ ] CLI werkt met duidelijke argumenten
- [ ] Volledige pipeline kan worden uitgevoerd
- [ ] Progress feedback aan gebruiker
- [ ] Configuration laden werkt
- [ ] Error messages zijn duidelijk
- [ ] Help functie beschikbaar
- [ ] Documentatie

---

### 2.8 Integration Tests
**Status:** TODO  
**Deadline:** Week 17 (2 juni 2026)

**Inhoud:**
- End-to-end test scenarios
- Maximo API integration tests
- Test data en fixtures
- Test rapportage

**Locatie:** `tests/integration/`

**Acceptatiecriteria:**
- [ ] Volledige pipeline test (MSG-3 → Maximo)
- [ ] Integration tests met Maximo test environment
- [ ] Test data voor verschillende scenario's
- [ ] Tests slagen 100%
- [ ] Test documentatie

---

### 2.9 Unit Tests
**Status:** Doorlopend  
**Deadline:** Per module bij implementatie

**Inhoud:**
- Unit tests voor alle modules
- Test coverage minimaal 80%
- Pytest configuratie
- Test fixtures en mock data

**Locatie:** `tests/unit/`

**Acceptatiecriteria:**
- [ ] 80%+ code coverage
- [ ] Tests voor alle public methods
- [ ] Edge cases getest
- [ ] Tests runnen automatisch
- [ ] Duidelijke test namen en documentatie

---

## 3. Template & Data Deliverables

### 3.1 Herontworpen MSG-3 Excel Template
**Status:** TODO  
**Deadline:** Week 15 (19 mei 2026)

**Inhoud:**
- Nieuwe Excel template (optimized voor parsing)
- Voorbeeld data in nieuwe format
- Template specificatie document
- Data validatie regels in Excel (dropdowns, formulas)
- Migratie handleiding (oud → nieuw format)

**Locatie:** `examples/msg3_template_v2.xlsx`

**Acceptatiecriteria:**
- [ ] Template is machine-readable
- [ ] Alle vereiste velden aanwezig
- [ ] Validatie in Excel zelf (waar mogelijk)
- [ ] Voorbeeld data compleet
- [ ] Template specificatie gedocumenteerd
- [ ] Parser werkt met nieuwe template
- [ ] Review en goedkeuring van stakeholders

---

### 3.2 Mapping Configuratie
**Status:** TODO  
**Deadline:** Week 11 (21 april 2026)

**Inhoud:**
- Field mapping configuratie (MSG-3 → Maximo)
- Transformatie regels
- Default waarden
- Configuratie documentatie

**Locatie:** `config/field_mapping.json`

**Acceptatiecriteria:**
- [ ] Volledige field mapping gedocumenteerd
- [ ] Configuratie is flexibel (aanpasbaar)
- [ ] Default waarden zijn redelijk
- [ ] Documentatie van alle mappings
- [ ] Review door stakeholders

---

## 4. Presentatie & Demo Deliverables

### 4.1 Sprint Demo's
**Status:** Doorlopend  
**Frequentie:** Elke 2 weken (per sprint)

**Inhoud:**
- Demo van werkende software
- Voortgang update
- Verzamelen van feedback

**Acceptatiecriteria:**
- [ ] Werkende demo wordt getoond
- [ ] Feedback wordt verzameld en gedocumenteerd
- [ ] Volgende stappen worden besproken

---

### 4.2 Eindpresentatie
**Status:** TODO  
**Deadline:** Week 18 (15 juni 2026)

**Inhoud:**
- **Slides**:
  - Introductie en context
  - Probleemstelling
  - Oplossing en architectuur
  - Demo van werkende systeem
  - Resultaten en impact
  - Learnings en reflectie
  - Toekomst en aanbevelingen
  
- **Live Demo**:
  - MSG-3 bestand uploaden
  - Parsing en validatie
  - Change detection
  - Maximo import
  - Resultaat in Maximo tonen

**Locatie:** `docs/presentatie/`

**Acceptatiecriteria:**
- [ ] Slides zijn professioneel en compleet
- [ ] Demo is voorbereid en geoefend
- [ ] Tijd: 30-45 minuten (presentatie + vragen)
- [ ] Live demo werkt foutloos
- [ ] Review door begeleider
- [ ] Presentatie gegeven aan stakeholders

---

## Oplevering Checklist

### Code Deliverables:
- [ ] MSG-3 Parser Module
- [ ] Data Validator
- [ ] Change Detection Engine
- [ ] Mapping Engine
- [ ] Maximo REST Connector
- [ ] Main Application (CLI)
- [ ] Unit Tests (80%+ coverage)
- [ ] Integration Tests

### Documentatie Deliverables:
- [x] Projectdefinitie
- [x] Plan van Aanpak
- [ ] Onderzoek Documenten
- [ ] Technisch Ontwerp
- [ ] Gebruikershandleiding
- [ ] Technische Documentatie
- [ ] Overdracht Documentatie

### Template & Configuratie:
- [ ] Herontworpen MSG-3 Excel Template
- [ ] Mapping Configuratie
- [ ] Voorbeeld Data

### Comakership:
- [ ] Reflectie Document
- [ ] Portfolio Update
- [ ] Eindpresentatie (slides + demo)

### Repository:
- [ ] Git repository met volledige history
- [ ] README.md met quickstart
- [ ] requirements.txt
- [ ] CONTRIBUTING.md (indien relevant)
- [ ] LICENSE (indien relevant)

---

## Succes Criteria per Deliverable

### Code:
- ✅ Werkt volgens specificatie
- ✅ Unit tests met 80%+ coverage
- ✅ Gedocumenteerd (docstrings, comments)
- ✅ Code review gedaan
- ✅ Geen blocking bugs

### Documentatie:
- ✅ Compleet en actueel
- ✅ Duidelijk en begrijpelijk
- ✅ Review door stakeholders
- ✅ Voorbeelden waar nodig

### Demo/Presentatie:
- ✅ Werkende demo
- ✅ Duidelijke communicatie
- ✅ Feedback verzameld
- ✅ Stakeholders tevreden

---

*Datum: 4 februari 2026*  
*Auteur: Pedro Eduardo Cardoso*  
*Project: MSG-3 to Maximo Converter*  
*Versie: 1.0*

---

## AI Authenticiteitsverklaring

Tijdens de voorbereiding van het Plan van Aanpak heb ik **Cursor AI** gebruikt om te **verkennen van Agile methodieken, planning frameworks, en risicoanalyse templates**. Ik verklaar dat het ingeleverde werk geen AI-gegenereerde inhoud bevat. De daadwerkelijke planning, risico's en mitigatie strategieën zijn gebaseerd op mijn eigen analyse van het project en in overleg met de begeleider. Ik draag de volledige verantwoordelijkheid voor de inhoud van dit werk.

*AIAS Niveau: 2 - AI Exploratie*
