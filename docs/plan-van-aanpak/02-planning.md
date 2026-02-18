# Planning

## Project Periode
**Start:** 4 februari 2026  
**Eind:** 15 juni 2026  
**Duur:** ~18 weken (circa 4.5 maanden)

**Status (18 feb 2026):** Project bevindt zich in de execution phase (OnStage); Projectdefinitie en PvA zijn ingeleverd.

---

## Fasen

### Phase 0: Opstarten (Week 1-2)
**Datum:** 4 feb - 17 feb 2026

**Activiteiten:**
- [x] Repository setup
- [x] Projectdefinitie schrijven
- [x] Plan van Aanpak maken
- [ ] Development environment setup
- [ ] Toegang Maximo test environment regelen
- [ ] Voorbeeld MSG-3 bestanden verzamelen
- [ ] Kennismaking met stakeholders

**Deliverables:**
- ✅ Projectdefinitie (compleet)
- ✅ Plan van Aanpak (compleet)
- ✅ Git repository met structuur
- Development environment gedocumenteerd
- Toegang tot Maximo test environment

**Milestone:** ✓ Project geïnitialiseerd en klaar voor development

---

### Phase 1: Onderzoek (Week 3-4)
**Datum:** 18 feb - 3 mrt 2026

**Sprint 1: Research & POC**

**Activiteiten:**
- [ ] MSG-3 Excel structuur analyse
- [ ] Maximo API onderzoek en documentatie
- [ ] Technologie selectie en argumentatie
- [ ] Proof of Concept: Excel parsing (openpyxl vs pandas)
- [ ] Proof of Concept: Maximo API calls
- [ ] Data mapping analyse (MSG-3 → Maximo)

**Deliverables:**
- Onderzoek document: MSG-3 Excel analyse
- Onderzoek document: Maximo API capabilities
- POC code: Excel parsing
- POC code: Maximo API connection
- Technisch ontwerp (draft versie)

**Milestone:** ✓ Technische haalbaarheid aangetoond

---

### Phase 2: Parser & Validator (Week 5-7)
**Datum:** 4 mrt - 24 mrt 2026

**Sprint 2 (week 5-6): Excel Parser**
- [ ] Excel parsing implementeren (sheets, tabs, cells)
- [ ] JSON schema definitie voor MSG-3 data
- [ ] Basic validator (structuur, verplichte velden)
- [ ] Error handling en reporting
- [ ] Unit tests voor parser

**Sprint 3 (week 7): Business Rules**
- [ ] Business rules validator implementeren
- [ ] Data quality checks
- [ ] Validatie rapportage
- [ ] Integration tests
- [ ] Documentatie

**Deliverables:**
- Werkende MSG-3 parser module
- Validator met business rules
- Unit tests (80%+ coverage)
- Parser documentatie
- Voorbeeld validatie rapporten

**Milestone:** ✓ MSG-3 Excel kan worden ingelezen en gevalideerd

---

### Phase 3: Change Detection (Week 8-9)
**Datum:** 25 mrt - 7 apr 2026

**Sprint 4: Diff Engine**

**Activiteiten:**
- [ ] Versie vergelijking logica (old vs new MSG-3)
- [ ] Change detection algoritme (added/modified/deleted)
- [ ] Field-level diff voor modified tasks
- [ ] Changelog generatie (human-readable)
- [ ] Delta rapportage (wat moet naar Maximo?)
- [ ] Tests met verschillende scenario's

**Deliverables:**
- Change detection module
- Diff engine met algoritme
- Change report generator
- Unit en integration tests
- Documentatie met voorbeelden

**Milestone:** ✓ Wijzigingen tussen MSG-3 versies kunnen worden gedetecteerd

---

### Phase 4: Mapping Engine (Week 10-11)
**Datum:** 8 apr - 21 apr 2026

**Sprint 5 (week 10): Field Mapping**
- [ ] Field mapping configuratie (MSG-3 → Maximo)
- [ ] PM (Preventive Maintenance) mapper implementatie
- [ ] JobPlan mapper implementatie
- [ ] Relaties tussen PM en JobPlan

**Sprint 6 (week 11): Transformaties**
- [ ] Transformatie regels (data conversies)
- [ ] Mapping validatie
- [ ] Edge cases handling
- [ ] Unit tests voor mappers
- [ ] Integration tests

**Deliverables:**
- Mapping engine module
- PM mapper component
- JobPlan mapper component
- Mapping configuratie documentatie
- Tests met voorbeeld data

**Milestone:** ✓ MSG-3 data kan naar Maximo formaat gemapped worden

---

### Phase 5: Maximo Connector (Week 12-13)
**Datum:** 22 apr - 5 mei 2026

