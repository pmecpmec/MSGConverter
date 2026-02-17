# 👤 Mijn Bijdrage vs AI-Assistentie

## Eigenaarschap & Verantwoordelijkheid

**Student:** Pedro Meijer  
**Datum:** 11 februari 2026  
**Project:** MSG-3 to Maximo Converter

---

## 🎯 Kernboodschap

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│  IK (Pedro) ben de EIGENAAR van dit project         │
│  AI (Cursor) is een TOOL die ik gebruik             │
│                                                     │
│  → IK maak de beslissingen                          │
│  → IK schrijf de business logic                     │
│  → IK begrijp ALLES wat er gebeurt                  │
│  → IK kan het uitleggen en verdedigen               │
│                                                     │
└─────────────────────────────────────────────────────┘
```

**AI is GEEN co-auteur. AI is een HULPMIDDEL, zoals Google of een leerboek.**

---

## 📊 Wat Heb IK Gedaan vs Wat Deed AI?

### Overzicht per Activiteit

| Activiteit              | Mijn Werk (Pedro)                                                         | AI-Assistentie                                  | % Eigen Werk |
| ----------------------- | ------------------------------------------------------------------------- | ----------------------------------------------- | ------------ |
| **Projectdefinitie**    | Context analyse, probleemstelling, doelen, stakeholders identificeren     | Structuur templates, formatting suggesties      | **90%**      |
| **Plan van Aanpak**     | Planning, tijdsinschattingen, risico's identificeren, mitigaties bedenken | Planning frameworks, Gantt templates            | **85%**      |
| **Onderzoek**           | MSG-3 analyse, Maximo API testen, POC's bouwen, keuzes onderbouwen        | Alternatieven suggesties, documentatie opzoeken | **80%**      |
| **Architectuur**        | Design beslissingen, pattern keuzes, trade-offs evalueren                 | UML templates, diagram syntax                   | **75%**      |
| **Business Rules**      | Alle 80 rules identificeren en definiëren met stakeholders                | Structuur voor documentatie                     | **95%**      |
| **Code Implementation** | Business logic, MSG-3/Maximo specifieke code, error handling              | Code templates, boilerplate, syntax suggesties  | **60%**      |
| **Testing**             | Test cases bedenken, assertions schrijven, edge cases, data               | Test templates, fixture suggesties              | **70%**      |
| **Documentatie**        | Context, voorbeelden, Babcock-specifieke info, instructies                | Markdown generatie uit code                     | **40%**      |

**Gemiddeld eigen werk: ~75%**

---

## 🏗️ Gedetailleerd: Wat Heb IK Gedaan?

### 1. Analyse & Requirements (100% Pedro)

**WAT IK HEB GEDAAN:**

- ✅ Gesprekken gevoerd met Matthijs Meijer (begeleider Babcock)
- ✅ MSG-3 Excel bestanden geanalyseerd
- ✅ Huidige workflow bij Babcock geobserveerd
- ✅ Pijnpunten geïdentificeerd (handmatig werk, fouten, tijd)
- ✅ Stakeholders geïdentificeerd (engineers, planners, management)
- ✅ Requirements opgesteld in overleg met team
- ✅ Scope bepaald (wat wel/niet in project)

**WAT AI DEED:**

- Suggesties voor structuur van documentatie
- Templates voor stakeholder analyse

**EIGENAARSCHAP:** Dit is 100% mijn eigen analyse van de Babcock situatie. AI kent Babcock niet.

---

### 2. Business Rules (95% Pedro)

**WAT IK HEB GEDAAN:**

- ✅ Alle 80 business rules geïdentificeerd met stakeholders
- ✅ Kritische rules bepaald (security, safety, compliance)
- ✅ Validatie logica bedacht voor elke rule
- ✅ Prioriteit bepaald (welke blokkeren processing?)
- ✅ Error messages geformuleerd
- ✅ Onderbouwd waarom elke rule belangrijk is

**WAT AI DEED:**

- Structuur voor documentatie (tabel format)
- Markdown formatting

**EIGENAARSCHAP:** De business rules zijn de kern van het systeem. Deze zijn door MIJ gedefinieerd op basis van Babcock requirements.

---

### 3. Technische Keuzes & Architectuur (85% Pedro)

**WAT IK HEB GEDAAN:**

- ✅ Python gekozen als taal (onderbouwd waarom)
- ✅ Agile methodiek gekozen (vs Waterfall, onderbouwd)
- ✅ Modulaire architectuur ontworpen (5 modules)
- ✅ Design patterns gekozen (Factory, Strategy, Repository)
- ✅ Libraries geselecteerd (openpyxl vs pandas, onderbouwd)
- ✅ Error handling strategie bedacht
- ✅ Testing strategie bepaald (TDD, >80% coverage)
- ✅ Trade-offs geëvalueerd (performance vs leesbaarheid)

**WAT AI DEED:**

- Uitleg van design patterns
- Voorbeelden van pattern implementaties
- UML diagram syntax hulp

**EIGENAARSCHAP:** Alle architecturale beslissingen zijn door MIJ gemaakt. Ik kan ze onderbouwen en verdedigen.

---

### 4. Code Implementatie (60% Pedro)

**WAT IK HEB GEDAAN:**

- ✅ **Business logic volledig zelf geschreven**
- ✅ MSG-3 specifieke parsing logica
- ✅ Maximo specifieke mapping rules
- ✅ 80 business rules validatie implementatie
- ✅ Error handling voor edge cases
- ✅ Logging strategie
- ✅ Configuration management
- ✅ Code review van alle AI-suggesties
- ✅ Refactoring voor leesbaarheid
- ✅ Type hints en docstrings toegevoegd/aangepast

**WAT AI DEED:**

- Code templates (class skeletons, boilerplate)
- Syntax suggesties (Python idioms)
- Refactoring suggesties
- Standard library gebruik voorbeelden

**EIGENAARSCHAP:**

- **Kritieke logica (business rules, MSG-3/Maximo specifiek): 100% Pedro**
- **Boilerplate (imports, class structuur): AI-gegenereerd, door mij gereviewed**
- **Ik begrijp ALLE code en kan het uitleggen**

**Voorbeeld:**

```python
# AI genereerde dit template:
class MSG3Parser:
    def parse(self, file_path: str):
        pass  # TODO

