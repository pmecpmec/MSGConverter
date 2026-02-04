# 🗓️ START HIER - Plan van Aanpak

**Dit document helpt je bij het maken van je Plan van Aanpak (PvA).**

Het PvA beschrijft **HOE** je het project gaat aanpakken.

---

## 📝 Wat moet er in het Plan van Aanpak?

Het PvA geeft antwoord op:
- **Hoe** ga je het project uitvoeren? (Methodiek)
Ik ga op mijn laptop aan het werk samen met AI, ik beantwoord alle vragen en check of de code goed werkt. Aan de hand van AI kan ik goed samenwerken omdat ik een goed plan voor mezelf kan maken en dan goed aan het werk kan gaan
- **Wanneer** Ik doe het aan de hand van de planning die de AI voor me maakt, (als er een planning ergens is geef de file door zo niet maak ff een planning aan)
- **Wat kan er misgaan?** Fouten binnen de code, concentratie problemen en netwerk problemen meer problemen kan ik nu nog niet inzien
- **Wat heb je nodig?** Permissies vanuit babcock, permissies vanuit schiphol, internet connectie, een laptop, en concenctratie
- **Wat lever je op?** Een werkende tussenkoppeling

---

## 📋 Documenten om te Maken

### 1. Projectaanpak (`01-projectaanpak.md`)

**Doel:** Beschrijf welke methodiek je gebruikt en waarom.

**Template:**
```markdown
# Projectaanpak

## Gekozen Methodiek

### Agile / Iteratief
Dit project volgt een **iteratieve aanpak** met 2-weekse sprints:

**Waarom Agile?**
- Flexibiliteit voor wijzigende requirements
- Regelmatige feedback van stakeholders
- Snelle iteraties met werkende software
- Geschikt voor één persoon

**Niet Waterfall omdat:**
- Requirements niet 100% duidelijk aan start
- Technische onzekerheden (Maximo API, Excel parsing)
- Voorkeur voor vroege feedback

## Sprint Structuur

### Sprint Duur: 2 weken

### Sprint Activiteiten:
1. **Sprint Planning** (dag 1)
   - Selecteer taken voor deze sprint
   - Definieer sprint goal

2. **Development** (dag 1-9)
   - Implementatie
   - Testing
   - Documentatie

3. **Sprint Review** (dag 10)
   - Demo aan Babcock
   - Verzamel feedback

4. **Sprint Retrospective** (dag 10)
   - Wat ging goed?
   - Wat kan beter?
   - Acties voor volgende sprint

## Development Workflow

1. **Analyse & Design**
   - Requirements gathering
   - Technical design
   - Documentatie

2. **Implementatie**
   - Code schrijven
   - Tests schrijven (TDD waar mogelijk)
   - Code review (via Cursor AI)

3. **Testing**
   - Unit tests
   - Integration tests
   - Manual testing

4. **Documentatie**
   - Code documentatie (docstrings)
   - Technical docs
   - User documentation

5. **Review & Feedback**
   - Demo aan stakeholders
   - Verwerk feedback

## Tools & Platforms

- **IDE**: Cursor (VS Code met AI)
- **Version Control**: Git
- **Repository**: GitHub/GitLab
- **Testing**: pytest
- **Documentation**: Markdown
- **Planning**: TODO.md + Sprint board
```

---

### 2. Planning (`02-planning.md`)

**Doel:** (Cursor kan dat het beste voor mij doen)

