# MSG-3 → Maximo Mapping Flow
## Visueel Overzicht

**Datum:** 17 februari 2026
**Auteur:** Pedro Eduardo Cardoso

---

## Complete Data Flow

```
┌─────────────────────────────────────────────────────────────┐
│ MSG-3 Excel File │
│ (examples/msg3_original.xlsm) │
└────────────────────┬────────────────────────────────────────┘
 │
 ▼
┌─────────────────────────────────────────────────────────────┐
│ STEP 1: PARSE │
│ ├─ excel_reader.py │
│ ├─ msg3_parser.py │
│ └─ Output: Python Dict │
└────────────────────┬────────────────────────────────────────┘
 │
 ▼
┌─────────────────────────────────────────────────────────────┐
│ STEP 2: VALIDATE │
│ ├─ schema_validator.py (structuur) │
│ ├─ msg3_validator.py (data types) │
│ ├─ business_rules.py (90 regels!) │
│ └─ Output: Validated Dict + Warnings │
└────────────────────┬────────────────────────────────────────┘
 │
 ▼
┌─────────────────────────────────────────────────────────────┐
│ STEP 3: CHANGE DETECTION (optional) │
│ ├─ change_detector.py │
│ ├─ diff_engine.py │
│ └─ Output: Change Report │
└────────────────────┬────────────────────────────────────────┘
 │
 ▼
┌─────────────────────────────────────────────────────────────┐
│ STEP 4: MAPPING - MSG3MaximoMapper │
│ │
│ ┌──────────────────────────────────────────────────────┐ │
│ │ 4.1: COMMODITIES (item_mapper._extract_commodities) │ │
│ │ ──────────────────────────────────────────────────── │ │
│ │ Input: MSG-3 ATA Chapters & Systems │ │
│ │ Output: Commodity Groups & Codes │ │
│ │ │ │
│ │ Example: │ │
│ │ ATA 32 → Commodity Group "ATA-32" │ │
│ │ System 11 → Commodity Code "32-11" │ │
│ └──────────────────────────────────────────────────────┘ │
│ │ │
│ ▼ │
│ ┌──────────────────────────────────────────────────────┐ │
│ │ 4.2: ITEMS (item_mapper.map_task_to_item) │ │
│ │ ──────────────────────────────────────────────────── │ │
│ │ Input: MSG-3 Task │ │
│ │ Output: Maximo Item Master Record │ │
│ │ │ │
│ │ Key Fields: │ │
│ │ ITEMNUM: MSG3-{task_code} │ │
│ │ DESCRIPTION: {description} (max 100) │ │
│ │ ITEMTYPE: "ITEM" │ │
│ │ STATUS: "PLANNING" │ │
│ │ STOCKCATEGORY: "NS" │ │
│ │ COMMODITY: "ATA-{chapter}" │ │
│ │ COMMODITYCODE: "{chapter}-{system}" │ │
│ └──────────────────────────────────────────────────────┘ │
│ │ │
│ ▼ │
│ ┌──────────────────────────────────────────────────────┐ │
│ │ 4.3: ITEM/ORG (item_mapper.map_task_to_item_org) │ │
│ │ ──────────────────────────────────────────────────── │ │
│ │ Input: MSG-3 Task │ │
│ │ Output: Item/Organization Record │ │
│ │ │ │
│ │ Links item to specific organization │ │
│ └──────────────────────────────────────────────────────┘ │
│ │ │
│ ▼ │
│ ┌──────────────────────────────────────────────────────┐ │
│ │ 4.4: PM (pm_mapper.map_task) │ │
│ │ ──────────────────────────────────────────────────── │ │
│ │ Input: MSG-3 Task │ │
│ │ Output: Maximo PM Record │ │
│ │ │ │
│ │ Key Fields: │ │
│ │ PMNUM: MSG3-{task_code} │ │
│ │ DESCRIPTION: {description} │ │
│ │ FREQUENCY: {interval} │ │
│ │ FREQUNIT: {mapped unit} │ │
│ │ LOCATION: {zone} │ │
│ │ ITEMNUM: MSG3-{task_code} (references Item!) │ │
│ └──────────────────────────────────────────────────────┘ │
│ │ │
│ ▼ │
│ ┌──────────────────────────────────────────────────────┐ │
│ │ 4.5: JOBPLAN (jobplan_mapper.map_task) │ │
│ │ ──────────────────────────────────────────────────── │ │
│ │ Input: MSG-3 Task │ │
│ │ Output: Maximo JobPlan Record │ │
│ │ │ │
│ │ Key Fields: │ │
│ │ JPNUM: MSG3-{task_code} │ │
│ │ DESCRIPTION: {description} │ │
│ │ WORKTYPE: "PM" │ │
│ │ PLUSCJPREVDUR: {man_hours} │ │
│ └──────────────────────────────────────────────────────┘ │
│ │
└────────────────────┬────────────────────────────────────────┘
 │
 ▼
┌─────────────────────────────────────────────────────────────┐
│ OUTPUT: Maximo Objects Dictionary │
│ { │
│ "commodities": [...], # Commodity Groups & Codes │
│ "items": [...], # Item Master records │
│ "item_orgs": [...], # Item/Org records │
│ "pm": [...], # PM records │
│ "jobplan": [...] # JobPlan records │
│ } │
└────────────────────┬────────────────────────────────────────┘
 │
 ▼
┌─────────────────────────────────────────────────────────────┐
│ STEP 5: SEND TO MAXIMO │
│ ├─ maximo_client.py │
│ ├─ rest_client.py │
│ └─ Output: Success/Failure Report │
└─────────────────────────────────────────────────────────────┘
```

