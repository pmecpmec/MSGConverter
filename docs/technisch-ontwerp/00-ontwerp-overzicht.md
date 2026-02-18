# Functioneel & Technisch Ontwerp – Overzicht

**Project:** MSG-3 to Maximo Converter  
**Organisatie:** Babcock Schiphol  
**Auteur:** Pedro Eduardo Cardoso  
**Opleiding:** Associate Degree Software Developer (ADSD), Windesheim  
**Datum:** 18 februari 2026

---

## Doel van dit document

Dit document is het **hoofddocument** voor de OnStage-inlevertaak "FO/design document". Het geeft een overzicht van alle functioneel en technisch ontwerpdocumenten in deze map en hun onderlinge relatie. De gedetailleerde specificaties, business rules en mapping staan in de hieronder genoemde bestanden.

---

## Inhoudsopgave ontwerpdocumenten

| Document | Beschrijving |
|----------|--------------|
| [business-rules.md](business-rules.md) | Volledige documentatie van de 80 Babcock business rules: veiligheid, compliance, kwaliteit en efficiency. Basis voor alle validatie en transformaties. |
| [business-rules-quick-reference.md](business-rules-quick-reference.md) | Snelle referentie en codevoorbeelden voor de business rules; handig tijdens development. |
| [BUSINESS-RULES-FIRST.md](BUSINESS-RULES-FIRST.md) | Guideline: alle ontwikkeling moet compliant zijn met de business rules. Verplichte leesstof vóór development. |
| [CHANGELOG-business-rules.md](CHANGELOG-business-rules.md) | Wijzigingslog van de business rules (toevoegingen, aanpassingen, versies). |
| [MAPPING-FLOW-VISUAL.md](MAPPING-FLOW-VISUAL.md) | Visueel overzicht van de end-to-end dataflow: MSG-3 Excel → Parse → Validate → Map → Maximo API. |
| [maximo-specificaties.md](maximo-specificaties.md) | Maximo-specifieke specificaties (Item Master, statuses, commodity groups, verplichte velden, validatieregels) op basis van maximosecrets.com. |
| [MAXIMO-INTEGRATIE-UPDATE.md](MAXIMO-INTEGRATIE-UPDATE.md) | Statusupdate van de Maximo-integratie: toegepaste specificaties, nieuwe mappers, volgorde Item → PM → JobPlan. |

---

## Relatie tussen de documenten

- **Business rules** vormen de kern: zij bepalen wat geldige data is en hoe transformaties plaatsvinden.
- **Maximo specificaties** bepalen hoe data in Maximo (velden, statuses, relaties) moet worden weergegeven.
- **Mapping flow** beschrijft de stappen van bron (MSG-3 Excel) tot doel (Maximo API).
- **FO/design** voor OnStage wordt geleverd als: dit overzicht + de genoemde documenten (bijvoorbeeld als één ZIP van de map `technisch-ontwerp/`).

---

*Datum: 18 februari 2026*  
*Auteur: Pedro Eduardo Cardoso*  
*Project: MSG-3 to Maximo Converter*

---

## AI Authenticiteitsverklaring

Tijdens het technisch onderzoek en ontwerp heb ik **Cursor AI** gebruikt om te **genereren van diagram templates, analyseren van API documentatie, en structureren van technische beslissingen**. Na het gebruik van deze tool heb ik de uitkomsten ervan uitvoerig gecontroleerd en aangepast om er voor te zorgen dat het ingeleverde werk mijn eigen competenties en leeruitkomsten reflecteert. Alle architecturale beslissingen, business rules en technische keuzes zijn gebaseerd op mijn eigen analyse en in overleg met stakeholders. Ik draag de volledige verantwoordelijkheid voor de inhoud van dit werk.

*AIAS Niveau: 3 - AI Samenwerking*