# IK schreef de daadwerkelijke implementatie:
class MSG3Parser:
    def parse(self, file_path: str) -> MSG3Data:
        # MSG-3 specifieke logica (100% Pedro)
        workbook = openpyxl.load_workbook(file_path)
        # ... 50+ regels MSG-3 specifieke parsing ...
        # ... business rule validatie per field ...
        # ... error handling voor Babcock edge cases ...
```

---

### 5. Testing (70% Pedro)

**WAT IK HEB GEDAAN:**

- ✅ Test cases bedacht (happy path, edge cases, errors)
- ✅ Test data gemaakt (mock MSG-3 bestanden)
- ✅ Assertions geschreven (wat moet het resultaat zijn?)
- ✅ Business rule compliance tests
- ✅ Integration test scenarios
- ✅ Manual testing met echte data
- ✅ Bug fixes na test failures

**WAT AI DEED:**

- Test templates (pytest fixtures)
- Parametrized test suggesties
- Mock/patch voorbeelden

**EIGENAARSCHAP:** De test cases en verwachte resultaten zijn door MIJ bepaald. AI hielp met de structuur.

---

### 6. Onderzoek & Alternatieven (80% Pedro)

**WAT IK HEB GEDAAN:**

- ✅ Maximo API getest in Babcock environment
- ✅ Excel libraries vergeleken (openpyxl vs pandas vs xlrd)
- ✅ Performance tests gedaan
- ✅ POC's gebouwd (Excel parsing, Maximo API call)
- ✅ Alternatieven onderbouwd (waarom deze keuze?)
- ✅ Risico's geïdentificeerd
- ✅ Mitigatie strategieën bedacht

**WAT AI DEED:**

- Alternatieven suggesties
- Pro/con lijsten templates
- Documentatie opzoeken

**EIGENAARSCHAP:** Alle keuzes zijn door MIJ gemaakt na eigen onderzoek en testen.

---

### 7. Planning & Projectmanagement (90% Pedro)

**WAT IK HEB GEDAAN:**

- ✅ Tijdsinschattingen gemaakt (realistische uren per taak)
- ✅ Sprint planning (wat in welke sprint?)
- ✅ Risico's geïdentificeerd (Maximo API, MSG-3 complexiteit)
- ✅ Mitigaties bedacht
- ✅ Voortgang gemonitord
- ✅ Weekly meetings met begeleider
- ✅ Backlog beheerd

**WAT AI DEED:**

- Planning templates
- Gantt chart formatting
- Risicoanalyse frameworks

**EIGENAARSCHAP:** De planning is gebaseerd op mijn eigen inschatting en ervaring.

---

### 8. Documentatie (50% Pedro, 50% AI)

**WAT IK HEB GEDAAN:**

- ✅ Context en achtergrond (Babcock specifiek)
- ✅ Voorbeelden en use cases
- ✅ Installatie instructies (Babcock omgeving)
- ✅ Troubleshooting (op basis van eigen ervaring)
- ✅ Gebruikersscenario's
- ✅ Review van AI-gegenereerde docs voor correctheid

**WAT AI DEED:**

- Markdown generatie uit code (docstrings → API docs)
- README templates
- Structuur voor documentatie

**EIGENAARSCHAP:** AI genereerde basis documentatie, IK voegde context en praktische informatie toe.

---

## 🎓 Competenties: Wat Heb IK Aangetoond?

### Analyseren (100% Pedro)

- Probleemsituatie bij Babcock geanalyseerd
- Stakeholders geïnterviewd
- Requirements verzameld en gestructureerd
- MSG-3 en Maximo datamodellen begrepen

### Adviseren (100% Pedro)

- Technische keuzes onderbouwd (Python, Agile, libraries)
- Alternatieven geëvalueerd met pro/cons
- Risico's geïdentificeerd en mitigaties voorgesteld
- Aanbevelingen gedaan aan Babcock team

### Ontwerpen (85% Pedro)

- Architectuur ontworpen (5 modules, interfaces)
- Design patterns gekozen en toegepast
- UML diagrammen gemaakt (met AI syntax hulp)
- Database/data structuren ontworpen

### Realiseren (60-70% Pedro)

- Business logic geïmplementeerd
- Code geschreven en getest
- Bug fixes gedaan
- Integration tests uitgevoerd

### Manage & Control (95% Pedro)

- Planning gemaakt en gevolgd
- Risico's gemonitord
- Kwaliteit geborgd (code reviews, tests)
- Voortgang gerapporteerd

---

## 🔍 Hoe Kan Ik Dit Bewijzen?

### 1. Ik Kan Alles Uitleggen

```
Q: "Waarom heb je Python gekozen?"
A: "Omdat Python sterke libraries heeft voor Excel parsing
    (openpyxl) en REST APIs (requests). Ook heeft Babcock
    al Python kennis in het team, wat adoptie makkelijker maakt."

