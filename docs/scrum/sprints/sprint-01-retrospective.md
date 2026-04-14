# Sprint 1 Retrospective – Research & Foundation

**Sprint:** 1
**Periode:** 18 februari – 6 maart 2026
**Datum:** 6 maart 2026
**Deelnemer:** Pedro Eduardo Cardoso

---

## Retrospective Format: Start / Stop / Continue

### Start (Meer van doen)

1. **Eerder beginnen met code** – De architectuurbeslissingen werden laat in de sprint gemaakt. In sprint 2 begin ik op dag 1 met de skeleton-code, zodat de implementatie meer ruimte krijgt.
2. **Stakeholder-afspraken inplannen aan begin sprint** – Sprint 1 had geen vaste overleg-momenten met Matthijs/Rick. In sprint 2: wekelijks 15-minuten check-in inplannen op maandag of dinsdag.
3. **Testdriven aanpak** – De POC was functioneel maar zonder gestructureerde tests. Sprint 2 werkt strict TDD: test schrijven vóór implementatie.

### Stop (Minder van doen)

1. **Scope te breed verkennen** – Ik heb extra tijd gestoken in onderwerpen (Docker, CI/CD) die niet direct voor de beoordeling tellen. Focus stricter op backlog-items.
2. **Documentatie achteraf schrijven** – Onderzoeksdocumenten werden pas na het werk geschreven. In sprint 2: documenteer direct tijdens het werk.

### Continue (Goed, zo doorgaan)

1. **Dagelijkse aantekeningen bijhouden** – Korte notities per dag hielpen om de voortgang en blokkades bij te houden.
2. **Cursor AI als assistent** – Effectief gebruikt voor templates, code-scaffolding en refactoring, met eigen verantwoordelijkheid voor inhoud en beslissingen.
3. **Gestructureerde map-indeling** – De `docs/`, `src/`, `tests/` opzet werkt goed; gemakkelijk navigeerbaar.

---

## What Went Well

| # | Wat ging goed |
|---|---------------|
| 1 | Onderzoeksrapport afgerond met voldoende diepgang |
| 2 | MSG-3-structuur snel en correct begrepen |
| 3 | Python + openpyxl technologie-keuze snel gemaakt en goed onderbouwd |
| 4 | Business rules (90 stuks) vroegtijdig gedefinieerd – bespaart later tijd |
| 5 | Werkende Excel parser aan einde sprint |
| 6 | Development environment direct professioneel opgezet (pytest, requirements.txt, linting) |

---

## What Could Be Better

| # | Verbeterpunt | Wortel-oorzaak | Actie sprint 2 |
|---|-------------|----------------|----------------|
| 1 | Maximo testomgeving niet beschikbaar | Te laat gevraagd, afhankelijk van Babcock | Vraag in week 1 sprint 2 opnieuw aan |
| 2 | Scope "CI/CD pipeline" was te groot | Geen duidelijke MoSCoW-prioritering | Strict Must/Should/Won't-Have hanteren |
| 3 | Documentatie-achterstand halverwege sprint | Schrijven uitgesteld tot eind week | 30 min per dag reserveren voor docs |
| 4 | Geen formele sprint review met stakeholders | Geen afspraak ingepland | Sprint 2: demo inplannen eind sprint |

---

## Action Items voor Sprint 2

| # | Actie | Wanneer | Eigenaar |
|---|-------|---------|---------|
| 1 | Maximo testomgeving aanvragen bij Matthijs | Dag 1, sprint 2 | Pedro |
| 2 | Wekelijks 15-min check-in inplannen | Sprint 2 start | Pedro + Matthijs |
| 3 | Elke dag 30 min documenteren (docstrings + technische notities) | Doorlopend | Pedro |
| 4 | Sprint 2 review demo voorbereiden (live pipeline run) | Eind sprint 2 | Pedro |
| 5 | Coverage target: ≥80% handhaven via pytest-cov | Doorlopend | Pedro |

---

## Persoonlijke Reflectie

**Wat heb ik geleerd deze sprint:**

- MSG-3 is complexer dan verwacht: combinaties van interval-typen, ATA-hiërarchie en task-types vereisen een robuuste parser.
- Vroeg architectuurbeslissingen maken (dataclasses, layered design) bespaart later rewrite-werk.
- Business rules formeel vastleggen vóór implementeren helpt enorm bij validatie en testen.
- Cursor AI is een krachtige assistent, maar inhoudelijke beslissingen (keuzes, analyse) moeten altijd door mij worden gemaakt en verdedigd.

**Wat wil ik verbeteren in sprint 2:**

- Meer gestructureerde TDD-aanpak handhaven (test first, code second).
- Minder tijd aan "nice to have" infrastructuur, meer focus op werkende kernfunctionaliteit.
- Stakeholders eerder betrekken voor feedback op tussentijdse deliverables.

---

## Sprint Velocity

| Metric | Waarde |
|--------|--------|
| Geplande story points | 57 |
| Geleverde story points | ~50 |
| Velocity (% compleet) | 88% |
| Grootste blokkade | Geen live Maximo-omgeving |
| Beste resultaat | Werkende Excel parser + 90 business rules |

---

## Authenticiteitsverklaring AI-gebruik

Deze retrospectieve is door mij zelf geschreven op basis van mijn eigen sprint-ervaringen. Cursor AI heeft de structuur voorgesteld; de inhoud (reflecties, verbeterpunten, learnings) is volledig mijn eigen werk.
