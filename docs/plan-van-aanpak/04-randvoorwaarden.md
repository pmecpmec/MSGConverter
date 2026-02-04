# Randvoorwaarden

## Inleiding

Dit document beschrijft de **randvoorwaarden** en **vereisten** die noodzakelijk zijn voor het succesvol uitvoeren van het MSG-3 to Maximo project. Zonder deze randvoorwaarden kan het project niet (volledig) worden uitgevoerd.

---

## 1. Toegang & Permissies

### 🔴 KRITIEK: Maximo Test Environment

**Vereiste:**
- Toegang tot Maximo test environment
- API endpoints en documentatie
- Credentials (API key / gebruikersnaam + wachtwoord)
- Read en Write permissies voor PM en JobPlan objecten

**Waarom Noodzakelijk:**
- Zonder Maximo toegang kan integratie niet worden ontwikkeld
- Testing is onmogelijk zonder test environment
- Core functionaliteit van het project

**Verwachte Beschikbaarheid:**
- **Deadline**: Uiterlijk einde Week 2 (17 februari 2026)
- **Verantwoordelijke**: Matthijs Meijer / IT Babcock
- **Status**: 🟡 Nog te regelen

**Risico bij Afwezigheid:**
- Project kan niet verder na Week 11
- Mogelijk volledige blokkade
- Planning in gevaar

---

### 🟠 HOOG: Permissies Babcock & Schiphol

**Vereiste:**
- Permissie om op Babcock netwerk te werken
- Toegang tot relevante systemen
- VPN toegang indien remote werken

**Waarom Noodzakelijk:**
- Nodig om met Maximo te kunnen verbinden
- Access tot interne documentatie
- Communicatie met stakeholders

**Verwachte Beschikbaarheid:**
- **Deadline**: Week 1 (10 februari 2026)
- **Verantwoordelijke**: Matthijs Meijer / HR
- **Status**: 🟡 Vermoedelijk geen probleem, maar moet bevestigd

**Risico bij Afwezigheid:**
- Kan niet op locatie werken
- Beperkte toegang tot resources
- Communicatie vertraagd

---

## 2. Data & Documentatie

### 🔴 KRITIEK: MSG-3 Voorbeeld Bestanden

**Vereiste:**
- Minimaal 2-3 echte MSG-3 Excel bestanden
- Bij voorkeur verschillende versies (voor change detection testing)
- Geanonimiseerd indien nodig voor privacy
- Representatief voor productie data

**Waarom Noodzakelijk:**
- Parser kan niet ontwikkeld worden zonder voorbeelden
- Testing vereist realistische data
- Validatie van business rules
- Change detection vereist meerdere versies

**Verwachte Beschikbaarheid:**
- **Deadline**: Week 1 (10 februari 2026)
- **Verantwoordelijke**: Roy Minkels / Engineering team
- **Status**: 🟡 Nog te vragen

**Risico bij Afwezigheid:**
- Kan geen parser ontwikkelen
- Testing met synthetische data is minder betrouwbaar
- Mogelijk verkeerde aannames

---

### 🟠 HOOG: Maximo API Documentatie

**Vereiste:**
- REST API documentatie (endpoints, parameters, responses)
- PM (Preventive Maintenance) object schema
- JobPlan object schema
- Authentication documentatie
- Voorbeeld API calls

**Waarom Noodzakelijk:**
- Nodig voor correcte API integratie
- Field mapping vereist kennis van Maximo structuur
- Error handling en edge cases

**Verwachte Beschikbaarheid:**
- **Deadline**: Week 3 (24 februari 2026)
- **Verantwoordelijke**: IT Babcock / Maximo beheerders
- **Status**: 🟢 Vermoedelijk beschikbaar (IBM documentatie + interne docs)

**Risico bij Afwezigheid:**
- Trial and error ontwikkeling (inefficiënt)
- Mogelijk incorrecte implementatie
- Meer tijd nodig

---

### 🟡 MEDIUM: MSG-3 Specificatie & Business Rules

**Vereiste:**
- Documentatie over MSG-3 structuur en standaarden
- Business rules voor validatie
- Mapping specificatie (MSG-3 velden → Maximo velden)
- Domain expertise beschikbaar voor vragen

**Waarom Noodzakelijk:**
- Correcte validatie van MSG-3 data
- Juiste mapping naar Maximo
- Begrip van domain logic

**Verwachte Beschikbaarheid:**
- **Deadline**: Doorlopend tijdens project
- **Verantwoordelijke**: Roy Minkels / Engineering team
- **Status**: 🟡 Beschikbaar via stakeholders

**Risico bij Afwezigheid:**
- Incorrecte validatie regels
- Fouten in mapping
- Data kwaliteit problemen

---

## 3. Technische Infrastructuur

### 🔴 KRITIEK: Laptop met Development Omgeving

**Vereiste:**
- Laptop met voldoende specs (minimaal 8GB RAM, 100GB opslag)
- Python 3.11+ installeerbaar
- Git beschikbaar
- Cursor IDE of VS Code
- Internet connectie

