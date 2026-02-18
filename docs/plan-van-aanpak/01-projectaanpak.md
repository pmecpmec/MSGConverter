# Projectaanpak

## Gekozen Methodiek

### Agile / Iteratief

Dit project volgt een **iteratieve aanpak** met 2-weekse sprints:

**Waarom Agile?**

- Flexibiliteit voor wijzigende requirements
- Regelmatige feedback van stakeholders
- Snelle iteraties met werkende software
- Geschikt voor één persoon
- Mogelijkheid om te leren en aan te passen tijdens het proces

**Niet Waterfall omdat:**

- Requirements niet 100% duidelijk aan start
- Technische onzekerheden (Maximo API, Excel parsing)
- Voorkeur voor vroege feedback
- MSG-3 structuur kan tijdens project wijzigen
- Flexibiliteit nodig voor onvoorziene uitdagingen

---

## Sprint Structuur

### Sprint Duur: 2 weken

### Sprint Activiteiten:

1. **Sprint Planning** (dag 1)
   - Selecteer taken voor deze sprint
   - Definieer sprint goal
   - Schat effort per taak
   - Identificeer blockers

2. **Development** (dag 1-9)
   - Implementatie
   - Testing (TDD waar mogelijk)
   - Documentatie (inline)
   - Code review (via Cursor AI + Pedro)

3. **Sprint Review** (dag 10)
   - Demo aan Babcock stakeholders
   - Verzamel feedback
   - Toon werkende software
   - Bespreek voortgang

4. **Sprint Retrospective** (dag 10)
   - Wat ging goed?
   - Wat kan beter?
   - Acties voor volgende sprint
   - Persoonlijke reflectie

---

## Development Workflow

### 1. Analyse & Design

- Requirements gathering van stakeholders
- Technical design documentatie
- UML diagrammen waar nodig
- Documentatie in Markdown

### 2. Implementatie

- Code schrijven met Cursor AI assistentie
- Tests schrijven (TDD waar mogelijk)
- Unit tests per component
- Code review via AI feedback

### 3. Testing

- Unit tests (pytest)
- Integration tests met Maximo test environment
- Manual testing van edge cases
- Performance testing waar relevant

### 4. Documentatie

- Code documentatie (docstrings, type hints)
- Technical docs (architectuur, design decisions)
- User documentation (gebruikershandleiding)
- README en QUICKSTART updates

### 5. Review & Feedback

- Demo aan stakeholders (wekelijks of per sprint)
- Verwerk feedback in backlog
- Prioriteer aanpassingen
- Plan iteraties

---

## Samenwerking met AI

### Cursor AI als Pair Programming Partner

Dit project maakt intensief gebruik van AI-assistentie, conform de **AI Assessment Scale (AIAS)** van Windesheim.

**Voordelen:**

- Snellere code ontwikkeling
- Direct feedback op code kwaliteit
- Hulp bij debugging en troubleshooting
- Kennisoverdracht tijdens development
- 24/7 beschikbaar voor vragen

**Werkwijze:**

1. Planning maken met AI hulp
2. Code implementatie met AI suggesties
3. Review van AI-gegenereerde code
4. Testing en validatie door mens
5. Documentatie met AI ondersteuning

**Verantwoordelijkheid:**

- Alle code wordt kritisch gereviewed
- Tests valideren correctheid
- Eindverantwoordelijkheid ligt bij developer (Pedro)
- AI is tool, geen vervanging van eigen denken

**AIAS Niveaus toegepast:**

- **Niveau 2 (AI Exploratie)**: Brainstorming, planning, structuur bepalen
- **Niveau 3 (AI Samenwerking)**: Code development, testing, refinement
- **Niveau 4 (Volledig AI)**: Documentatie generatie uit code

**Volledige documentatie:** Zie `/docs/AI-GEBRUIK.md` voor gedetailleerde verantwoording van AI-gebruik per projectfase.

---

## Tools & Platforms

### Development

- **IDE**: Cursor (VS Code met AI)
- **Language**: Python 3.11+
- **Version Control**: Git
- **Repository**: GitHub/GitLab

### Testing

- **Framework**: pytest
- **Coverage**: pytest-cov
- **Test Environment**: Maximo test instance

### Documentation

