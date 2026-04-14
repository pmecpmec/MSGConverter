# Scope

## In scope

**Functioneel.** MSG-3 Excel inlezen (origineel en herontworpen formaat), valideren volgens structuur en business rules, wijzigingen tussen versies detecteren, data mappen naar Maximo PM en JobPlan, en via de REST API naar Maximo sturen (create, read, update; geen delete). Daarnaast het herontwerpen van het MSG-3 Excel-template voor betere verwerking en documentatie: technisch, gebruikershandleiding en installatie.

**Technisch.** Python 3.11+, modulaire opzet, command-line interface, logging en foutafhandeling, unit- en integratietests (minimaal 80% coverage). Afhankelijkheden: openpyxl/pandas voor Excel, requests voor de API, pydantic voor validatie, pytest voor tests.

## Buiten scope

Geen automatische planning van onderhoud (dat doet Maximo). Geen migratie van historische data; alleen nieuwe en gewijzigde data. Geen webapplicatie of grafische interface; de primaire interface is de command line. Geen koppeling met andere systemen dan Maximo. Geen real-time synchronisatie; verwerking on demand of in batch. Geen aanpassingen aan het Maximo-datamodel; we gebruiken de standaard API. Geen mobiele app. Geen automatische delete in Maximo.

Mogelijke vervolgstappen later: webinterface, e-mailnotificaties, extra rapportage. Die horen niet bij dit project.

## Aannames

De Maximo REST API is beschikbaar; we krijgen toegang tot een testomgeving en credentials. Het MSG-3 Excel-formaat is valide en relatief consistent. De business rules en verplichte velden zijn bekend. Stakeholders zijn beschikbaar voor feedback; voorbeelddata is beschikbaar voor ontwikkeling en test.

## Afhankelijkheden

Toegang tot de Maximo-testomgeving, MSG-3 voorbeeldbestanden, wekelijkse beschikbaarheid van de Babcock-stakeholders (Matthijs, Rick, Roy) en een Python-ontwikkelomgeving. Goedkeuring van IT voor API-toegang en van stakeholders voor het Excel-herontwerp.

Datum: 4 februari 2026  
Auteur: Pedro Eduardo Cardoso  
Project: MSG-3 to Maximo Converter

## Authenticiteitsverklaring AI-gebruik

Voor het verfijnen van teksten in de projectdefinitie heb ik Cursor AI gebruikt om formulering en schrijfstijl te verbeteren. Ik heb de uitkomsten gecontroleerd en aangepast. Ik draag de volledige verantwoordelijkheid voor de inhoud. AIAS Niveau: 3 – AI Samenwerking.