**Waarom Noodzakelijk:**
- Development environment voor code schrijven
- Testing en debugging
- Communicatie met team

**Verwachte Beschikbaarheid:**
- **Deadline**: Nu (beschikbaar)
- **Verantwoordelijke**: Pedro (eigen laptop) of Babcock (company laptop)
- **Status**: ✅ Beschikbaar

**Risico bij Afwezigheid:**
- Kan niet ontwikkelen
- Project kan niet starten

---

### 🟢 LAAG: Internet Connectie

**Vereiste:**
- Stabiele internet verbinding
- Voldoende snelheid voor API calls en communicatie
- Backup optie (mobiele hotspot)

**Waarom Noodzakelijk:**
- API calls naar Maximo
- Communicatie met team (Teams, email)
- Toegang tot documentatie en resources

**Verwachte Beschikbaarheid:**
- **Deadline**: Doorlopend
- **Verantwoordelijke**: Babcock (op locatie) / Pedro (thuis)
- **Status**: ✅ Beschikbaar

**Risico bij Afwezigheid:**
- Tijdelijke productiviteitsverlies
- Geen toegang tot Maximo
- Communicatie problemen

---

### 🟡 MEDIUM: Git Repository

**Vereiste:**
- Git repository (GitHub, GitLab, of Babcock internal)
- Version control voor code
- Backup van werk

**Waarom Noodzakelijk:**
- Code versioning en backup
- Collaboration mogelijk maken
- Traceerbaarheid van changes

**Verwachte Beschikbaarheid:**
- **Deadline**: Week 1 (reeds opgezet)
- **Verantwoordelijke**: Pedro
- **Status**: ✅ Beschikbaar (lokale Git repo)

**Risico bij Afwezigheid:**
- Risico op data verlies
- Geen version control
- Moeilijk samenwerken

---

## 4. Menselijke Resources

### 🔴 KRITIEK: Stakeholder Beschikbaarheid

**Vereiste:**
- **Matthijs Meijer** (Bedrijfsbegeleider): Wekelijks beschikbaar (1-2 uur/week)
- **Rick Kramer**: Beschikbaar voor requirements en feedback
- **Roy Minkels**: Beschikbaar voor MSG-3 en Maximo domein kennis

**Waarom Noodzakelijk:**
- Feedback op deliverables
- Antwoorden op vragen
- Goedkeuring van design beslissingen
- Demo's en reviews

**Verwachte Beschikbaarheid:**
- **Deadline**: Doorlopend tijdens project
- **Verantwoordelijke**: Stakeholders
- **Status**: 🟢 Commitment aanwezig

**Risico bij Afwezigheid:**
- Verkeerde richting in development
- Vertraging in decision making
- Mogelijk rework nodig

---

### 🟡 MEDIUM: Schoolbegeleider

**Vereiste:**
- Schoolbegeleider beschikbaar voor periodieke evaluaties
- Feedback op comakership aspecten
- Ondersteuning bij problemen

**Waarom Noodzakelijk:**
- Begeleiding vanuit school
- Evaluatie van leerproces
- Ondersteuning bij issues

**Verwachte Beschikbaarheid:**
- **Deadline**: Per periode (maandelijks)
- **Verantwoordelijke**: School
- **Status**: 🟢 Vermoedelijk geregeld

**Risico bij Afwezigheid:**
- Minder ondersteuning
- Comakership aspecten minder goed
- Geen escalatie mogelijkheid

---

## 5. Tijd & Commitment

### 🔴 KRITIEK: Fulltime Stage Commitment

**Vereiste:**
- 32-40 uur per week beschikbaar voor stage
- 18 weken project duur (4 feb - 15 juni 2026)
- Minimale afwezigheid door vakantie/ziekte

**Waarom Noodzakelijk:**
- Project scope vereist fulltime inzet
- Planning is gebaseerd op fulltime werk
- Complexiteit vereist focus en tijd

**Verwachte Beschikbaarheid:**
- **Deadline**: Doorlopend (4 feb - 15 juni)
- **Verantwoordelijke**: Pedro
- **Status**: ✅ Commitment aanwezig

**Risico bij Afwezigheid:**
- Project wordt niet afgerond
- Deadline in gevaar
- Scope moet drastisch verkleind

---

### 🟡 MEDIUM: Concentratie & Focus Tijd

**Vereiste:**
- Omgeving waar gefocust gewerkt kan worden
- Minimale afleidingen tijdens development
- Goede werkplek (thuis of op locatie)

**Waarom Noodzakelijk:**
- Development vereist diepe focus
- Complexe problemen oplossen
- Kwaliteit van code

**Verwachte Beschikbaarheid:**
- **Deadline**: Doorlopend
- **Verantwoordelijke**: Pedro / Babcock (werkplek)
- **Status**: 🟡 Aandachtspunt (concentratieproblemen genoemd)

**Risico bij Afwezigheid:**
- Lagere productiviteit
- Meer fouten
- Langere development tijd

---

## 6. Tools & Software

### 🟢 LAAG: Development Tools

**Vereiste:**
- **Python 3.11+**: Programming language
- **Cursor IDE / VS Code**: Code editor met AI
- **Git**: Version control
- **pytest**: Testing framework

