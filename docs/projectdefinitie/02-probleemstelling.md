# Probleemstelling

## 1. Huidige Situatie

Op dit moment wordt MSG-3 data **handmatig** verwerkt en ingevoerd in IBM Maximo. Dit proces verloopt als volgt:

### Huidige Workflow
1. **Ontvangst**: MSG-3 document wordt ontvangen (Excel formaat)
2. **Analyse**: Engineering team analyseert het document
3. **Extract**: Relevante informatie wordt handmatig geëxtraheerd
4. **Input**: Data wordt handmatig ingevoerd in Maximo
5. **Creatie**: PM records en JobPlans worden aangemaakt
6. **Verificatie**: Controle of alles correct is ingevoerd

### Geschatte Tijdsinvestering
- **Per MSG-3 document**: Circa 1 werkdag (8 uur)
- **Aantal documenten per jaar**: Variabel, afhankelijk van updates en nieuwe systemen
- **Totale tijdsinvestering**: Meerdere werkdagen per jaar

---

## 2. Pijnpunten

### 🕐 1. Tijdrovend Proces
**Probleem:**
- Handmatig doorlopen van MSG-3 documenten kost veel tijd
- Engineering team besteedt waardevolle uren aan administratieve taken
- Vertraging in implementatie van nieuwe onderhoudsprogramma's

**Impact:**
- Kostbare engineering tijd gaat naar data-entry in plaats van engineering werk
- Langere doorlooptijd bij MSG-3 updates
- Team kan zich niet volledig focussen op kerntaken

### ❌ 2. Foutgevoelig
**Probleem:**
- Handmatige invoer is inherent foutgevoelig
- Copy-paste fouten kunnen voorkomen
- Verkeerde interpretatie van MSG-3 data mogelijk
- Geen geautomatiseerde validatie

**Impact:**
- Incorrecte onderhoudsinstructies in Maximo
- Potentieel verkeerde onderhoudsfrequenties
- Extra tijd nodig voor correcties
- Risico op gemiste inspecties

### 📈 3. Niet Schaalbaar
**Probleem:**
- Bij elke MSG-3 update moet het hele proces opnieuw
- Toevoegen van nieuwe assets vereist volledige handmatige invoer
- Geen version control of change tracking
- Moeilijk om wijzigingen tussen versies te detecteren

**Impact:**
- Groeiende workload bij uitbreiding van het systeem
- Herhalend werk bij updates
- Onduidelijkheid over wat er precies veranderd is

### 📋 4. Gebrek aan Standaardisatie
**Probleem:**
- Proces is afhankelijk van individuele interpretatie
- Geen gestandaardiseerde mapping tussen MSG-3 en Maximo
- Knowledge is vastgelegd bij personen, niet in proces

**Impact:**
- Inconsistente data invoer
- Afhankelijkheid van specifieke medewerkers
- Moeilijke overdracht bij personeelswisselingen

---

## 3. Impact & Consequenties

### Operationeel
- **Vertraging** in maintenance planning bij MSG-3 updates
- **Verhoogd risico** op fouten in onderhoudsprogramma's
- **Hoge workload** voor engineering team

### Economisch
- **Kostbare tijd** van hoogopgeleide engineers besteed aan data-entry
- **Inefficiënt gebruik** van beschikbare resources
- **Opportunity cost**: engineers kunnen zich niet focussen op waardevoegend werk

### Kwaliteit
- **Risico op fouten** in kritische maintenance data
- **Geen consistente validatie** van ingevoerde data
- **Moeilijk traceerbaar** welke wijzigingen zijn doorgevoerd

### Strategisch
- **Belemmert schaalbaarheid** van operations
- **Beperkt flexibiliteit** bij wijzigingen
- **Verhoogt afhankelijkheid** van specifieke personen

---

## 4. Gewenste Situatie

### Ideale Workflow
Ideaal zou het proces als volgt verlopen:

1. **Upload**: MSG-3 Excel bestand wordt geüpload naar systeem
2. **Automatische Parsing**: Systeem leest en valideert MSG-3 data
3. **Change Detection**: Systeem detecteert wijzigingen t.o.v. vorige versie
4. **Mapping**: Data wordt automatisch gemapped naar Maximo structuur
5. **Validatie**: Automatische business rules validatie
6. **Import**: Data wordt geautomatiseerd naar Maximo gestuurd
7. **Rapportage**: Overzicht van geïmporteerde/gewijzigde records

### Voordelen Gewenste Situatie
- ⚡ **Snelheid**: Proces van uren/dagen naar minuten
- ✅ **Nauwkeurigheid**: Geautomatiseerde validatie voorkomt fouten
- 📈 **Schaalbaarheid**: Makkelijk om meerdere MSG-3 updates te verwerken
- 📊 **Traceerbaarheid**: Duidelijk overzicht van wijzigingen
- 👥 **Ontlasting**: Engineering team kan focussen op engineering

---

## 5. Probleemstelling Conclusie

**Het huidige handmatige proces van MSG-3 data naar Maximo is tijdrovend, foutgevoelig en niet schaalbaar. Dit leidt tot inefficiënt gebruik van engineering resources, verhoogd risico op fouten en vertraging in maintenance planning.**

**Dit project richt zich op het ontwikkelen van een geautomatiseerde tussenkoppeling die het proces stroomlijnt, fouten reduceert en waardevolle tijd bespaart.**

---

## 6. Succes Metrics

Het probleem is opgelost als:
- ✅ Tijd voor MSG-3 verwerking is gereduceerd met minimaal 80%
- ✅ Handmatige invoerfouten zijn geëlimineerd door validatie
- ✅ Engineering team rapporteert significante tijdsbesparing
- ✅ MSG-3 updates kunnen binnen uren verwerkt worden (i.p.v. dagen)
- ✅ Wijzigingen tussen versies zijn automatisch traceerbaar

---

*Datum: 4 februari 2026*  
*Auteur: Pedro Eduardo Cardoso*  
*Project: MSG-3 to Maximo Converter*

---

## AI Authenticiteitsverklaring

Voor het verfijnen van teksten in de projectdefinitie heb ik **Cursor AI** gebruikt om te **verbeteren van formulering en professionele schrijfstijl**. Na het gebruik van deze tool heb ik de uitkomsten ervan uitvoerig gecontroleerd en aangepast om er voor te zorgen dat het ingeleverde werk mijn eigen competenties en leeruitkomsten reflecteert. Ik draag de volledige verantwoordelijkheid voor de inhoud van dit werk.

*AIAS Niveau: 3 - AI Samenwerking*