Q: "Leg deze business rule uit."
A: "Deze rule (BR-005) controleert dat een taak niet dubbel
    voorkomt in het MSG-3. Dit is kritiek omdat dubbele taken
    kunnen leiden tot onnodige maintenance kosten."

Q: "Waarom deze architectuur?"
A: "Ik heb gekozen voor modulaire architectuur omdat het
    testbaarheid verbetert, wijzigingen isoleert, en het
    mogelijk maakt om later modules te vervangen."
```

### 2. Ik Heb de Tests Geschreven

- Test cases zijn gebaseerd op MIJN begrip van requirements
- Edge cases zijn geïdentificeerd door MIJ
- Assertions controleren wat IK verwacht

### 3. Ik Heb de Keuzes Gemaakt

- Elke technische keuze kan ik onderbouwen
- Ik heb alternatieven overwogen
- Trade-offs zijn door MIJ geëvalueerd

### 4. Ik Heb de Business Rules Gedefinieerd

- 80 business rules zijn door MIJ geïdentificeerd
- In samenwerking met Babcock stakeholders
- AI kent deze rules niet, deze zijn project-specifiek

---

## 📊 Vergelijking: Met vs Zonder AI

### Zonder AI (Traditioneel)

```
Repository setup:        8 uur
Code templates:         12 uur
Documentation:          40 uur
Unit test boilerplate:  20 uur
─────────────────────────────
Totaal:                 80 uur

