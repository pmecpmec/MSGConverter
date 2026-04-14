# Zelfevaluatie Tracking - Live Scorecard

## MSG-3 to Maximo Converter Project

**Student:** Pedro Eduardo Cardoso
**Studentnummer:** 1201832
**Organisatie:** Babcock Schiphol
**Periode:** 4 feb 2026 - 15 juni 2026
**Bedrijfsnaam en plaats:** Babcock Schiphol te Schiphol-Oost

**Datum laatste update:** 11 februari 2026 (Week 2)
**Versie:** 1.0

---

## Geschat Eindcijfer Dashboard

### Overall Score Prediction

| Categorie | Gewicht | Huidige Score | **Target MAXIMAAL** | **Realistisch** | Bijdrage |
| -------------------- | ------- | ------------- | ---------------------- | --------------- | -------- |
| **Analyseren** | 15% | 6.5 | **9.0** | 8.0 | 1.20 |
| **Adviseren** | 15% | 5.0 | **8.5** | 8.0 | 1.20 |
| **Ontwerpen** | 15% | 7.0 | **9.0** | 8.5 | 1.28 |
| **Realiseren** | 15% | 4.0 | **8.5** | 8.0 | 1.20 |
| **Manage & Control** | 15% | 6.0 | **8.0** | 7.5 | 1.13 |
| **Eindverslag** | 12.5% | 0.0 | **8.5** | 8.0 | 1.00 |
| **Presentatie** | 12.5% | 0.0 | **9.0** | 8.5 | 1.06 |
| **TOTAAL** | 100% | - | **8.7** | **8.1** | **8.1** |

**Minimale eis:** 5.5 (per competentie EN totaal)
**Oude projectie (bescheiden):** 7.2 - Ruim voldoende
**NIEUWE projectie (maximaal):** **8.1** - Goed tot Uitstekend!

**Status:** **Ambitieus maar haalbaar** - Focus op excellentie!

** Strategie:** We gaan voor 8+ scores waar mogelijk, niet tevreden met "voldoende"!

---

## Competentie Progress Overview

### Quick Status

```
Analyseren ████████░░ 80% (Goed op weg)
Adviseren ████░░░░░░ 40% (Onderzoek moet nog)
Ontwerpen █████████░ 90% (Bijna compleet)
Realiseren ███░░░░░░░ 30% (Code fase start week 5)
Manage & Control ██████░░░░ 60% (Sprint docs lopen)
```

---

## 1. ANALYSEREN (Niveau 1 vereist)

### Huidige Status

**Zelfbeoordeling NU:** 6.5 (Voldoende)
**Geschat EIND (bescheiden):** 7.0 (Goed)
** TARGET MAXIMAAL:** **8.0** (Goed tot Uitstekend!)
**Progress:** 80% ████████░░

### Gekozen Rubric Niveau

**Voldoende (6):** "Werkt volgens geplande stappen naar onderbouwde conclusies"

**Onderbouwing:**

- Systematische analyse van MSG-3 structuur (80 business rules geïdentificeerd)
- Probleemanalyse Babcock situatie
- Stakeholder analyse
- Onderzoeksrapport nog niet compleet (Week 3-4)

### Bewijsmateriaal (LIVE)

| Document | Status | Kwaliteit | Bijdrage |
| ---------------------------------------------- | ------------------- | ---------- | -------- |
| `docs/projectdefinitie/01-context-analyse.md` | Compleet | Goed | ++++ |
| `docs/projectdefinitie/02-probleemstelling.md` | Compleet | Goed | ++++ |
| `docs/technisch-ontwerp/business-rules.md` | Compleet | Uitstekend | +++++ |
| `docs/onderzoek/01-msg3-analyse.md` | Planned (Week 3) | - | +++++ |
| `docs/onderzoek/02-maximo-api.md` | Planned (Week 3) | - | ++++ |
| `docs/onderzoek/04-alternatieven-evaluatie.md` | Planned (Week 4) | - | +++++ |

**Totaal bewijsstukken:** 3 compleet, 3 gepland

### Complexiteit Beschrijving

**MSG-3 Analyse Complexiteit:**

- 12+ verschillende task types (Inspection, Lubrication, Servicing, etc.)
- Multiple interval types (Flight Hours, Flight Cycles, Calendar intervals)
- ATA Chapter hierarchie (complexe structuur)
- 80+ business rules gedocumenteerd voor validatie
- Cross-referenties tussen tasks en zones
- Versie vergelijking complexiteit (change detection)

**Analysemethode:**

- Systematisch: Excel structuur → JSON schema → Business rules
- Iteratief: Meerdere MSG-3 voorbeelden geanalyseerd
- Stakeholder input: Matthijs & Rick (maintenance engineers)

### Update Triggers

**Update dit als:**

- Onderzoeksrapport compleet (Week 3-4) → Verwachte boost naar 7.0
- POC's uitgevoerd en geanalyseerd (Week 4) → Mogelijk 7.5
- Alternatieve oplossingen geëvalueerd (Week 4)

---

## 2. ADVISEREN (Niveau 1 vereist)

### Huidige Status

**Zelfbeoordeling NU:** 5.0 (Net Voldoende - nog weinig bewijs)
**Geschat EIND (bescheiden):** 7.0 (Goed)
** TARGET MAXIMAAL:** **8.0** (Goed tot Uitstekend!)
**Progress:** 40% ████░░░░░░

### Gekozen Rubric Niveau

**Voldoende (6):** "Werkt volgens geplande stappen naar onderbouwde adviezen"

**Onderbouwing:**

- Advies over Agile aanpak (Plan van Aanpak)
- Advies over risicomitigatie strategieën
- Technologie keuzes advies (nog te documenteren)
- Onderzoeksrapport met aanbevelingen (Week 3-4)

