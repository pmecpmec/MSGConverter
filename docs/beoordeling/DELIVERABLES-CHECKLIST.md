# Deliverables Checklist - Windesheim Comakership
## MSG-3 to Maximo Converter Project

**Student:** Pedro Eduardo Cardoso
**Organisatie:** Babcock Schiphol
**Periode:** 4 feb - 15 juni 2026
**Opleiding:** Associate Degree Software Developer (ADSD)
**Instelling:** Windesheim

**Begeleiding:**
- Matthijs Meijer - Sr. Maintenance Engineer (Stagebegeleider Babcock)
- Rick Kramer - Maintenance Service Coordinator (Stagebegeleider Babcock)
- Jasper van Polen - Data Analyst (Code support)
- Fajjaaz Chandoe - Data Analyst (Code support)
- Arie Ismael - Stage Coach (Windesheim)

---

## Gerelateerde Documenten

### **[ZELFEVALUATIE-TRACKING.md](ZELFEVALUATIE-TRACKING.md)** **LIVE SCORECARD**
**Jouw persoonlijke dashboard - zie hier altijd waar je staat!**
- Live progress per competentie (0% → 100%)
- Geschat eindcijfer calculator (huidige: 7.2 verwacht)
- Auto-updates bij nieuwe code/docs
- Wekelijkse versie geschiedenis
- Risico waarschuwingen

**Check dit ELKE VRIJDAG tijdens je weekly review!**

### **[BEOORDELINGSCRITERIA.md](BEOORDELINGSCRITERIA.md)** - Beoordelingscriteria
- Alle criteria uit het beoordelingsformulier
- Per competentie: Uitstekend, Goed, Voldoende, Onvoldoende
- Concrete voorbeelden uit jouw project
- Bewijs mapping (welke docs bewijzen wat?)

### **Workflow:**
1. **Vrijdag:** Check ZELFEVALUATIE-TRACKING → Waar sta ik deze week?
2. **Planning:** Check DELIVERABLES-CHECKLIST → Wat moet ik maken?
3. **Schrijven:** Check BEOORDELINGSCRITERIA → Aan welke criteria moet het voldoen?
4. **Na voltooiing:** Update alle 3 documenten

---

## Oplevering Overzicht

**Opleveren via:** Brightspace
**Format:** .zip bestand met mappenstructuur
**Deadline:** 15 juni 2026
**Wie levert in:** 1 teamlid (in dit geval: Pedro Eduardo Cardoso - solo project)

---

## Deliverables Status

### 1. PROJECTARCHIEF

#### Projectdefinitie (COMPLEET)
**Locatie:** `docs/projectdefinitie/`
```
 01-context-analyse.md
 02-probleemstelling.md
 03-doelstellingen.md
 04-scope.md
 05-stakeholders.md
```
**Status:** Compleet, inclusief authenticiteitsverklaringen
**Ingeleverd:** Via OnStage (execution phase)

---

#### Plan van Aanpak (COMPLEET)
**Locatie:** `docs/plan-van-aanpak/`
```
 01-projectaanpak.md (Agile methodiek)
 02-planning.md (18 weken roadmap)
 03-risicoanalyse.md (risico's + mitigaties)
 04-probleemstelling-vragen.md
 05-randvoorwaarden.md
 06-deliverables.md
```
**Status:** Compleet, inclusief authenticiteitsverklaringen
**Ingeleverd:** Via OnStage (execution phase)

---

#### Onderzoeksrapport (IN PROGRESS)
**Locatie:** `docs/onderzoek/`
**Huidige status:** Folder bestaat, templates klaar, nog GEEN volledig rapport

**Wat er moet komen (Week 3-4):**
```
□ 01-msg3-analyse.md - MSG-3 Excel structuur onderzoek
□ 02-maximo-api.md - Maximo REST API capabilities
□ 03-technologie-keuzes.md - Python/libraries onderbouwing
□ 04-alternatieven-evaluatie.md - Openpyxl vs Pandas, etc.
□ 05-poc-resultaten.md - Proof of Concept bevindingen
□ 00-onderzoeksrapport.md - HOOFDDOCUMENT (samenvatting)
```

