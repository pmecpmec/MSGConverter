# Onderzoeksrapport

**Project:** MSG-3 to Maximo Converter
**Organisatie:** Babcock Schiphol
**Auteur:** Pedro Eduardo Cardoso
**Opleiding:** Associate Degree Software Developer (ADSD), Windesheim
**Datum:** 18 februari 2026
**Status:** Uitgewerkt, week 3–4 (18 feb – 3 mrt 2026)

## Hoofdvraag

**Is een geautomatiseerde koppeling van MSG-3 Excel naar Maximo technisch haalbaar voor Babcock Schiphol?**

Dit rapport beantwoordt deze hoofdvraag aan de hand van drie deelvragen en de uitwerking daarvan in de onderstaande secties.

## Deelvragen

1. Hoe is het MSG-3 Excel-formaat opgebouwd en welke gegevens zijn nodig voor de koppeling naar Maximo?
2. Welke mogelijkheden en beperkingen biedt de Maximo REST API voor PM en JobPlan?
3. Welke aanpak en technologieën zijn het meest geschikt om MSG-3 data te parsen en naar Maximo te sturen?

## Inleiding

Dit onderzoeksrapport hoort bij de execution phase van het Comakership en de OnStage-inlevertaak "Onderzoeksdocumenten". Het volledige onderzoek (MSG-3-structuur, Maximo API, technologiekeuzes en POC’s). Het beschrijft het technisch en functioneel onderzoek naar de MSG-3 Excel-structuur, de Maximo API, de gekozen technologieën en alternatieven, en de conclusies voor haalbaarheid van de MSG-3 naar Maximo-koppeling. De hoofdvraag en deelvragen sluiten aan op het Plan van Aanpak (hoofdstuk 4).

## Uitwerking per deelvraag

