# 🚀 START HIER - Projectdefinitie

**Welkom Pedro!**

Dit is de start van je Comakership documentatie. Dit document helpt je om de projectdefinitie stap voor stap uit te werken.

---

## 📝 Wat moet er in de Projectdefinitie?

De projectdefinitie legt de basis voor je hele project. Het geeft antwoord op:
- **Waarom** doe je dit project? (Context, probleem)
Ik doe dit project omdat dit mijn stageopdracht is, binnen babcock word er veel handmatig gedaan met excel documenten en dat kost veel tijd. Om tijd te besparen heb ik samen met Matthijs Meijer en Rick Kramer bedacht dat ik dus een tussenkoppeling maak om 
- **Wat** ga je precies doen? (Doelstellingen, scope)
Uitzoeken wat ik precies moet doen en met wat voor MSG-3 Documenten en wat er in staat
daarnaast ga ik kijken hoe lang ik er over doe.
- **Voor wie** doe je het? (Stakeholders)
De stakeholders zijn denk ik het bedrijf babcock, matthijs en rick, en het projecten team die vooral werkt met msg-3 documenten. en natuurlijk voor school of mijn docenten
---

## 📋 Documenten om te Maken

### 1. Context Analyse (`01-context-analyse.md`)

**Doel:** Leg uit in welke context dit project plaatsvindt.

**Vragen om te beantwoorden:**
- Wat doet Babcock Schiphol?
Babcock schiphol heeft de helft van het bagagesysteem in controle, ze zorgen ervoor dat het systeem zo vaak mogelijk foutloos blijft draaien en als er problemen zijn proberen hun er zo snel mogelijk bij te zijn.

- Wat is MSG-3 en waarom is het belangrijk?
het msg-3 document is belangrijk want daar staat veel informatie in zoals:
object codes, routes die gelopen worden tijdens inspecties, configuraties - msi's (route + motivatie bij vragen 1 t/m 4)
- Wat is IBM Maximo en hoe wordt het gebruikt?
IBM Maximo is een systeem die door veel bedrijven wordt gebruikt
hierin worden werkbonnen/inspecties bijgehouden ook word er veel andere soort data in opgeslagen zoals items in het magazijn. Inspecties worden duidelijk opgeschreven met veel informatie en ook als er dingen mis gaan in het systeem kan dat ook vermeld worden in maximo. als voorbeeld Loop inspectie bij band 1, check de motor, check de rollerband, check voor geluiden etc. als de inspectie is gelopen word daarna de inspectie ingevuld door de monteurs met evt fouten of dat het juist helemaal goed is. Er zijn super veel inspecties en daarom word het dus ook bijgehouden en wat voor materialen er bij zijn gebruikt welke supervisor en welk team er aan het werk is en ook word er duidelijk geschreven wat er gedaan is aan bepaalde situaties

- Wat is de huidige situatie?
(Ik weet niet wat er word bedoeld met deze vraag dus stel m opnieuw aan mij met extra uitleg)
**Template:**
```markdown
# Context Analyse - Babcock Schiphol

## Organisatie
Babcock is...

## MSG-3 in de Luchtvaart
MSG-3 (Maintenance Steering Group - 3) is...

## IBM Maximo bij Babcock
Maximo wordt gebruikt voor...

## Huidige Situatie
Op dit moment wordt MSG-3 data...
```

---

### 2. Probleemstelling (`02-probleemstelling.md`)

**Doel:** Beschrijf het probleem dat je gaat oplossen.
Het doel van de tussenkoppeling creeeren van msg-3 en maximo is dat er super veel tijd word bespaard, er word ervoor gezorgd dat het msg-3 automatisch word overgelezen en ingevuld in maximo door 1 druk op de knop (zo gezegd)

**Vragen om te beantwoorden:**
- Wat gaat er nu mis/inefficiënt?
MSG-3 documenten moeten vaak handmatig ingevuld worden en dat kost veel tijd.

- Hoeveel tijd kost het huidige proces?
(gok 1 dag)
- Wat zijn de pijnpunten?
Het handmatig invullen en veel verloren tijd.
- Wat zijn de gevolgen van het probleem?
Veel kostbare tijd verloren door het handmatig invullen
**Template:**
```markdown
# Probleemstelling

## Huidige Situatie
Op dit moment wordt MSG-3 data handmatig...

## Pijnpunten
1. **Tijdrovend**: Het duurt X uur om...
2. **Foutgevoelig**: Handmatige invoer leidt tot...
3. **Niet schaalbaar**: Bij updates moet...

## Impact
Dit heeft de volgende gevolgen:
- Vertraging in maintenance planning
- Verhoogd risico op fouten
- Hoge workload voor engineering team

## Gewenste Situatie
Ideaal zou het proces...
```