**Planning:** Week 3-4 (18 feb - 3 mrt)
**Deadline intern:** 3 maart 2026

---

#### Scrum/Sprint Documentatie (MOET NOG)
**Locatie:** `docs/scrum/` (nieuw aan te maken)

**Wat er moet komen:**
```
□ Sprint planning documenten (per sprint)
□ Sprint review documenten
□ Sprint retrospectives
□ Daily stand-up notities (optioneel)
□ Backlog management (kan TODO.md zijn)
□ Velocity tracking
□ Burndown charts (optioneel)
```

**Planning:** Start Week 3 (Sprint 1), elke 2 weken update
**Deadline intern:** Continue tijdens project

**Alternatief:** We gebruiken Agile ipv pure Scrum - documenteer dit in projectaanpak

---

#### Authenticiteitsverklaring AI Gebruik (COMPLEET!)
**Locatie:** `docs/ai/`
```
 AI-GEBRUIK.md - Volledige AI-documentatie
 AI-AUTHENTICITEITSVERKLARINGEN.md - Quick reference
 MIJN-BIJDRAGE-VS-AI.md - Eigenaarschap bewijs
 AI-GEBRUIK.md - Hoofddocument en presentatiebron AI-gebruik
 Authenticiteitsverklaringen in ALLE deliverables
```
**Status:** 100% compleet, AIAS-compliant
**Te doen:** Alleen updaten tijdens project indien nieuw AI-gebruik

---

### 2. PROJECTRESULTAAT

#### Hoofdproduct: Applicatie (IN PROGRESS)
**Vereiste:** Minimaal 250 regels eigen geschreven code

**Huidige status:**
- Repository structuur
- Code templates
- Business rules (40% gedaan - src/validator/business_rules.py)
- Parser implementatie (0%)
- Mapping implementatie (0%)
- Maximo connector (0%)

**Code regels verwachting:**
```
Parser module: ~300 regels (Pedro)
Validator module: ~400 regels (Pedro)
Mapping engine: ~350 regels (Pedro)
Maximo connector: ~250 regels (Pedro)
Change detection: ~200 regels (Pedro)
Tests: ~500 regels (Pedro)
──────────────────────────────────────
TOTAAL VERWACHT: ~2000 regels (>250 vereist)
```

**Planning:** Week 5-13 (implementatie fases)
**Deadline intern:** 5 mei 2026 (Week 13)

**Code support beschikbaar:**
- Jasper van Polen (Data Analyst)
- Fajjaaz Chandoe (Data Analyst)

---

#### Technische Ontwerpen (IN PROGRESS)
**Locatie:** `docs/technisch-ontwerp/`

**Huidige status:**
```
 01-architectuur-ontwerp.md (basis klaar)
 business-rules.md (80 rules gedocumenteerd)
 UML diagrammen (class, sequence, component, usecase)
□ 02-datamodellen.md - MSG-3 & Maximo data structures
□ 03-api-specificaties.md - Maximo REST API specs
□ 04-class-diagram.md - OOP design uitgebreid
□ 05-sequence-diagrams.md - Flow diagrammen
□ 06-error-handling.md - Error strategie
□ 07-security.md - Security design
□ 08-performance.md - Performance requirements
```

**Planning:** Week 4-5 (ontwerp fase)
**Deadline intern:** 10 maart 2026

---

#### Testcases (PLANNED)
**Locatie:** `docs/testcases/`

**Wat er moet komen:**
```
□ 01-teststrategie.md - Overall test aanpak
□ 02-testplan-parser.md - Parser test cases
□ 03-testplan-validator.md - Validator test cases
□ 04-testplan-mapping.md - Mapping test cases
□ 05-testplan-integration.md - End-to-end scenarios
□ 06-testresultaten.md - Test runs & coverage
```

