# Doelstellingen

## Hoofddoel

Het project heeft tot doel de MSG-3 naar Maximo datakoppeling te automatiseren: tijd besparen, fouten terugdringen en het engineering team ontlasten.

## Subdoelen (SMART)

**1. MSG-3 parser.** Een parser bouwen die MSG-3 Excel inleest, valideert en omzet naar gestructureerde data (bijv. JSON). Specifiek: inlezen, valideren, foutafhandeling. Meetbaar: het grootste deel van de taken correct geparseerd, verwerking binnen enkele seconden per bestand. Haalbaar met Python en openpyxl/pandas. Deadline volgens planning (zie plan van aanpak).

**2. Change detection.** Wijzigingen tussen MSG-3-versies detecteren (toegevoegd, gewijzigd, verwijderd) en rapporteren. Nodig voor incrementele updates in Maximo. Deadline volgens planning.

**3. Maximo-integratie.** MSG-3-data via de REST API naar Maximo sturen, met correcte mapping naar PM en JobPlan. Inclusief authenticatie, foutafhandeling en retry. Succes betekent dat PM- en JobPlan-records correct in Maximo staan na import.

**4. MSG-3 Excel-herontwerp.** Het Excel-template zo herontwerpen dat het beter machine-leesbaar is en eenvoudiger te verwerken. Template documenteren en met stakeholders valideren.

**5. Documentatie en overdracht.** Technische documentatie, gebruikershandleiding en installatie-instructies. Het systeem moet door anderen te gebruiken en te onderhouden zijn. Overdrachtsessie met Babcock.

## Tijdgebonden, mijlpalen en acceptatiecriteria (eerste fase)

Onderstaande afbeelding toont de volledige stagetijdlijn (18 weken), alle mijlpalen en de acceptatiecriteria per fase.

![Stagetijdlijn – Mijlpalen en Acceptatiecriteria](../../milestones.png)

**Tijdgebonden**

- Deadline eerste fase: week 5–7 van het project (parser en validator). Mijlpaal week 7: MSG-3 Excel kan worden ingelezen en gevalideerd; demo aan stakeholders.

**Mijlpalen (eerste fase, week 5–7)**

- Week 5: Excel-parser basis; MSG-3 Excel inlezen en omzetten naar gestructureerde data (bijv. JSON).
- Week 6: Validator en business rules; schema-validatie en foutrapportage; error handling.
- Week 7: Afronding parser en validator; unit tests, documentatie en demo. Oplevering eerste werkbare oplevering.

**Acceptatiecriteria (eerste fase)**

- MSG-3 Excel kan worden ingelezen.
- Data wordt geconverteerd naar gestructureerd formaat (bijv. JSON).
- Schema-validatie werkt correct (inclusief relevante business rules).
- Unit tests met 90%+ coverage voor parser en validator.
- Documentatie (gebruik, installatie) is beschikbaar.

De volledige planning en alle mijlpalen staan in het plan van aanpak (docs/plan-van-aanpak/02-planning.md).

## Wanneer is het project geslaagd?

Het project is geslaagd als MSG-3 Excel correct wordt geparseerd, wijzigingen worden gedetecteerd, data succesvol naar Maximo gaat, PM en JobPlan correct worden aangemaakt, het herontworpen template is getest en goedgekeurd, documentatie en overdracht zijn afgerond en het systeem in de testomgeving operationeel is. De exacte planning staat in het plan van aanpak.

Datum: 4 februari 2026  
Auteur: Pedro Eduardo Cardoso  
Project: MSG-3 to Maximo Converter

## Authenticiteitsverklaring AI-gebruik

Voor het verfijnen van teksten in de projectdefinitie heb ik Cursor AI gebruikt om formulering en schrijfstijl te verbeteren. Ik heb de uitkomsten gecontroleerd en aangepast. Ik draag de volledige verantwoordelijkheid voor de inhoud. AIAS Niveau: 3 – AI Samenwerking.
