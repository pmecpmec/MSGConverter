# Maximo Specificaties voor MSGConverter
## Item Master & Inventory Management

**Bron:** maximosecrets.com - Complete referentie voor Maximo items  
**Datum:** 17 februari 2026  
**Auteur:** Pedro Eduardo Cardoso

---

## 📋 Inhoudsopgave

1. [Item Structuur](#1-item-structuur)
2. [Item Statuses](#2-item-statuses)
3. [Item Sets & Organizations](#3-item-sets--organizations)
4. [Commodity Groups & Codes](#4-commodity-groups--codes)
5. [Verplichte Velden](#5-verplichte-velden)
6. [Validatie Regels](#6-validatie-regels)
7. [Business Rules voor MSGConverter](#7-business-rules-voor-msgconverter)

---

## 1. Item Structuur

### 1.1 Item Definitie

#### ITEMNUM (Item Number)
- **Type:** UPPER 30 (max 30 characters, uppercase)
- **Best Practice:** Gebruik autonumbering of max 12 karakters voor UI readability
- **Belangrijk:** Kan NIET worden gewijzigd na save
- **Belangrijk:** Kan NIET worden verwijderd (geen Delete Item actie)
- **Oplossing duplicaten:** Status op OBSOLETE zetten

#### DESCRIPTION
- **Type:** ALN 100 (max 100 characters)
- **Verplicht:** JA
- **Best Practice:** Zeer duidelijk en uniek (10,000+ items in systeem)
- **Zoekbaar:** Wordt gebruikt in Select Value lookups

#### Item Types
1. **ITEM** - Standaard items (storeroom inventory)
2. **TOOL** - Tool items (Stocked Tools application)
3. **STDSERVICE** - Standard Service (geen inventory)

### 1.2 Item Master Settings

#### Commodity Fields
- **COMMODITY (Commodity Group)** - 2-level hiërarchie
- **COMMODITY (Commodity Code)** - Specifieke code binnen group
- **Type:** UPPER 8 voor beide
- **Verplicht:** Nee, maar HIGHLY RECOMMENDED voor:
  - Zoekbaarheid (10,000+ items)
  - Purchase Order lines
  - Reporting & analysis
  - Vendor associations

#### Meter Fields
- **Meter Group** - Alleen voor Rotating Items
- **Meter** - Voor measured materials (petrol, diesel, oils)
  - Alleen Continuous type meters toegestaan

#### Other Settings
- **Maximum Quantity Issued** - Limiet voor totaal issued qty per asset
- **Receipt Tolerance %** - Over-receive percentage op PO's
- **Capitalized** - Read-only, change via "Change Capitalized Status"
- **Inspect on Receipt** - Inspection requirement
- **Add as Spare Part** - Auto-add to asset bij issue
- **Attach to Parent Asset on Issue** - Voor rotating items
- **Tax Exempt** - Tax exemption status

### 1.3 Item Classifications & Specifications

#### Classification System
- **CLASSIFICATION** - Categorisatie van item
- **CLASSPEC** - Specification attributes
- **Use Classification** - Voor description generation
- **Generate Description** - Auto-generate from attributes
- **Max Description:** 100 characters (let op!)

#### Attribute Search
- **Classification Search** - Drilldown per classification
- **Attribute Search** - Search op attribute values
- **Refine Action** - Narrow down results

### 1.4 Alternate Items

- **Purpose:** Interchangeable items aangeven
- **Use Case:** Verschillende brands van zelfde item type
- **Benefit:** Beschikbaarheid check bij stock-out

### 1.5 Item Assembly Structures

- **Purpose:** Subassemblies en spare parts voor assets
- **Restrictions:**
  - Max 3 levels praktisch (4+ wordt onoverzichtelijk)
  - Alleen bottom nodes mogen non-rotating zijn
  - Alle nodes met children moeten rotating zijn
- **Fields:**
  - **Quantity** - Hoeveel per level
  - **Remarks** - Positie indicatie
- **Actions:**
  - Copy Item Assembly Structure
  - Apply Item Assembly Structure (to Asset/Location)

---

## 2. Item Statuses

### 2.1 Status Hiërarchie

Items hebben status op **3 niveaus:**
1. **Item Level** - In Item Master/Tools/Service Items
2. **Item/Organization Level** - Per organization
3. **Inventory Level** - Per storeroom

### 2.2 Status Waarden

| Status | Code | Beschrijving | Gebruik |
|--------|------|--------------|---------|
| **PENDING** | PENDING | Nog niet gereed | Niet zichtbaar in lookups |
| **PLANNING** | PLANNING | In planning fase | Zichtbaar maar niet voor transactions |
| **ACTIVE** | ACTIVE | Volledig actief | Geen restricties |
| **PENDOBS** | PENDOBS | Pending Obsolescence | Geen nieuwe orders mogelijk |
| **OBSOLETE** | OBSOLETE | Verouderd | Niet meer bruikbaar, IRREVERSIBLE |

### 2.3 Status Beperkingen

#### PENDING Status
- ✅ Kan worden toegevoegd aan storeroom
- ❌ Niet zichtbaar in lookups
- ❌ Kan niet worden toegevoegd aan job plan, work order, purchasing docs

#### PLANNING Status
- ✅ Zichtbaar in lookups
- ✅ Kan worden toegevoegd aan job plan
- ✅ Kan worden toegevoegd aan work order (met reservations)
- ❌ Kan niet worden issued of transferred
- ❌ PO approval geblokkeerd
- ❌ Receiving geblokkeerd
- ❌ Sommige inventory adjustments geblokkeerd

#### ACTIVE Status
- ✅ Geen restricties
- ✅ Alle functies beschikbaar

#### PENDOBS Status
- ✅ Issues, returns, transfers mogelijk
- ❌ Reordering geblokkeerd
- ❌ PO approval geblokkeerd
- **Workflow:** Eerst Inventory → Organization → Item level

#### OBSOLETE Status
- ❌ Volledig geblokkeerd
- ❌ IRREVERSIBLE - kan niet terug!
- **Validaties voor OBSOLETE:**
  - ❌ Geen work plan references
  - ❌ Geen job plan references
  - ❌ Geen desktop requisition lines
  - ❌ Geen purchase requisition lines
  - ❌ Geen purchase order lines
  - ❌ Geen item balance
- **Checkbox:** "Roll New Status to Organizations and Inventory" wordt automatisch set

### 2.4 Default Status

#### Default Item Status in Sets
- **Veld:** Default Item Status
- **Verplicht:** JA
- **Opties:** PENDING, PLANNING, ACTIVE (alleen deze 3)
- **Gebruikt bij:** Nieuwe item creatie

#### Default Item Status in Organizations
- **Veld:** Default Item Status
- **Verplicht:** JA
- **Opties:** PENDING, PLANNING, ACTIVE (alleen deze 3)
- **Gebruikt bij:** Item/Organization Details creation

### 2.5 Status Change Regels

#### Roll Status Down
- **Item → Organization:** "Roll New Status to Organizations?"
- **Item → Inventory:** "Roll New Status to Inventory?"
- **Organization → Inventory:** Automatisch
- **WAARSCHUWING:** Bij OBSOLETE wordt checkbox automatisch set!

#### Status History
- Status changes worden getracked op alle 3 levels
- **Item level** - ITEMSTATUSHISTORY
- **Item/Organization level** - History tracking
- **Inventory level** - History tracking

---

## 3. Item Sets & Organizations

### 3.1 Item Sets

#### Definitie
- **Purpose:** Data sharing tussen organizations
- **Shared:** Same items across multiple organizations
- **Key:** ITEMSETID
- **Best Practice:** Gebruik common item set waar mogelijk

#### Item Set Regels
- Items worden **automatisch** associated met alle orgs in same item set
- ITEMORGINFO records worden **automatisch** gecreëerd
- Bij nieuwe org → alle items uit item set worden toegevoegd
- **CRITICAL:** Bij data loading moet item aan ALLE orgs in set worden toegevoegd!

### 3.2 Organizations

#### Definitie per Currency
- **Key Factor:** Base currency
- **Example:** 
  - France + Germany + Italy = Same org (Euro)
  - Poland = Different org (Złoty)
  - Romania = Different org (Leu)

#### Organization Rules
- Gebruikt voor **data sharing**
- Sites gebruikt voor **data separation**
- Item Set en Company Set ook voor data sharing
- **Design Factor:** ERP interface kan organization design restricteren

### 3.3 Multi-Language Support

#### Language Tables
- Item descriptions kunnen per language
- **Objects met language support:**
  - ITEM
  - CLASSIFICATION (optioneel configureren)
  - CLASSSTRUCTURE (optioneel configureren)
- **Benefit:** Same item set met verschillende languages per org

### 3.4 Item/Organization Details

Deze actie in Item Master heeft belangrijke fields:

#### Receipt Tolerance
- **Type:** Percentage
- **Purpose:** Over-receive limiet op PO's
- **Hierarchy:** 
  1. Inventory/Vendor record (hoogste priority)
  2. Inventory record
  3. Item/Organization level (default)

#### Tax Exempt
- **Type:** Checkbox
- **Defaulted from:** Item level
- **Used for:** Inventory/Vendor records default

#### Tax Code
- **Priority in Maximo:**
  1. Ship To Address (hoogste)
  2. Item/Vendor record
  3. Companies record
  4. Item/Organization level (laagste)
- **Multiple Tax Codes:** Max 27 via Database Configuration

#### Hazard
- **Purpose:** MSDS reference voor hazardous materials
- **Added to:** Work Order Safety Plans bij planned material

#### Status
- **Change Status button** in table window
- **Zie:** [Section 2: Item Statuses](#2-item-statuses)

#### Stock Category
- **Options:**
  - STK (Stocked) - default
  - NS (Non-Stocked)
  - SP (Special Order)
- **Rule:** Gebruik NS als item niet in storerooms

---

## 4. Commodity Groups & Codes

### 4.1 Structuur

#### Two-Level Hierarchy
- **Level 1:** Commodity Group (UPPER 8)
- **Level 2:** Commodity Code (UPPER 8)
- **Object:** COMMODITIES table
- **Parent Field:** NULL voor Group, populated voor Code
- **Key:** COMMODITY + ITEMSETID

### 4.2 Service Flag

#### Is Service
- **Checkbox:** Per commodity group/code
- **Purpose:** Filter services vs materials
- **Used in:** Service Items application
- **Service Type Values:**
  - PROCURE - Commodity codes (procurement)
  - PROVIDE - Service Groups (providing services)
  - BOTH - Both procurement and services

### 4.3 Gebruik in Maximo

#### Zoeken & Filtering
- **Item lookups:** Job Plan, Work Order, Asset Spare Parts
- **Benefit:** Narrow search in 10,000+ items
- **Search methods:**
  - Description search
  - Commodity Group filter
  - Commodity Code filter

#### Transacties & Reporting
Commodity info wordt geschreven naar:
- Material requisition lines
- Purchase requisition lines
- Request for quotation lines
- Purchase order lines
- Invoice lines
- Material receipts (MATRECTRANS)
- Service receipts (SERVRECTRANS)
- Issues & returns (MATUSETRANS)

**Purpose:** Material cost analysis & reporting

### 4.4 Associations

#### Companies Application
- **Action:** "Associate Commodities"
- **Purpose:** Class of items/services company provides
- **Note:** Lookup configuration required (not OOB)

#### People Application
- **Action:** "Associate Commodities"
- **Purpose:** Buyer responsibilities
- **Filters:** Organization, Site, Storeroom level
- **Note:** Configuration required for contract lookup

#### Contract Applications
- **Available in:**
  - Purchase Contracts
  - Lease/Rental Contracts
  - Master Contracts
- **NOT in:**
  - Labor Rate Contracts
  - Warranty Contracts
- **Purpose:** Commodity-based contract structure

### 4.5 UNSPSC Standard

#### United Nations Standard Products and Services Code
- **Format:** 8-digit number
- **Levels:** 4 levels × 2 digits
- **Benefit:** Worldwide standard
- **Available:** Spreadsheet voor members
- **Use:** Import als basis voor commodity structure

### 4.6 GL Account Integration

#### Chart of Accounts
- **Action:** "Resource Codes"
- **Purpose:** Default partial GL Account per commodity group
- **Used in:**
  - Work Plan Materials
  - Purchase Order Lines
- **Benefit:** Automatic accounting code assignment

---

## 5. Verplichte Velden

### 5.1 Item Master (ITEM Object)

| Veld | Type | Verplicht | Max Length | Opmerkingen |
|------|------|-----------|------------|-------------|
| ITEMNUM | UPPER | JA | 30 | Key field, immutable |
| DESCRIPTION | ALN | JA | 100 | Clear and unique |
| ITEMTYPE | ALN | JA | - | ITEM/TOOL/STDSERVICE |
| ITEMSETID | - | JA | - | From Sets application |
| STATUS | ALN | JA | - | Default from Set/Org |

### 5.2 Item/Organization Details

| Veld | Type | Verplicht | Max Length | Opmerkingen |
|------|------|-----------|------------|-------------|
| ITEMNUM | UPPER | JA | 30 | From Item |
| ORGID | - | JA | - | Organization |
| STATUS | ALN | JA | - | Default from Org |
| STOCKCATEGORY | - | JA | - | STK/NS/SP |

### 5.3 Inventory (Items in Storeroom)

| Veld | Type | Verplicht | Max Length | Opmerkingen |
|------|------|-----------|------------|-------------|
| ITEMNUM | UPPER | JA | 30 | From Item |
| LOCATION | - | JA | - | Storeroom |
| SITEID | - | JA | - | Site |
| STATUS | ALN | JA | - | Default from Item/Org |
| MINLEVEL | NUM | Aanbevolen | - | Reorder point |
| MAXLEVEL | NUM | Aanbevolen | - | Max stock |

### 5.4 Commodity Groups & Codes

| Veld | Type | Verplicht | Max Length | Opmerkingen |
|------|------|-----------|------------|-------------|
| COMMODITY | UPPER | JA | 8 | Code |
| ITEMSETID | - | JA | - | From Sets |
| PARENT | - | Voor Code | - | NULL voor Group |
| ISSERVICE | BOOL | JA | - | Service flag |

---

## 6. Validatie Regels

### 6.1 Item Creation Rules

#### ITEMNUM Validation
```python
def validate_itemnum(itemnum: str) -> bool:
    """
    Validate ITEMNUM field.
    
    Rules:
    - Max 30 characters
    - Uppercase only
    - Recommend max 12 for UI
    - No spaces (best practice)
    - No special characters (best practice)
    """
    if not itemnum:
        return False
    if len(itemnum) > 30:
        return False
    if itemnum != itemnum.upper():
        return False
    if len(itemnum) > 12:
        # Warning maar niet error
        logger.warning(f"ITEMNUM {itemnum} > 12 chars, UI scrolling required")
    return True
```

#### Description Validation
```python
def validate_description(description: str, itemnum: str) -> bool:
    """
    Validate DESCRIPTION field.
    
    Rules:
    - Required
    - Max 100 characters
    - Must be unique (practical requirement)
    - Should be meaningful for 10,000+ items search
    """
    if not description:
        return False
    if len(description) > 100:
        return False
    if len(description) < 10:
        # Warning voor te korte descriptions
        logger.warning(f"ITEMNUM {itemnum}: Description very short")
    return True
```

### 6.2 Status Validation Rules

#### Status Transition Validation
```python
def validate_status_transition(old_status: str, new_status: str) -> bool:
    """
    Validate status transitions.
    
    Rules:
    - OBSOLETE requires PENDOBS first
    - OBSOLETE is irreversible
    - Others can freely transition
    """
    if new_status == "OBSOLETE" and old_status != "PENDOBS":
        return False
    if old_status == "OBSOLETE":
        return False  # Cannot change from OBSOLETE
    return True
```

#### OBSOLETE Pre-Validation
```python
def validate_obsolete_allowed(itemnum: str, level: str) -> List[str]:
    """
    Validate if item can be set to OBSOLETE.
    
    Args:
        itemnum: Item number
        level: "ITEM" / "ITEMORG" / "INVENTORY"
    
    Returns:
        List of blocking reasons (empty = allowed)
    
    Validations:
    - No work plan references
    - No job plan references
    - No desktop requisition lines (MRLINE)
    - No purchase requisition lines
    - No purchase order lines
    - No item balance (for inventory level)
    """
    blocking_reasons = []
    
    # Check work plans
    if has_workplan_references(itemnum, level):
        blocking_reasons.append(f"Item exists on work plan at {level} level")
    
    # Check job plans
    if has_jobplan_references(itemnum, level):
        blocking_reasons.append(f"Item exists on job plan at {level} level")
    
    # Check MRLINE
    if has_mrline_references(itemnum, level):
        blocking_reasons.append(f"Item exists on desktop requisition at {level} level")
    
    # Check PR lines
    if has_pr_references(itemnum, level):
        blocking_reasons.append(f"Item exists on purchase requisition at {level} level")
    
    # Check PO lines
    if has_po_references(itemnum, level):
        blocking_reasons.append(f"Item exists on purchase order at {level} level")
    
    # Check balances (inventory level only)
    if level == "INVENTORY" and has_balance(itemnum):
        blocking_reasons.append(f"Item has remaining balance")
    
    return blocking_reasons
```

### 6.3 Commodity Validation

#### Commodity Code Validation
```python
def validate_commodity(commodity: str, is_group: bool, itemsetid: str) -> bool:
    """
    Validate commodity group/code.
    
    Rules:
    - Required: No (but HIGHLY recommended)
    - Max 8 characters
    - Uppercase only
    - Must exist in COMMODITIES table
    - If code, parent group must exist
    """
    if not commodity:
        return True  # Optional maar niet aanbevolen
    
    if len(commodity) > 8:
        return False
    
    if commodity != commodity.upper():
        return False
    
    # Check existence
    if not commodity_exists(commodity, itemsetid):
        return False
    
    # If code, validate parent
    if not is_group:
        parent = get_commodity_parent(commodity, itemsetid)
        if not parent:
            return False
    
    return True
```

### 6.4 Receipt Tolerance Validation

```python
def validate_receipt_tolerance(tolerance_pct: float) -> bool:
    """
    Validate receipt tolerance percentage.
    
    Rules:
    - Must be >= 0
    - Typically 0-25%
    - Warning if > 25%
    """
    if tolerance_pct < 0:
        return False
    
    if tolerance_pct > 25:
        logger.warning(f"Receipt tolerance {tolerance_pct}% is very high")
    
    return True
```

### 6.5 Stock Category Validation

```python
def validate_stock_category(stock_category: str, has_inventory: bool) -> bool:
    """
    Validate stock category.
    
    Rules:
    - Must be STK, NS, or SP
    - If no inventory across all sites → should be NS
    - SP only for special order items
    """
    valid_categories = ["STK", "NS", "SP"]
    
    if stock_category not in valid_categories:
        return False
    
    if not has_inventory and stock_category == "STK":
        logger.warning("Item marked STK but no inventory exists")
    
    return True
```

---

## 7. Business Rules voor MSGConverter

### 7.1 Item Creation Rules

#### ITEMS-1: ITEMNUM Generation
- **Rule:** Gebruik consistent nummer format voor MSG-3 items
- **Suggestion:** `MSG3-{ATA}-{TASK}` format
- **Example:** `MSG3-32-11-001` voor ATA 32, task 11-001
- **Max:** 30 chars (current format = 15 chars, safe)
- **Validation:** Uppercase, no spaces

#### ITEMS-2: Description Quality
- **Rule:** Description moet specifiek en zoekbaar zijn
- **Format:** `{Task Type} - {System} - {Component} - {Action}`
- **Example:** "Inspection - Landing Gear - Door - Visual Check"
- **Max:** 100 chars
- **Validation:** Min 20 chars voor duidelijkheid

#### ITEMS-3: Default Status
- **Rule:** Nieuwe items starten als PLANNING
- **Reason:** Allows job plan setup before production use
- **Workflow:** PLANNING → ACTIVE na goedkeuring
- **Organization Level:** Ook PLANNING

#### ITEMS-4: Commodity Mapping
- **Rule:** ALTIJD commodity group/code toewijzen
- **MSG-3 Mapping:**
  - ATA Chapter → Commodity Group
  - ATA System → Commodity Code
- **Example:** 
  - ATA 32 (Landing Gear) → Commodity Group: "ATA-32"
  - System 11 (Doors) → Commodity Code: "32-11"

### 7.2 Status Management Rules

#### STATUS-1: Initial Status
- **Item Level:** PLANNING (default)
- **Item/Org Level:** PLANNING (default)
- **Inventory Level:** N/A (geen inventory voor MSG-3 items)

#### STATUS-2: Activation Workflow
```
PLANNING (initial)
    ↓ (na review & approval)
ACTIVE (production ready)
    ↓ (als item wordt vervangen)
PENDOBS (phasing out)
    ↓ (na validaties passed)
OBSOLETE (retired)
```

#### STATUS-3: Geen Inventory
- **Rule:** MSG-3 items hebben GEEN inventory
- **Reason:** Tasks, not physical items
- **Stock Category:** NS (Non-Stocked)
- **Impact:** Status alleen op Item & Item/Org level

### 7.3 Organization Rules

#### ORG-1: Item Set Configuration
- **Rule:** Alle MSG-3 items in dedicated item set
- **Item Set Name:** "MSG3-MAINT" (example)
- **Shared Across:** Alle Babcock organizations bij Schiphol
- **Benefit:** Consistent maintenance tasks

#### ORG-2: Item/Organization Sync
- **Rule:** Bij nieuwe org → auto-add alle MSG-3 items
- **Handled by:** Maximo (automatic)
- **Validation:** Verify ITEMORGINFO records created

### 7.4 Data Quality Rules

#### QUALITY-1: No Duplicates
- **Rule:** Check duplicate items VOORDAT creatie
- **Check Fields:**
  - ITEMNUM (exact)
  - Description (similar)
  - ATA + Task combination
- **Action:** Warning + merge suggestion

#### QUALITY-2: Complete Data
- **Required Fields Check:**
  - ITEMNUM ✓
  - DESCRIPTION ✓
  - ITEMTYPE = "ITEM" ✓
  - STATUS = "PLANNING" ✓
  - STOCKCATEGORY = "NS" ✓
  - COMMODITY (Group) ✓
  - COMMODITY (Code) ✓

#### QUALITY-3: Validation Before Create
- **Pre-Creation Checks:**
  1. ITEMNUM format valid
  2. ITEMNUM niet in gebruik
  3. Description meaningful
  4. Commodity exists in COMMODITIES table
  5. Organization exists
  6. Item Set exists

### 7.5 Change Management Rules

#### CHANGE-1: Description Updates
- **Rule:** Description mag worden geüpdatet
- **Validation:** Max 100 chars
- **Version Control:** Log changes in change detection

#### CHANGE-2: Status Cannot Downgrade
- **Rule:** OBSOLETE is irreversible
- **Validation:** Check status transition validity
- **Alert:** Warn user bij OBSOLETE (requires PENDOBS first)

#### CHANGE-3: ITEMNUM Immutable
- **Rule:** ITEMNUM kan NOOIT worden gewijzigd
- **Workaround:** Oude item OBSOLETE + nieuw item maken
- **Change Detection:** Track als "retired + new"

### 7.6 Integration Rules

#### INTEGRATE-1: Create Before Reference
- **Rule:** Item MOET bestaan voordat gebruikt in Job Plan/PM
- **Validation:** Pre-check item existence
- **Error Handling:** Create item first, then job plan

#### INTEGRATE-2: Commodity Pre-Load
- **Rule:** Commodities moeten bestaan voor item creation
- **Action:** Load commodity structure EERST
- **Validation:** Check COMMODITIES table before item creation

#### INTEGRATE-3: Organization Pre-Check
- **Rule:** Organization MOET bestaan
- **Validation:** Check organization + item set combination
- **Error:** Clear error message als org missing

---

## 8. Mapping Specificaties MSG-3 → Maximo Items

### 8.1 Field Mapping

| MSG-3 Field | Maximo Field | Type | Required | Notes |
|-------------|--------------|------|----------|-------|
| Task Code | ITEMNUM | UPPER 30 | YES | Format: MSG3-{ATA}-{TASK} |
| Task Description | DESCRIPTION | ALN 100 | YES | Clear & unique |
| - | ITEMTYPE | ALN | YES | Always "ITEM" |
| - | ITEMSETID | - | YES | "MSG3-MAINT" |
| - | STATUS | - | YES | "PLANNING" initially |
| - | STOCKCATEGORY | - | YES | Always "NS" |
| ATA Chapter | COMMODITY (Group) | UPPER 8 | YES | e.g., "ATA-32" |
| ATA System | COMMODITY (Code) | UPPER 8 | YES | e.g., "32-11" |
| - | ROTATING | BOOL | YES | Always FALSE |
| - | LOTTYPE | - | NO | NULL |
| - | CONDITIONENABLED | BOOL | YES | FALSE |
| - | ISKIT | BOOL | YES | FALSE |

### 8.2 Item/Organization Mapping

| MSG-3 Field | Maximo Field | Type | Required | Notes |
|-------------|--------------|------|----------|-------|
| Task Code | ITEMNUM | UPPER 30 | YES | Same as Item |
| - | ORGID | - | YES | Current organization |
| - | STATUS | - | YES | "PLANNING" initially |
| - | STOCKCATEGORY | - | YES | "NS" |
| - | RECEIPTOL | NUM | NO | 0 (not applicable) |
| - | TAXEXEMPT | BOOL | NO | FALSE |

### 8.3 Validation bij Conversie

```python
def validate_msg3_item_for_maximo(msg3_task: dict) -> tuple[bool, list]:
    """
    Validate MSG-3 task kan worden geconverteerd naar Maximo item.
    
    Returns:
        (valid: bool, errors: list)
    """
    errors = []
    
    # ITEMNUM
    itemnum = generate_itemnum(msg3_task)
    if len(itemnum) > 30:
        errors.append(f"ITEMNUM too long: {itemnum}")
    if not itemnum.isupper():
        errors.append(f"ITEMNUM must be uppercase: {itemnum}")
    
    # DESCRIPTION
    desc = msg3_task.get("description", "")
    if len(desc) > 100:
        errors.append(f"Description too long: {len(desc)} chars")
    if len(desc) < 10:
        errors.append(f"Description too short: {desc}")
    
    # COMMODITY
    ata_chapter = msg3_task.get("ata_chapter")
    if not ata_chapter:
        errors.append("ATA Chapter missing for commodity group")
    
    ata_system = msg3_task.get("ata_system")
    if not ata_system:
        errors.append("ATA System missing for commodity code")
    
    return (len(errors) == 0, errors)
```

---

## 9. Implementatie Checklist

### 9.1 Voor Item Creation

- [ ] Verify Item Set exists ("MSG3-MAINT")
- [ ] Verify Organization exists and linked to Item Set
- [ ] Pre-load ALL Commodity Groups & Codes from MSG-3 ATA structure
- [ ] Validate ITEMNUM format and uniqueness
- [ ] Validate Description quality (length, uniqueness)
- [ ] Set Status = "PLANNING"
- [ ] Set STOCKCATEGORY = "NS"
- [ ] Set ROTATING = FALSE
- [ ] Set ISKIT = FALSE
- [ ] Set CONDITIONENABLED = FALSE
- [ ] Map ATA Chapter to Commodity Group
- [ ] Map ATA System to Commodity Code

### 9.2 Voor Item Updates

- [ ] Verify item exists (by ITEMNUM)
- [ ] Verify status transition is allowed
- [ ] Validate new Description if changed (max 100 chars)
- [ ] Log change in change detection system
- [ ] DO NOT attempt to change ITEMNUM (impossible)
- [ ] Check status before allowing updates (OBSOLETE = read-only)

### 9.3 Voor Item Deletion/Retirement

- [ ] Set status to PENDOBS first
- [ ] Validate no active references (work plans, job plans, etc.)
- [ ] Set status to OBSOLETE
- [ ] Log retirement in change detection
- [ ] Update documentation with retirement date

---

## 10. Error Scenarios & Handling

### 10.1 Common Errors

#### Error: "BMXAA4210E - Cannot change the value"
- **Cause:** Trying to change ITEMNUM after save
- **Solution:** Create new item with correct number, set old to OBSOLETE

#### Error: "Cannot set status to OBSOLETE"
- **Cause:** Item has active references or wrong status transition
- **Solution:** 
  1. Check current status (must be PENDOBS)
  2. Validate no references exist
  3. Check on correct level (Inventory → Org → Item)

#### Error: "Item not found in lookup"
- **Cause:** Item status is PENDING or OBSOLETE
- **Solution:** Check status, must be PLANNING or ACTIVE for lookups

#### Error: "Commodity not found"
- **Cause:** Commodity Group/Code doesn't exist in COMMODITIES table
- **Solution:** Create commodity structure first, then items

### 10.2 Validation Error Messages

```python
ERROR_MESSAGES = {
    "ITEMNUM_TOO_LONG": "ITEMNUM exceeds 30 characters: {itemnum}",
    "ITEMNUM_NOT_UPPER": "ITEMNUM must be uppercase: {itemnum}",
    "ITEMNUM_EXISTS": "ITEMNUM already exists: {itemnum}",
    "DESC_TOO_LONG": "Description exceeds 100 characters",
    "DESC_TOO_SHORT": "Description too short, recommend min 20 chars",
    "DESC_EMPTY": "Description is required",
    "COMMODITY_NOT_FOUND": "Commodity {commodity} not found in set {itemsetid}",
    "COMMODITY_TOO_LONG": "Commodity exceeds 8 characters: {commodity}",
    "STATUS_INVALID": "Invalid status: {status}",
    "STATUS_TRANSITION_INVALID": "Cannot transition from {old} to {new}",
    "OBSOLETE_HAS_REFERENCES": "Cannot set to OBSOLETE: {blocking_reasons}",
    "ITEMSET_NOT_FOUND": "Item Set not found: {itemsetid}",
    "ORG_NOT_FOUND": "Organization not found: {orgid}",
    "ORG_NOT_IN_ITEMSET": "Organization {orgid} not linked to Item Set {itemsetid}",
}
```

---

## 11. Testing Requirements

### 11.1 Unit Tests

```python
# Test ITEMNUM validation
def test_itemnum_validation():
    assert validate_itemnum("MSG3-32-11-001") == True
    assert validate_itemnum("msg3-32-11-001") == False  # Not uppercase
    assert validate_itemnum("A" * 31) == False  # Too long
    assert validate_itemnum("") == False  # Empty

# Test Description validation
def test_description_validation():
    assert validate_description("Short", "TEST") == False  # Too short
    assert validate_description("A" * 101, "TEST") == False  # Too long
    assert validate_description("Good description for test item", "TEST") == True

# Test Status transitions
def test_status_transitions():
    assert validate_status_transition("PENDING", "PLANNING") == True
    assert validate_status_transition("PLANNING", "ACTIVE") == True
    assert validate_status_transition("ACTIVE", "PENDOBS") == True
    assert validate_status_transition("PENDOBS", "OBSOLETE") == True
    assert validate_status_transition("ACTIVE", "OBSOLETE") == False  # Skip PENDOBS
    assert validate_status_transition("OBSOLETE", "ACTIVE") == False  # Irreversible

# Test Commodity validation
def test_commodity_validation():
    assert validate_commodity("ATA-32", True, "MSG3-MAINT") == True
    assert validate_commodity("TOOLONGCODE", True, "MSG3-MAINT") == False
    assert validate_commodity("ata-32", True, "MSG3-MAINT") == False  # Not uppercase
```

### 11.2 Integration Tests

```python
# Test complete item creation workflow
def test_create_msg3_item():
    msg3_task = {
        "task_code": "32-11-001",
        "description": "Inspection - Landing Gear - Door - Visual Check",
        "ata_chapter": "32",
        "ata_system": "11"
    }
    
    # Convert to Maximo format
    maximo_item = convert_msg3_to_maximo_item(msg3_task)
    
    # Validate
    assert maximo_item["ITEMNUM"] == "MSG3-32-11-001"
    assert len(maximo_item["DESCRIPTION"]) <= 100
    assert maximo_item["STATUS"] == "PLANNING"
    assert maximo_item["STOCKCATEGORY"] == "NS"
    assert maximo_item["COMMODITY_GROUP"] == "ATA-32"
    assert maximo_item["COMMODITY_CODE"] == "32-11"
```

---

## 12. Referenties

### 12.1 Maximo Secrets Artikelen

1. **Item Master**  
   URL: https://maximosecrets.com/2026/02/11/item-master/  
   Datum: 11 februari 2026

2. **Item Statuses**  
   URL: https://maximosecrets.com/2026/02/13/item-statuses-2/  
   Datum: 13 februari 2026

3. **Item Sets and Organizations**  
   URL: https://maximosecrets.com/2026/02/02/item-sets-and-organizations-and-item-types/  
   Datum: 2 februari 2026

4. **Commodity Groups and Codes**  
   URL: https://maximosecrets.com/2026/02/04/commodity-groups-and-codes/  
   Datum: 4 februari 2026

### 12.2 Maximo Objects

- **ITEM** - Main item table
- **ITEMORGINFO** - Item/Organization records
- **INVENTORY** - Item in storeroom (inventory)
- **COMMODITIES** - Commodity groups & codes
- **ITEMSTATUSHISTORY** - Status change tracking

### 12.3 Related MSGConverter Documents

- `docs/technisch-ontwerp/business-rules.md` - Business rules (80 rules)
- `src/validator/business_rules.py` - Business rules implementation
- `src/mapping/msg3_maximo_mapper.py` - Main mapping logic
- `docs/mapping/` - Field mapping specifications

---

## 📝 Change Log

| Datum | Auteur | Wijziging |
|-------|--------|-----------|
| 2026-02-17 | Pedro | Initial creation from maximosecrets.com research |

---

## ✅ Authenticiteitsverklaring

**AI-Gebruik:** Dit document is samengesteld met behulp van Cursor AI (Claude Sonnet 4.5).

**Mijn Bijdrage (Pedro):**
- ✅ Research opdracht gegeven aan AI
- ✅ Maximo Secrets website aangedragen als bron
- ✅ Structuur en focus bepaald
- ✅ Validatie van gegenereerde content
- ✅ Verificatie dat alle informatie relevant is voor MSGConverter
- ✅ Goedkeuring voor implementatie in project

**AI Bijdrage:**
- Content extractie uit Maximo Secrets artikelen
- Structurering in overzichtelijk document
- Validatie regels en code examples
- Error scenarios en handling
- Testing requirements

**Verificatie:** Ik heb de content gelezen, begrepen en goedgekeurd voor gebruik in dit project. De informatie is afkomstig van de officiële Maximo Secrets website (maximosecrets.com), een gerenommeerde bron voor Maximo documentatie.

**Datum:** 17 februari 2026  
**Student:** Pedro Eduardo Cardoso

---

## AI Authenticiteitsverklaring

Tijdens het technisch onderzoek en ontwerp heb ik **Cursor AI** gebruikt om te **genereren van diagram templates, analyseren van API documentatie, en structureren van technische beslissingen**. Na het gebruik van deze tool heb ik de uitkomsten ervan uitvoerig gecontroleerd en aangepast om er voor te zorgen dat het ingeleverde werk mijn eigen competenties en leeruitkomsten reflecteert. Alle architecturale beslissingen, business rules en technische keuzes zijn gebaseerd op mijn eigen analyse en in overleg met stakeholders. Ik draag de volledige verantwoordelijkheid voor de inhoud van dit werk.

*AIAS Niveau: 3 - AI Samenwerking*