**Planning:** Week 5-17 (parallel met development)
**Deadline intern:** 2 juni 2026 (Week 17)

---

#### Overdrachtsdocumenten (PLANNED)
**Locatie:** `docs/overdracht/`

**Wat er moet komen:**
```
□ 01-gebruikershandleiding.md - Hoe te gebruiken
□ 02-technische-handleiding.md - Voor developers
□ 03-installatie-instructies.md - Deployment guide
□ 04-troubleshooting.md - Common issues
□ 05-changelog.md - Version history
□ 06-toekomstige-verbeteringen.md - Roadmap
```

**Planning:** Week 16-18 (afronding)
**Deadline intern:** 8 juni 2026

---

#### Demonstratie (PLANNED)
**Format:** Video of live demo tijdens assessment

**Wat te demonstreren:**
```
□ MSG-3 Excel uploaden
□ Validatie proces
□ Change detection tussen versies
□ Mapping naar Maximo objecten
□ Maximo API call
□ Error handling
□ Rapportage
```

**Planning:** Week 17-18
**Deadline:** Assessment dag (juni 2026)

---

### 3. REFLECTIEVERSLAG

#### Reflectieverslag (MOET NOG)
**Locatie:** `docs/reflectie/` (nieuw aan te maken)

**Vereiste:** Individuele reflectie op:
- Projectproces
- Persoonlijke ontwikkeling
- Leerresultaten
- Samenwerking (indien van toepassing)
- Keuzes en professionele groei

**Wat erin moet:**
```
□ Inleiding - Project context
□ Competentieontwikkeling (per HBO-i competentie)
 - Analyseren
 - Adviseren
 - Ontwerpen
 - Realiseren
 - Manage & Control
□ Leerpunten - Wat heb ik geleerd?
□ Uitdagingen - Wat was moeilijk?
□ Successen - Wat ging goed?
□ Professionele groei - Hoe ben ik gegroeid?
□ Toekomst - Wat neem ik mee?
□ AI-gebruik reflectie - Wat leerde ik over AI?
```

**Planning:** Week 17-18 (einde project)
**Deadline:** 12 juni 2026

**Template maken:** Week 16

---

### 4. PRESENTATIE (Optioneel)

#### Criteriumgericht Interview / Presentatie (PLANNED)
**Format:** PowerPoint of Keynote presentatie

**Inhoud:**
```
□ Intro - Wie ben ik, wat is het project?
□ Probleem - Babcock situatie
□ Oplossing - MSG-3 to Maximo converter
□ Aanpak - Agile, sprints, methodiek
□ Resultaten - Demo, cijfers, impact
□ Techniek - Architectuur, design keuzes
□ AI-gebruik - Transparantie, eigenaarschap
□ Leerpunten - Wat heb ik geleerd?
□ Conclusie - Oplevering en reflectie
```

**Planning:** Week 17-18
**Deadline:** Assessment dag

**Materiaal:** Gebruik `docs/ai/AI-GEBRUIK.md` (of AI-WORKFLOW-DAGELIJKS.md) voor AI-slides

---

### 5. EVALUATIEFORMULIEREN

#### Zelfevaluatieformulier (MOET NOG)
**Format:** Windesheim template (waarschijnlijk via Brightspace)

**Wat te doen:**
```
□ Download template van Brightspace
□ Reflecteer per HBO-i domein:
 - User Interaction
 - Software Realisatie
 - Future-Oriented Organisation
 - Investigative Problem Solving
 - Personal Leadership
□ Geef zelfscore (1-5) per competentie
□ Onderbouw met voorbeelden uit project
```

**Planning:** Week 17-18
**Deadline:** 12 juni 2026

**Actie:** Check Brightspace voor template

---

#### Evaluatieformulier Opdrachtgever (MOET NOG) - ZEER BELANGRIJK!
**Van:** Matthijs Meijer & Rick Kramer (Babcock stagebegeleiders)