---

## Mapping Volgorde (CRITICAL!)

```
┌────────────────────────────────────────────────┐
│ 1. COMMODITIES │
│ ↓ │
│ Must exist BEFORE items reference them │
│ ↓ │
├────────────────────────────────────────────────┤
│ 2. ITEMS (Item Master) │
│ ↓ │
│ Must exist BEFORE PM/JobPlan reference │
│ ↓ │
├────────────────────────────────────────────────┤
│ 3. ITEM/ORG (Item/Organization) │
│ ↓ │
│ Links item to organization │
│ ↓ │
├────────────────────────────────────────────────┤
│ 4. PM (Preventive Maintenance) │
│ ↓ │
│ References ITEMNUM │
│ ↓ │
├────────────────────────────────────────────────┤
│ 5. JOBPLAN (Job Plans) │
│ ↓ │
│ Optional: references ITEMNUM │
│ ↓ │
└────────────────────────────────────────────────┘

 WAARSCHUWING: Verkeerde volgorde = Foreign Key Errors!
```

---

## MSG-3 Task → Maximo Objects

### Example MSG-3 Task:
```json
{
 "task_code": "32-11-01-001",
 "description": "Visual inspection landing gear door actuator",
 "ata_chapter": "32",
 "ata_system": "11",
 "interval": 500,
 "interval_unit": "FH",
 "man_hours": 2.5,
 "zone": "NOSE"
}
```

### Generates 5 Maximo Objects:

#### 1. Commodity Group
```json
{
 "COMMODITY": "ATA-32",
 "PARENT": null,
 "ITEMSETID": "MSG3-MAINT",
 "ISSERVICE": false,
 "DESCRIPTION": "ATA Chapter 32"
}
```

#### 2. Commodity Code
```json
{
 "COMMODITY": "32-11",
 "PARENT": "ATA-32",
 "ITEMSETID": "MSG3-MAINT",
 "ISSERVICE": false,
 "DESCRIPTION": "ATA 32-11"
}
```

#### 3. Item Master
```json
{
 "ITEMNUM": "MSG3-32-11-01-001",
 "DESCRIPTION": "Visual inspection landing gear door actuator",
 "ITEMTYPE": "ITEM",
 "ITEMSETID": "MSG3-MAINT",
 "STATUS": "PLANNING",
 "STOCKCATEGORY": "NS",
 "COMMODITY": "ATA-32",
 "COMMODITYCODE": "32-11",
 "ROTATING": false,
 "ISKIT": false
}
```

#### 4. PM Record
```json
{
 "PMNUM": "MSG3-32-11-01-001",
 "DESCRIPTION": "Visual inspection landing gear door actuator",
 "FREQUENCY": 500,
 "FREQUNIT": "HOURS",
 "LOCATION": "NOSE",
 "STATUS": "PLANNING",
 "WORKTYPE": "PM",
 "COMMODITY": "ATA-32",
 "COMMODITYCODE": "32-11",
 "ITEMNUM": "MSG3-32-11-01-001" ← References Item!
}
```