### Bewijsmateriaal (LIVE)

| Document | Status | Kwaliteit | Bijdrage |
| ------------------------------------------------- | -------------- | --------- | -------- |
| `docs/plan-van-aanpak/01-projectaanpak.md` | Compleet | Goed | +++ |
| `docs/plan-van-aanpak/03-risicoanalyse.md` | Compleet | Goed | ++++ |
| `docs/onderzoek/00-onderzoeksrapport.md` | Not Started | - | +++++ |
| `docs/onderzoek/03-technologie-keuzes.md` | Not Started | - | +++++ |
| `docs/onderzoek/04-alternatieven-evaluatie.md` | Not Started | - | +++++ |
| `docs/overdracht/06-toekomstige-verbeteringen.md` | Week 16-18 | - | +++ |

**Totaal bewijsstukken:** 2 compleet, 4 gepland

### Complexiteit Beschrijving

**Advies Complexiteit:**

- Technologie stack selectie (Python vs C#/Java, Openpyxl vs Pandas)
- API strategie (Maximo REST vs SOAP vs MIF)
- Architecture pattern keuzes (OOP design, error handling)
- Security & performance trade-offs
- Aanbevelingen voor MSG-3 template verbetering (Week 14-15)

**Advies methode:**

- Comparatief onderzoek (meerdere alternatieven)
- Onderbouwing met criteria (performance, maintainability, leercurve)
- Stakeholder afstemming (Jasper & Fajjaaz - code support)

### Update Triggers

**Update dit als:**

- Onderzoeksrapport met aanbevelingen compleet (Week 3-4) → Boost naar 7.0
- Technologie keuzes gedocumenteerd en onderbouwd (Week 4)
- Alternatieven evaluatie compleet (Week 4) → Mogelijk 7.5
- Toekomstige verbeteringen advies (Week 16-18)

** LET OP:** Dit is momenteel de zwakste competentie - focus hierop in Week 3-4!

---

## 3. ONTWERPEN (Niveau 1 vereist)

### Huidige Status

**Zelfbeoordeling NU:** 7.0 (Goed)
**Geschat EIND (bescheiden):** 7.5 (Goed tot Uitstekend)
** TARGET MAXIMAAL:** **8.5** (Uitstekend!)
**Progress:** 90% █████████░

### Gekozen Rubric Niveau

**Goed (8):** "Ontwerpt volgens geplande stappen bruikbare oplossingen en verwerkt nieuwe inzichten"

**Onderbouwing:**

- Complete architectuur ontwerp
- 80 business rules ontwerp gedocumenteerd
- UML diagrammen (Class, Sequence, Component, Use Case)
- Detail ontwerpen (data models, API specs) nog te completeren

### Bewijsmateriaal (LIVE)

| Document | Status | Kwaliteit | Bijdrage |
| --------------------------------------------------- | ----------- | ---------- | -------- |
| `docs/technisch-ontwerp/01-architectuur-ontwerp.md` | Compleet | Uitstekend | +++++ |
| `docs/technisch-ontwerp/business-rules.md` | Compleet | Uitstekend | +++++ |
| `docs/technisch-ontwerp/uml-diagrammen/` | Compleet | Goed | ++++ |
| `docs/technisch-ontwerp/02-datamodellen.md` | Week 4-5 | - | ++++ |
| `docs/technisch-ontwerp/03-api-specificaties.md` | Week 4-5 | - | ++++ |
| `docs/technisch-ontwerp/06-error-handling.md` | Week 5 | - | +++ |
| `docs/technisch-ontwerp/07-security.md` | Week 5 | - | +++ |

**Totaal bewijsstukken:** 3 compleet, 4 gepland

### Complexiteit Beschrijving

**Ontwerp Complexiteit:**

- **OOP Design:** 5 hoofdklassen (Parser, Validator, Mapper, MaximoConnector, ChangeDetector)
- **Design Patterns:** Strategy (validatie), Factory (object creation), Adapter (API)
- **Data Flow:** Complex (Excel → JSON → Validation → Mapping → Maximo)
- **Business Rules Engine:** 80+ validatieregels met prioriteit levels
- **Error Handling:** Multi-level (field, row, file, API)
- **API Integration:** REST API ontwerp met retry logic, rate limiting

**Ontwerp keuzes:**

- Modular architecture (loose coupling, high cohesion)
- Single Responsibility Principle per module
- Testability (dependency injection, mocking)
- Extensibility (nieuwe business rules eenvoudig toevoegen)

### Update Triggers

**Update dit als:**

- Datamodellen compleet (Week 4-5) → Blijft waarschijnlijk 7.5
- API specs gedocumenteerd (Week 4-5)
- Security & performance ontwerp (Week 5)

** STERKE PUNT:** Dit is een van je sterkste competenties!

---

## 4. REALISEREN (Niveau 2 vereist)

### Huidige Status

**Zelfbeoordeling NU:** 4.0 (Onvoldoende - nog geen code)
**Geschat EIND (bescheiden):** 7.5 (Goed)
** TARGET MAXIMAAL:** **8.0-8.5** (Uitstekend!)
**Progress:** 30% ███░░░░░░░

** LET OP:** Dit is niveau 2 - HOGERE EIS dan andere competenties!
** BELANGRIJK:** Met code excellence (CI/CD, tests, docs) → 8.5 is haalbaar!

### Gekozen Rubric Niveau

**Goed (8):** "Realiseert volgens geplande stappen bruikbare oplossingen en verwerkt nieuwe inzichten"

**Onderbouwing:**

- Repository structuur opgezet
- Code templates klaar
- Business rules implementation (40% - `src/validator/business_rules.py`)
- Parser implementatie (0% - Week 5-7)
- Mapping engine (0% - Week 8-10)
- Maximo connector (0% - Week 11-12)
- Tests (0% - Week 5-17)

### Bewijsmateriaal (LIVE)

| Code Module | Regels | Status | Kwaliteit | Bijdrage |
| --------------------------------- | --------- | ------------- | --------- | -------- |
| **TOTAAL VERWACHT** | **2000+** | - | - | - |
| `src/parser/` | ~300 | Week 5-7 | - | +++++ |
| `src/validator/business_rules.py` | ~150/400 | 40% | Goed | +++++ |
| `src/mapping/` | ~350 | Week 8-10 | - | +++++ |
| `src/maximo/connector.py` | ~250 | Week 11-12 | - | +++++ |
| `src/change_detection/` | ~200 | Week 12-13 | - | ++++ |
| `tests/` | ~500 | Week 5-17 | - | +++++ |

**Huidige code:** ~150 regels (6% van target 2500)
**Vereist minimum:** 250 regels (wordt makkelijk behaald)
**Target eind project:** 2000+ regels

### Complexiteit Beschrijving

**Realisatie Complexiteit:**

- **Excel Parsing:** Openpyxl library, dynamic cell ranges, merged cells handling
- **Business Rules Engine:** 80+ validatieregels met custom error messages
- **Data Transformation:** MSG-3 → Maximo object mapping (complexe veldtransformaties)
- **API Integration:** REST API met authentication, retry logic, error handling
- **Change Detection:** Algoritme voor versie vergelijking (hash-based + field-level)
- **Testing:** Unit tests, integration tests, >80% coverage target

**Technische uitdagingen:**

- Dynamische Excel structuur (niet alle MSG-3's identiek)
- Maximo API rate limiting en error recovery
- Data validatie met context-aware business rules
- Performance (grote Excel files, 1000+ rows)

**Code support beschikbaar:**

- Jasper van Polen (Data Analyst)
- Fajjaaz Chandoe (Data Analyst)

### Update Triggers

**Update dit als:**

- Parser module compleet (Week 7) → Verwachte boost naar 6.0
- Validator compleet (Week 8) → Boost naar 6.5
- Mapping engine compleet (Week 10) → Boost naar 7.0
- Maximo connector compleet (Week 12) → Boost naar 7.5
- Tests >80% coverage (Week 17) → Boost naar 8.0
- Demo werkend (Week 18) → **Target 8.0-8.5**

** PRIORITEIT 1:** Dit is de belangrijkste competentie - niveau 2 vereist!

### Van Goed (7.5) naar Uitstekend (8.0-8.5)

**Wat maakt het verschil?**

#### Code Kwaliteit (niet alleen werkende code)

- **Clean Code principes:**
 - Functienamen die exact vertellen wat ze doen
 - Geen magic numbers (gebruik constanten)
 - DRY principle (Don't Repeat Yourself)
 - Single Responsibility per functie/class

- **Professionele documentatie:**
 - Docstrings met Google/NumPy style
 - Type hints overal (Python 3.10+)
 - README met installatie + gebruik + architectuur
 - API documentatie (Sphinx of MkDocs)

#### Testing Excellence

- **Niet alleen tests, maar GOEDE tests:**
 - > 90% coverage (niet 80%)
 - Edge cases getest (niet alleen happy path)
 - Integration tests (niet alleen unit tests)
 - Performance tests (hoe snel?)
 - Mock objecten voor Maximo API

#### Professionele Setup

- **Development best practices:**
 - Git branching strategy (feature branches)
 - Meaningful commit messages
 - CI/CD pipeline (GitHub Actions of GitLab CI)
 - Pre-commit hooks (black, flake8, mypy)
 - Requirements.txt + requirements-dev.txt

#### Documentatie die WOW is

- **Niet alleen wat, maar waarom:**
 - Architecture Decision Records (ADR's)
 - "Waarom openpyxl en niet pandas?" → Gedocumenteerd met benchmarks
 - Design patterns gebruikt → Uitgelegd waarom
 - Code comments: "Why" not "What"

#### Extra Mile

- **Wat assessoren WOW vinden:**
 - Performance metrics: "Parser verwerkt 1000 rows in 2.3s"
 - Error recovery: "Bij API failure: retry 3x met exponential backoff"
 - Logging: Proper logging met levels (DEBUG, INFO, WARNING, ERROR)
 - Config management: .env file + pydantic settings
 - Containerization: Docker file voor easy deployment

**Concrete Actieplan:**

```markdown
Week 5-7: Parser + Validator

- Write clean code from start (niet refactoren later)
- 90%+ test coverage
- Type hints overal
- Docstrings overal

Week 8-10: Mapping + API

- Integration tests
- Mock Maximo API
- Performance tests
- Error handling met retries

Week 11-13: Polish & Excellence

- CI/CD pipeline opzetten
- Sphinx documentatie genereren
- Docker containerization
- Performance benchmarks runnen

Week 14-17: Professional Touch

- Code review met Jasper/Fajjaaz
- Refactor based on feedback
- Add pre-commit hooks
- Architecture Decision Records schrijven
```

**Dit maakt verschil tussen 7.5 en 8.5!**

---

## 5. MANAGE & CONTROL (Niveau 1 vereist)

### Huidige Status

**Zelfbeoordeling NU:** 6.0 (Voldoende)
**Geschat EIND (bescheiden):** 7.0 (Goed)
** TARGET MAXIMAAL:** **7.5-8.0** (Goed tot Uitstekend!)
**Progress:** 60% ██████░░░░

### Gekozen Rubric Niveau

**Voldoende (6):** "Werkt volgens geplande stappen aan het beheren, monitoren en optimaliseren van ICT-systemen en/of organisatieprocessen"

**Onderbouwing:**

- Planning gemaakt (18 weken roadmap)
- Risico's geïdentificeerd en mitigaties bedacht
- Agile aanpak gedefinieerd
- Sprint documentatie (moet nog bijgehouden worden vanaf Week 3)
- Testresultaten tracking (Week 5-17)
- Overdracht planning (Week 16-18)

### Bewijsmateriaal (LIVE)

| Document | Status | Kwaliteit | Bijdrage |
| ----------------------------------------------- | ------------- | ---------- | -------- |
| `docs/plan-van-aanpak/01-projectaanpak.md` | Compleet | Goed | ++++ |
| `docs/plan-van-aanpak/02-planning.md` | Compleet | Goed | ++++ |
| `docs/plan-van-aanpak/03-risicoanalyse.md` | Compleet | Uitstekend | +++++ |
| `docs/scrum/` | Week 3+ | Basis | +++ |
| `docs/testcases/06-testresultaten.md` | Week 5-17 | - | ++++ |
| `docs/overdracht/03-installatie-instructies.md` | Week 16-18 | - | +++ |
| `docs/overdracht/04-troubleshooting.md` | Week 16-18 | - | +++ |
| `docs/overdracht/05-changelog.md` | Week 5-18 | - | +++ |

**Totaal bewijsstukken:** 3 compleet, 5 gepland

### Complexiteit Beschrijving

**Management Complexiteit:**

- **Projectmanagement:** 18 weken, solo project, meerdere stakeholders
- **Risicomanagement:** 15+ geïdentificeerde risico's met mitigatie strategieën
- **Kwaliteitsborging:** Test-driven development, code reviews met Jasper/Fajjaaz
- **Stakeholder management:**
 - Matthijs Meijer (Sr. Maintenance Engineer)
 - Rick Kramer (Maintenance Service Coordinator)
 - Arie Ismael (Coach Windesheim)
 - Jasper & Fajjaaz (Code support)
- **Agile werkwijze:** Sprints van 2 weken, daily standups (solo), sprint reviews
- **Versiecontrole:** Git, branching strategy, commit conventions

**Management uitdagingen:**

- Solo project (geen team, alle rollen zelf)
- Nieuwe technologie leren (Maximo API)
- Complexe stakeholder verwachtingen managen
- Planning aanpassen bij wijzigingen (MSG-3 template redesign Week 14-15)

### Update Triggers

**Update dit als:**

- Sprint 1 documentatie compleet (Week 3-4) → Blijft 6.0
- Elke sprint retrospective (elke 2 weken) → Geleidelijke groei naar 7.0
- Testresultaten tracking start (Week 5)
- Overdracht documenten compleet (Week 16-18) → Boost naar 7.0
- Succesvolle oplevering (Week 18) → Mogelijk 7.5

---

## PROFESSIONAL SKILLS

### Overzicht

| Skill | Huidige | **MAXIMAAL Target** | Realistisch | Status |
| -------------------------------------- | ------- | ---------------------- | ----------- | -------------- |
| Persoonlijk Leiderschap - Ondernemend | 7.0 | **9.0** | 8.5 | Sterk |
| Persoonlijk Leiderschap - Ontwikkeling | 6.0 | **8.5** | 8.0 | Reflectie++ |
| Toekomstgericht - Normen & Waarden | 8.0 | **9.0** | 9.0 | Uitstekend! |
| Toekomstgericht - Organisatie | 6.5 | **8.5** | 8.0 | Sterk |
| Onderzoekend Probleemoplossend | 6.0 | **9.0** | 8.5 | Onderzoek++ |
| Doelgericht - Samenwerking | 6.5 | **8.5** | 8.0 | Sterk |
| Doelgericht - Communicatie | 7.0 | **9.0** | 8.5 | Sterk |

### 1. Persoonlijk Leiderschap - Ondernemend zijn

**Huidige:** 7.0 (Goed) | **Geschat Eind:** 7.5 (Goed)

**Bewijs:**

- Proactief stage gezocht en gevonden bij Babcock
- Eigen initiatief voor MSG-3 template verbetering (Week 14-15)
- Zelfstandig technische architectuur opgezet
- Weekly progress updates naar stakeholders

**Complexiteit:** Solo project, zelfstandig opereren, eigen doelen stellen

### 2. Persoonlijk Leiderschap - Professionele ontwikkeling

**Huidige:** 6.0 (Voldoende) | **Geschat Eind:** 7.0 (Goed)

**Bewijs:**

- `docs/MIJN-BIJDRAGE-VS-AI.md` - Reflectie op AI-gebruik
- Sprint retrospectives (vanaf Week 3)
- `docs/reflectie/reflectieverslag.md` (Week 17-18) - Belangrijkste bewijs!

**Update Trigger:** Reflectieverslag compleet → Boost naar 7.0

### 3. Toekomstgericht Organiseren - Normen & Waarden

**Huidige:** 8.0 (Uitstekend) | **Geschat Eind:** 8.0 (Uitstekend)

**Bewijs:**

- `docs/ai/AI-GEBRUIK.md` - Ethisch verantwoord AI-gebruik
- `docs/ai/AI-AUTHENTICITEITSVERKLARINGEN.md` - Transparantie
- Data privacy (geen credentials in code)
- Open source approach

** STERKE PUNT:** Excellente AI-transparantie documentatie!

### 4. Toekomstgericht Organiseren - Organisatorische context

**Huidige:** 6.5 (Voldoende tot Goed) | **Geschat Eind:** 7.0 (Goed)

**Bewijs:**

- `docs/projectdefinitie/01-context-analyse.md` - Business case
- `docs/projectdefinitie/05-stakeholders.md` - Stakeholder management
- `docs/overdracht/` (Week 16-18) - Overdrachtsplan

### 5. Onderzoekend Probleemoplossend

**Huidige:** 6.0 (Voldoende) | **Geschat Eind:** 7.0 (Goed)

**Bewijs:**

- `docs/onderzoek/00-onderzoeksrapport.md` (Week 3-4)
- POC's en experimenten (Week 4)
- Creatieve oplossing voor MSG-3 complexiteit

**Update Trigger:** Onderzoeksrapport compleet → Boost naar 7.0

### 6. Doelgericht Interacteren - Samenwerking

**Huidige:** 6.5 (Voldoende tot Goed) | **Geschat Eind:** 7.0 (Goed)

**Bewijs:**

- Samenwerking Jasper & Fajjaaz (code reviews)
- Weekly meetings Matthijs & Rick
- Sprint reviews met stakeholders
- Reflectie op samenwerking (Week 17-18)

### 7. Doelgericht Interacteren - Communicatie

**Huidige:** 7.0 (Goed) | **Target:** 8.5 (Uitstekend)

**Bewijs:**

- Professionele documentatie (Nederlands)
- Code comments (Engels)
- README's (Engels)
- Presentatie assessment (Week 18)

**Van Goed (7.0) naar Uitstekend (8.5):**

- Presentatie met visuele storytelling
- Code comments met "waarom" niet alleen "wat"
- Technische blog post schrijven over MSG-3 project
- Demo video met professionele voice-over

---

## BEDRIJFSEVALUATIE (Babcock Schiphol)

**Belangrijk:** Dit formulier wordt ingevuld door **Matthijs Meijer** en **Rick Kramer**.
**Impact:** Adviserend maar ZEER belangrijk voor eindoordeel!
**Deadline:** Week 17 (aanvragen), Week 18 (ontvangen en ondertekend)

### Target Scores Bedrijfsevaluatie

| Criterium | Beschrijving | Huidige | **MAXIMAAL** | Realistisch |
| ---------------------- | --------------------------------------------------------- | ------- | --------------- | ----------- |
| **Zelfstandigheid** | Zelfsturing, initiatief, lerende houding | 7.0 | **9.0** | 8.5 |
| **Gedrag** | Motivatie, communicatie, inzet, verantwoordelijkheid | 7.5 | **9.0** | 8.5 |
| **Omgaan met Context** | Flexibiliteit, grip op situatie, omgaan met veranderingen | 7.0 | **8.5** | 8.0 |
| **Professionaliteit** | Betrouwbaarheid, samenwerking, emotioneel evenwicht | 7.5 | **9.0** | 8.5 |

**Gemiddelde verwacht:** 8.4 (Uitstekend!)

### Strategie voor Maximale Bedrijfsevaluatie

#### 1. Zelfstandigheid (Target: 8.5)

**Hoe bereik je 8.5+?**

- Neem initiatief VOOR ze het vragen
 - Voorbeelden: "Ik heb al voorbereid...", "Ik wilde voorstellen..."
- Los problemen zelf op (met documentatie)
 - "Ik had issue X, heb oplossing Y gevonden via Z"
- Stel verdiepende vragen
 - Niet alleen "Hoe werkt dit?" maar "Waarom is gekozen voor deze aanpak?"
- Kom met verbetervoorstellen
 - MSG-3 template redesign (Week 14-15) is PERFECT voorbeeld!

**Bewijs verzamelen:**

- Wekelijkse email updates (proactief, niet wachten op vraag)
- Documenteer je problem-solving proces
- MSG-3 template verbetering voorstel

#### 2. Gedrag (Target: 8.5)

**Hoe bereik je 8.5+?**

- Toon enthousiasme voor het project
 - "Ik vind het interessant dat..."
 - "Ik wil graag meer leren over..."
- Wees betrouwbaar: deadlines halen
 - Liever vroeg dan op tijd, nooit te laat
- Communiceer proactief bij problemen
 - "Ik loop tegen X aan, mijn plan is Y, akkoord?"
- Vraag om feedback en verwerk het zichtbaar

**Bewijs verzamelen:**

- Track alle deadlines (haal ze ALLEMAAL)
- Documenteer feedback en hoe je het verwerkt hebt
- Toon enthousiasme in meetings

#### 3. Omgaan met Context (Target: 8.0)

**Hoe bereik je 8.0+?**

- Pas je aan aan hun werkwijze
 - Babcock gebruikt eigen MSG-3 proces → Leer het!
- Flexibel bij wijzigingen
 - MSG-3 template redesign (Week 14-15) = BEWIJS van flexibiliteit!
- Leer de maintenance engineering context
 - ATA chapters, task types, intervals → Snap het écht!

**Bewijs verzamelen:**

- MSG-3 template aanpassing = PERFECT bewijs!
- Documenteer hoe je je aanpaste aan hun werkwijze
- Laat zien dat je de aviation maintenance context snapt

#### 4. Professionaliteit (Target: 8.5)

**Hoe bereik je 8.5+?**

- Kom altijd voorbereid naar meetings
 - Agenda, vragen, voortgang update ready
- Respecteer hun tijd
 - Op tijd, efficiënte meetings, duidelijke vragen
- Netwerk opbouwen
 - Ook contact met Jasper & Fajjaaz (code support)
- Professionele communicatie
 - Email: Formeel maar vriendelijk
 - Meetings: Luisteren én bijdragen

**Bewijs verzamelen:**

- Meeting notulen (laat zien dat je voorbereid was)
- Professionele email communicatie
- Samenwerking met Jasper & Fajjaaz gedocumenteerd

### Kritieke Acties voor Bedrijfsevaluatie

**Week 17 (2 weken voor oplevering):**

1. Vraag evaluatieformulier op bij Windesheim
2. Stuur naar Matthijs & Rick met:
 - Brief waarin je vraagt om evaluatie
 - Link naar alle deliverables
 - Uitleg wat ze moeten doen
 - Deadline: 1 week voor assessment

**Week 18 (voor assessment):** 3. Follow-up als je nog geen formulier hebt 4. Ontvang ondertekend formulier 5. Include in oplevering

** ZONDER ONDERTEKEND FORMULIER = GEEN ASSESSMENT = NIET AFSTUDEREN!**

### Open Vragen Voorbereiding

Het formulier heeft 3 open vragen. Help ze door voorbeelden te geven:

**1. "Waarom is het product geschikt voor uw gebruikssituatie?"**

_Suggestie wat je kunt voorbereiden:_

> Het MSG-3 to Maximo conversietool lost een kritiek probleem op: handmatige invoer van 1000+ maintenance tasks kost nu 40+ uur en is foutgevoelig. De tool reduceert dit naar <1 uur met geautomatiseerde validatie van 80+ business rules. Dit verhoogt data kwaliteit en bespaart maintenance engineers significant tijd.

**2. "Waarom is de student geschikt voor het hbo-werkveld?"**

_Wat ze kunnen schrijven (gebaseerd op jouw acties):_

> Pedro toonde sterke zelfstandigheid en probleemoplossend vermogen. Hij kwam zelfstandig met een verbetering van onze MSG-3 template (Week 14-15) en documenteerde alles professioneel. Hij communiceerde proactief over voortgang en problemen. Zijn technische vaardigheden (Python, API integratie) en lerende houding maken hem zeer geschikt voor junior developer rol.

**3. "Welke overige opmerkingen over de opdrachtuitvoering?"**

_Wat ze kunnen schrijven:_

> Het project werd professioneel uitgevoerd volgens afgesproken planning. Pedro hield zich aan deadlines, communiceerde helder en leverde kwaliteit werk op. De documentatie is uitstekend en maakt overdracht gemakkelijk. Zijn transparantie over AI-gebruik is voorbeeldig.

** TIP:** Stuur 2 weken voor eind een "Project Samenvatting" email naar Matthijs & Rick met:

- Wat heb ik opgeleverd?
- Wat waren de resultaten?
- Wat waren de hoogtepunten?

Dit maakt het voor hen makkelijker om het formulier in te vullen!

---

## Versie Geschiedenis & Updates

### Week 2 (11 feb 2026) - BASELINE

**Overall Score:** 5.8 → Geschat Eind: 7.2

**Wat is klaar:**

- Projectdefinitie compleet
- Plan van Aanpak compleet
- Technisch ontwerp basis (90%)
- AI-documentatie uitstekend
- Business rules gedocumenteerd (80 regels)

**Wat moet nog:**

- Onderzoeksrapport (Week 3-4) - **PRIORITEIT**
- Sprint documentatie starten (Week 3)
- Code schrijven (Week 5-13) - **GROOTSTE IMPACT**
- Reflectieverslag (Week 17-18)

**Focus volgende 2 weken:**

1. Onderzoeksrapport compleet → Boost Analyseren & Adviseren naar 7.0
2. Sprint 1 documentatie → Manage & Control op peil houden
3. POC's maken → Voorbereiden op code fase

---

### Week 4 (Verwacht: 3 maart 2026)

**Geschatte Overall Score:** 6.2 → Geschat Eind: 7.2

**Verwacht klaar:**

- Onderzoeksrapport compleet
- Sprint 1 & 2 documentatie
- Detail ontwerpen (datamodellen, API specs)
- POC's uitgevoerd

**Impact:**

- Analyseren: 6.5 → 7.0
- Adviseren: 5.0 → 7.0 (Grootste boost)
- Ontwerpen: 7.0 → 7.5

---

### Week 8 (Verwacht: 31 maart 2026)

**Geschatte Overall Score:** 6.5 → Geschat Eind: 7.2

**Verwacht klaar:**

- Parser module compleet (~300 regels)
- Validator compleet (~400 regels)
- Sprints 1-4 gedocumenteerd
- Eerste tests geschreven

**Impact:**

- Realiseren: 4.0 → 6.5 (Enorme boost)

---

### Week 13 (Verwacht: 5 mei 2026)

**Geschatte Overall Score:** 7.0 → Geschat Eind: 7.2

**Verwacht klaar:**

- Mapping engine compleet (~350 regels)
- Maximo connector compleet (~250 regels)
- Change detection (~200 regels)
- Core applicatie werkend
- Sprints 1-7 gedocumenteerd

**Impact:**

- Realiseren: 6.5 → 7.5 (Target niveau bereikt!)

---

### Week 18 (Verwacht: 15 juni 2026)

**Geschatte Overall Score:** 7.2 (TARGET BEREIKT!)

**Verwacht klaar:**

- Alle code compleet (2000+ regels)
- Tests >80% coverage
- Reflectieverslag compleet
- Overdracht documentatie compleet
- Demo video
- Presentatie klaar

**Impact:**

- Alle competenties op target niveau
- Reflectieverslag & Presentatie: 0 → 7.0-7.5

---

## Auto-Update Triggers (voor AI Assistant)

**Update deze zelfevaluatie automatisch wanneer:**

### Code Updates

```
IF nieuwe code in src/
 EN totale regels > vorige versie + 50
THEN update "Realiseren" sectie
 - Update regelcount tabel
 - Update progress percentage
 - Herbereken geschatte score
 - Update overall dashboard
```

### Documentatie Updates

```
IF nieuwe docs in onderzoek/
THEN update "Analyseren" EN "Adviseren"

IF nieuwe docs in technisch-ontwerp/
THEN update "Ontwerpen"

IF nieuwe docs in scrum/
THEN update "Manage & Control"

IF nieuwe docs in overdracht/
THEN update "Manage & Control"
```

### Weekly Reviews

```
EVERY Friday
THEN:
 - Check all progress percentages
 - Update version history
 - Recalculate overall score
 - Check if geschatte eindscores nog realistisch zijn
 - Notify Pedro van huidige status
```

### Milestone Triggers

```
IF Week 3 OR Week 4
THEN update verwacht naar Week 4 baseline

IF Week 7 OR Week 8
THEN update verwacht naar Week 8 baseline

IF Week 12 OR Week 13
THEN update verwacht naar Week 13 baseline

IF Week 18
THEN final update voor oplevering
```

---

## Risico's & Waarschuwingen

### Kritieke Aandachtspunten

1. **Realiseren (Niveau 2 vereist!)**
 - Status: 4.0 (ONVOLDOENDE)
 - Actie: Code schrijven MOET starten Week 5
 - Risico: Als code niet op tijd klaar → ONVOLDOENDE voor gehele module!

2. **Adviseren (Zwakste punt)**
 - Status: 5.0 (Net voldoende)
 - Actie: Onderzoeksrapport Week 3-4 is CRUCIAAL
 - Risico: Zonder goed onderzoeksrapport mogelijk onvoldoende

3. **Reflectieverslag (12.5% van eindcijfer)**
 - Status: 0.0 (Nog niet gemaakt)
 - Actie: NIET uitstellen tot laatste week!
 - Advies: Begin notities te maken vanaf Week 10

### Aandachtspunten

1. **Sprint Documentatie**
 - Moet ELKE 2 weken worden bijgewerkt
 - Gemiste sprints kan je niet meer "inhalen" aan het einde
 - Start Week 3 en hou vol!

2. **Test Coverage**
 - > 80% vereist voor goede score
 - Begin tests te schrijven vanaf Week 5 (parallel met code)
 - Niet wachten tot Week 17!

---

## Tips voor Succes

### 1. Week-to-Week Monitoring

Check elke vrijdag:

- [ ] Welke deliverables zijn af?
- [ ] Welke competenties zijn verbeterd?
- [ ] Lig ik op schema voor mijn geschatte eindscores?

### 2. Bewijs Verzamelen

Bij elke deliverable:

- [ ] Voeg toe aan "Bewijsmateriaal" sectie hierboven
- [ ] Update progress percentage
- [ ] Noteer complexiteit aspecten
- [ ] Check of competentie score moet worden aangepast

### 3. Balans

Let op verdeling tussen competenties:

- Niet alleen focussen op "Realiseren" (code)
- Ook "Adviseren" en "Manage & Control" blijven bijhouden
- Professional Skills niet vergeten!

### 4. Early Warning Systeem

Als een competentie <6.0 blijft na:

- Week 8: Alarm! Actie ondernemen
- Week 13: Laatste kans om bij te sturen
- Week 16: Te laat om grote wijzigingen te maken

---

## Score Berekenaar

### Gebruik dit om je cijfer te berekenen:

```
Eindcijfer =
 (Analyseren × 0.15) +
 (Adviseren × 0.15) +
 (Ontwerpen × 0.15) +
 (Realiseren × 0.15) +
 (Manage & Control × 0.15) +
 (Eindverslag × 0.125) +
 (Presentatie × 0.125)

Minimale eis per competentie: 5.5
Minimale eis totaal: 5.5

Als 1 competentie < 5.5 → Automatisch cijfer 1.0!
```

### Huidige Berekening:

```
(6.5 × 0.15) + # Analyseren
(5.0 × 0.15) + # Adviseren
(7.0 × 0.15) + # Ontwerpen
(4.0 × 0.15) + # Realiseren (NOG ONDER MINIMUM!)
(6.0 × 0.15) + # Manage & Control
(0.0 × 0.125) + # Eindverslag
(0.0 × 0.125) # Presentatie
= 4.3 (TIJDELIJK - veel nog niet af)
```

### Oude (Bescheiden) Berekening:

```
(7.0 × 0.15) + # Analyseren
(7.0 × 0.15) + # Adviseren
(7.5 × 0.15) + # Ontwerpen
(7.5 × 0.15) + # Realiseren
(7.0 × 0.15) + # Manage & Control
(7.0 × 0.125) + # Eindverslag
(7.5 × 0.125) # Presentatie
= 7.2 (Goed)
```

### NIEUWE (Maximale) Berekening:

```
(8.0 × 0.15) + # Analyseren (+1.0!)
(8.0 × 0.15) + # Adviseren (+1.0!)
(8.5 × 0.15) + # Ontwerpen (+1.0!)
(8.0 × 0.15) + # Realiseren (+0.5!)
(7.5 × 0.15) + # Manage & Control (+0.5!)
(8.0 × 0.125) + # Eindverslag (+1.0!)
(8.5 × 0.125) # Presentatie (+1.0!)
= 8.1 (UITSTEKEND!)

Verschil: +0.9 punten door focus op excellence!
```

** Strategie:** Van "voldoende" naar "excellent" mentaliteit!

---

## STRATEGIE: Maximale Punten Behalen (8.0+)

### Filosofie: Excellence, niet "Voldoende"

**Mindset shift:**

- "Is dit goed genoeg?" (leidt tot 6.0-7.0)
- "Hoe kan ik dit EXCELLENT maken?" (leidt tot 8.0-9.0)

### Top 10 Differentiators (Goed → Uitstekend)

#### 1. **Extra Mile gaan (niet alleen requirements)**

- Minimum: MSG-3 parser
- Extra: + Change detection + Version comparison + Reporting dashboard

#### 2. **Documentatie is een PRODUCT**

- Minimum: Code comments
- Extra: Architecture Decision Records + API docs + Tutorial videos

#### 3. **Testing is SERIOUS**

- Minimum: 80% coverage
- Extra: 95% coverage + Integration tests + Performance benchmarks + CI/CD

#### 4. **Professionele Setup**

- Minimum: Git repository
- Extra: + Branching strategy + Pre-commit hooks + Docker + CI/CD pipeline

#### 5. **Communicatie is PROACTIEF**

- Minimum: Reageren op vragen
- Extra: Wekelijkse updates + Blog posts + Demo videos

#### 6. **Leer de CONTEXT**

- Minimum: Weet wat MSG-3 is
- Extra: Snap de aviation maintenance industry + ATA standards + Regulatory context

#### 7. **Reflectie met DIEPGANG**

- Minimum: "Ik heb geleerd..."
- Extra: "Ik ontdekte dat X, daarom paste ik Y aan, resultaat was Z, conclusie..."

#### 8. **Code Quality MATTERS**

- Minimum: Werkende code
- Extra: Clean code + Design patterns + Type hints + Docstrings + Performance optimized

#### 9. **Stakeholder Management is KEY**

- Minimum: Meetings bijwonen
- Extra: Voorbereide agenda + Follow-up emails + Actief vragen stellen + Netwerken

#### 10. **Presentation WOW Factor**

- Minimum: PowerPoint slides
- Extra: Storytelling + Live demo + Visuele metaforen + Engaging delivery

### Per Competentie: Goed → Uitstekend Acties

#### ANALYSEREN (Target: 8.0)

**Van 7.0 naar 8.0:**

- Niet alleen "wat" maar "waarom" analyseren
- Multiple perspect ieven: Technical + Business + User
- Kwantitatief: Meetbare metrics ("40 uur → <1 uur")
- Vergelijkend: Alternatieven systematisch geëvalueerd
- Validatie: Analyse teruggelegd aan stakeholders

#### ADVISEREN (Target: 8.0)

**Van 7.0 naar 8.0:**

- Evidence-based: Elke aanbeveling met bewijs
- Trade-offs: "Optie A is sneller maar minder maintainable, advies: B omdat..."
- Risk assessment: Per advies de risico's benoemen
- Implementation path: Niet alleen WÁT maar HOE implementeren
- Draagvlak: Stakeholders betrekken bij advisering

#### ONTWERPEN (Target: 8.5)

**Van 7.5 naar 8.5:**

- Design patterns: Expliciet benoemen en motiveren
- Toekomstbestendig: "Als we later X willen, kunnen we..."
- Trade-off analysis: Performance vs Maintainability documented
- Multiple iterations: "Versie 1 was X, na feedback werd het Y"
- Validation: Design review met Jasper/Fajjaaz

#### REALISEREN (Target: 8.0-8.5) - MEEST BELANGRIJK!

**Van 7.5 naar 8.5:**

- Professional code quality (zie sectie hierboven)
- Testing excellence: 95%+ coverage
- CI/CD pipeline: Automated testing + deployment
- Performance: Benchmarks + optimization
- Production-ready: Docker + Monitoring + Logging

#### MANAGE & CONTROL (Target: 7.5-8.0)

**Van 7.0 naar 8.0:**

- Proactieve planning updates
- Risk management: Niet alleen identify maar ook monitor & mitigate
- Quality gates: Per sprint: Definition of Done checklist
- Retrospectives met ACTIONS (niet alleen praten)
- Metrics: Velocity tracking, burndown charts

### Weekly Excellence Checklist

**Elke week vraag jezelf:**

- [ ] Heb ik de extra mile gegaan? (niet alleen minimum)
- [ ] Is mijn documentatie excellent? (niet alleen voldoende)
- [ ] Heb ik proactief gecommuniceerd? (niet alleen gereageerd)
- [ ] Heb ik stakeholders betrokken? (niet alleen geïnformeerd)
- [ ] Is mijn code production-ready? (niet alleen werkend)
- [ ] Heb ik gereflecteerd met diepgang? (niet alleen oppervlakkig)

### Red Flags die Excellence blokkeren

** Vermijd deze:**

1. "Is dit goed genoeg?" mentaliteit
2. Documentatie als afterthought
3. Tests alleen voor coverage %
4. Copy-paste code zonder begrip
5. Communiceren alleen als het nodig is
6. Reflectie van 1 pagina (te kort!)
7. Demo zonder voorbereiding
8. Code zonder comments/docstrings
9. Git commits: "changes" (niet beschrijvend)
10. Presentatie met alleen bullet points

** Doe dit in plaats:**

1. "Hoe maak ik dit EXCELLENT?" mentaliteit
2. Documentatie vanaf dag 1
3. Tests die waarde toevoegen
4. Begrijp elke regel code die je schrijft
5. Wekelijkse proactieve updates
6. Reflectie van 10+ pagina's met voorbeelden
7. Demo met script + back-up plan
8. Code self-documenting + docstrings
9. Git commits: "feat(parser): Add support for interval validation #42"
10. Presentatie met verhaal + visuele metaforen

---

## Conclusie & Actiepunten

### Huidige Situatie (Week 2)

 **Goede basis:** Ontwerpen en AI-documentatie zijn uitstekend
 **Aandacht nodig:** Adviseren en Realiseren
 **Nieuwe Ambitie:** Niet 7.2 maar **8.1** target!

### Top 3 Prioriteiten Komende 4 Weken:

1. **Onderzoeksrapport** (Week 3-4) → Boost Analyseren & Adviseren naar 8.0
2. **Sprint Documentatie** starten (Week 3+) → Excellence from start
3. **Code Excellence setup** (Week 5) → Pre-commit hooks, CI/CD, testing framework

### Verwachting:

- Oude (bescheiden) target: **7.2** (Goed)
- **NIEUWE (excellent) target: 8.1** (Goed tot Uitstekend)

**Verschil:** Focus op excellence, niet "voldoende"!

**Laatste update:** 11 februari 2026, 15:30
**Volgende update:** Vrijdag 21 februari 2026 (Week 3 review)

---

_ Dit document wordt automatisch bijgewerkt door je AI Assistant tijdens het project._
_Check elke vrijdag je progress en update je planning indien nodig!_
