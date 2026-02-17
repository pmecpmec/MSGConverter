# 📋 Product Backlog
## MSG-3 to Maximo Converter Project

**Project:** MSG-3 to Maximo Converter  
**Product Owner:** Matthijs Meijer & Rick Kramer (Babcock)  
**Developer:** Pedro Eduardo Cardoso  
**Laatste update:** 11 februari 2026

---

## 🎯 Product Vision

**Probleem:**
Handmatige invoer van MSG-3 maintenance tasks in IBM Maximo kost 40+ uur per aircraft type en is foutgevoelig (15% foutpercentage).

**Oplossing:**
Geautomatiseerde conversietool die MSG-3 Excel files parseert, valideert en uploadt naar Maximo in <1 uur met <1% foutpercentage.

**Waarde:**
- ⏱️ Tijdsbesparing: 40 uur → <1 uur (97.5% reductie)
- ✅ Kwaliteitsverbetering: 15% fouten → <1% fouten
- 💰 ROI: Tool verdient zich terug in 2 maanden
- 📈 Schaalbaarheid: Bruikbaar voor alle aircraft types

---

## 📊 Backlog Overview

### Sprint Toewijzing

**⚠️ Werkschema:** Pedro werkt **Di/Wo/Do** (3 dagen/week bij Babcock)  
**Sprint lengte:** 2-3 weken (6-9 werkdagen) afhankelijk van scope

| Sprint | Periode | Werkdagen | Focus | Epic | Items |
|--------|---------|-----------|-------|------|-------|
| Sprint 1 | Week 3-5 (18 feb - 6 mrt) | 9 dagen | Research & POC | Epic 1 | 8 items |
| Sprint 2 | Week 6-7 (11 mrt - 20 mrt) | 6 dagen | Excel Parser | Epic 2 | 6 items |
| Sprint 3 | Week 8-9 (25 mrt - 3 apr) | 6 dagen | Business Rules | Epic 2 | 5 items |
| Sprint 4 | Week 10-11 (8 apr - 17 apr) | 6 dagen | Change Detection | Epic 3 | 5 items |
| Sprint 5 | Week 12-13 (22 apr - 1 mei) | 6 dagen | Mapping Engine | Epic 4 | 6 items |
| Sprint 6 | Week 14-15 (6 mei - 15 mei) | 6 dagen | Maximo Connector | Epic 5 | 7 items |
| Sprint 7 | Week 16-17 (20 mei - 29 mei) | 6 dagen | MSG-3 Redesign | Epic 6 | 4 items |
| Sprint 8 | Week 18-19 (3 jun - 12 jun) | 6 dagen | Testing & Polish | Epic 7 | 8 items |

**Totaal:** 49 backlog items | 8 sprints | 57 werkdagen (3 dagen/week)

---

## 🎯 Epics

### Epic 1: Research & Foundation (Sprint 1)
**Doel:** Onderzoek, POC's en technische basis leggen  
**Value:** Onderbouwde keuzes, gevalideerde aanpak  
**Deliverable:** Onderzoeksrapport + POC code

### Epic 2: Excel Parsing & Validation (Sprint 2-3)
**Doel:** MSG-3 Excel kunnen inlezen en valideren  
**Value:** Eerste werkende module, foutdetectie  
**Deliverable:** Parser + Validator modules + tests

### Epic 3: Change Detection (Sprint 4)
**Doel:** Versies kunnen vergelijken en wijzigingen detecteren  
**Value:** Alleen changes uploaden (efficiency)  
**Deliverable:** ChangeDetector module + tests

### Epic 4: Mapping Engine (Sprint 5)
**Doel:** MSG-3 data mappen naar Maximo object structuur  
**Value:** Correcte transformatie naar Maximo formaat  
**Deliverable:** Mapper module + mapping specs

### Epic 5: Maximo Integration (Sprint 6)
**Doel:** Data uploaden naar IBM Maximo via REST API  
**Value:** End-to-end werkende flow  
**Deliverable:** MaximoConnector + API docs

### Epic 6: MSG-3 Template Improvement (Sprint 7)
**Doel:** Babcock MSG-3 template verbeteren  
**Value:** Betere data kwaliteit, minder fouten  
**Deliverable:** Nieuwe template + migration guide

### Epic 7: Testing, Documentation & Handover (Sprint 8)
**Doel:** Production-ready maken en overdragen  
**Value:** Deployment klaar, Babcock kan gebruiken  
**Deliverable:** Overdracht package + training

---

## 📋 Detailed Backlog (Prioriteit volgorde)

### 🔴 SPRINT 1 BACKLOG (Week 3-4: 18 feb - 3 mrt)

#### Epic 1: Research & Foundation