**Template:**
```markdown
# Planning

## Project Periode
**Start:** 4 februari 2026  
**Eind:** 15 juni 2026  
**Duur:** ~18 weken

## Fasen

### Phase 0: Opstarten (Week 1-2)
**Datum:** 4 feb - 17 feb

**Activiteiten:**
- [x] Repository setup
- [x] Projectdefinitie schrijven
- [x] Plan van Aanpak maken
- [ ] Development environment setup
- [ ] Toegang Maximo test environment regelen

**Deliverables:**
- Projectdefinitie
- Plan van Aanpak
- Git repository met structuur

---

### Phase 1: Onderzoek (Week 3-4)
**Datum:** 18 feb - 3 mrt

**Activiteiten:**
- [ ] MSG-3 Excel analyse
- [ ] Maximo API onderzoek
- [ ] Technologie selectie
- [ ] Proof of Concept (Excel parsing)
- [ ] Proof of Concept (Maximo API)

**Deliverables:**
- Onderzoek documenten
- POC code
- Technisch ontwerp (draft)

**Milestone:** ✓ Technische haalbaarheid aangetoond

---

### Phase 2: Parser & Validator (Week 5-7)
**Datum:** 4 mrt - 24 mrt

**Sprint 1 (week 5-6):**
- [ ] Excel parsing implementeren
- [ ] JSON schema definitie
- [ ] Basic validator

**Sprint 2 (week 7):**
- [ ] Business rules validator
- [ ] Error handling & reporting
- [ ] Unit tests

**Deliverables:**
- Werkende parser
- Validator met tests
- Documentatie

**Milestone:** ✓ MSG-3 Excel kan worden ingelezen en gevalideerd

---

### Phase 3: Change Detection (Week 8-9)
**Datum:** 25 mrt - 7 apr

**Activiteiten:**
- [ ] Versie vergelijking logica
- [ ] Change detection algoritme
- [ ] Changelog generatie
- [ ] Delta rapportage

**Deliverables:**
- Change detection module
- Tests
- Documentatie

**Milestone:** ✓ Wijzigingen kunnen worden gedetecteerd

---

### Phase 4: Mapping Engine (Week 10-11)
**Datum:** 8 apr - 21 apr

**Sprint 3 (week 10):**
- [ ] Field mapping configuratie
- [ ] PM mapper implementatie
- [ ] JobPlan mapper implementatie

**Sprint 4 (week 11):**
- [ ] Transformatie regels
- [ ] Mapping validatie
- [ ] Tests

**Deliverables:**
- Mapping engine
- Mapping documentatie
- Tests

**Milestone:** ✓ MSG-3 data kan naar Maximo formaat gemapped worden

---

### Phase 5: Maximo Connector (Week 12-13)
**Datum:** 22 apr - 5 mei

**Sprint 5:**
- [ ] REST API client
- [ ] Authentication
- [ ] CRUD operaties
- [ ] Error handling & retry logica
- [ ] Integration tests

**Deliverables:**
- Maximo connector
- Integration tests
- API documentatie

**Milestone:** ✓ Data kan naar Maximo gestuurd worden

---

### Phase 6: MSG-3 Redesign (Week 14-15)
**Datum:** 6 mei - 19 mei

**Sprint 6:**
- [ ] Analyse huidige Excel structuur
- [ ] Ontwerp nieuwe template
- [ ] Implementeer nieuwe template
- [ ] Update parser voor redesign
- [ ] Validatie en testing

**Deliverables:**
- Herontworpen MSG-3 template
- Parser update
- Migratie handleiding

**Milestone:** ✓ Nieuwe MSG-3 template klaar

---

### Phase 7: Testing & Refinement (Week 16-17)
**Datum:** 20 mei - 2 juni

**Activiteiten:**
- [ ] End-to-end testing
- [ ] Performance testing
- [ ] Bug fixes
- [ ] Code cleanup
- [ ] Documentation review

**Deliverables:**
- Test rapportage
- Bug fixes
- Finalized code

**Milestone:** ✓ Systeem production-ready

---

### Phase 8: Afronding (Week 18)
**Datum:** 3 juni - 15 juni

**Activiteiten:**
- [ ] Gebruikershandleiding
- [ ] Technische handleiding
- [ ] Overdracht documentatie
- [ ] Presentatie voorbereiden
- [ ] Reflectie schrijven

**Deliverables:**
- Volledige documentatie
- Presentatie
- Reflectie

**Milestone:** ✓ Project opgeleverd

---

## Gantt Chart

\`\`\`
Phase 0: Opstarten       [██] Week 1-2
Phase 1: Onderzoek       [  ██] Week 3-4
Phase 2: Parser          [    ███] Week 5-7
Phase 3: Change Detect   [       ██] Week 8-9
Phase 4: Mapping         [         ██] Week 10-11
Phase 5: Maximo Conn     [           ██] Week 12-13
Phase 6: Redesign        [             ██] Week 14-15
Phase 7: Testing         [               ██] Week 16-17
Phase 8: Afronding       [                 █] Week 18
\`\`\`

## Critical Path
1. Parser (critical - alles hangt hiervan af)
2. Maximo Connector (critical - core functionaliteit)
3. Mapping Engine (critical - verbindt parser en connector)

## Buffers
- Week 17: Extra tijd voor onvoorziene issues
- Elk weekend: Extra tijd indien nodig

## Weekly Time Investment
- **Target:** 32-40 uur/week (fulltime stage)
- **Breakdown:**
  - Development: 24 uur
  - Documentation: 6 uur
  - Meetings: 4 uur
  - Learning: 4 uur
```

---

### 3. Risicoanalyse (`03-risicoanalyse.md`)

**Doel:** Identificeer risico's en bedenk mitigatie strategieën.
Bedenken welke talen het beste werken ipv meteen aan het werk gaan met coderen, vergelijken wat de plus en minpunten zijn aan bepaalde dingen en of het uberhaupt wel samenwerkt met maximo (hiervoor ga ik nog een meeting inplannen)

**Template:**

Key risico's om te overwegen:
- Technische risico's (API changes, Excel parsing complexity)
- Planning risico's (scope creep, onderschatting)
- Resource risico's (toegang Maximo, data availability)
- Kwaliteit risico's (test coverage, documentation)

---

### 4. Randvoorwaarden (`04-randvoorwaarden.md`)

**Doel:** Wat heb je nodig om te slagen?

---

### 5. Deliverables (`05-deliverables.md`)

**Doel:** Overzicht van alle op te leveren producten.

---

## ✅ Checklist

- [ ] Projectaanpak gedefinieerd
- [ ] Gedetailleerde planning met milestones
- [ ] Risico's geïdentificeerd met mitigatie
- [ ] Randvoorwaarden gedocumenteerd
- [ ] Deliverables lijst gemaakt
- [ ] Planning besproken met begeleider
- [ ] Feedback verwerkt

---

**Veel succes met je planning! 📅**