#### 5. JobPlan Record
```json
{
 "JPNUM": "MSG3-32-11-01-001",
 "DESCRIPTION": "Visual inspection landing gear door actuator",
 "STATUS": "ACTIVE",
 "WORKTYPE": "PM",
 "PLUSCJPREVDUR": 2.5
}
```

---

## Object Relationships

```
COMMODITIES
 ├── COMMODITY GROUP: "ATA-32" (PARENT = null)
 └── COMMODITY CODE: "32-11" (PARENT = "ATA-32")
 ↓
 └─ Referenced by ITEM

ITEM MASTER
 └── ITEMNUM: "MSG3-32-11-01-001"
 ├── COMMODITY: "ATA-32"
 └── COMMODITYCODE: "32-11"
 ↓
 └─ Referenced by PM

PM (Preventive Maintenance)
 └── PMNUM: "MSG3-32-11-01-001"
 ├── ITEMNUM: "MSG3-32-11-01-001" ← FK to ITEM
 ├── COMMODITY: "ATA-32"
 └── COMMODITYCODE: "32-11"

JOBPLAN
 └── JPNUM: "MSG3-32-11-01-001"
 └── (optional) ITEMNUM reference
```

---

## Validation Flow

```
MSG-3 Task Input
 ↓
┌───────────────────────────────────────┐
│ VALIDATION LAYER 1: Schema │
│ ├─ Required fields present? │
│ ├─ Correct data types? │
│ └─ Valid structure? │
└───────────────┬───────────────────────┘
 ↓
┌───────────────────────────────────────┐
│ VALIDATION LAYER 2: Data Types │
│ ├─ Dates valid? │
│ ├─ Numbers in range? │
│ └─ Enums correct? │
└───────────────┬───────────────────────┘
 ↓
┌───────────────────────────────────────┐
│ VALIDATION LAYER 3: Business Rules │
│ ├─ 80 Babcock business rules │
│ ├─ 10 Maximo-specific rules │
│ └─ Total: 90 rules checked! │
└───────────────┬───────────────────────┘
 ↓
┌───────────────────────────────────────┐
│ VALIDATION LAYER 4: Maximo Limits │
│ ├─ ITEMNUM ≤ 30 chars? │
│ ├─ Description ≤ 100 chars? │
│ ├─ Commodity ≤ 8 chars? │
│ ├─ All UPPERCASE? │
│ └─ Status transitions valid? │
└───────────────┬───────────────────────┘
 ↓
 VALID → Continue to Mapping
 INVALID → Return Errors
```

---

## Class Architecture

```
msg3_maximo_mapper.py (Main Orchestrator)
 │
 ├─> item_mapper.py
 │ ├─ map_task_to_item()
 │ ├─ map_task_to_item_org()
 │ ├─ validate_item_for_obsolete()
 │ ├─ _generate_itemnum()
 │ ├─ _validate_itemnum()
 │ ├─ _format_description()
 │ ├─ _map_commodity_group()
 │ └─ _map_commodity_code()
 │
 ├─> pm_mapper.py
 │ ├─ map_task()
 │ ├─ map_tasks()
 │ ├─ _generate_pmnum()
 │ ├─ _format_description()
 │ ├─ _map_commodity_group()
 │ ├─ _map_commodity_code()
 │ ├─ _map_interval_unit()
 │ └─ _map_priority()
 │
 └─> jobplan_mapper.py
 ├─ map_task()
 ├─ map_tasks()
 ├─ _generate_jpnum()
 └─ _format_description()
```

---

## Field Length Limits

```
┌─────────────────┬─────────┬──────────┬─────────────────┐
│ Field │ Maximo │ Current │ Status │
│ │ Max │ Usage │ │
├─────────────────┼─────────┼──────────┼─────────────────┤
│ ITEMNUM │ 30 │ ~17 │ SAFE │
│ PMNUM │ 30 │ ~17 │ SAFE │
│ JPNUM │ 30 │ ~17 │ SAFE │
│ DESCRIPTION │ 100 │ varies │ VALIDATE │
│ COMMODITY Grp │ 8 │ 6 │ SAFE │
│ COMMODITY Code │ 8 │ 5 │ SAFE │
└─────────────────┴─────────┴──────────┴─────────────────┘

Format Examples:
 ITEMNUM: "MSG3-32-11-01-001" (17 chars)
 PMNUM: "MSG3-32-11-01-001" (17 chars)
 JPNUM: "MSG3-32-11-01-001" (17 chars)
 Comm Grp: "ATA-32" (6 chars)
 Comm Code: "32-11" (5 chars)
```