**BAC-001: MSG-3 Structuur Analyse**
- **Prioriteit:** Must Have
- **Story Points:** 8
- **Geschatte tijd:** 8 uur
- **Acceptatiecriteria:**
  - [ ] MSG-3 Excel structuur volledig gedocumenteerd
  - [ ] Alle task types geïdentificeerd (12+)
  - [ ] Interval types gedocumenteerd (FH, FC, Calendar)
  - [ ] ATA Chapter structuur in kaart
  - [ ] Document: `docs/onderzoek/01-msg3-analyse.md`

**BAC-002: Maximo API Research**
- **Prioriteit:** Must Have
- **Story Points:** 8
- **Geschatte tijd:** 8 uur
- **Acceptatiecriteria:**
  - [ ] Maximo REST API endpoints gedocumenteerd
  - [ ] PM, JobPlan, Location object structuren bekend
  - [ ] Authentication mechanisme duidelijk
  - [ ] Rate limiting requirements bekend
  - [ ] Document: `docs/onderzoek/02-maximo-api.md`

**BAC-003: Technology Stack Selection**
- **Prioriteit:** Must Have
- **Story Points:** 5
- **Geschatte tijd:** 6 uur
- **Acceptatiecriteria:**
  - [ ] Python vs C#/Java vergelijking (met criteria)
  - [ ] Openpyxl vs Pandas benchmarks
  - [ ] REST library selection (requests vs httpx)
  - [ ] Testing framework keuze (pytest)
  - [ ] Document: `docs/onderzoek/03-technologie-keuzes.md`

**BAC-004: Alternative Solutions Evaluation**
- **Prioriteit:** Should Have
- **Story Points:** 5
- **Geschatte tijd:** 5 uur
- **Acceptatiecriteria:**
  - [ ] Minimaal 3 alternatieven geëvalueerd
  - [ ] Decision matrix met criteria
  - [ ] Trade-off analysis
  - [ ] Recommendation met onderbouwing
  - [ ] Document: `docs/onderzoek/04-alternatieven-evaluatie.md`

**BAC-005: Proof of Concept - Excel Parsing**
- **Prioriteit:** Must Have
- **Story Points:** 5
- **Geschatte tijd:** 6 uur
- **Acceptatiecriteria:**
  - [ ] POC code: Excel inlezen met openpyxl
  - [ ] Kan task rows parsen
  - [ ] Kan intervals herkennen
  - [ ] Performance gemeten
  - [ ] Code: `poc/excel_parser_poc.py`

**BAC-006: Proof of Concept - Maximo API**
- **Prioriteit:** Must Have
- **Story Points:** 8
- **Geschatte tijd:** 8 uur
- **Acceptatiecriteria:**
  - [ ] POC code: Maximo API call (test environment)
  - [ ] Authentication werkend
  - [ ] PM object kunnen aanmaken (test)
  - [ ] Error handling basis
  - [ ] Code: `poc/maximo_api_poc.py`

**BAC-007: Onderzoeksrapport Hoofddocument**
- **Prioriteit:** Must Have
- **Story Points:** 13
- **Geschatte tijd:** 12 uur
- **Acceptatiecriteria:**
  - [ ] Executive summary
  - [ ] Methodologie beschreven
  - [ ] Alle onderzoeksvragen beantwoord
  - [ ] Conclusies en aanbevelingen
  - [ ] APA bronvermelding (>10 bronnen)
  - [ ] >30 pagina's met diepgang
  - [ ] Document: `docs/onderzoek/00-onderzoeksrapport.md`

**BAC-008: Development Environment Setup**
- **Prioriteit:** Should Have (Excellence!)
- **Story Points:** 5
- **Geschatte tijd:** 4 uur
- **Acceptatiecriteria:**
  - [ ] pytest configuratie (pytest.ini)
  - [ ] Pre-commit hooks (.pre-commit-config.yaml)
  - [ ] CI/CD skeleton (GitHub Actions)
  - [ ] requirements.txt + requirements-dev.txt
  - [ ] .env.example
  - [ ] Docker skeleton (Dockerfile)

**Sprint 1 Totaal:** 57 story points ≈ 57 uur (24 uur/week × 2 weken = 48 uur beschikbaar)  
**Fit:** ⚠️ Tight maar haalbaar (sprint commitment!)

---

### 🟠 SPRINT 2 BACKLOG (Week 5-6: 4-17 mrt)

#### Epic 2: Excel Parsing & Validation

**BAC-009: Excel Parser - Core Functionaliteit**
- **Prioriteit:** Must Have
- **Story Points:** 13
- **Geschatte tijd:** 12 uur
- **Acceptatiecriteria:**
  - [ ] Kan MSG-3 Excel openen (openpyxl)
  - [ ] Detecteert alle relevante sheets
  - [ ] Parse task rows naar dict/dataclass
  - [ ] Detecteert merged cells
  - [ ] Error handling voor corrupt files
  - [ ] Code: `src/parser/excel_parser.py`
  - [ ] Tests: >90% coverage