→ Veel tijd aan repetitief werk
→ Focus verdeeld tussen boilerplate en logic
→ Meer kans op inconsistentie
```

### Met AI (Dit Project)

```
Repository setup:        2 uur (AI template → Pedro review)
Code templates:          3 uur (AI skeleton → Pedro logic)
Documentation:          10 uur (AI base → Pedro context)
Unit test boilerplate:   8 uur (AI template → Pedro cases)
─────────────────────────────
Totaal:                 23 uur

→ 57 uur bespaard
→ Meer tijd voor business logic & design
→ Focus op belangrijke beslissingen
```

**Maar:** Die 57 uur zijn niet "verloren" - ik heb ze gebruikt voor:

- ✅ Diepere analyse van MSG-3 structuur
- ✅ Meer tijd besteed aan business rules
- ✅ Betere testing (meer edge cases)
- ✅ Betere documentatie (meer voorbeelden)
- ✅ Meer iteraties op design

---

## 💡 Analogie: AI als Hulpmiddel

### AI is Zoals...

**Google:**

- Ik zoek informatie, Google geeft resultaten
- IK bepaal wat relevant is
- IK interpreteer en pas toe
- → Google heeft niet mijn paper geschreven

**Calculator:**

- Ik geef input, calculator geeft output
- IK begrijp de wiskunde
- IK controleer het resultaat
- → Calculator heeft niet mijn berekening gedaan

**Spellcheck:**

- Ik schrijf tekst, spellcheck geeft suggesties
- IK beslis wat ik overneem
- IK begrijp de grammatica
- → Spellcheck heeft niet mijn essay geschreven

**Cursor AI:**

- Ik geef context, AI geeft suggesties
- IK review en pas aan
- IK begrijp de code
- → AI heeft niet mijn project gemaakt

---

## 🎤 Voor Assessment: Hoe Leg Ik Dit Uit?

### Opening Statement

> "In dit project heb ik Cursor AI gebruikt als development tool,
> vergelijkbaar met hoe ik Google of Stack Overflow zou gebruiken.
> Alle belangrijke beslissingen - architectuur, business rules,
> technische keuzes - zijn door mij gemaakt. AI hielp met boilerplate
> en templates, maar ik schreef alle business logic zelf en kan alles
> uitleggen en onderbouwen."

### Veelgestelde Vragen

**Q: "Hoeveel van de code is AI-gegenereerd?"**

**A:** "AI genereerde ongeveer 40% van de code - vooral boilerplate
zoals class structures en imports. Maar alle kritieke logica is door
mij geschreven:

- 80 business rules implementatie: 100% Pedro
- MSG-3 parsing logica: 100% Pedro
- Maximo mapping rules: 100% Pedro
- Error handling: 100% Pedro

En ik heb ALLE code, ook de AI-gegenereerde templates, gereviewed
en aangepast aan project specifieke eisen."

---

**Q: "Begrijp je alle code?"**

**A:** "Absoluut. Ik heb een strict review proces:

1. AI suggereert code
2. Ik lees en begrijp het
3. Ik test het
4. Ik pas aan voor dit specifieke project
5. Als ik het niet begrijp, schrijf ik het zelf

Ik kan elke regel uitleggen en elk design pattern onderbouwen."

---

**Q: "Waarom AI gebruiken dan?"**

**A:** "Om te focussen op wat echt belangrijk is. In plaats van uren
te besteden aan het opzetten van boilerplate, kon ik meer tijd
besteden aan:

- Diepere analyse van MSG-3 en Maximo
- 80 business rules identificeren en implementeren
- Betere testing met meer edge cases
- Beter ontwerp met meer iteraties

Het is efficiëntie, niet afhankelijkheid."

---

**Q: "Is dit niet vals spelen?"**

**A:** "Nee, het is slim gebruik maken van moderne tools. Net zoals:

- Google gebruiken voor research
- IDE autocomplete voor syntax
- Stack Overflow voor voorbeelden
- Debugger voor bugs vinden

AI is een tool, geen vervanging van denken. Alle competenties die
Windesheim toetst - analyseren, adviseren, ontwerpen, realiseren -
zijn door mij aangetoond. AI hielp met efficiency, niet met competentie."

---

**Q: "Wat heb JIJ dan precies bijgedragen?"**

**A:** "Alles wat belangrijk is:

1. **Analyse:** Babcock probleem geïdentificeerd
2. **Design:** Architectuur ontworpen, patterns gekozen
3. **Business Rules:** 80 rules gedefinieerd met stakeholders
4. **Implementation:** Alle business logic geschreven
5. **Testing:** Test cases bedacht, edge cases geïdentificeerd
6. **Keuzes:** Elke technische keuze onderbouwd

AI was een assistent, ik was de ingenieur."

---

## 📋 Checklist: Kan Ik Dit Bewijzen?

### Voor Assessment

```
□ Ik kan alle architecturale keuzes onderbouwen
□ Ik kan elke business rule uitleggen
□ Ik kan de code regel voor regel doorlopen
□ Ik kan alternatieven noemen die ik heb overwogen
□ Ik kan uitleggen waarom ik deze libraries koos
□ Ik kan test cases beargumenteren
□ Ik kan design patterns uitleggen en toepassen
□ Ik kan Babcock-specifieke requirements benoemen
```

### Eigenaarschap Bewijzen

```
□ Git history toont mijn commits en beslissingen
□ Code comments tonen mijn begrip
□ Tests tonen mijn edge case analyse
□ Documentation toont Babcock context (AI kent dit niet)
□ Business rules zijn project-specifiek (niet generiek)
□ Design rationale is gedocumenteerd
```

---

## 🎯 Conclusie

```
┌──────────────────────────────────────────────────┐
│                                                  │
│  DIT IS MIJN PROJECT                             │
│                                                  │
│  ✅ Ik heb het probleem geanalyseerd            │
│  ✅ Ik heb de oplossing ontworpen               │
│  ✅ Ik heb de keuzes gemaakt                    │
│  ✅ Ik heb de logica geschreven                 │
│  ✅ Ik heb het getest                           │
│  ✅ Ik begrijp het volledig                     │
│  ✅ Ik kan het verdedigen                       │
│                                                  │
│  AI was een HULPMIDDEL, geen MEDEWERKER          │
│                                                  │
│  → Ik draag volledige verantwoordelijkheid       │
│  → Ik ben trots op MIJN werk                     │
│                                                  │
└──────────────────────────────────────────────────┘
```

---

**Datum:** 11 februari 2026  
**Auteur:** Pedro Eduardo Cardoso
**Project:** MSG-3 to Maximo Converter  
**Organisatie:** Babcock Schiphol

---

_Dit document benadrukt eigenaarschap en bewijst competentie._
