# Scope

## ✅ In Scope

### Functioneel

#### 1. MSG-3 Excel Parsing
- **Origineel formaat**: Parser voor huidige MSG-3 Excel structuur
- **Redesign formaat**: Parser voor herontworpen Excel template
- **Multi-format support**: Ondersteuning voor beide formaten
- **Data extractie**: Automatisch uitlezen van alle relevante velden

#### 2. Data Validatie
- **Structuur validatie**: Verificatie van Excel structuur en verplichte velden
- **Business rules**: Implementatie van bedrijfslogica validaties
- **Data quality checks**: Controleren op consistentie en compleetheid
- **Error reporting**: Duidelijke foutmeldingen bij validatie problemen

#### 3. Change Detection
- **Added tasks**: Detecteren van nieuwe taken in MSG-3 update
- **Modified tasks**: Identificeren van gewijzigde taken met specifieke veld-wijzigingen
- **Deleted tasks**: Vinden van verwijderde taken
- **Diff reporting**: Genereren van change rapport voor review

#### 4. Mapping naar Maximo
- **PM (Preventive Maintenance) objecten**: Mapping van MSG-3 naar Maximo PM structuur
- **JobPlan objecten**: Mapping van MSG-3 taken naar Maximo JobPlans
- **Relaties**: Correcte linking tussen PM's en JobPlans
- **Field mapping**: Vertaling van MSG-3 velden naar Maximo velden

#### 5. Maximo REST API Integratie
- **Authenticatie**: Veilige connectie met Maximo
- **CRUD operaties**: Create, Read, Update operaties (geen Delete)
- **Batch processing**: Efficiënt verwerken van meerdere records
- **Error handling**: Retry logic en foutafhandeling bij API calls

#### 6. MSG-3 Excel Redesign
- **Template ontwerp**: Nieuwe geoptimaliseerde Excel template
- **Documentatie**: Specificaties en gebruikershandleiding voor template
- **Voorbeeld data**: Template met voorbeelddata
- **Validatie regels**: In-Excel validaties waar mogelijk

#### 7. Documentatie
- **Technische documentatie**: Architectuur, design decisions, API documentatie
- **Gebruikershandleiding**: Stap-voor-stap instructies voor eindgebruikers
- **Installation guide**: Deployment en configuratie instructies
- **Code documentatie**: Comments en docstrings in code

---

### Technisch

#### 1. Applicatie
- **Python 3.11+**: Moderne Python versie
- **Modular architecture**: Herbruikbare componenten
- **Clean code**: PEP 8 compliant, SOLID principles
- **Configuration**: Externe configuratie voor flexibiliteit

#### 2. Interface
- **Command-line interface (CLI)**: Primaire gebruikersinterface
- **Arguments en flags**: Flexibele command-line opties
- **Interactive prompts**: Gebruiksvriendelijke input waar nodig
- **Progress indicators**: Feedback tijdens processing

#### 3. Logging & Error Handling
- **Structured logging**: Gedetailleerde logs van alle operaties
- **Error handling**: Graceful failure handling
- **Debug mode**: Extra logging voor troubleshooting
- **Log rotation**: Beheer van log bestanden

#### 4. Testing
- **Unit tests**: Tests voor individuele componenten
- **Integration tests**: End-to-end tests met Maximo test environment
- **Test coverage**: Minimaal 80% code coverage
- **Test data**: Voorbeeld MSG-3 bestanden voor testing

#### 5. Dependencies
- **openpyxl/pandas**: Excel parsing
- **requests**: HTTP calls naar Maximo REST API
- **pytest**: Testing framework
- **pydantic**: Data validatie
- **requirements.txt**: Dependency management

---

## ❌ Out of Scope

### Functioneel

#### 1. Automatische Scheduling
- **Niet inbegrepen**: Automatische planning van onderhoudstaken
- **Reden**: Dit is functionaliteit van Maximo zelf
- **Alternatief**: Maximo PM scheduling wordt gebruikt

#### 2. Historische Data Migratie
- **Niet inbegrepen**: Import van oude/historische MSG-3 data
- **Reden**: Focus op nieuwe en gewijzigde data
- **Alternatief**: Alleen forward-looking data wordt verwerkt

#### 3. User Interface / Web Applicatie
- **Niet inbegrepen**: Grafische interface of web applicatie
- **Reden**: Beperkte scope, CLI is voldoende voor MVP
- **Alternatief**: Command-line interface

#### 4. Integratie met Andere Systemen
- **Niet inbegrepen**: Koppeling met andere systemen dan Maximo
- **Reden**: Specifieke scope op MSG-3 → Maximo
- **Alternatief**: Eventueel in toekomstige versies

#### 5. Real-time Synchronisatie
- **Niet inbegrepen**: Live sync tussen MSG-3 en Maximo
- **Reden**: Batch processing is voldoende
- **Alternatief**: On-demand processing wanneer nodig

#### 6. Multi-tenancy
- **Niet inbegrepen**: Ondersteuning voor meerdere klanten/omgevingen
- **Reden**: Single-tenant (Babcock Schiphol) is voldoende
- **Alternatief**: Configuratie per omgeving mogelijk

---

### Technisch

#### 1. Maximo Customizatie
- **Niet inbegrepen**: Aanpassingen aan Maximo datamodel of UI
- **Reden**: Werkt met standaard Maximo API en objecten
- **Alternatief**: Standard Maximo functionaliteit wordt gebruikt

#### 2. Mobile App
- **Niet inbegrepen**: iOS/Android applicatie
- **Reden**: Buiten scope voor dit project
- **Alternatief**: CLI op desktop/server