** KRITIEK:** Zonder ondertekend formulier = GEEN ASSESSMENT = NIET AFSTUDEREN!

**Wat het formulier bevat:**
```
4 Beoordelingscategorieën (checkboxen):
1. Zelfstandigheid (initiatief, lerende houding, aanpak)
2. Gedrag (motivatie, communicatie, inzet, verantwoordelijkheid)
3. Omgaan met onvoorspelbaarheid (flexibiliteit, aanpassing)
4. Professionaliteit (betrouwbaarheid, samenwerking)

3 Open vragen:
1. Waarom is het product geschikt voor jullie?
2. Waarom is de student geschikt voor hbo-werkveld?
3. Overige opmerkingen over opdrachtuitvoering
```

**Wat te doen:**
```
Week 17 (begin juni):
□ Download formulier van Brightspace (Bedrijf - Evaluatieformulier Comakership)
□ Stuur naar Matthijs Meijer EN Rick Kramer met:
 - Brief: "Graag jullie evaluatie voor mijn assessment"
 - Link naar alle deliverables (Projectdefinitie, PvA, Onderzoek, Code)
 - Uitleg wat ze moeten doen (4 checkboxen + 3 open vragen)
 - Deadline: 1 week voor assessment

□ OPTIONEEL: Stuur "Project Samenvatting" email (maakt invullen makkelijker):
 - Wat heb ik opgeleverd?
 - Wat waren de resultaten? (40 uur → <1 uur)
 - Wat waren hoogtepunten? (MSG-3 template verbetering)

Week 18 (voor 12 juni):
□ Follow-up als je nog geen formulier hebt (na 3 dagen)
□ Ontvang ondertekend formulier (PDF scan of origineel)
□ Check: Alle vragen ingevuld? Handtekening aanwezig?
□ Include in oplevering .zip

 Zonder handtekening wordt eindwerk NIET beoordeeld!
```

**Planning:** Week 17 (aanvragen 2 juni), Week 18 (ontvangen vóór 12 juni)
**Deadline:** 12 juni 2026 (dag voor assessment)

**Impact op beoordeling:**
- Adviserend maar ZEER belangrijk
- Positieve feedback → boost je cijfer
- Negatieve feedback → kan cijfer verlagen
- Zie ZELFEVALUATIE-TRACKING.md sectie "Bedrijfsevaluatie" voor target scores (8.5!)

---

## Aanbevolen Mappenstructuur voor Oplevering