---

### 3. Doelstellingen (`03-doelstellingen.md`)

**Doel:** Formuleer SMART doelen voor je project.

**SMART criteria:**
- **S**pecifiek: Wat ga je precies maken? Een tussenkoppeling voor MSG-3 en Maximo
- **M**eetbaar: Hoe meet je succes? Als ik succesvol een msg-3 automatisch kan implementeren in maximo
- **A**cceptabel: Is het realistisch? Ja
- **R**elevant: Draagt het bij aan het doel? Ja het doel is dat er uiteindelijk veel tijd word bespaard door deze tussenkoppeling
- **T**ijdgebonden: Wanneer moet het klaar zijn? Het lieft zo snel mogelijk maar de echte eindtijd zou het einde van mijn stage zijn

**Template:**
```markdown
# Doelstellingen

## Hoofddoel
Automatiseren van de MSG-3 → Maximo datakoppeling.

## Subdoelen (SMART)

### 1. MSG-3 Parser
**Doel:** Een parser bouwen die MSG-3 Excel kan inlezen en valideren.

- **Specifiek**: Parser kan Excel lezen, converteren naar JSON, en valideren
- **Meetbaar**: 95% van taken correct geparseerd, <5 seconden per bestand
- **Acceptabel**: Haalbaar met openpyxl/pandas in Python
- **Relevant**: Noodzakelijk voor automatische verwerking
- **Tijdgebonden**: Week 1-2 (14 februari 2026)

### 2. Change Detection
**Doel:** Wijzigingen tussen MSG-3 versies automatisch detecteren.

[Vul aan met SMART criteria]

### 3. Maximo Integratie
**Doel:** Data automatisch naar Maximo uploaden via REST API.

[Vul aan met SMART criteria]

### 4. MSG-3 Redesign
**Doel:** MSG-3 Excel herontwerpen voor automatische verwerking.

[Vul aan met SMART criteria]

## Acceptatiecriteria
Het project is geslaagd als:
- [ ] MSG-3 Excel wordt correct geparseerd
- [ ] Wijzigingen worden gedetecteerd
- [ ] Data wordt succesvol naar Maximo gestuurd
- [ ] Herontworpen Excel is getest en goedgekeurd
- [ ] Proces is gedocumenteerd en overdraagbaar
```

---

### 4. Scope (`04-scope.md`)

**Doel:** Definieer wat WEL en NIET in scope is.

**Waarom belangrijk:**
### Functioneel
- MSG-3 Excel parsing (original + redesign format)
- Data validatie (structuur + business rules)
- Change detection (added/modified/deleted tasks)
- Mapping naar Maximo PM en JobPlan objecten
- Maximo REST API integratie
- MSG-3 Excel redesign en template
- Documentatie (technisch + gebruikershandleiding)

### Technisch
- Python 3.11+ applicatie
- Command-line interface
- Logging en error handling
- Unit en integration tests


**Template:**
```markdown
# Scope

## ✅ In Scope

### Functioneel
- MSG-3 Excel parsing (original + redesign format)
- Data validatie (structuur + business rules)
- Change detection (added/modified/deleted tasks)
- Mapping naar Maximo PM en JobPlan objecten
- Maximo REST API integratie
- MSG-3 Excel redesign en template
- Documentatie (technisch + gebruikershandleiding)

### Technisch
- Python 3.11+ applicatie
- Command-line interface
- Logging en error handling
- Unit en integration tests

## ❌ Out of Scope

### Functioneel
- Automatische scheduling (dit doet Maximo zelf)
- Historische data migratie (alleen nieuwe/gewijzigde data)
- User interface / web applicatie (alleen CLI)
- Integratie met andere systemen dan Maximo

### Technisch
- Maximo customizatie (werkt met standaard API)
- Real-time synchronisatie (batch processing)
- Multi-tenant support
- Mobile app

## 🔮 Future Enhancements (Nice to Have)
- Web interface voor niet-technische gebruikers
- Real-time monitoring dashboard
- Automatische email notificaties
- Integratie met andere data bronnen

## ⚠️ Assumptions (Aannames)
- Maximo REST API is beschikbaar en toegankelijk
- MSG-3 Excel bevat valide ATA MSG-3 data
- Babcock heeft test omgeving beschikbaar
- Bestaande Maximo datamodel is voldoende (geen custom fields nodig)

## 🔗 Dependencies (Afhankelijkheden)
- Toegang tot Maximo test environment
- MSG-3 voorbeeld data
- Babcock stakeholder beschikbaar voor feedback
- Python development omgeving
```