**Sprint 7: REST API Integratie**

**Activiteiten:**
- [ ] REST API client implementeren
- [ ] Authentication (API key / OAuth)
- [ ] CRUD operaties (Create, Read, Update)
- [ ] Batch processing voor meerdere records
- [ ] Error handling & retry logica
- [ ] Rate limiting en throttling
- [ ] Integration tests met test environment
- [ ] Logging en monitoring

**Deliverables:**
- Maximo REST client module
- CRUD operaties voor PM objecten
- CRUD operaties voor JobPlan objecten
- Integration tests met Maximo
- API documentatie

**Milestone:** ✓ Data kan naar Maximo test environment gestuurd worden

---

### Phase 6: MSG-3 Redesign (Week 14-15)
**Datum:** 6 mei - 19 mei 2026

**Sprint 8: Excel Template Redesign**

**Activiteiten:**
- [ ] Analyse huidige Excel structuur (pijnpunten)
- [ ] Ontwerp nieuwe template (machine-readable)
- [ ] Implementeer nieuwe template met voorbeelden
- [ ] Update parser voor nieuwe format
- [ ] Validatie in Excel (dropdown, formulas)
- [ ] Testing met beide formaten
- [ ] Gebruikershandleiding voor template
- [ ] Review met stakeholders

**Deliverables:**
- Herontworpen MSG-3 Excel template
- Template specificatie document
- Parser update voor nieuwe format
- Voorbeeld data in nieuwe template
- Gebruikershandleiding
- Migratie handleiding

**Milestone:** ✓ Nieuwe MSG-3 template klaar en goedgekeurd

---

### Phase 7: Testing & Refinement (Week 16-17)
**Datum:** 20 mei - 2 juni 2026

**Sprint 9: Integration & Testing**

**Activiteiten:**
- [ ] End-to-end testing (volledige pipeline)
- [ ] Performance testing en optimalisatie
- [ ] Edge cases en error scenarios
- [ ] Security review (credentials, API keys)
- [ ] Bug fixes en refinements
- [ ] Code cleanup en refactoring
- [ ] Documentation review en updates
- [ ] User acceptance testing met stakeholders

**Deliverables:**
- Test rapportage (end-to-end)
- Performance benchmarks
- Bug fixes en patches
- Finalized en geoptimaliseerde code
- Bijgewerkte documentatie

**Milestone:** ✓ Systeem production-ready en volledig getest

---

### Phase 8: Afronding & Overdracht (Week 18)
**Datum:** 3 juni - 15 juni 2026

**Sprint 10: Finalisatie**

**Activiteiten:**
- [ ] Gebruikershandleiding schrijven
- [ ] Technische handleiding (maintenance)
- [ ] Installation guide en deployment
- [ ] Troubleshooting guide
- [ ] Overdracht documentatie
- [ ] Kennisoverdracht sessies met team
- [ ] Presentatie voorbereiden (demo + resultaten)
- [ ] Reflectie schrijven (comakership)
- [ ] Portfolio bijwerken

**Deliverables:**
- Volledige gebruikersdocumentatie
- Technische documentatie (architecture, API)
- Installation en deployment guide
- Presentatie (slides + demo)
- Reflectie document (comakership)
- Eindrapport project

**Milestone:** ✓ Project succesvol opgeleverd en overgedragen

---

## Gantt Chart

```
Phase 0: Opstarten       [██░░░░░░░░░░░░░░░░] Week 1-2
Phase 1: Onderzoek       [░░██░░░░░░░░░░░░░░] Week 3-4
Phase 2: Parser          [░░░░███░░░░░░░░░░░] Week 5-7
Phase 3: Change Detect   [░░░░░░░██░░░░░░░░░] Week 8-9
Phase 4: Mapping         [░░░░░░░░░██░░░░░░░] Week 10-11
Phase 5: Maximo Conn     [░░░░░░░░░░░██░░░░░] Week 12-13
Phase 6: Redesign        [░░░░░░░░░░░░░██░░░] Week 14-15
Phase 7: Testing         [░░░░░░░░░░░░░░░██░] Week 16-17
Phase 8: Afronding       [░░░░░░░░░░░░░░░░░█] Week 18
```

---

## Sprint Overzicht

| Sprint | Weken | Focus | Deliverable |
|--------|-------|-------|-------------|
| 1 | 3-4 | Onderzoek & POC | Haalbaarheid aangetoond |
| 2 | 5-6 | Excel Parser | Werkende parser |
| 3 | 7 | Validator | Business rules validatie |
| 4 | 8-9 | Change Detection | Diff engine |
| 5 | 10 | Mapping | PM/JobPlan mappers |
| 6 | 11 | Transformaties | Mapping compleet |
| 7 | 12-13 | Maximo API | REST integratie |
| 8 | 14-15 | Excel Redesign | Nieuwe template |
| 9 | 16-17 | Testing | Production ready |
| 10 | 18 | Afronding | Oplevering |