```
MSGConverter-Oplevering-PedroCardoso.zip
│
├── 1-Projectarchief/
│ ├── Projectdefinitie/
│ │ ├── 01-context-analyse.pdf
│ │ ├── 02-probleemstelling.pdf
│ │ ├── 03-doelstellingen.pdf
│ │ ├── 04-scope.pdf
│ │ └── 05-stakeholders.pdf
│ │
│ ├── Plan-van-Aanpak/
│ │ ├── 01-projectaanpak.pdf
│ │ ├── 02-planning.pdf
│ │ ├── 03-risicoanalyse.pdf
│ │ ├── 04-probleemstelling-vragen.pdf
│ │ ├── 05-randvoorwaarden.pdf
│ │ └── 06-deliverables.pdf
│ │
│ ├── Onderzoeksrapport/
│ │ ├── 00-onderzoeksrapport.pdf (hoofddocument)
│ │ ├── 01-msg3-analyse.pdf
│ │ ├── 02-maximo-api.pdf
│ │ └── 03-technologie-keuzes.pdf
│ │
│ ├── Sprint-Documentatie/
│ │ ├── Sprint-1-Planning.pdf
│ │ ├── Sprint-1-Review.pdf
│ │ ├── Sprint-1-Retrospective.pdf
│ │ └── [... per sprint ...]
│ │
│ └── AI-Authenticiteitsverklaring/
│ ├── AI-GEBRUIK.pdf (hoofddocument)
│ ├── MIJN-BIJDRAGE-VS-AI.pdf
│ └── (eventueel export van AI-GEBRUIK of AI-WORKFLOW naar PDF)
│
├── 2-Projectresultaat/
│ ├── Applicatie/
│ │ ├── src/ (volledige source code)
│ │ ├── tests/
│ │ ├── examples/
│ │ ├── README.md
│ │ └── requirements.txt
│ │
│ ├── Technisch-Ontwerp/
│ │ ├── 01-architectuur.pdf
│ │ ├── 02-datamodellen.pdf
│ │ ├── business-rules.pdf
│ │ └── UML-diagrammen.pdf
│ │
│ ├── Testcases/
│ │ ├── teststrategie.pdf
│ │ ├── testplannen.pdf
│ │ └── testresultaten.pdf
│ │
│ ├── Overdracht/
│ │ ├── gebruikershandleiding.pdf
│ │ ├── technische-handleiding.pdf
│ │ ├── installatie-instructies.pdf
│ │ └── troubleshooting.pdf
│ │
│ └── Demonstratie/
│ └── demo-video.mp4 (of link naar YouTube)
│
├── 3-Reflectie/
│ └── Reflectieverslag-PedroMeijer.pdf
│
├── 4-Presentatie/
│ └── Presentatie-Assessment.pdf
│
├── 5-Evaluaties/
│ ├── Zelfevaluatie-PedroMeijer.pdf
│ └── Evaluatie-Opdrachtgever-Babcock.pdf
│
└── README.md (Navigatie voor beoordelaars)
```

---

## Ontbrekende Documenten - Actielijst

### Hoge Prioriteit (Moet nog aangemaakt)

#### 1. Sprint/Scrum Documentatie Structuur
**Actie:** Maak `docs/scrum/` folder met templates
**Wanneer:** Start Week 3 (Sprint 1)
**Template:**
```markdown
# Sprint [Nummer] - [Naam]

## Sprint Goal
[Wat willen we deze sprint bereiken?]

## Planning
- Duration: 2 weeks
- Start: [Datum]
- End: [Datum]

## Backlog Items Selected
1. [ ] [User story / taak]
2. [ ] [User story / taak]

## Daily Progress
### Dag 1 - [Datum]
- Done: [Wat is af]
- Blockers: [Problemen]

## Sprint Review
- Demo: [Wat is gedemonstreerd]
- Feedback: [Van stakeholders]

## Sprint Retrospective
- What went well:
- What could be better:
- Action items:
```

---

