# Plan van Aanpak – start

Dit document ondersteunt je bij het opstellen van je Plan van Aanpak (PvA). Het PvA beschrijft hoe je het project gaat aanpakken, niet het technische ontwerp.

## Wat hoort in het Plan van Aanpak?

Het PvA beantwoordt: hoe ga je het project uitvoeren (methodiek), wanneer (planning), wat kan er misgaan (risico’s), wat heb je nodig (randvoorwaarden), en wat lever je op (deliverables). Technische ontwerpkeuzes, architectuur en gedetailleerde specificaties horen in het technisch ontwerp (SDD), niet in de PvA.

**Officiële basis:** Structuur volgens Opzet Plan van Aanpak (Windesheim) en Plan van Aanpak Template (Brightspace). Zie [PVA-STRUCTUUR-WINDESHEIM.md](PVA-STRUCTUUR-WINDESHEIM.md). Voorbeelden: hbo-kennisbank.nl. Gebruik de PvA-template op Brightspace en kijk naar voorbeelden op internet. Op hbo-kennisbank.nl vind je afstudeerwerken en stageverslagen met PvA’s; die helpen om je eigen document naast een concreet voorbeeld te leggen.

## Documenten in deze map

- **PVA-STRUCTUUR-WINDESHEIM.md** – Officiële PvA-structuur (Opzet). Koppeling met bestanden.
- **PVA-TEMPLATE-BRIGHTSPACE.md** – Volledige template uit Brightspace (screenshots): 10 hoofdstukken, alle subsecties, woordenaantallen, documenteigenschappen. Gebruik dit als invulstructuur.
- **01-projectaanpak.md** – Methodiek; hoofdstuk 3 (Het project).
- **02-planning.md** – Planning; hoofdstuk 7.
- **03-risicoanalyse.md** – Risico’s en mitigatie; hoofdstuk 6.
- **04-probleemstelling-vragen.md** – Probleemstelling, hoofdvraag en deelvragen; hoofdstuk 4.
- **05-randvoorwaarden.md** – Randvoorwaarden; hoofdstuk 7.
- **06-deliverables.md** – Deliverables; hoofdstuk 5 (Eindproduct).

**Word-document genereren:** `python scripts/export_pva_to_word.py` (uit repo-root). De script leest de sectievolgorde uit **word-export-order.txt** in deze map (afgestemd op PVA-TEMPLATE-BRIGHTSPACE.md). Output: `Plan-van-Aanpak-MSG3-Maximo-Converter.docx` in deze map.

**Waarom meerdere bestanden (01 t/m 06)?** Per hoofdstuk een bestand sluit aan op de PvA-template en maakt bewerken per sectie eenvoudiger. Als je liever één geheel bestand wilt (bijv. Plan-van-Aanpak.md), kun je de inhoud daarin samenvoegen en de exportscript aanpassen om dat ene bestand te gebruiken.

_Datum: februari 2026_
