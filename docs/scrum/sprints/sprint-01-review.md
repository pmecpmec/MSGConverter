# Sprint 1 Review – Research & Foundation

**Sprint:** 1
**Periode:** 18 februari – 6 maart 2026
**Datum review:** 6 maart 2026
**Aanwezig:** Pedro Eduardo Cardoso (solo project)
**Project:** MSG-3 to Maximo Converter

---

## Sprint Goal – Behaald?

**Goal:** "Compleet onderzoeksrapport met onderbouwde technologie keuzes en werkende POC's, zodat we met vertrouwen kunnen starten met development in Sprint 2."

**Status:** Gedeeltelijk behaald. Onderzoeksrapport en technologie-onderbouwing zijn afgerond. De Maximo API POC is op basis van documentatie uitgewerkt (geen live Maximo testomgeving beschikbaar tijdens sprint). De project-architectuur is ontworpen en vastgelegd.

---

## Opgeleverde Items

### Voltooid

| Item | Beschrijving | Bewijs |
|------|-------------|--------|
| MSG-3 structuur analyse | Alle task types, interval-eenheden en kolommen gedocumenteerd | `docs/onderzoek/01-msg3-analyse.md` |
| Maximo API research | Relevante endpoints, objectstructuren en authenticatie beschreven | `docs/onderzoek/02-maximo-api.md` |
| Technologie keuzes | Python + openpyxl/pandas gekozen, onderbouwd met vergelijkingstabel | `docs/onderzoek/03-technologie-keuzes.md` |
| Alternatieven evaluatie | 4 oplossingsrichtingen vergeleken (macro, no-code, Python, MIF) | `docs/onderzoek/04-alternatieven-evaluatie.md` |
| Excel parser POC | Werkende parser met openpyxl; redesign + origineel formaat ondersteund | `src/parser/excel_reader.py`, `src/parser/msg3_parser.py` |
| Maximo connector ontwerp | REST client structuur gedefinieerd op basis van OSLC API-documentatie | `src/maximo_connector/` |
| Onderzoeksrapport | Hoofddocument met conclusies en aanbevelingen | `docs/onderzoek/00-onderzoeksrapport.md` |
| Project-architectuur | Volledige package-structuur, SDD-basis, business rules gedocumenteerd | `docs/technisch-ontwerp/`, `src/` |

### Niet voltooid / Verschoven naar Sprint 2

| Item | Reden | Sprint 2 actie |
|------|-------|----------------|
| Live Maximo API POC | Testomgeving niet beschikbaar in sprint-periode | REST connector volledig implementeren in sprint 2 |
| CI/CD pipeline | GitHub Actions niet geconfigureerd (geen remote repo) | Lokaal pytest pipeline; CI/CD optioneel later |

---

## Demo

Gedemonstreerd tijdens sprint-afsluiting (interne demo, geen stakeholders aanwezig):

1. **Excel parser** – `tests/fixtures/test_msg3_redesign.xlsx` succesvol geparseerd naar JSON
2. **Versie-detectie** – redesign-formaat herkend op basis van headers
3. **Validator** – 90 business rules geladen, structuurvalidatie werkend
4. **JSON output** – Maximo-objecten gegenereerd (items, PM, jobplans, commodities)

---

## Resultaten t.o.v. Acceptatiecriteria

| Criterium | Status | Opmerking |
|-----------|--------|-----------|
| Onderzoeksrapport compleet | Ja | Alle deelonderwerpen uitgewerkt |
| Technologie keuzes onderbouwd | Ja | Python + openpyxl, met alternatieven |
| Excel POC werkend | Ja | 10 taken geparseerd in <100ms |
| Maximo API POC werkend | Gedeeltelijk | Op basis van documentatie; live test volgt sprint 2 |
| Dev environment setup | Ja | pytest, requirements.txt, .coveragerc aanwezig |
| Sprint docs compleet | Ja | Planning, review, retrospective |

---

## Metrisch overzicht

| Metric | Waarde |
|--------|--------|
| Story points gepland | 57 |
| Story points opgeleverd | ~50 |
| Netto capaciteit gebruikt | ~52 uur |
| Onderzochte alternatieven | 4 oplossingen, 3 technologie-paren |
| Regels productie-code (eind sprint) | ~800 regels |
| Unit tests (eind sprint) | 53 tests, 70% coverage |

---

## Stakeholder Feedback

Geen formele stakeholder-review gehouden in sprint 1 (Matthijs/Rick beschikbaar maar geen vaste afspraak ingepland). Bevindingen zijn per e-mail gedeeld. Feedback ontvangen:

- MSG-3 redesign-formaat is het primaire formaat voor nieuwe bestanden
- Origineel formaat moet als fallback ondersteund blijven
- Maximo testomgeving toegang wordt in sprint 2 geregeld

**Actiepunten uit feedback:**
1. Parser focust primair op redesign-formaat (gedaan)
2. Maximo toegang aanvragen via Matthijs (actie sprint 2)

---

## Authenticiteitsverklaring AI-gebruik

Cursor AI (Claude) is gebruikt als assistent bij het uitwerken van document-structuren en het opzetten van de code-architectuur. Analyse van MSG-3, technologie-keuzes en alle inhoudelijke conclusies zijn door mij zelf gedaan op basis van documentatie en praktijkervaring tijdens de sprint.
