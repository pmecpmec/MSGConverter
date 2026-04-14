# Risicoanalyse

Dit document beschrijft de belangrijkste risico’s voor het MSG-3–Maximo-project en hoe we die beperken. Risico’s zijn ingeschat op impact en waarschijnlijkheid; de zwaarste worden actief gemonitord.

## Technische risico’s

**Maximo API.** De REST API kan beperkingen hebben die we nu nog niet kennen (rate limits, ontbrekende velden, authenticatie). Mitigatie: vroeg in het project (week 3–4) API-onderzoek en een kleine POC doen voordat we veel code bouwen. Maximo-documentatie goed doornemen. Bij problemen alternatieven voorbereiden (bijv. SOAP of directe database) en zo nodig Maximo-experts betrekken.

**Excel-parsing.** MSG-3-bestanden kunnen complexer zijn dan verwacht (samengevoegde cellen, formules, macros). Mitigatie: meerdere voorbeelden analyseren, robuuste foutafhandeling in de parser en het voorzien van een Excel-redesign om de structuur te vereenvoudigen. Validatie stapt detecteert parsingfouten.

**Prestaties.** Grote bestanden of batch-imports kunnen traag zijn. Mitigatie: in de testfase prestaties meten en waar nodig batchverwerking of progressiefeedback toevoegen.

## Planning en scope

**Scope creep.** Er kunnen tijdens het project extra wensen ontstaan. Mitigatie: duidelijke scope in de projectdefinitie, een “buiten scope”-lijst bijhouden en nieuwe wensen eerst op de backlog zetten. Alleen in overleg en met duidelijke trade-off scope uitbreiden.

**Onderschatting.** Taken kunnen langer duren dan gedacht. Mitigatie: conservatievere inschattingen, buffer in week 17 en vroeg prototypen om complexiteit te ontdekken. Bij achterstand: herprioriteren en zo nodig scope beperken.

## Middelen en toegang

**Geen toegang tot Maximo-testomgeving.** Zonder testomgeving is integratie- en API-testen niet mogelijk. Mitigatie: toegang in week 1–2 regelen en escaleren als het uitblijft. Tijdelijk met mocks of gesimuleerde API werken zodat parser en validator door kunnen.

**Te weinig of geen MSG-3-voorbeelden.** Dan is ontwikkeling van de parser en testen lastig. Mitigatie: in week 1 voorbeeldbestanden vragen, desnoods geanonimiseerd. Als fallback: synthetische testdata of samen met de opdrachtgever een voorbeeld opstellen.

**Concentratie en focus.** Persoonlijke concentratie kan de productiviteit beïnvloeden. Mitigatie: duidelijke dagplanning, korte pauzes, taken opdelen en werken op momenten met de meeste energie. Bij aanhoudende problemen met de begeleider bespreken.

## Kwaliteit en organisatie

**Testdekking en documentatie.** Te weinig tests of uitlopende documentatie maken overdracht en onderhoud moeilijk. Mitigatie: testen en documentatie meenemen in de werkwijze per sprint, niet alleen aan het eind. In de laatste weken gericht tijd reserveren voor review en aanvulling.

**Vertraging permissies (Babcock/Schiphol).** Toegang tot systemen of data kan laat komen. Mitigatie: permissies vroeg aanvragen en opvolgen. Ondertussen werken aan parser en validator; mock-omgeving gebruiken tot toegang er is.

## Prioritering en monitoring

Kritiek: geen Maximo-toegang (actie in week 1–2). Hoog: Maximo-API-beperkingen (POC in week 3–4), scope creep (voortdurend in de gaten houden), ontbrekende MSG-3-data (actie week 1), permissies (opvolging week 1–2). Overige risico’s hebben standaardmitigatie; we evalueren ze wekelijks en bij de sprintretrospective.

Als het project structureel (bijv. twee weken of meer) achterloopt: focus op must-have (parser, connector), nice-to-have uitstellen, transparant communiceren en zo nodig in overleg kijken naar extra tijd of scope-aanpassing. Als Maximo-integratie onhaalbaar blijkt: alternatieven (bijv. CSV-export voor handmatige import of SOAP) en Maximo-experts betrekken.

_Datum: 4 februari 2026_
_Auteur: Pedro Eduardo Cardoso_
_Project: MSG-3 naar Maximo Converter_

## AI-authenticiteitsverklaring

Bij de voorbereiding van het Plan van Aanpak is Cursor AI gebruikt om te verkennen welke methodieken, planning en risicoanalyse-templates passen. De inhoud van dit PvA (planning, risico’s, mitigatie) is gebaseerd op mijn eigen analyse en afstemming met de begeleider. Ik draag de volledige verantwoordelijkheid voor de inhoud.

_AIAS-niveau: 2 – AI-exploratie_
