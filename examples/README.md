# MSG-3 Excel Voorbeelden

Deze map bevat voorbeeld MSG-3 Excel bestanden:

## Bestanden

### `msg3_original.xlsx`
Het originele MSG-3 Excel formaat zoals gebruikt bij Babcock Schiphol.
- Bevat productie data structuur
- Gebruikt voor reverse engineering en analyse
- **Let op:** Dit bestand is vertrouwelijk en niet gecommit in Git

### `msg3_redesign.xlsx`
Het herontworpen MSG-3 Excel formaat, geoptimaliseerd voor automatische verwerking:
- Duidelijke header rij
- Gestandaardiseerde kolom namen
- Ingebouwde validatie
- Change tracking velden (Version, Last Modified, etc.)
- Data type hints

### `msg3_template.xlsx`
Een lege template van het redesign formaat voor nieuwe projecten.

## Gebruik

```python
from src.parser import MSG3Parser

parser = MSG3Parser()

# Parse origineel formaat
data = parser.parse(Path("examples/msg3_original.xlsx"))

# Parse redesign formaat
data = parser.parse(Path("examples/msg3_redesign.xlsx"))
```

## Kolom Mapping

### Origineel Formaat
- Kolom A: Task Code
- Kolom B: Description
- Kolom C: Interval
- (etc.)

### Redesign Formaat
- Kolom A: TASK_CODE (verplicht, uniek)
- Kolom B: DESCRIPTION (verplicht)
- Kolom C: TASK_TYPE (INS/LUB/SVC/etc.)
- Kolom D: INTERVAL (numeriek)
- Kolom E: INTERVAL_UNIT (FH/FC/MO/WK)
- Kolom F: ZONE (optioneel)
- Kolom G: ATA_CHAPTER (optioneel)
- Kolom H: MAN_HOURS (optioneel)
- Kolom I: SKILLS (optioneel, comma separated)
- Kolom J: VERSION (auto-generated)
- Kolom K: LAST_MODIFIED (auto-generated)

## Test Data

Voor unit tests, zie `/tests/fixtures/` voor kleinere test bestanden.