#### 3. Advanced Analytics
- **Niet inbegrepen**: Dashboards, reporting, analytics
- **Reden**: Focus op data transfer, niet analyse
- **Alternatief**: Maximo's eigen reporting tools

#### 4. Maximo Data Export
- **Niet inbegrepen**: Export van data uit Maximo
- **Reden**: Eenrichtingsverkeer MSG-3 → Maximo
- **Alternatief**: Read operaties alleen voor verificatie

#### 5. Delete Operaties
- **Niet inbegrepen**: Automatisch verwijderen van Maximo records
- **Reden**: Veiligheid - geen automatische deletes
- **Alternatief**: Handmatige review en delete indien nodig

---

## 🔮 Future Enhancements (Nice to Have)

Deze features zijn niet in scope voor dit project, maar kunnen in de toekomst toegevoegd worden:

### Korte Termijn (3-6 maanden)
1. **Web Interface**: Grafische interface voor niet-technische gebruikers
2. **Email Notificaties**: Automatische meldingen bij succesvolle/gefaalde imports
3. **Enhanced Reporting**: Uitgebreide rapporten over import statistieken
4. **Scheduling**: Automatische periodieke import checks

### Middellange Termijn (6-12 maanden)
5. **Real-time Monitoring Dashboard**: Live status van MSG-3 imports
6. **API voor Externe Systemen**: REST API voor integratie met andere tools
7. **Batch Processing UI**: Interface voor meerdere MSG-3 bestanden tegelijk
8. **Version Control**: Volledige history tracking van MSG-3 versies

### Lange Termijn (12+ maanden)
9. **AI-assisted Mapping**: Machine learning voor automatische field mapping
10. **Multi-source Integration**: Support voor andere data bronnen naast Excel
11. **Predictive Validation**: Voorspellen van potentiële validatie issues
12. **Cloud Deployment**: SaaS variant van de tool

---

## ⚠️ Assumptions (Aannames)

Deze aannames zijn gemaakt bij het bepalen van de scope:

### Technische Aannames
1. **Maximo REST API** is beschikbaar en toegankelijk voor het project
2. **API credentials** kunnen worden verkregen voor test en productie
3. **Test environment** is beschikbaar zonder impact op productie
4. **Maximo datamodel** is voldoende (geen custom fields nodig)
5. **Python 3.11+** kan worden gebruikt op target machines
6. **Network access** naar Maximo server is mogelijk

### Data Aannames
7. **MSG-3 Excel** bevat valide ATA MSG-3 gestructureerde data
8. **Excel formaat** blijft relatief consistent over tijd
9. **Verplichte velden** zijn gedefinieerd en gedocumenteerd
10. **Business rules** zijn bekend en gedocumenteerd

### Organisatie Aannames
11. **Stakeholders** zijn beschikbaar voor feedback en review
12. **Voorbeeld data** is beschikbaar voor development en testing
13. **Domain expertise** is beschikbaar bij vragen over MSG-3/Maximo
14. **Testing time** is beschikbaar in test environment

### Proces Aannames
15. **Handmatig review** blijft bestaan voor kritische changes
16. **Backup proces** bestaat voor Maximo data
17. **Rollback mogelijkheid** is aanwezig bij problemen
18. **Change management** proces wordt gevolgd bij deployment

---

## 🔗 Dependencies (Afhankelijkheden)

Het project is afhankelijk van:

### Externe Dependencies
1. **Maximo Test Environment**
   - Beschikbaar vanaf start project
   - Credentials voor API access
   - Vergelijkbaar met productie

2. **MSG-3 Voorbeeld Data**
   - Minimaal 2-3 echte MSG-3 documenten
   - Zowel origineel als verschillende versies (voor change detection)
   - Geanonimiseerd indien nodig

3. **Stakeholder Beschikbaarheid**
   - **Matthijs Meijer**: Wekelijks beschikbaar voor technische vragen
   - **Rick Kramer**: Beschikbaar voor requirements en feedback
   - **Roy Minkels**: Beschikbaar voor MSG-3 domein kennis

4. **Development Omgeving**
   - Python 3.11+ development machine
   - IDE (VS Code, PyCharm, of vergelijkbaar)
   - Git voor version control

### Interne Dependencies
5. **Documentatie**
   - Maximo REST API documentatie
   - MSG-3 specificatie documenten
   - Babcock specifieke requirements

6. **Goedkeuringen**
   - IT goedkeuring voor API access
   - Security review voor credentials handling
   - Stakeholder goedkeuring voor Excel redesign

---

## 🎯 Success Criteria

Het project voldoet aan de scope als:

### Functionele Criteria
- ✅ MSG-3 Excel kan automatisch worden verwerkt
- ✅ Data wordt correct gevalideerd
- ✅ Wijzigingen worden gedetecteerd
- ✅ Data komt correct in Maximo aan
- ✅ Nieuwe Excel template is goedgekeurd

### Technische Criteria
- ✅ Code voldoet aan kwaliteitseisen
- ✅ Tests hebben voldoende coverage
- ✅ Performance eisen worden gehaald
- ✅ Error handling is robuust

### Documentatie Criteria
- ✅ Technische en gebruikersdocumentatie is compleet
- ✅ Code is goed gedocumenteerd
- ✅ Overdracht kan plaatsvinden

### Business Criteria
- ✅ Minimaal 80% tijdsbesparing t.o.v. handmatig proces
- ✅ Stakeholders zijn tevreden met resultaat
- ✅ Systeem is overdraagbaar en onderhoudbaar

---

*Datum: 4 februari 2026*  
*Auteur: Pedro*  
*Project: MSG-3 to Maximo Converter*