**BAC-010: Parser - Interval Parsing**
- **Prioriteit:** Must Have
- **Story Points:** 8
- **Geschatte tijd:** 8 uur
- **Acceptatiecriteria:**
  - [ ] Parse Flight Hours (FH) intervals
  - [ ] Parse Flight Cycles (FC) intervals
  - [ ] Parse Calendar intervals
  - [ ] Multi-interval support
  - [ ] Code: `src/parser/interval_parser.py`

**BAC-011: Parser - ATA Chapter Support**
- **Prioriteit:** Must Have
- **Story Points:** 5
- **Geschatte tijd:** 5 uur
- **Acceptatiecriteria:**
  - [ ] Parse ATA chapters
  - [ ] Hierarchie behouden
  - [ ] Cross-referencing support
  - [ ] Code: `src/parser/ata_parser.py`

**BAC-012: Data Model Classes**
- **Prioriteit:** Must Have
- **Story Points:** 8
- **Geschatte tijd:** 8 uur
- **Acceptatiecriteria:**
  - [ ] Pydantic models voor MSG-3 data
  - [ ] Type validation automatisch
  - [ ] JSON schema generatie
  - [ ] Code: `src/models/msg3_models.py`

**BAC-013: Parser Tests Suite**
- **Prioriteit:** Must Have
- **Story Points:** 8
- **Geschatte tijd:** 8 uur
- **Acceptatiecriteria:**
  - [ ] Unit tests per parser module
  - [ ] Edge case tests (corrupt files, missing data)
  - [ ] Parametrized tests (multiple MSG-3 files)
  - [ ] Coverage >95%
  - [ ] Code: `tests/unit/test_parser.py`

**BAC-014: CI/CD Pipeline Active**
- **Prioriteit:** Should Have (Excellence!)
- **Story Points:** 5
- **Geschatte tijd:** 4 uur
- **Acceptatiecriteria:**
  - [ ] GitHub Actions workflow running
  - [ ] Tests run bij elke commit
  - [ ] Coverage report gegenereerd
  - [ ] Linting (black, flake8, mypy)
  - [ ] Badges in README

**Sprint 2 Totaal:** 47 story points ≈ 45 uur

---

### 🟡 SPRINT 3 BACKLOG (Week 7: 18-24 mrt)

#### Epic 2: Business Rules Validation

**BAC-015: Business Rules Engine**
- **Prioriteit:** Must Have
- **Story Points:** 13
- **Geschatte tijd:** 12 uur
- **Acceptatiecriteria:**
  - [ ] 80+ business rules geïmplementeerd
  - [ ] Prioriteit levels (Error, Warning, Info)
  - [ ] Custom error messages
  - [ ] Code: `src/validator/business_rules.py`

**BAC-016: Validation Context System**
- **Prioriteit:** Must Have
- **Story Points:** 8
- **Geschatte tijd:** 8 uur
- **Acceptatiecriteria:**
  - [ ] Context-aware validation
  - [ ] Dependencies tussen rules
  - [ ] Validation report generation
  - [ ] Code: `src/validator/validator.py`

**BAC-017: Validator Tests**
- **Prioriteit:** Must Have
- **Story Points:** 5
- **Geschatte tijd:** 5 uur
- **Acceptatiecriteria:**
  - [ ] Tests per business rule
  - [ ] Edge cases tested
  - [ ] Coverage >95%
  - [ ] Code: `tests/unit/test_validator.py`

**BAC-018: Error Reporting System**
- **Prioriteit:** Should Have
- **Story Points:** 5
- **Geschatte tijd:** 4 uur
- **Acceptatiecriteria:**
  - [ ] User-friendly error messages
  - [ ] Error summary report
  - [ ] Export errors to Excel/CSV
  - [ ] Code: `src/validator/error_reporter.py`

**BAC-019: Performance Benchmarks**
- **Prioriteit:** Could Have (Excellence!)
- **Story Points:** 3
- **Geschatte tijd:** 3 uur
- **Acceptatiecriteria:**
  - [ ] Benchmark parser performance
  - [ ] Benchmark validator performance
  - [ ] Compare met handmatig (40 uur baseline)
  - [ ] Document: `docs/technisch-ontwerp/09-performance-benchmarks.md`

**Sprint 3 Totaal:** 34 story points ≈ 32 uur

---

### 🟢 SPRINT 4-8 BACKLOG (Samenvatting)

**Sprint 4 (Week 8-9): Change Detection** - 30 story points
- BAC-020 t/m BAC-024: Hash-based comparison, field-level diffing, version tracking

