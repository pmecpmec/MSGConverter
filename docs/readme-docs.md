# Documentatie Overzicht

**MSG-3 to Maximo Converter**, Pedro Eduardo Cardoso, ADSD Windesheim

## Documentatie herschrijven

De deliverable-documenten worden herschreven op basis van **templates uit de lessen** (Brightspace) en **voorbeelden op [hbo-kennisbank.nl](https://hbo-kennisbank.nl/)**. Zie [DOCUMENTATIE-BRONNEN.md](DOCUMENTATIE-BRONNEN.md) voor uitleg en zoektips.

**Prioriteit nu:** Eerst de **projectdefinitie** afmaken en herinleveren. Daarna PvA, onderzoek, FO/Design. Zie [STAPPENPLAN-NU.md](STAPPENPLAN-NU.md) en [FEEDBACK-HERINLEVEREN.md](FEEDBACK-HERINLEVEREN.md).

**SP3-colleges:** Voor correct doorlopen van documentatie en eindopdracht (stakeholderanalyse, Product Goal & Vision, Product backlog) zie [SP3-Colleges-Referentie.md](SP3-Colleges-Referentie.md). Daar staan begrippen, eisen en checklist uit alle zeven colleges.

## Stappenplan nu

**Zie:** [STAPPENPLAN-NU.md](STAPPENPLAN-NU.md): wat doe je nu (volgorde herinleveren: projectdefinitie → PvA → onderzoek → FO/Design).
**Feedback herinleveren:** [FEEDBACK-HERINLEVEREN.md](FEEDBACK-HERINLEVEREN.md) bevat de docentfeedback en de acties per deliverable (templates, Kennisbank, humaniseren, hoofdvraag onderzoek, SDD-vorm).

## Mappenstructuur

```
docs/
├── projectdefinitie/ Windesheim deliverable: Projectdefinitie
├── plan-van-aanpak/ Windesheim deliverable: Plan van Aanpak
├── technisch-ontwerp/ Architectuur, business rules, Maximo specs
├── onderzoek/ Onderzoeksrapport (MSG-3, Maximo API, POC)
├── scrum/ Backlog, sprints, weekly routine
├── beoordeling/ Checklists, criteria, zelfevaluatie
├── ai/ AI-gebruik, transparantie, logboek
├── reflectie/ Persoonlijke reflectie
└── TEAM-CONTACTEN.md Contactgegevens team
```

## Projectdefinitie (`projectdefinitie/`)

**Geconsolideerd:** 1 bestand per deliverable. Alle inhoud staat in `projectdefinitie.md` (Inleiding, 1–8 volgens Windesheim-template).

| Bestand | Inhoud |
|---------|--------|
| `projectdefinitie.md` | **Hoofddocument** – Inleiding, context, project, aanpak, organisatie, strategieën, planning, literatuur, bijlagen |

**Competentie:** Analyseren

**Word-document:** `python scripts/export_projectdefinitie_to_word.py` → `Projectdefinitie-MSG3-Maximo-Converter.docx` (in deze map). Vereist: `pip install python-docx`.

## Plan van Aanpak (`plan-van-aanpak/`)

**Geconsolideerd:** 1 bestand per deliverable. Alle inhoud staat in `plan-van-aanpak.md`.

| Bestand | Inhoud |
|---------|--------|
| `plan-van-aanpak.md` | **Hoofddocument** – Projectaanpak, planning, risicoanalyse, probleemstelling, randvoorwaarden, deliverables |

**Competentie:** Manage & Control

**Word-document:** `python scripts/export_pva_to_word.py` → `Plan-van-Aanpak-MSG3-Maximo-Converter.docx` (in deze map). Vereist: `pip install python-docx`.

## Technisch Ontwerp / FO design (`technisch-ontwerp/`)

**Geconsolideerd:** 1 bestand per deliverable. Alle inhoud staat in `technisch-ontwerp.md` (SDD, architectuur, business rules, mapping, Maximo specs).

| Bestand | Inhoud |
|---------|--------|
| `technisch-ontwerp.md` | **Hoofddocument** – SDD, ontwerp-overzicht, architectuur, business rules, mapping flow, Maximo specificaties |

**Word (voor OnStage):** `python scripts/export_technisch_ontwerp_to_word.py` → `FO-design-MSG3-Maximo-Converter.docx` (in deze map).

**Competentie:** Ontwerpen

## Onderzoek (`onderzoek/`)

| Bestand | Inhoud |
|---------|--------|
| `00-onderzoeksrapport.md` | **Hoofddocument**, vijf onderzoeksvragen (MSG-3 structuur, Maximo API, technologiekeuzes, alternatieven, POC), conclusie en aanbevelingen |

**Competentie:** Analyseren, Adviseren

**Word-document:** Genereer één Word-bestand met `python scripts/export_onderzoeksrapport_to_word.py`. Output: `Onderzoeksrapport-MSG3-Maximo-Converter.docx` (in deze map). Vereist: `pip install python-docx`.

**OnStage:** Inleveren als dit document (of PDF/Word) en/of ZIP van `docs/onderzoek/`.

## Scrum (`scrum/`)

| Bestand | Inhoud |
|---------|--------|
| `README.md` | Scrum werkwijze, routine (Di/Wo/Do, weekly review), backlog-overzicht |
| `backlog.md` | Product backlog |
| `sprint-template.md` | Template voor sprint planning |
| `sprints/sprint-01-planning.md` | Sprint 1 planning |

**Competentie:** Manage & Control

## Beoordeling (`beoordeling/`)

| Bestand | Inhoud |
|---------|--------|
| `BEOORDELINGSCRITERIA.md` | Alle beoordelingscriteria Comaker 1 |
| `DELIVERABLES-CHECKLIST.md` | Status per deliverable |
| `CHECKLIST-VOOR-INLEVEREN.md` | Pre-inlevering checklist |
| `ACTIEPLAN-8PLUS.md` | Actieplan voor 8+ beoordeling |
| `ZELFEVALUATIE-TRACKING.md` | Live scorecard (check elke vrijdag) |
| `CORRECTE-INFORMATIE.md` | Factcheck & correcte gegevens |

## AI Documentatie (`ai/`)

| Bestand | Inhoud |
|---------|--------|
| `AI-GEBRUIK.md` | Volledige AI-gebruik verantwoording (AIAS) |
| `AI-AUTHENTICITEITSVERKLARINGEN.md` | Copy-paste verklaringen per deliverable |
| `AI-WORKFLOW-DAGELIJKS.md` | Dagelijkse AI workflow + cheat sheet |
| `AI-LOGBOEK.md` | Chronologisch AI-gebruik logboek |
| `MIJN-BIJDRAGE-VS-AI.md` | Eigenaarschap: 75% Pedro / 25% AI |

## Reflectie (`reflectie/`)

| Bestand | Inhoud |
|---------|--------|
| `README.md` | Persoonlijke reflectie (in ontwikkeling) |

## Root-niveau bestanden

| Bestand | Inhoud |
|---------|--------|
| `README.md` | Project README |
| `QUICKSTART.md` | Snel aan de slag |
| `CONTRIBUTING.md` | Bijdrage richtlijnen |
| `MAXIMO-QUICK-REFERENCE.md` | Maximo quick reference |

*Laatst bijgewerkt: 24 februari 2026 – Geconsolideerd naar 1 MD-bestand per deliverable*