---

## Critical Path

Deze componenten zijn **kritisch** voor het project succes:

1. **Parser** (Week 5-7)
   - Alles hangt af van correcte parsing
   - Blokkert alle downstream functionaliteit
   - Hoogste prioriteit

2. **Maximo Connector** (Week 12-13)
   - Core functionaliteit van het systeem
   - Zonder dit is er geen automatisering
   - Kritisch voor ROI

3. **Mapping Engine** (Week 10-11)
   - Verbindt parser en connector
   - Bepaalt data kwaliteit in Maximo
   - Essentieel voor correctheid

---

## Buffers & Contingency

### Time Buffers
- **Week 17**: Extra tijd voor onvoorziene issues
- **Elk weekend**: Beschikbaar indien nodig voor achterstand
- **Phase 7**: Volledige fase is buffer voor refinement

### Flexibility Points
- **Excel Redesign** (Phase 6) kan worden ingekort of uitgesteld
- **Advanced features** kunnen naar toekomst worden geschoven
- **Documentation** kan parallel aan development

### Risk Mitigation
- Start met hoogste prioriteit items (parser, connector)
- Early prototyping in Phase 1 vermindert risico's
- Regular stakeholder feedback voorkomt verkeerde richting

---

## Weekly Time Investment

**Target:** 32-40 uur/week (fulltime stage)

### Breakdown per Week:
- **Development & Coding**: 20-24 uur (60%)
- **Documentation**: 6-8 uur (20%)
- **Meetings & Communication**: 4 uur (10%)
- **Learning & Research**: 4 uur (10%)

### Daily Schedule (indicatief):
- **09:00 - 12:00**: Development (focus time)
- **12:00 - 13:00**: Pauze
- **13:00 - 16:00**: Development of testing
- **16:00 - 17:00**: Documentation, meetings, administratie

---

## Milestones & Review Moments

| Week | Milestone | Review Type |
|------|-----------|-------------|
| 2 | Project setup compleet | Internal |
| 4 | Haalbaarheid aangetoond | Stakeholder demo |
| 7 | Parser & validator werken | Stakeholder demo |
| 9 | Change detection werkt | Internal review |
| 11 | Mapping compleet | Stakeholder demo |
| 13 | Maximo integratie werkt | Stakeholder demo |
| 15 | Nieuwe template goedgekeurd | Stakeholder review |
| 17 | Systeem production-ready | Final review |
| 18 | Project opgeleverd | Oplevering & presentatie |

---

## Dependencies & Blockers

### Kritische Dependencies:
- **Maximo test environment toegang** (Week 1-2)
- **MSG-3 voorbeeld bestanden** (Week 1)
- **Maximo API documentatie** (Week 3)
- **Stakeholder beschikbaarheid** (doorlopend)

### Potentiële Blockers:
- Vertraging in Maximo toegang → Escaleren naar IT
- Onvolledige MSG-3 data → Contact met stakeholders
- Maximo API beperkingen → Alternatieve aanpak zoeken
- Concentratieproblemen → Pauzes en planning aanpassen

---

## Communicatie Plan

### Wekelijks:
- **Maandag**: Planning voor de week
- **Woensdag**: Stand-up met begeleider (30 min)
- **Vrijdag**: Reflectie en voorbereiding volgende week

### Per Sprint (2 weken):
- **Sprint Planning**: Selectie taken (1 uur)
- **Sprint Review**: Demo aan stakeholders (1 uur)
- **Sprint Retrospective**: Evaluatie en learnings (30 min)

### Ad-hoc:
- Bij blockers of kritieke issues
- Bij belangrijke design beslissingen
- Bij scope wijzigingen

---

*Datum: 4 februari 2026*  
*Auteur: Pedro Eduardo Cardoso*  
*Project: MSG-3 to Maximo Converter*

---

## AI Authenticiteitsverklaring

Tijdens de voorbereiding van het Plan van Aanpak heb ik **Cursor AI** gebruikt om te **verkennen van Agile methodieken, planning frameworks, en risicoanalyse templates**. Ik verklaar dat het ingeleverde werk geen AI-gegenereerde inhoud bevat. De daadwerkelijke planning, risico's en mitigatie strategieën zijn gebaseerd op mijn eigen analyse van het project en in overleg met de begeleider. Ik draag de volledige verantwoordelijkheid voor de inhoud van dit werk.

*AIAS Niveau: 2 - AI Exploratie*
