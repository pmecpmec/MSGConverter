# Maximo Quick Reference
## De 10 Belangrijkste Regels

**Voor:** Developers die werken met Maximo Item Master  
**Bron:** maximosecrets.com  
**Datum:** 17 februari 2026

---

## 🚨 TOP 10 CRITICAL RULES

### 1. ❌ ITEMNUM IS IMMUTABLE
```
ITEMNUM kan NOOIT worden gewijzigd na save!
→ Oude item OBSOLETE + nieuwe item maken
```

### 2. ❌ NO DELETE ACTION
```
Er is GEEN delete actie voor items!
→ Gebruik status OBSOLETE om items te retiren
```

### 3. ❌ OBSOLETE IS IRREVERSIBLE
```
OBSOLETE status kan NOOIT meer terug!
→ Requires PENDOBS status eerst
→ Check alle references voordat je OBSOLETE zet
```

### 4. ⚠️ MAX FIELD LENGTHS
```
ITEMNUM:    30 characters (recommend 12 for UI)
DESCRIPTION: 100 characters
COMMODITY:   8 characters (Group & Code)
```

### 5. ✅ ITEMS FIRST, THEN PM/JOBPLAN
```
Volgorde is CRITICAL:
1. Commodities
2. Items
3. PM records
4. JobPlan records
```

### 6. ✅ STATUS WORKFLOW
```
PENDING → PLANNING → ACTIVE → PENDOBS → OBSOLETE
         ↑ Start here          ↑ Required for OBSOLETE
```

### 7. ✅ UPPERCASE ONLY
```
ITEMNUM:   UPPERCASE (convention)
COMMODITY: UPPERCASE (required)
```

### 8. ✅ MSG-3 ITEMS ARE NON-STOCKED
```
STOCKCATEGORY = "NS"
→ Tasks zijn geen fysieke items
→ Geen inventory records
```

### 9. ✅ ALWAYS USE COMMODITIES
```
HIGHLY RECOMMENDED (not technically required)
→ Needed voor search in 10,000+ items
→ Needed voor reporting & analysis
```

### 10. ✅ VALIDATE BEFORE CREATE
```
Check ALLES voordat je naar Maximo stuurt:
✓ Field lengths
✓ Uppercase
✓ No spaces in ITEMNUM
✓ Commodity exists
✓ Organization exists
```

---

## 📊 Field Limits Cheat Sheet

| Field | Max Length | Type | Notes |
|-------|------------|------|-------|
| ITEMNUM | 30 | UPPER | Immutable! Recommend ≤12 |
| DESCRIPTION | 100 | ALN | Must be unique & clear |
| COMMODITY (Group) | 8 | UPPER | Format: ATA-{chapter} |
| COMMODITY (Code) | 8 | UPPER | Format: {chapter}-{system} |
| PMNUM | 30 | UPPER | Same as ITEMNUM |
| JPNUM | 30 | UPPER | Same as ITEMNUM |

---

## 🔄 Status Transitions

```
✅ ALLOWED:
PENDING → PLANNING
PENDING → ACTIVE
PLANNING → ACTIVE
ACTIVE → PENDOBS
PENDOBS → OBSOLETE
(Any → Any except from OBSOLETE)

❌ NOT ALLOWED:
Any → OBSOLETE (without PENDOBS first)
OBSOLETE → Any (irreversible!)
```

---

## 🚀 MSG-3 Mapping Format

```python
# ITEMNUM
Format: MSG3-{task_code}
Example: MSG3-32-11-01-001
Max: 30 chars (current = ~17, safe!)

# Commodity Group
Format: ATA-{chapter}
Example: ATA-32
Max: 8 chars

# Commodity Code
Format: {chapter}-{system}
Example: 32-11
Max: 8 chars
```

---

## ⚡ Quick Validation Code

```python
# ITEMNUM
assert len(itemnum) <= 30, "ITEMNUM too long!"
assert itemnum == itemnum.upper(), "ITEMNUM must be uppercase!"
assert " " not in itemnum, "No spaces in ITEMNUM!"

# Description
assert len(description) <= 100, "Description too long!"
assert len(description) >= 10, "Description too short!"

# Commodity
assert len(commodity) <= 8, "Commodity too long!"
assert commodity == commodity.upper(), "Commodity must be uppercase!"

# Status
assert status in ["PENDING", "PLANNING", "ACTIVE", "PENDOBS", "OBSOLETE"]
if new_status == "OBSOLETE":
    assert old_status == "PENDOBS", "Must be PENDOBS first!"
if old_status == "OBSOLETE":
    raise ValueError("Cannot change from OBSOLETE!")
```

---

## 🎯 Creation Checklist

```
Voor ELKE item creation:
☐ ITEMNUM ≤ 30 chars & uppercase
☐ ITEMNUM is unique
☐ Description ≤ 100 chars
☐ Description is meaningful
☐ Commodity Group exists (≤ 8 chars, uppercase)
☐ Commodity Code exists (≤ 8 chars, uppercase)
☐ Status = "PLANNING" (recommended start)
☐ STOCKCATEGORY = "NS" (for MSG-3)
☐ ITEMTYPE = "ITEM"
☐ ROTATING = FALSE
☐ ISKIT = FALSE
```

---

## 🛑 OBSOLETE Checklist

```
Voor ELKE OBSOLETE operation:
☐ Current status is PENDOBS (required!)
☐ No work plan references
☐ No job plan references
☐ No desktop requisition lines
☐ No purchase requisition lines
☐ No purchase order lines
☐ No item balance (if inventory level)
☐ WARNING given to user (irreversible!)
☐ Rollback plan exists (create new item)
```

---

## 📚 Full Documentation

- **Complete specs:** `docs/maximo-specificaties.md`
- **All changes:** `docs/MAXIMO-INTEGRATIE-UPDATE.md`
- **Business rules:** `src/validator/business_rules.py`
- **Mapping code:** `src/mapping/`

---

## 🆘 Common Errors

### "Cannot change the value"
→ Trying to change ITEMNUM (immutable!)
→ Solution: Create new item, set old to OBSOLETE

### "Cannot set status to OBSOLETE"
→ Not at PENDOBS status or has references
→ Solution: Set to PENDOBS first, check references

### "Item not found in lookup"
→ Item status is PENDING or OBSOLETE
→ Solution: Check status, must be PLANNING or ACTIVE

### "Commodity not found"
→ Commodity doesn't exist in COMMODITIES table
→ Solution: Create commodities FIRST

### "Foreign key violation"
→ Referenced object doesn't exist (item, commodity, etc.)
→ Solution: Create in correct order (see rule #5)

---

**Print dit uit en hang naast je scherm! 📌**

**Laatste update:** 17 februari 2026  
**Auteur:** Pedro Eduardo Cardoso
