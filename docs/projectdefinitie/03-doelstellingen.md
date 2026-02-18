# Doelstellingen

## Hoofddoel

**Automatiseren van de MSG-3 → Maximo datakoppeling om tijd te besparen, fouten te reduceren en het engineering team te ontlasten.**

---

## Subdoelen (SMART)

### 1. MSG-3 Parser Ontwikkelen

**Doel:** Een robuuste parser bouwen die MSG-3 Excel kan inlezen, valideren en converteren naar gestructureerde data.

#### SMART Criteria

- **Specifiek**: 
  - Parser kan MSG-3 Excel bestanden inlezen
  - Data converteren naar JSON formaat
  - Structuur valideren volgens MSG-3 standaard
  - Error handling voor ongeldige bestanden

- **Meetbaar**: 
  - ✅ 95% van MSG-3 taken correct geparseerd
  - ✅ Verwerking binnen 5 seconden per bestand
  - ✅ Alle verplichte velden gedetecteerd
  - ✅ Duidelijke error messages bij validatie fouten

- **Acceptabel**: 
  - Haalbaar met openpyxl/pandas in Python
  - Voorbeeld MSG-3 bestanden beschikbaar
  - Python expertise aanwezig

- **Relevant**: 
  - Noodzakelijk voor automatische verwerking
  - Basis voor alle volgende stappen
  - Direct impact op data kwaliteit

- **Tijdgebonden**: 
  - **Deadline**: Week 1-2 van project (14 februari 2026)
  - **Mijlpalen**:
    - Week 1: Basic Excel parsing
    - Week 2: Validatie en error handling

#### Acceptatiecriteria
- [ ] MSG-3 Excel kan worden ingelezen
- [ ] Data wordt geconverteerd naar JSON
- [ ] Schema validatie werkt correct
- [ ] Unit tests met 90%+ coverage
- [ ] Documentatie beschikbaar

---

### 2. Change Detection Implementeren

**Doel:** Wijzigingen tussen verschillende MSG-3 versies automatisch detecteren en rapporteren.

#### SMART Criteria

- **Specifiek**: 
  - Vergelijken van twee MSG-3 versies (oud vs nieuw)
  - Detecteren van toegevoegde taken (added)
  - Detecteren van gewijzigde taken (modified)
  - Detecteren van verwijderde taken (deleted)
  - Genereren van change report

- **Meetbaar**: 
  - ✅ 100% van wijzigingen correct gedetecteerd
  - ✅ Geen false positives/negatives
  - ✅ Change report in <2 seconden gegenereerd
  - ✅ Overzichtelijk diff rapport

- **Acceptabel**: 
  - Algoritme voor object vergelijking is bewezen
  - Diff libraries beschikbaar in Python
  - Test data met verschillende versies beschikbaar

- **Relevant**: 
  - Essentieel voor incremental updates in Maximo
  - Voorkomt volledige re-import bij kleine wijzigingen
  - Geeft inzicht in impact van MSG-3 updates

- **Tijdgebonden**: 
  - **Deadline**: Week 3-4 van project (28 februari 2026)
  - **Mijlpalen**:
    - Week 3: Diff algoritme implementatie
    - Week 4: Rapportage en testing

#### Acceptatiecriteria
- [ ] Toegevoegde taken worden gedetecteerd
- [ ] Gewijzigde taken worden gedetecteerd met specifieke velden
- [ ] Verwijderde taken worden gedetecteerd
- [ ] Change report is leesbaar en accuraat
- [ ] Unit tests voor verschillende scenario's

---

### 3. Maximo Integratie Realiseren

**Doel:** MSG-3 data automatisch naar Maximo uploaden via REST API met correcte mapping naar PM en JobPlan objecten.

#### SMART Criteria

- **Specifiek**: 
  - MSG-3 data mappen naar Maximo PM (Preventive Maintenance) structuur
  - MSG-3 data mappen naar Maximo JobPlan structuur
  - REST API integratie met authenticatie
  - CRUD operaties (Create, Read, Update) implementeren
  - Error handling en retry logic