---

## Error Handling

```
Try Block per Task
 │
 ├─> Task 1: Success → Add to results
 │
 ├─> Task 2: Error → Log error, continue
 │ │
 │ └─> Error logged to mapping_errors[]
 │
 ├─> Task 3: Success → Add to results
 │
 └─> Task N: Error → Log error, continue

Result:
 ├─ Partial Success: Some tasks mapped
 ├─ Error Report: List of failed tasks
 └─ Continue processing remaining tasks
```

---

## Status Lifecycle

```
NEW ITEM:
┌─────────┐
│ PENDING │ ← Default in Sets (optional)
└────┬────┘
 │ (Initial status for MSG-3)
 ▼
┌──────────┐
│ PLANNING │ ← Start here!
└────┬─────┘ Can be in job plans but not used yet
 │ (After review & approval)
 ▼
┌────────┐
│ ACTIVE │ ← Fully operational
└────┬───┘ Can be issued, ordered, used
 │ (Item is being phased out)
 ▼
┌─────────┐
│ PENDOBS │ ← Pending Obsolescence
└────┬────┘ Can be issued but not reordered
 │ (After all checks pass)
 ▼
┌──────────┐
│ OBSOLETE │ ← IRREVERSIBLE!
└──────────┘ Cannot be used or changed back!
```

---

## Quick Decision Tree

```
Need to create Maximo records from MSG-3?
 │
 ├─> YES → Do commodities exist?
 │ │
 │ ├─> NO → Create commodities FIRST
 │ │ (Step 1 in mapping)
 │ │
 │ └─> YES → Create items
 │ │
 │ └─> Then create PM/JobPlan
 │
 └─> Need to update existing item?
 │
 ├─> Change ITEMNUM? → IMPOSSIBLE!
 │ Create new + OBSOLETE old
 │
 ├─> Change Description? → ALLOWED
 │
 ├─> Change Status? → Check transition rules
 │
 └─> Make OBSOLETE? → Check references first!
 Must be PENDOBS first!
```

---

## Pro Tips

1. **Always validate before mapping**
 - Saves time by catching errors early
 - Prevents half-completed Maximo records

2. **Create in batches per type**
 - All commodities first
 - Then all items
 - Finally all PM/JobPlans

3. **Log everything**
 - Success and failures
 - Helps with debugging
 - Audit trail for compliance

4. **Test with small dataset first**
 - Validate 1-10 tasks before full run
 - Catch issues early

5. **Have rollback plan**
 - OBSOLETE is irreversible
 - Cannot delete items
 - May need to create corrected versions

---

## Related Documentation

- **Quick Reference:** [`../MAXIMO-QUICK-REFERENCE.md`](../MAXIMO-QUICK-REFERENCE.md)
- **Full Specs:** [`maximo-specificaties.md`](./maximo-specificaties.md)
- **Update Details:** [`MAXIMO-INTEGRATIE-UPDATE.md`](./MAXIMO-INTEGRATIE-UPDATE.md)
- **Business Rules:** [`../src/validator/business_rules.py`](../src/validator/business_rules.py)

---

**Laatste Update:** 17 februari 2026
**Auteur:** Pedro Eduardo Cardoso
**Status:** Complete & Ready for Use

---

## AI Authenticiteitsverklaring

Tijdens het technisch onderzoek en ontwerp heb ik **Cursor AI** gebruikt om te **genereren van diagram templates, analyseren van API documentatie, en structureren van technische beslissingen**. Na het gebruik van deze tool heb ik de uitkomsten ervan uitvoerig gecontroleerd en aangepast om er voor te zorgen dat het ingeleverde werk mijn eigen competenties en leeruitkomsten reflecteert. Alle architecturale beslissingen, business rules en technische keuzes zijn gebaseerd op mijn eigen analyse en in overleg met stakeholders. Ik draag de volledige verantwoordelijkheid voor de inhoud van dit werk.

*AIAS Niveau: 3 - AI Samenwerking*