#### 2. Onderzoeksrapport Hoofddocument
**Actie:** Maak `docs/onderzoek/00-onderzoeksrapport.md`
**Wanneer:** Week 4 (na POC's)
**Template:**
```markdown
# Onderzoeksrapport
## MSG-3 to Maximo Integration

## Executive Summary
[Samenvatting bevindingen]

## Onderzoeksvragen
1. Hoe kan MSG-3 Excel automatisch worden geparset?
2. Welke Maximo API endpoints zijn relevant?
3. Wat is de beste mapping strategie?

## Methodologie
[Hoe heb je onderzocht?]

## Bevindingen
[Per onderzoeksvraag]

## Conclusies
[Antwoorden en keuzes]

## Aanbevelingen
[Voor implementatie]

## Bijlagen
[Verwijzingen naar detail documenten]
```

---

#### 3. Reflectieverslag Template
**Actie:** Maak `docs/reflectie/reflectieverslag.md`
**Wanneer:** Week 16 (template), Week 17-18 (invullen)
**Template:**
```markdown
# Reflectieverslag Comakership
## Pedro Eduardo Cardoso - MSG-3 to Maximo Converter

## Inleiding
[Context project, rol, periode]

## Competentie Ontwikkeling

### Analyseren
[Wat heb ik geanalyseerd, hoe, resultaat, wat leerde ik]

### Adviseren
[Welke adviezen, onderbouwing, impact, wat leerde ik]

### Ontwerpen
[Wat heb ik ontworpen, keuzes, trade-offs, wat leerde ik]

### Realiseren
[Wat heb ik gebouwd, uitdagingen, oplossingen, wat leerde ik]

### Manage & Control
[Hoe heb ik gemanaged, planning, risico's, wat leerde ik]

## Leerpunten
[Top 5 belangrijkste learnings]

## Professionele Groei
[Hoe ben ik gegroeid als professional]

## AI-Gebruik Reflectie
[Wat leerde ik over werken met AI]

## Toekomst
[Wat neem ik mee naar volgende projecten]

## Conclusie
[Terugblik op hele periode]
```

---

## Planning Update - Ontbrekende Items

### Week 3-4 (18 feb - 3 mrt): Onderzoek
```
□ Start Sprint 1 documentatie
□ Schrijf onderzoek documenten
□ Maak POC's
□ Schrijf 00-onderzoeksrapport.md
```

### Week 5-13 (4 mrt - 5 mei): Implementatie
```
□ Sprint documentatie elke 2 weken
□ Code schrijven (2000+ regels)
□ Technisch ontwerp updaten
□ Testcases schrijven
```

### Week 14-15 (6 mei - 19 mei): MSG-3 Redesign
```
□ Nieuwe MSG-3 template
□ Documentatie
□ Sprint docs
```

### Week 16-17 (20 mei - 2 juni): Testing & Docs
```
□ End-to-end testing
□ Testresultaten documenteren
□ Overdrachtsdocumenten schrijven
□ Maak reflectieverslag template
□ Vraag evaluatieformulieren op
```

### Week 18 (3 juni - 15 juni): Afronding
```
□ Reflectieverslag schrijven
□ Zelfevaluatie invullen
□ Evaluatie van opdrachtgever ophalen
□ Presentatie maken
□ Demo video opnemen
□ Alles bundelen in .zip
□ README voor oplevering schrijven
□ Uploaden naar Brightspace
```

---

## Pre-Oplevering Checklist (Week 18)

### Documenten Check
```
□ Alle PDF's gegenereerd uit Markdown
□ Alle authenticiteitsverklaringen aanwezig
□ Alle diagrammen zichtbaar
□ Geen placeholder tekst (<<naam tool>>)
□ Datum/naam consistent
□ Spelling/grammatica check
```

### Code Check
```
□ >250 regels code (target: 2000+)
□ Code werkt en is getest
□ Tests passing (>80% coverage)
□ README up-to-date
□ requirements.txt compleet
□ .env.example aanwezig (geen echte credentials!)
□ Commentaar/docstrings compleet
```

### Mappenstructuur Check
```
□ Logische folder structuur
□ README.md in root van .zip
□ Alle documenten in juiste folders
□ Bestandsnamen consistent
□ Geen overbodige bestanden (.pyc, __pycache__, etc.)
```

### Evaluaties Check
```
□ Zelfevaluatie ingevuld en ondertekend
□ Evaluatie opdrachtgever ontvangen
□ Beide als PDF in zip
```

---

## Acties voor DEZE WEEK

```
1. □ Maak docs/scrum/ folder aan (nu)
2. □ Maak Sprint 1 planning template (Week 3)
3. □ Check Brightspace voor evaluatieformulier templates
4. □ Email Matthijs & Rick voor MSG-3 voorbeelden en Maximo toegang
5. □ Kennismaken met Jasper & Fajjaaz (code support team)
6. □ Bookmark deze checklist
7. □ Voeg toe aan wekelijkse review (vrijdag)
```

---

**Datum:** 11 februari 2026
**Versie:** 1.0
**Eigenaar:** Pedro Eduardo Cardoso
**Laatste check:** Voor oplevering Week 18

---

*Update deze checklist wekelijks tijdens je Friday review!*