- **Meetbaar**: 
  - ✅ 100% succesvolle API calls (met retry)
  - ✅ Correcte data in Maximo na import (verificatie)
  - ✅ Response time <500ms per record
  - ✅ Duidelijke logging van alle acties

- **Acceptabel**: 
  - Maximo REST API documentatie beschikbaar
  - Test environment toegankelijk
  - API credentials beschikbaar
  - Python requests library

- **Relevant**: 
  - Core functionaliteit van het project
  - Direct meetbare impact op proces
  - Eindgebruikers zien resultaat in Maximo

- **Tijdgebonden**: 
  - **Deadline**: Week 5-7 van project (21 maart 2026)
  - **Mijlpalen**:
    - Week 5: API connectie en authenticatie
    - Week 6: Mapping logica PM/JobPlan
    - Week 7: Testing en refinement

#### Acceptatiecriteria
- [ ] Verbinding met Maximo REST API werkt
- [ ] PM records worden correct aangemaakt
- [ ] JobPlans worden correct aangemaakt
- [ ] Update operaties werken voor wijzigingen
- [ ] Error handling en logging aanwezig
- [ ] Integration tests met test environment

---

### 4. MSG-3 Excel Redesign

**Doel:** MSG-3 Excel template herontwerpen voor optimale machine-leesbaarheid en automatische verwerking.

#### SMART Criteria

- **Specifiek**: 
  - Analyseren huidige MSG-3 Excel structuur
  - Identificeren van verbeterpunten voor parsing
  - Ontwerpen nieuwe template met gestandaardiseerde structuur
  - Documenteren van template specificaties
  - Valideren met stakeholders

- **Meetbaar**: 
  - ✅ Nieuwe template 100% compatibel met parser
  - ✅ Alle vereiste velden aanwezig en gevalideerd
  - ✅ 50% snellere parsing dan origineel formaat
  - ✅ Goedkeuring van minimaal 2 stakeholders

- **Acceptabel**: 
  - Excel expertise beschikbaar
  - Stakeholder input mogelijk
  - Tijd voor iteraties beschikbaar

- **Relevant**: 
  - Verbetert toekomstige MSG-3 verwerking
  - Reduceert complexiteit van parser
  - Maakt proces duurzamer

- **Tijdgebonden**: 
  - **Deadline**: Week 8-10 van project (11 april 2026)
  - **Mijlpalen**:
    - Week 8: Analyse en ontwerp
    - Week 9: Template creatie en testing
    - Week 10: Stakeholder review en finalisatie

#### Acceptatiecriteria
- [ ] Nieuwe template ontworpen en gedocumenteerd
- [ ] Template werkt met bestaande parser (met aanpassingen)
- [ ] Voorbeeld data in nieuwe format
- [ ] Gebruikershandleiding voor template
- [ ] Goedkeuring van Babcock stakeholders

---

### 5. Documentatie & Overdracht

**Doel:** Volledige en overdraagbare documentatie leveren zodat het systeem door anderen kan worden gebruikt en onderhouden.

#### SMART Criteria

- **Specifiek**: 
  - Technische documentatie (architectuur, code, API)
  - Gebruikershandleiding (hoe te gebruiken)
  - Installation guide (deployment)
  - Troubleshooting guide
  - Code comments en docstrings

- **Meetbaar**: 
  - ✅ Alle componenten gedocumenteerd
  - ✅ Minimaal 1 persoon kan systeem zelfstandig gebruiken
  - ✅ Code coverage van docstrings >80%
  - ✅ Positieve feedback van stakeholders op documentatie

- **Acceptabel**: 
  - Templates beschikbaar
  - Tijd ingepland voor documentatie
  - Review mogelijk door stakeholders

- **Relevant**: 
  - Essentieel voor overdracht aan Babcock
  - Noodzakelijk voor onderhoud
  - Vereiste voor Comakership afstuderen