**Waarom Noodzakelijk:**
- Development omgeving
- Code kwaliteit
- Testing

**Verwachte Beschikbaarheid:**
- **Deadline**: Week 1
- **Verantwoordelijke**: Pedro
- **Status**: ✅ Beschikbaar (free/open source)

---

### 🟢 LAAG: Python Libraries

**Vereiste:**
- **openpyxl / pandas**: Excel parsing
- **requests**: HTTP API calls
- **pydantic**: Data validatie
- Andere libraries volgens requirements.txt

**Waarom Noodzakelijk:**
- Core functionaliteit
- Geen reinventing the wheel
- Industry standard libraries

**Verwachte Beschikbaarheid:**
- **Deadline**: Per fase wanneer nodig
- **Verantwoordelijke**: Pedro
- **Status**: ✅ Beschikbaar via pip install

---

## 7. Kennis & Vaardigheden

### 🟡 MEDIUM: Python Programmeer Kennis

**Vereiste:**
- Basis Python kennis
- Object-oriented programming
- Error handling
- Testing met pytest

**Waarom Noodzakelijk:**
- Project is in Python
- Code kwaliteit
- Debugging

**Verwachte Beschikbaarheid:**
- **Deadline**: Tijdens project (learning on the job)
- **Verantwoordelijke**: Pedro + AI assistentie
- **Status**: 🟡 Basis aanwezig, verfijning tijdens project

**Risico bij Afwezigheid:**
- Langzamere development
- Lagere code kwaliteit
- Meer bugs

**Mitigatie:**
- AI assistentie (Cursor)
- Online tutorials en documentatie
- Code reviews
- Learning by doing

---

### 🟡 MEDIUM: REST API Kennis

**Vereiste:**
- Begrip van REST APIs
- HTTP methods (GET, POST, PUT)
- JSON data structuren
- Authentication (API keys, tokens)

**Waarom Noodzakelijk:**
- Maximo integratie via REST API
- Core functionaliteit

**Verwachte Beschikbaarheid:**
- **Deadline**: Week 3-4 (learning)
- **Verantwoordelijke**: Pedro + AI assistentie
- **Status**: 🟡 Kan geleerd worden tijdens project

**Risico bij Afwezigheid:**
- Langzamere API development
- Mogelijk incorrecte implementatie

**Mitigatie:**
- POC in Week 3-4
- AI assistentie
- Maximo documentatie
- Trial and error in test environment

---

## Samenvatting: Critical Path Requirements

### Week 1-2 (KRITIEK):
- ✅ Laptop met development omgeving
- ⏳ Permissies Babcock/Schiphol
- ⏳ MSG-3 voorbeeld bestanden
- ⏳ Maximo test environment toegang (deadline einde week 2)

### Week 3-4 (HOOG):
- ⏳ Maximo API documentatie
- ⏳ MSG-3 specificatie en business rules
- Stakeholder beschikbaarheid voor POC review

### Week 5+ (MEDIUM):
- Doorlopende stakeholder beschikbaarheid
- Fulltime commitment
- Concentratie en focus

---

## Escalatie Procedure

**Als kritieke randvoorwaarde niet beschikbaar is:**

1. **Week 1**: Identificeer blocker
2. **Dag 1-2**: Probeer zelf op te lossen
3. **Dag 3**: Informeer begeleider (Matthijs Meijer)
4. **Dag 4-5**: Escaleer naar stakeholders/management indien nodig
5. **Week 2**: Noodplan activeren (mock data, alternative approach)

**Verantwoordelijkheden:**
- **Pedro**: Proactief identificeren van ontbrekende randvoorwaarden
- **Matthijs**: Faciliteren van toegang en permissies
- **Stakeholders**: Leveren van data en documentatie

---

## Checklist Randvoorwaarden

### Voor Start Development (Week 1-2):
- [ ] Laptop met Python 3.11+ development omgeving
- [ ] Git repository opgezet
- [ ] Cursor IDE geïnstalleerd
- [ ] Permissies Babcock/Schiphol verkregen
- [ ] Maximo test environment toegang verkregen
- [ ] MSG-3 voorbeeld bestanden ontvangen (minimaal 2)
- [ ] Stakeholder contacten gevestigd
- [ ] Werkplek geregeld (thuis/op locatie)

### Voor Maximo Integratie (Week 3-12):
- [ ] Maximo API documentatie beschikbaar
- [ ] API credentials ontvangen
- [ ] PM en JobPlan object schemas
- [ ] MSG-3 specificatie en business rules
- [ ] Test environment beschikbaar en stabiel

### Voor Testing & Deployment (Week 16-18):
- [ ] Test data voor end-to-end testing
- [ ] Stakeholders beschikbaar voor UAT
- [ ] Deployment environment geïdentificeerd
- [ ] Documentatie template/format afgestemd

---

*Datum: 4 februari 2026*  
*Auteur: Pedro Meijer*  
*Project: MSG-3 to Maximo Converter*  
*Status: Requirements identificatie compleet - Actie vereist Week 1-2*