1. **MSG-3 Excel structuur.** Hoe is het huidige MSG-3 Excel-formaat opgebouwd (sheets, kolommen, relaties) en welke varianten/edge cases bestaan er?
 **Antwoord:** Het bestand bevat 10 sheets (Inhoudsopgave, Versiebeheer, Object codes, Routes, Configuratie–MSI's, Dienstenboom, **Onderhoudstaken**, Totale uren, MSG3 Diagrammen, Diverse gegevens). Sheet 7 (Onderhoudstaken) is het kernsheet voor de Maximo-koppeling. Volledige kolomindeling per sheet staat in sectie 1.2.

2. **Maximo API.** Welke REST API-mogelijkheden biedt Maximo voor PM, JobPlan en gerelateerde objecten, en wat zijn de beperkingen?
 **Antwoord:** Maximo biedt een REST/OSLC-API voor o.a. Item, PM en JobPlan (CRUD, Basic/API key auth). Beperkingen: ITEMNUM immutable, OBSOLETE onomkeerbaar, geen echte delete. Zie sectie 2.

3. **Technologiekeuzes.** Welke Python-bibliotheken (openpyxl, pandas, xlrd, etc.) zijn het meest geschikt voor parsing en validatie, en waarom?
 **Antwoord:** openpyxl (.xlsx/.xlsm), pandas (bulk), pydantic (validatie), requests (Maximo API). Onderbouwing in sectie 3.

4. **Alternatieven.** Welke alternatieve aanpakken (bijv. MIF, MEA, handmatige import) zijn overwogen en waarom is gekozen voor de gekozen oplossing?
 **Antwoord:** Handmatige import, MIF en MEA overwogen; gekozen voor eigen Python-REST-koppeling (beheersbaarheid, compliance, schaalbaarheid). Zie sectie 4.

5. **Proof of Concept.** Wat zijn de resultaten van de POC’s (Excel-parsing, Maximo-connectie) en wat is de conclusie m.b.t. haalbaarheid?
 **Antwoord:** Parser- en connector-opzet staan; afronding vereist implementatie met echt bestand en live Maximo POC. Conclusie: technisch haalbaar. Zie sectie 5.

## 1. MSG-3 Excel structuur

### 1.1 Bron en context

MSG-3 (Maintenance Steering Group - 3) is de gestandaardiseerde methodologie voor onderhoudsprogramma’s in de luchtvaart. Bij Babcock wordt de MSG-3-inhoud beheerd in Excel: object codes, routes, configuraties en MSI’s (Maintenance Significant Items). Het onderzoek richt zich op de opbouw van deze Excel-bestanden om een betrouwbare parser te kunnen ontwerpen.

### 1.2 Structuur huidige MSG-3 bestanden

Uit de projectdefinitie en het technisch ontwerp volgt dat het MSG-3 document onder meer bevat:

- **Object codes:** unieke identificatie van componenten en systemen
- **Routes:** inspectieroutes die tijdens onderhoud gelopen worden
- **Configuraties:** instellingen en parameters van systemen
- **MSI’s**: Combinatie van route en motivatie (safety, operational, economic, hidden failures)

Voor de koppeling naar Maximo is de datamodel-vertaling vastgelegd in een **taak-georiënteerd model**: elke onderhoudstaak heeft onder andere een taakcode, beschrijving, taaktype (INS, LUB, etc.), interval en eenheid (FH, FC, MO), zone, ATA-hoofdstuk, man-uren en vaardigheden. Dit sluit aan op Maximo-objecten PM (Preventive Maintenance) en JobPlan.

**Concrete sheetindeling (op basis van msg3_original.xlsm):**

| Sheet | Naam | Inhoud (hoofdkolommen / onderwerpen) |
|-------|------|--------------------------------------|
| 1 | Inhoudsopgave | Versiebeheer, legenda, systeemdecompositie, configuratie en MSI's, routes, objectcodes, onderhoudstaken, overzicht totale uren, jaarplan onderhoud |
| 2 | Versiebeheer | Versie-informatie |
| 3 | Object codes | Afkorting, omschrijving, opmerking, aantal MSI-lijst |
| 4 | Routes | Area, Routenaam, Routevolgorde, Naam, Markcode, Manuren (dagen in/uit bedrijf), Personen per route |
| 5 | Configuratie – MSI's | Dienstenboom-niveau, area, naam, AAS-code, vragen 1 t/m 4 (bijv. "Could failure be undetectable…?"), MSI?, Motivatie |
| 6 | Dienstenboom | Dienstenboom-structuur |
| 7 | **Onderhoudstaken** | AAS objectcode, AAS-omschrijving, functie, storing, effect, oorzaak, MSG-3 logic categorie, uitvoerder, taak tijden inspectie, taaktype, taakomschrijving, criterium, type onderhoud, **interval**, **intervaleenheid**, opmerking, bedrijfs-toestand, tijdens operatie, aantal minuten pp, aantal man, mtbf, voorbereidingstaak, discipline (E/W), Werkinstructie, Agenda |
| 8 | Totale uren | Aantal per object, in/uit bedrijf (per dag/week), totaal per area (dagelijkse/jaar/wekelijkse/4- en 13-wekelijkse taken) |
| 9 | MSG3 Diagrammen | Diagrammen (optioneel voor parser) |
| 10 | Diverse gegevens | Hoofdgroep (communicatie, voeding, veiligheid, e.d.), Groep, Subgroep, definities taaktype, area en omschrijving |

Sheet 7 (Onderhoudstaken) is het **kernsheet** voor de Maximo-koppeling: daar staan taakcode, taaktype, interval, intervaleenheid, taakomschrijving en man-uren die naar PM/JobPlan gemapt worden.

De parser ondersteunt twee varianten: *original* (bovenstaand formaat) en *redesign* (toekomstig). Validatie van kolomposities en headerrij tegen het actuele bestand blijft nodig vóór definitieve implementatie.

### 1.3 Varianten en implicaties

- **Bestandsformaten:** .xlsx (openpyxl) en indien nodig .xls (xlrd); .xlsm wordt als .xlsx benaderd (macros niet nodig voor data-extractie).
- **Headerpositie:** Headers staan niet altijd op rij 1; de parser voorziet in `find_header_row` op basis van verwachte kolomnamen.
- **Implicaties voor parser en validatie:** Eenduidige mapping van kolommen naar het interne taakmodel (o.a. `MSG3Task`) en aansluiting op de 80 business rules uit het technisch ontwerp (zie `docs/technisch-ontwerp/business-rules.md` en `BUSINESS-RULES-FIRST.md`).

## 2. Maximo API

### 2.1 Beschikbare endpoints en objecten

IBM Maximo biedt een **REST API** (o.a. OSLC-stijl) voor integratie. Voor de MSG-3 → Maximo-koppeling zijn de volgende objecten relevant:

- **Item (Item Master):** technische items/onderdelen; ITEMNUM is **immutable** (na creatie niet wijzigen).
- **PM (Preventive Maintenance):** preventieve onderhoudsregels; koppeling naar JobPlans.
- **JobPlan:** stappen/werkorders; bevat o.a. beschrijving, duur, vereiste vaardigheden.

De gedetailleerde veldspecificaties (verplichte velden, lengtes, domeinen) staan in `docs/technisch-ontwerp/maximo-specificaties.md` (o.a. gebaseerd op maximosecrets.com). De mapping MSG-3 → PM en JobPlan is uitgewerkt in de codebase (`src/mapping/`) en in `MAXIMO-QUICK-REFERENCE.md`.

### 2.2 Authenticatie en rate limits

- **Authenticatie:** Basic Auth of API key (afhankelijk van Maximo-versie en Babcock-configuratie). Credentials via omgevingsvariabelen (`.env`), niet in code.
- **Rate limits:** Afhankelijk van de Maximo-omgeving; bij bulk-import moet batching en eventueel throttling toegepast worden om time-outs en weigeringen te voorkomen.

### 2.3 Beperkingen en aanbevelingen

- **ITEMNUM:** Nooit wijzigen na aanmaak; bij fouten moet een nieuw item aangemaakt worden of moet de bron (MSG-3) gecorrigeerd worden.
- **OBSOLETE:** Markering als obsolete is in de praktijk onomkeerbaar; alleen zetten na bevestiging.
- **Geen echte delete:** Objecten worden doorgaans inactief of obsolete gezet in plaats van fysiek verwijderd.
- **Aanbeveling:** Wijzigingsdetectie (change detection) in de converter gebruiken zodat alleen gewijzigde/nieuwe records naar Maximo gaan; dit beperkt API-calls en risico op conflicten.

## 3. Technologiekeuzes

### 3.1 Vergelijking parsing-bibliotheken

| Bibliotheek | Gebruik | Sterke punten | Beperkingen |
|---------------|--------------------|-----------------------------------|--------------------------|
| **openpyxl** | .xlsx / .xlsm | Cell-level toegang, formules, geen Excel nodig | Geen .xls; geheugengebruik bij zeer grote bestanden |
| **pandas** | read_excel, bulk | Snel voor tabellen, data-analyse | Legt .xls vaak op xlrd; minder geschikt voor vrije layout |
| **xlrd** | .xls (legacy) | Ondersteuning oude formaten | Alleen lezen; .xlsx niet ondersteund |

### 3.2 Gekozen stack en onderbouwing

- **openpyxl (3.1.2)**: Primaire keuze voor het lezen van MSG-3 Excel: ondersteunt .xlsx/.xlsm, vaste versie voor reproduceerbaarheid. Gebruikt voor sheetlijst, header-detectie en cell ranges (`ExcelReader`, `MSG3Parser`).
- **pandas (2.2.0)**: Voor bulk-verwerking van tabellen zodra de dataregio bekend is; sluit aan op bestaande data-analyse en transformaties.
- **xlrd (2.0.1)**: Alleen indien er daadwerkelijk .xls-bestanden moeten worden ondersteund; anders optioneel.
- **pydantic (2.6.1)**: Validatie van het interne datamodel (o.a. MSG3Task) en aansluiting op de business rules.
- **requests (2.31.0)**: HTTP-client voor de Maximo REST API; eenvoudig en voldoende voor synchrone calls.

Python 3.11+ is de doelversie (type hints, performance, onderhoud).

### 3.3 Risico’s en mitigerende maatregelen

- **Excel-layout wijzigt:** Versie-detectie (original vs redesign) en configuratie van kolommapping (bijv. YAML/JSON) zodat aanpassingen zonder code-wijziging kunnen.
- **Grote bestanden:** Streaming of chunked lezen overwegen; eerst valideren met representatieve bestanden bij Babcock.
- **Maximo API-versie:** Afstemmen met beheer (Babcock) over endpoint-URL’s en auth; POC in testomgeving uitvoeren vóór productie.

## 4. Alternatieven evaluatie

### 4.1 Overwogen alternatieven

1. **Handmatige import**: MSG-3 gegevens handmatig overnemen of via Excel-import in Maximo. Geen ontwikkeling, maar foutgevoelig, niet schaalbaar en geen spoor van wijzigingen.
2. **Maximo Integration Framework (MIF)**: Enterprise integratielaag van Maximo (o.a. integratiepunten, queues). Vereist Maximo-kennis en mogelijk extra licenties; zwaarder dan nodig voor een gerichte MSG-3 → PM/JobPlan-koppeling.
3. **Mobile Enterprise Application (MEA) / andere UI-tools**: Richt zich op gebruikersinterfaces en mobiel gebruik, niet op batch-import van MSG-3 data.
4. **Eigen koppeling via REST API (gekozen)**: Een eigen Python-applicatie die MSG-3 Excel parseert, valideert, mapt en via de Maximo REST API PM/JobPlan (en gerelateerde objecten) aanmaakt of bijwerkt. Volledige controle, traceerbaarheid (logging, change detection) en aansluiting op bestaande business rules.

### 4.2 Criteria en afweging

- **Beheersbaarheid:** Eigen applicatie is in één codebase te beheren en te testen (unit + integratietests).
- **Compliance:** Business rules en Maximo-regels (ITEMNUM immutable, OBSOLETE-beleid) centraal in code en documentatie.
- **Schaalbaarheid:** Geautomatiseerde flow; bij wijzigingen in MSG-3 alleen delta’s verwerken via change detection.
- **Kosten en complexiteit:** Geen afhankelijkheid van MIF of extra producten; wel onderhoud van de Python-keten en afstemming met Maximo-beheer.

### 4.3 Gekozen aanpak en rationale

Gekozen is voor **eigen koppeling via REST API**: een dedicated MSG-3 → Maximo-converter in Python die Excel leest, valideert, mapt en via REST met Maximo communiceert. Dit sluit aan bij de bestaande projectstructuur (parser, validator, change detection, mapping, maximo_connector) en bij de behoefte van Babcock aan een voorspelbare, gedocumenteerde en onderhoudbare koppeling.

## 5. Proof of Concept resultaten

### 5.1 POC Excel parsing

- **Opzet:** De parser-module (`src/parser/`) is opgezet met `ExcelReader` (sheetnamen, ranges, header-detectie) en `MSG3Parser` (parse naar metadata + taken, ondersteuning original/redesign). Het interne model is vastgelegd in de `MSG3Task`-dataclass (taakcode, beschrijving, type, interval, eenheid, zone, ATA, man-uren, vaardigheden).
- **Resultaten:** De code-structuur en het datamodel zijn klaar; de daadwerkelijke implementatie van `get_sheet_names`, `read_range` en `parse` is de volgende stap. Validatie tegen een concreet MSG-3 bestand (bijv. `examples/msg3_original.xlsm`) moet plaatsvinden om kolommapping en edge cases te bevestigen.
- **Conclusie:** Excel-parsing met openpyxl/pandas is technisch haalbaar; de POC wordt afgerond door de parser volledig te implementeren en te testen met echte Babcock-data.

### 5.2 POC Maximo-connectie

- **Opzet:** De `maximo_connector` (REST client) en de mappers (PM, JobPlan) zijn in de codebase voorbereid. De Maximo-specificaties (velden, regels) zijn gedocumenteerd; authenticatie en endpoints worden via configuratie/omgeving ingesteld.
- **Resultaten:** Een volledige end-to-end POC (van Excel tot aanmaak in Maximo testomgeving) vereist toegang tot de Maximo test-API en geldige credentials. Zolang die beschikbaar zijn, is de aanpak (REST, OSLC-stijl) onderbouwd door documentatie en bestaande specificaties.
- **Conclusie:** De Maximo-koppeling is haalbaar mits de testomgeving en auth beschikbaar zijn; aanbevolen is om eerst een minimale POC (één PM of JobPlan aanmaken via de API) uit te voeren en daarna de volledige pipeline te bouwen.

### 5.3 Haalbaarheidsoordeel en vervolgstappen

- **Haalbaarheid:** Het project is **technisch haalbaar**. De MSG-3 structuur is voldoende in beeld, de Maximo API voldoet voor PM/JobPlan-integratie, de technologiekeuze is onderbouwd en de alternatieven zijn afgewogen. De resterende risico’s zijn vooral organisatorisch (toegang testomgeving, acceptatie testdata) en inhoudelijk (definitieve kolommapping na validatie met echte bestanden).
- **Vervolgstappen:** (1) Parser volledig implementeren en valideren met `msg3_original.xlsm` (of actueel Babcock-bestand). (2) Maximo POC uitvoeren in testomgeving (één object aanmaken). (3) Change detection en mapping verder aansluiten op de REST-client. (4) Integratietests en documentatie bijwerken.

## Conclusie en aanbevelingen

Het onderzoek beantwoordt de hoofdvraag ("Is een geautomatiseerde koppeling van MSG-3 Excel naar Maximo technisch haalbaar voor Babcock Schiphol?") met **ja**, onderbouwd door de antwoorden op de drie deelvragen:

1. **MSG-3 Excel structuur**: De MSG-3-inhoud is taakgeoriënteerd (taakcode, type, interval, zone, ATA, etc.); de exacte sheet/kolom-indeling moet met een representatief Babcock-bestand worden gevalideerd. De parser ondersteunt twee varianten (original, redesign) en header-detectie.
2. **Maximo API**: De REST API biedt voldoende mogelijkheden voor PM en JobPlan. Belangrijke beperkingen: ITEMNUM immutable, OBSOLETE in de praktijk onomkeerbaar, geen echte delete. Documentatie en mapping zijn in het project aanwezig.
3. **Technologie en aanpak**: openpyxl en pandas zijn gekozen voor Excel; pydantic voor validatie; requests voor de Maximo API. Handmatige import, MIF en MEA zijn overwogen; gekozen is voor een eigen Python-koppeling via REST vanwege beheersbaarheid, compliance en schaalbaarheid. De POC-opzet ondersteunt de conclusie dat de koppeling technisch haalbaar is; afronding vraagt om volledige parser-implementatie met echt bestand en een live Maximo POC in de testomgeving.

**Aanbeveling:** Doorgaan met de gekozen aanpak. Prioriteit: parser afmaken en valideren met echte MSG-3 data, daarna Maximo POC in testomgeving uitvoeren en de end-to-end pipeline (inclusief change detection) voltooien.

*Datum: 18 februari 2026*
*Auteur: Pedro Eduardo Cardoso*
*Project: MSG-3 to Maximo Converter*

## AI Authenticiteitsverklaring

Tijdens het technisch onderzoek en ontwerp heb ik **Cursor AI** gebruikt om te **genereren van diagram templates, analyseren van API documentatie, en structureren van technische beslissingen**. Na het gebruik van deze tool heb ik de uitkomsten ervan uitvoerig gecontroleerd en aangepast om er voor te zorgen dat het ingeleverde werk mijn eigen competenties en leeruitkomsten reflecteert. Alle architecturale beslissingen, business rules en technische keuzes zijn gebaseerd op mijn eigen analyse en in overleg met stakeholders. Ik draag de volledige verantwoordelijkheid voor de inhoud van dit werk.

*AIAS Niveau: 3 - AI Samenwerking*