---

### 5. Stakeholders (`05-stakeholders.md`)

**Doel:** 

Pedro (Student)
- **Rol**: Developer, projecteigenaar
- **Belang**: Succesvol afronden Comakership
- **Betrokkenheid**: Dagelijks, volledige betrokkenheid
- **Verwachtingen**: Leren, deliveren, goed cijfer
Matthijs Meijer (sr. maintanance engineer)(Zelfde verwachting als rick en roy)
Rick Kramer (Maintanace Service Coordinator)
Roy Minkels (Maintance Engineer)
Arie Ismaiel(Docent)
Dat het product goed is
Dat student stage goed doet
documentatie bijhouden
etc.

**Template:**
```markdown
# Stakeholders

## Primaire Stakeholders

### Pedro (Student)
- **Rol**: Developer, projecteigenaar
- **Belang**: Succesvol afronden Comakership
- **Betrokkenheid**: Dagelijks, volledige betrokkenheid
- **Verwachtingen**: Leren, deliveren, goed cijfer

### Babcock Schiphol Engineering Team
- **Rol**: Opdrachtgever, eindgebruiker
- **Belang**: Efficiënter MSG-3 proces
- **Betrokkenheid**: Wekelijks overleg, feedback
- **Verwachtingen**: Werkend systeem, overdracht documentatie

### Windesheim Begeleider
- **Rol**: Academic supervisor
- **Belang**: Leerproces, competentie ontwikkeling
- **Betrokkenheid**: Tweewekelijks overleg
- **Verwachtingen**: Goede documentatie, reflectie

## Secundaire Stakeholders

### Babcock IT
- **Rol**: Infrastructure, Maximo beheer
- **Belang**: Systeem stabiliteit, security
- **Betrokkenheid**: Op afroep
- **Verwachtingen**: Geen productie impact, security compliance

### Maintenance Planners
- **Rol**: Indirect gebruiker (via Maximo)
- **Belang**: Accurate maintenance data
- **Betrokkenheid**: Minimaal
- **Verwachtingen**: Data quality, geen disruption

## Stakeholder Communicatie

| Stakeholder | Frequentie | Medium | Onderwerpen |
|-------------|------------|--------|-------------|
| Engineering Team | Wekelijks | Meeting | Progress, feedback, requirements |
| Windesheim | Tweewekelijks | Meeting | Leerproces, competenties, documentatie |
| IT | On-demand | Email/Teams | Technical issues, access, deployment |

## Verwachtingen Management
- **Engineering Team**: Wekelijkse demo's, transparante communicatie
- **Windesheim**: Documentatie bijhouden, reflectie delen
- **Jezelf**: Realistische planning, vragen stellen, hulp vragen
```

---

## ✅ Checklist

- [ ] `01-context-analyse.md` geschreven
- [ ] `02-probleemstelling.md` geschreven
- [ ] `03-doelstellingen.md` geschreven (met SMART criteria)
- [ ] `04-scope.md` geschreven (in/out of scope)
- [ ] `05-stakeholders.md` geschreven
- [ ] Alle documenten reviewed
- [ ] Feedback van begeleider verwerkt

---

## 💡 Tips

### Gebruik Cursor AI
Cursor kan je helpen met het schrijven van deze documenten:

```
"Schrijf een context analyse voor Babcock Schiphol, een luchtvaart 
maintenance organisatie die MSG-3 data gebruikt met IBM Maximo"

"Formuleer SMART doelen voor het bouwen van een MSG-3 Excel parser"

"Maak een stakeholder analyse voor mijn Comakership project"
```

### Vraag Feedback
- Laat documenten reviewen door begeleider
- Bespreek met Babcock stakeholders
- Itereer op basis van feedback

### Wees Specifiek
- Gebruik concrete voorbeelden
- Geef cijfers waar mogelijk
- Verwijs naar bronnen (ATA MSG-3 spec, Maximo docs)

---

## 📚 Nuttige Bronnen

- [ATA MSG-3 Specification](https://www.ata.org/) (indien beschikbaar)
- [IBM Maximo Documentation](https://www.ibm.com/docs/en/mam)
- [Babcock Internal Documentation](verwijs naar interne docs)

---

**Je kunt dit! Veel succes met de projectdefinitie! 🚀**

*Volgende stap na projectdefinitie: Plan van Aanpak in `/docs/plan-van-aanpak/`*
