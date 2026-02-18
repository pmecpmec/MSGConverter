# Context Analyse - Babcock Schiphol

## 1. Organisatie

### Babcock Schiphol
Babcock Schiphol is verantwoordelijk voor het onderhoud en beheer van de helft van het bagagesysteem op Schiphol. De organisatie zorgt ervoor dat het bagagesysteem zo vaak mogelijk foutloos blijft draaien. Wanneer er problemen ontstaan, is het team van Babcock verantwoordelijk voor snelle respons en herstel om de operationele continuïteit te waarborgen.

**Kerntaken:**
- Onderhoud en beheer van bagagesysteem infrastructuur
- Preventief en correctief onderhoud
- Probleemoplossing en incident response
- Maintenance planning en engineering

---

## 2. MSG-3 in de Luchtvaart

### Wat is MSG-3?
MSG-3 (Maintenance Steering Group - 3) is een gestandaardiseerde methodologie voor het ontwikkelen van onderhoudsprogramma's in de luchtvaart- en gerelateerde industrie. Het MSG-3 document bevat essentiële informatie voor het onderhoud van complexe systemen.

### Inhoud MSG-3 Document
Het MSG-3 document bevat:
- **Object codes**: Unieke identificatie van componenten en systemen
- **Routes**: Vastgelegde inspectieroutes die tijdens onderhoud gelopen worden
- **Configuraties**: Specifieke instellingen en parameters van systemen
- **MSI's (Maintenance Significant Items)**: Combinatie van route en motivatie bij 4 kernvragen:
  1. Veiligheid (Safety)
  2. Operationele impact (Operational)
  3. Economische impact (Economic)
  4. Hidden failures (verborgen storingen)

### Waarom is MSG-3 belangrijk?
MSG-3 vormt de basis voor alle onderhoudsactiviteiten bij Babcock. Het document bepaalt:
- Welke inspecties uitgevoerd moeten worden
- Met welke frequentie onderhoud plaatsvindt
- Welke procedures gevolgd moeten worden
- Welke materialen en resources nodig zijn

---

## 3. IBM Maximo bij Babcock

### Wat is IBM Maximo?
IBM Maximo is een Enterprise Asset Management (EAM) systeem dat door veel bedrijven wereldwijd wordt gebruikt voor het beheren van assets, onderhoud en voorraad.

### Gebruik bij Babcock
Bij Babcock wordt Maximo gebruikt voor:

**Werkbonnen & Inspecties:**
- Registratie van alle onderhoudsactiviteiten
- Gedetailleerde beschrijving van uit te voeren werkzaamheden
- Voorbeeld: "Loop inspectie bij band 1: check de motor, check de rollerband, check voor geluiden, etc."

**Administratie:**
- Bijhouden welke inspecties gelopen zijn
- Registratie van bevindingen en afwijkingen
- Vastleggen van gebruikte materialen
- Toewijzing van supervisors en teams
- Documentatie van uitgevoerde werkzaamheden

**Magazijnbeheer:**
- Voorraad tracking
- Materiaalverbruik
- Spare parts management

**Rapportage:**
- Na elke inspectie wordt het resultaat ingevuld door monteurs
- Eventuele fouten of afwijkingen worden gedocumenteerd
- Normale situaties worden eveneens geregistreerd

Door het grote aantal inspecties is systematische registratie in Maximo cruciaal voor:
- Traceerbaarheid
- Compliance
- Planning
- Resource management

---

## 4. Huidige Situatie

### Huidig Proces
Op dit moment verloopt de verwerking van MSG-3 data naar Maximo via een **handmatig proces**:

1. MSG-3 documenten worden ontvangen (vaak in Excel formaat)
2. Engineering team leest het MSG-3 document door
3. Relevante informatie wordt handmatig overgenomen
4. Data wordt handmatig ingevoerd in Maximo
5. PM (Preventive Maintenance) records en JobPlans worden aangemaakt

### Problematiek
Dit handmatige proces:
- **Neemt veel tijd in beslag** (geschat: ongeveer 1 dag per document)
- **Is foutgevoelig** door handmatige invoer
- **Schaalt niet goed** bij updates of nieuwe MSG-3 versies
- **Bindt waardevolle resources** van het engineering team
- **Vertraagt** de implementatie van onderhoudsprogramma's

### Behoefte aan Automatisering
Er is een duidelijke behoefte aan automatisering om:
- Tijd te besparen
- Fouten te reduceren
- Het engineering team te ontlasten
- Snellere implementatie van MSG-3 updates mogelijk te maken

---

## 5. Conclusie

De combinatie van MSG-3 als industrie standaard en Maximo als asset management systeem is essentieel voor Babcock's operatie. Het huidige handmatige proces vormt echter een bottleneck in efficiency en schaalbaarheid. 

Dit project richt zich op het automatiseren van de datakoppeling tussen MSG-3 en Maximo, wat direct bijdraagt aan de operationele effectiviteit van Babcock Schiphol.

---

*Datum: 4 februari 2026*  
*Auteur: Pedro Eduardo Cardoso*  
*Project: MSG-3 to Maximo Converter*

---

## AI Authenticiteitsverklaring

Voor het verfijnen van teksten in de projectdefinitie heb ik **Cursor AI** gebruikt om te **verbeteren van formulering en professionele schrijfstijl**. Na het gebruik van deze tool heb ik de uitkomsten ervan uitvoerig gecontroleerd en aangepast om er voor te zorgen dat het ingeleverde werk mijn eigen competenties en leeruitkomsten reflecteert. Ik draag de volledige verantwoordelijkheid voor de inhoud van dit werk.

*AIAS Niveau: 3 - AI Samenwerking*