**Sprint 5 (Week 10-11): Mapping Engine** - 40 story points
- BAC-025 t/m BAC-030: MSG-3 → Maximo object mapping, field transformations

**Sprint 6 (Week 12-13): Maximo Connector** - 45 story points
- BAC-031 t/m BAC-037: REST API integration, retry logic, authentication

**Sprint 7 (Week 14-15): MSG-3 Template Redesign** - 25 story points
- BAC-038 t/m BAC-041: Template analysis, redesign, implementation, training

**Sprint 8 (Week 16-17): Testing & Handover** - 50 story points
- BAC-042 t/m BAC-049: Integration tests, documentation, Docker, handover package

---

## 📊 Backlog Metrics

**⚠️ Werkschema:** 3 dagen/week (Di/Wo/Do bij Babcock)

**Totaal backlog items:** 49  
**Totaal story points:** ~280  
**Totaal uren (geschat):** ~260 uur  
**Beschikbaar:** 18 weken × 3 dagen × 8 uur = **432 uur** ✅  
**Buffer:** 172 uur (40% reserve) - Zeer ruim!

**Velocity tracking:**
- Sprint 1 (3 weken): 57 story points (9 dagen)
- Gemiddelde sprint (2 weken): ~35 story points (6 dagen)
- Velocity per dag: ~6-7 story points
- Aanpassen na Sprint 1 (actuele velocity meten)

---

## 🎯 Prioritization Criteria

**Must Have:** Zonder dit werkt applicatie niet (minimum viable product)  
**Should Have:** Verhoogt kwaliteit significant (8.0+ target)  
**Could Have:** Excellence items (8.5+ target)  
**Won't Have:** Leuk maar niet nodig voor dit project

### MoSCoW Matrix

| Categorie | Items | Story Points | % van Totaal |
|-----------|-------|--------------|--------------|
| Must Have | 35 | 210 | 75% |
| Should Have | 10 | 50 | 18% |
| Could Have | 4 | 20 | 7% |
| Won't Have | 0 | 0 | 0% |

---

## 🔄 Backlog Refinement

**Wanneer:** Elke vrijdag (week review)  
**Wat:** 
- Nieuwe items toevoegen
- Prioriteiten aanpassen
- Story points her-schatten
- Items splitsen/mergen

**Changelog:**
- 11 feb 2026: Initial backlog created (49 items)
- [Toekomstige updates hier]

---

## 📝 User Stories Format

**Template:**
```markdown
Als [rol]
Wil ik [functionaliteit]
Zodat [waarde/doel]

Acceptatiecriteria:
- [ ] Criterium 1
- [ ] Criterium 2
```

**Voorbeeld:**
```markdown
Als maintenance engineer
Wil ik MSG-3 Excel uploaden en automatisch laten valideren
Zodat ik fouten voorkom voordat data in Maximo komt

Acceptatiecriteria:
- [ ] Excel file upload mogelijk
- [ ] 80+ business rules checken
- [ ] Error report genereren met regel/kolom nummers
- [ ] Alleen valid data doorgeven aan volgende stap
```

---

## ✅ Definition of Ready

**Een backlog item is "ready" als:**
- [ ] Duidelijke user story of taak beschrijving
- [ ] Acceptatiecriteria gedefinieerd
- [ ] Story points geschat
- [ ] Dependencies bekend
- [ ] Prioriteit toegewezen (MoSCoW)
- [ ] Geen blockers

---

## ✅ Definition of Done

**Een backlog item is "done" als:**
- [ ] Code geschreven en werkend
- [ ] Tests geschreven (>90% coverage)
- [ ] Code reviewed (Jasper/Fajjaaz)
- [ ] Documentatie bijgewerkt
- [ ] CI/CD pipeline groen
- [ ] Demo-able
- [ ] Acceptatiecriteria voldaan
- [ ] Stakeholder approved (indien van toepassing)

---

## 🏆 Excellence Items (voor 8.1+ target)

**Must Do Excellence (Impact: Hoog):**
- BAC-008: Development environment setup (CI/CD, pre-commit)
- BAC-014: CI/CD pipeline active
- BAC-019: Performance benchmarks
- BAC-038-041: MSG-3 Template Redesign (signature move!)
- BAC-045: Docker containerization
- BAC-046: Sphinx documentation

**Nice to Have Excellence (Impact: Medium):**
- Code quality metrics (SonarQube)
- Architecture Decision Records (ADR's)
- Video tutorials
- Visual presentation materials

---

**Laatste update:** 11 februari 2026  
**Eigenaar:** Pedro Eduardo Cardoso  
**Status:** Active - Sprint 1 start Week 3

---

*📝 Update deze backlog elke vrijdag tijdens weekly review!*
