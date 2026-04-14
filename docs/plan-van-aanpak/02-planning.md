# Planning

**Periode:** 4 februari 2026 – 15 juni 2026 (circa 18 weken).
**Status (18 feb 2026):** Projectdefinitie en PvA zijn ingeleverd; het project zit in de uitvoeringsfase.

## Fasering

**Opstart (week 1–2).** Repository, projectdefinitie en PvA zijn gereed. In deze fase regelen we de developmentomgeving, toegang tot de Maximo-testomgeving en voorbeeld-MSG-3-bestanden. De mijlpaal is: project gestart en klaar om te bouwen.

**Onderzoek (week 3–4).** We analyseren de MSG-3 Excel-structuur en de Maximo API, doen een technologiekeuze en bouwen een kleine proof of concept (Excel inlezen, eenvoudige API-call). Aan het eind is de technische haalbaarheid onderbouwd en staat een eerste versie van het technisch ontwerp op papier.

**Parser en validator (week 5–7).** Eerst de Excel-parser en een basisvalidator; daarna de business rules en foutrapportage. De mijlpaal: MSG-3 Excel kan worden ingelezen en gevalideerd.

**Change detection (week 8–9).** Logica om twee versies MSG-3 te vergelijken en wijzigingen (toegevoegd, gewijzigd, verwijderd) te rapporteren. Aan het eind kunnen we delta’s ten opzichte van een vorige versie bepalen.

**Mapping (week 10–11).** Veldmapping MSG-3 naar Maximo (PM en JobPlan) en transformatieregels. Daarna: MSG-3-data in Maximo-formaat kunnen omzetten.

**Maximo-connector (week 12–13).** REST-client, authenticatie, CRUD en foutafhandeling. De mijlpaal: data kan naar de Maximo-testomgeving worden gestuurd.

**MSG-3-redesign (week 14–15).** Analyse van de huidige Excel-structuur, ontwerp van een nieuw template dat beter machine-leesbaar is, en aanpassing van de parser. De nieuwe template wordt met stakeholders afgestemd.

**Testen en afronding (week 16–17).** End-to-end tests, bugfixes, performance en documentatie. Doel: systeem klaar voor overdracht.

**Afronding en overdracht (week 18).** Gebruikershandleiding, technische documentatie, overdrachtsdocumentatie, presentatie en reflectie. Project wordt opgeleverd.

## Mijlpalen en momenten van review

| Week | Mijlpaal | Soort review |
|------|----------|--------------|
| 2 | Opstart afgerond | Intern |
| 4 | Haalbaarheid aangetoond | Demo stakeholders |
| 7 | Parser en validator werken | Demo stakeholders |
| 9 | Change detection werkt | Intern |
| 11 | Mapping compleet | Demo stakeholders |
| 13 | Maximo-integratie werkt | Demo stakeholders |
| 15 | Nieuwe template goedgekeurd | Review stakeholders |
| 17 | Systeem production-ready | Eindreview |
| 18 | Project opgeleverd | Oplevering en presentatie |

## Tijd en prioriteit

De planning gaat uit van 32–40 uur per week (fulltime stage). De kritieke keten: eerst de parser (alles bouwt daarop), dan de mapping-engine, dan de Maximo-connector. Er is buffer in week 17 voor onvoorziene problemen. Als we achterlopen, gaan de must-have onderdelen voor; het Excel-redesign of extra functionaliteit kunnen we indien nodig inkorten of verschuiven.

Afhankelijkheden: tijdig toegang tot de Maximo-testomgeving, voorbeeld-MSG-3-bestanden en beschikbaarheid van stakeholders voor feedback. Communicatie: wekelijks kort overleg met de begeleider, per sprint een demo en reflectie.

_Datum: 4 februari 2026_
_Auteur: Pedro Eduardo Cardoso_
_Project: MSG-3 naar Maximo Converter_

## AI-authenticiteitsverklaring

Bij de voorbereiding van het Plan van Aanpak is Cursor AI gebruikt om te verkennen welke methodieken, planning en risicoanalyse-templates passen. De inhoud van dit PvA (planning, risico’s, mitigatie) is gebaseerd op mijn eigen analyse en afstemming met de begeleider. Ik draag de volledige verantwoordelijkheid voor de inhoud.

_AIAS-niveau: 2 – AI-exploratie_