- **Tijdgebonden**: 
  - **Deadline**: Doorlopend + finalisatie laatste 2 weken
  - **Mijlpalen**:
    - Continue: Code comments tijdens ontwikkeling
    - Week 11: Technische documentatie
    - Week 12: Gebruikersdocumentatie en review

#### Acceptatiecriteria
- [ ] README.md met quickstart
- [ ] Technische architectuur gedocumenteerd
- [ ] API documentatie beschikbaar
- [ ] Gebruikershandleiding geschreven
- [ ] Code comments en docstrings aanwezig
- [ ] Overdracht sessie met stakeholders gehouden

---

## Project Acceptatiecriteria

Het project is succesvol afgerond als aan **alle** onderstaande criteria is voldaan:

### Functioneel
- [x] MSG-3 Excel wordt correct geparseerd (zowel origineel als redesign formaat)
- [x] Data validatie werkt (structuur + business rules)
- [x] Wijzigingen tussen versies worden gedetecteerd
- [x] Data wordt succesvol naar Maximo gestuurd via REST API
- [x] PM en JobPlan records worden correct aangemaakt in Maximo
- [x] Herontworpen Excel template is getest en goedgekeurd

### Technisch
- [x] Unit tests met minimaal 80% code coverage
- [x] Integration tests met Maximo test environment
- [x] Error handling en logging aanwezig
- [x] Code voldoet aan Python best practices (PEP 8)
- [x] Performance eisen gehaald (processing times)

### Documentatie
- [x] Technische documentatie compleet
- [x] Gebruikershandleiding beschikbaar
- [x] Code is gedocumenteerd (comments, docstrings)
- [x] Installation guide beschikbaar

### Overdracht
- [x] Demo gegeven aan stakeholders
- [x] Overdracht sessie gehouden
- [x] Feedback verwerkt
- [x] Systeem is operationeel in test environment

### Leerproces (Comakership)
- [x] Competentie ontwikkeling gedocumenteerd
- [x] Reflectie geschreven
- [x] Portfolio bijgewerkt
- [x] Begeleider feedback verwerkt

---

## Tijdlijn Overzicht

| Week | Periode | Hoofdactiviteit | Deliverable |
|------|---------|-----------------|-------------|
| 1-2 | 3-14 feb | MSG-3 Parser | Werkende parser met validatie |
| 3-4 | 17-28 feb | Change Detection | Diff engine met reporting |
| 5-7 | 3-21 mrt | Maximo Integratie | REST API integratie |
| 8-10 | 24 mrt-11 apr | Excel Redesign | Nieuwe MSG-3 template |
| 11-12 | 14-25 apr | Documentatie & Overdracht | Volledige documentatie |

**Project Einde:** Einde stage (exacte datum afhankelijk van stageduur)

---

## Prioritering

### Must Have (P0)
1. MSG-3 Parser (basis functionaliteit)
2. Maximo Integratie (PM & JobPlan)
3. Basis documentatie

### Should Have (P1)
4. Change Detection
5. Excel Redesign
6. Uitgebreide documentatie

### Nice to Have (P2)
7. Web interface (future enhancement)
8. Monitoring dashboard (future enhancement)
9. Email notificaties (future enhancement)

---

*Datum: 4 februari 2026*  
*Auteur: Pedro Eduardo Cardoso*  
*Project: MSG-3 to Maximo Converter*

---

## AI Authenticiteitsverklaring

Voor het verfijnen van teksten in de projectdefinitie heb ik **Cursor AI** gebruikt om te **verbeteren van formulering en professionele schrijfstijl**. Na het gebruik van deze tool heb ik de uitkomsten ervan uitvoerig gecontroleerd en aangepast om er voor te zorgen dat het ingeleverde werk mijn eigen competenties en leeruitkomsten reflecteert. Ik draag de volledige verantwoordelijkheid voor de inhoud van dit werk.

*AIAS Niveau: 3 - AI Samenwerking*