- **Format**: Markdown
- **Diagrams**: PlantUML / draw.io
- **Code Docs**: Docstrings (Google style)

### Project Management

- **Planning**: TODO.md + Sprint board
- **Tracking**: Git commits en branches
- **Communication**: Teams/Email met stakeholders

### Python Libraries

- **Excel Parsing**: openpyxl, pandas
- **API Calls**: requests
- **Validation**: pydantic
- **Logging**: logging (standard library)

---

## Kwaliteitsborging

### Code Kwaliteit

- **PEP 8** compliance (Python style guide)
- **Type hints** waar mogelijk
- **SOLID principles** in design
- **DRY** (Don't Repeat Yourself)
- **Clean Code** principes

### Testing Strategy

- **Unit tests**: Minimaal 80% coverage
- **Integration tests**: End-to-end scenarios
- **Test data**: Voorbeeld MSG-3 bestanden
- **Regression tests**: Bij bug fixes

### Code Review

- **Self-review**: Kritisch eigen code bekijken
- **AI review**: Cursor AI feedback
- **Stakeholder review**: Demo's en feedback
- **Continuous**: Bij elke commit

---

## Risk Management Approach

### Proactieve Aanpak

- Identificeer risico's vroeg in het proces
- Wekelijkse evaluatie van risico's
- Mitigatie strategieën voorbereiden
- Escalatie bij majeure blockers

### Communicatie

- **Wekelijks**: Stand-up met begeleider
- **Per Sprint**: Demo en retrospective
- **Ad-hoc**: Bij problemen of vragen
- **Transparant**: Open over uitdagingen

---

## Iteratie en Feedback

### Feedback Loops

1. **Dagelijks**: Eigen reflectie op voortgang
2. **Wekelijks**: Check-in met begeleider
3. **Per Sprint**: Review met stakeholders
4. **Per Fase**: Evaluatie van milestone

### Aanpassing

- Backlog wordt aangepast op basis van feedback
- Prioriteiten kunnen verschuiven
- Scope kan worden aangepast in overleg
- Learning moments worden gedocumenteerd

---

## Lean Principes

### Focus op Value

- Wat levert waarde voor Babcock?
- Vermijd over-engineering
- MVP (Minimum Viable Product) eerst
- Iteratief uitbreiden

### Waste Reduction

- Automatiseer repetitieve taken
- Hergebruik code waar mogelijk
- Efficiënte communicatie
- Focus op essentials

---

## Comakership Leerproces

### Competentie Ontwikkeling

- **Technisch**: Python, API's, Testing
- **Professioneel**: Communicatie, Planning, Documentatie
- **Persoonlijk**: Zelfstandigheid, Probleemoplossing

### Reflectie

- Continue reflectie tijdens project
- Documentatie van learnings
- Portfolio updates
- Eindreflectie document

### Begeleiding

- **Matthijs Meijer** (Bedrijfsbegeleider): Wekelijkse meetings
- **Schoolbegeleider**: Periodieke evaluaties
- **Stakeholders**: Feedback op deliverables

---

## Definitie van "Done"

Een taak/feature is "Done" als:

- [ ] Code is geschreven en getest
- [ ] Unit tests zijn geschreven (80%+ coverage)
- [ ] Integration tests zijn succesvol
- [ ] Code is gereviewed
- [ ] Documentatie is bijgewerkt
- [ ] Demo aan stakeholder is gegeven
- [ ] Feedback is verwerkt
- [ ] Code is gecommit naar repository

---

_Datum: 4 februari 2026_  
_Auteur: Pedro Eduardo Cardoso_  
_Opleiding: Associate Degree Software Developer (ADSD)_  
_Project: MSG-3 to Maximo Converter_

---

## AI Authenticiteitsverklaring

Tijdens de voorbereiding van het Plan van Aanpak heb ik **Cursor AI** gebruikt om te **verkennen van Agile methodieken, planning frameworks, en risicoanalyse templates**. Ik verklaar dat het ingeleverde werk geen AI-gegenereerde inhoud bevat. De daadwerkelijke planning, risico's en mitigatie strategieën zijn gebaseerd op mijn eigen analyse van het project en in overleg met de begeleider. Ik draag de volledige verantwoordelijkheid voor de inhoud van dit werk.

*AIAS Niveau: 2 - AI Exploratie*
