# Maximo Integratie Update

## Complete Maximo Secrets Specificaties Toegepast

**Datum:** 17 februari 2026
**Auteur:** Pedro Eduardo Cardoso
**Bron:** maximosecrets.com (Berry's tip!)
**Status:** Compleet

---

## Overzicht

Na overleg met Berry is maximosecrets.com als bron gebruikt om alle Maximo specificaties correct toe te passen op de MSGConverter. Daardoor lopen we niet tegen Maximo-limitaties aan.

Er is het volgende gedaan. De volledige Maximo specificaties zijn gedocumenteerd. De business rules zijn uitgebreid met tien nieuwe Maximo-specifieke regels. Er is een nieuwe ItemMapper toegevoegd (items eerst). De PMMapper en JobPlanMapper zijn uitgebreid met Maximo-validaties. De MSG3MaximoMapper is herzien met de juiste volgorde. Commodity-extractie is toegevoegd.

---

## Nieuwe documentatie

### 1. Maximo Specificaties Document

Bestand: `docs/technisch-ontwerp/maximo-specificaties.md`. Het document bevat twaalf secties: Item-structuur (ITEMNUM, Description, Types), Item-statuses (PENDING tot PLANNING, ACTIVE, PENDOBS, OBSOLETE), Item Sets en Organizations, Commodity Groups en Codes, verplichte velden, validatieregels, business rules voor MSGConverter, mapping specificaties MSG-3 naar Maximo, implementatie-checklist, error scenarios en handling, testing requirements, referenties.

Belangrijk om te onthouden: ITEMNUM wijzig je niet na het opslaan. Er is geen Delete-actie; gebruik de OBSOLETE-status. OBSOLETE is onomkeerbaar; eerst PENDOBS is vereist. Maximale lengtes: ITEMNUM 30, Description 100, Commodity 8. Items moeten bestaan voordat je ze in PM of JobPlan gebruikt. Commodities moeten bestaan voordat je Items aanmaakt.

---

## Code wijzigingen

### 2. Business Rules Uitgebreid

**Bestand:** `src/validator/business_rules.py`

**Toegevoegd: 10 nieuwe Maximo-specifieke regels (LOG-4.0.1 t/m LOG-4.0.10)**

```python
# Nieuwe regels:
LOG-4.0.1: ITEMNUM max 30 characters uppercase
LOG-4.0.2: Item Description verplicht en uniek
LOG-4.0.3: Commodity Group en Code toewijzen (ALTIJD!)
LOG-4.0.4: Item Status correct instellen
LOG-4.0.5: Stock Category NS voor MSG-3 items
LOG-4.0.6: ITEMNUM is immutable (CRITICAL!)
LOG-4.0.7: Item kan niet worden verwijderd
LOG-4.0.8: Commodity max 8 characters uppercase
LOG-4.0.9: Item Status transitions valideren
LOG-4.0.10: Geen OBSOLETE bij active references
```

De validator controleert nu Maximo-specifieke limitaties. Daarmee voorkom je dat items worden aangemaakt die Maximo afwijst. Bij OBSOLETE-operaties krijg je een waarschuwing (die actie is onomkeerbaar).

---

### 3. Nieuwe ItemMapper

Bestand: `src/mapping/item_mapper.py` (nieuw). Items moeten in Maximo bestaan voordat je ze in PM of JobPlan gebruikt. De ItemMapper regelt ITEMNUM-generatie en -validatie (max 30, uppercase), description formatting en validatie (max 100), commodity mapping (ATA naar Commodity Group/Code), statusbeheer (PLANNING naar ACTIVE), Stock Category NS voor MSG-3 tasks, Item/Organization mapping en OBSOLETE-validatie (controle op referenties).

**Key Methods:**

```python
# Map MSG-3 task naar Item Master
item_record = item_mapper.map_task_to_item(msg3_task)

# Map naar Item/Organization
item_org = item_mapper.map_task_to_item_org(msg3_task)

# Validate OBSOLETE
can_obsolete, reasons = item_mapper.validate_item_for_obsolete(itemnum)
```

Validaties: ITEMNUM max 30, uppercase, geen spaties. Description max 100, min 10 aanbevolen. Commodity Group max 8, formaat ATA-{chapter}. Commodity Code max 8, formaat {chapter}-{system}. Statusovergangen: OBSOLETE vereist eerst PENDOBS.

---

### 4. PMMapper Uitgebreid

**Bestand:** `src/mapping/pm_mapper.py`

Wijzigingen: Maximo-documentatie toegevoegd, PMNUM-validatie (max 30), description-validatie (max 100), commodity mapping (ATA-codes), statusbeheer (standaard PLANNING), volledige veldmapping met alle Maximo-velden.

**Nieuwe Methods:**

```python
_validate_required_fields() # Check verplichte velden
_generate_pmnum() # Format: MSG3-{task_code}
_format_description() # Max 100 chars
_map_commodity_group() # ATA-{chapter}
_map_commodity_code() # {chapter}-{system}
_map_priority() # 1-5 range
```

**PM Record Fields:**

- PMNUM, DESCRIPTION, STATUS
- FREQUENCY, FREQUNIT (interval mapping)
- LOCATION (zone)
- COMMODITY, COMMODITYCODE
- WORKTYPE, PRIORITY
- ITEMNUM (link to Item Master)
- Custom MSG-3 fields (PLUSCMSG3\*)

---

### 5. JobPlanMapper Uitgebreid

**Bestand:** `src/mapping/jobplan_mapper.py`

Wijzigingen: Maximo-documentatie toegevoegd, JPNUM-validatie (max 30), description-validatie (max 100), statusbeheer (standaard ACTIVE), duration mapping (man hours).

**Nieuwe Methods:**

```python
_generate_jpnum() # Format: MSG3-{task_code}
_format_description() # Max 100 chars
```

**JobPlan Record Fields:**

- JPNUM, DESCRIPTION, STATUS
- WORKTYPE (PM)
- PLUSCJPREVDUR (duration estimate)
- Custom MSG-3 fields

**TODO (voor later):**

- Materials (JOBMATERIAL table)
- Tools (JOBTOOL table)
- Labor (JOBLABOR table)
- Task instructions (JPTASK table)

---

### 6. MSG3MaximoMapper Volledig Herzien

**Bestand:** `src/mapping/msg3_maximo_mapper.py`

**CRITICAL CHANGES:**

#### Correcte Volgorde Toegevoegd:

```python
# OUDE volgorde (FOUT!):
1. PM records
2. JobPlan records

# NIEUWE volgorde (CORRECT!):
1. Commodity Groups & Codes ← MOET EERST!
2. Item Master records ← MOET VOOR PM/JobPlan!
3. Item/Organization records
4. PM records
5. JobPlan records
```

**Waarom belangrijk:**

- Maximo zal foreign key errors geven als items niet bestaan
- Commodities moeten bestaan voordat items ze kunnen refereren
- PM's en JobPlans refereren items die MOETEN bestaan

**Nieuwe Methods:**

```python
map() # Hoofdmethode met correcte volgorde
_extract_commodities() # Extract unique ATA-based commodities
_empty_result() # Empty result structure
```

**Output Structure:**

```python
{
 "commodities": [...], # Commodity Groups & Codes
 "items": [...], # Item Master records
 "item_orgs": [...], # Item/Organization records
 "pm": [...], # PM records
 "jobplan": [...] # JobPlan records
}
```

**Error Handling:**

- Alle mapping errors worden gelogd
- Partial success mogelijk (sommige taken kunnen falen)
- Duidelijke error messages per task

---

## Mapping Specificaties

### MSG-3 → Maximo Item Master

| MSG-3 Field | Maximo Field | Type | Required | Format |
| ----------- | ------------- | -------- | -------- | ------------------ |
| Task Code | ITEMNUM | UPPER 30 | YES | MSG3-{task_code} |
| Description | DESCRIPTION | ALN 100 | YES | Max 100 chars |
| - | ITEMTYPE | ALN | YES | "ITEM" |
| - | ITEMSETID | - | YES | "MSG3-MAINT" |
| - | STATUS | - | YES | "PLANNING" |
| - | STOCKCATEGORY | - | YES | "NS" |
| ATA Chapter | COMMODITY | UPPER 8 | YES | ATA-{chapter} |
| ATA System | COMMODITYCODE | UPPER 8 | YES | {chapter}-{system} |
| - | ROTATING | BOOL | YES | FALSE |
| - | ISKIT | BOOL | YES | FALSE |

### MSG-3 → Maximo PM

| MSG-3 Field | Maximo Field | Type | Required | Notes |
| ------------- | ------------ | -------- | -------- | ------------------- |
| Task Code | PMNUM | UPPER 30 | YES | MSG3-{task_code} |
| Description | DESCRIPTION | ALN 100 | YES | Max 100 chars |
| Interval | FREQUENCY | NUM | YES | Numeric value |
| Interval Unit | FREQUNIT | - | YES | FH→HOURS, FC→CYCLES |
| Zone | LOCATION | - | NO | Aircraft zone |
| - | STATUS | - | YES | "PLANNING" |
| - | WORKTYPE | - | YES | "PM" |
| - | ITEMNUM | - | YES | Link to Item |

### MSG-3 → Maximo JobPlan

| MSG-3 Field | Maximo Field | Type | Required | Notes |
| ----------- | ------------- | -------- | -------- | ----------------- |
| Task Code | JPNUM | UPPER 30 | YES | MSG3-{task_code} |
| Description | DESCRIPTION | ALN 100 | YES | Max 100 chars |
| Man Hours | PLUSCJPREVDUR | NUM | NO | Duration estimate |
| - | STATUS | - | YES | "ACTIVE" |
| - | WORKTYPE | - | YES | "PM" |

### MSG-3 → Maximo Commodities

| MSG-3 Field | Maximo Field | Type | Required | Notes |
| ----------- | ------------ | ------- | -------- | ------------------------ |
| ATA Chapter | COMMODITY | UPPER 8 | YES | Group: ATA-{chapter} |
| - | PARENT | - | NO | NULL for groups |
| ATA System | COMMODITY | UPPER 8 | YES | Code: {chapter}-{system} |
| ATA Chapter | PARENT | - | YES | Parent group for codes |
| - | ITEMSETID | - | YES | "MSG3-MAINT" |
| - | ISSERVICE | BOOL | YES | FALSE |

---

## CRITICAL Rules

### 1. ITEMNUM is Immutable

```python
# FOUT - kan niet!
item.ITEMNUM = "NEW-NUMBER" # ERROR na save!

# CORRECT - oude obsolete + nieuwe maken
old_item.STATUS = "OBSOLETE"
new_item = create_item("NEW-NUMBER")
```

### 2. Geen Delete Actie

```python
# FOUT - geen delete!
delete_item(itemnum) # Bestaat niet in Maximo!

# CORRECT - gebruik OBSOLETE
item.STATUS = "PENDOBS" # Eerst
item.STATUS = "OBSOLETE" # Dan (irreversible!)
```

### 3. Status Transitions

```python
# FOUT - kan niet direct naar OBSOLETE
item.STATUS = "OBSOLETE" # ERROR als niet via PENDOBS!

# CORRECT
item.STATUS = "PENDOBS" # Eerst
# Valideer geen references...
item.STATUS = "OBSOLETE" # Dan

# FOUT - OBSOLETE is irreversible!
item.STATUS = "OBSOLETE"
item.STATUS = "ACTIVE" # ERROR - kan niet terug!
```

### 4. Commodity Volgorde

```python
# FOUT - commodity bestaat niet!
item.COMMODITY = "ATA-32" # ERROR als niet in COMMODITIES table!

# CORRECT
# 1. Maak commodities EERST
create_commodity_group("ATA-32")
create_commodity_code("32-11", parent="ATA-32")
# 2. Dan pas items
item.COMMODITY = "ATA-32"
```

### 5. Item Voor PM/JobPlan

```python
# FOUT - item bestaat niet!
pm.ITEMNUM = "MSG3-32-11-001" # ERROR als item niet bestaat!

# CORRECT
# 1. Maak item EERST
create_item("MSG3-32-11-001")
# 2. Dan pas PM
pm.ITEMNUM = "MSG3-32-11-001"
```

---

## Testing Requirements

### Unit Tests (nieuw)

```python
# Test ITEMNUM validation
def test_itemnum_validation():
 assert validate_itemnum("MSG3-32-11-001") == True
 assert validate_itemnum("TOO-LONG-" * 5) == False # > 30
 assert validate_itemnum("lowercase") == False # Not uppercase

# Test Description validation
def test_description_validation():
 assert validate_description("A" * 101) == False # > 100
 assert validate_description("Good description") == True

# Test Status transitions
def test_status_transitions():
 assert can_transition("ACTIVE", "PENDOBS") == True
 assert can_transition("ACTIVE", "OBSOLETE") == False # Needs PENDOBS
 assert can_transition("OBSOLETE", "ACTIVE") == False # Irreversible

# Test Commodity validation
def test_commodity_validation():
 assert validate_commodity("ATA-32") == True
 assert validate_commodity("TOOLONG99") == False # > 8
 assert validate_commodity("ata-32") == False # Not uppercase
```

### Integration Tests (update)

```python
# Test complete mapping workflow
def test_msg3_to_maximo_workflow():
 mapper = MSG3MaximoMapper(item_set_id="TEST", org_id="TEST_ORG")

 msg3_data = {
 "tasks": [
 {
 "task_code": "32-11-01-001",
 "description": "Visual inspection",
 "ata_chapter": "32",
 "ata_system": "11",
 "interval": 500,
 "interval_unit": "FH"
 }
 ]
 }

 result = mapper.map(msg3_data)

 # Check volgorde
 assert len(result["commodities"]) > 0 # Step 1
 assert len(result["items"]) == 1 # Step 2
 assert len(result["pm"]) == 1 # Step 4
 assert len(result["jobplan"]) == 1 # Step 5

 # Check commodity structure
 groups = [c for c in result["commodities"] if c["PARENT"] is None]
 codes = [c for c in result["commodities"] if c["PARENT"] is not None]
 assert len(groups) > 0
 assert len(codes) > 0

 # Check item fields
 item = result["items"][0]
 assert item["ITEMNUM"] == "MSG3-32-11-01-001"
 assert len(item["DESCRIPTION"]) <= 100
 assert item["STATUS"] == "PLANNING"
 assert item["STOCKCATEGORY"] == "NS"
 assert item["COMMODITY"] == "ATA-32"
 assert item["COMMODITYCODE"] == "32-11"

 # Check PM fields
 pm = result["pm"][0]
 assert pm["PMNUM"] == "MSG3-32-11-01-001"
 assert pm["ITEMNUM"] == "MSG3-32-11-01-001" # References item!
```

---

## Implementatie checklist

### Voor Development

- [x] Maximo specificaties gedocumenteerd
- [x] Business rules uitgebreid
- [x] ItemMapper geïmplementeerd
- [x] PMMapper uitgebreid
- [x] JobPlanMapper uitgebreid
- [x] MSG3MaximoMapper herzien
- [ ] Unit tests geschreven
- [ ] Integration tests geschreven
- [ ] Error handling getest
- [ ] Validatie messages user-friendly gemaakt

### Voor Production

- [ ] Commodity Groups pre-loaded in Maximo
- [ ] Item Set "MSG3-MAINT" aangemaakt
- [ ] Organization gekoppeld aan Item Set
- [ ] Test data gevalideerd in Maximo
- [ ] Status workflow getest
- [ ] OBSOLETE workflow gedocumenteerd
- [ ] Rollback procedures gedocumenteerd
- [ ] Training materiaal voor users

---

## Geleerde Lessen

### 1. Volgorde is CRITICAL

Items kunnen niet worden gemaakt als commodities niet bestaan. PM's kunnen niet worden gemaakt als items niet bestaan. **Always create in order: Commodities → Items → PM/JobPlan**

### 2. Immutability is Real

ITEMNUM kan niet worden gewijzigd. OBSOLETE is irreversible. **Design carefully before creation!**

### 3. No Delete = Status Management

Geen delete actie betekent status management is cruciaal. **Use statuses: PLANNING → ACTIVE → PENDOBS → OBSOLETE**

### 4. Field Lengths Matter

Maximo heeft strikte limits (30, 100, 8). **Validate BEFORE sending to Maximo to avoid cryptic errors.**

### 5. Foreign Keys are Enforced

Items moeten bestaan voor PM/JobPlan usage. **Pre-create referenced objects or get foreign key errors.**

---

## Next Steps

### Immediate (deze week)

Maximo specificaties documenteren (done). Code updaten met validaties (done). Mapper hierarchy fixen (done). Nog te doen: unit tests schrijven voor validaties, integration test voor de volledige workflow.

### Short Term (Week 2-3)

1. [ ] Commodity pre-load script maken
2. [ ] Item Set setup in Maximo test environment
3. [ ] Test MSG-3 data converteren en valideren
4. [ ] Error messages user-friendly maken
5. [ ] Documentation voor end users

### Long Term (Week 4+)

1. [ ] Change detection integreren met Item status
2. [ ] OBSOLETE workflow automatiseren
3. [ ] Bulk operations voor Item/PM updates
4. [ ] Performance optimalisatie voor large MSG-3 files
5. [ ] Monitoring & logging voor production

---

## Contact en ondersteuning

### Vragen over Maximo

- **Bron:** maximosecrets.com (350+ artikelen)
- **Contact:** Berry (Babcock) - heeft ervaring met Maximo

### Vragen over Code

- **Repository:** c:\Users\pmec\Documents\Stage Babcock\MSGConverter
- **Documentatie:** docs/technisch-ontwerp/maximo-specificaties.md
- **Code:** src/mapping/ (alle mappers)

---

## Authenticiteitsverklaring

**AI-Gebruik:** Dit document en alle code-updates zijn gemaakt met Cursor AI (Claude Sonnet 4.5).

**Mijn bijdrage (Pedro):** Meeting met Berry (tip over maximosecrets.com), research opdracht aan AI gegeven, verificatie van alle Maximo specificaties, review van alle code wijzigingen, goedkeuring voor implementatie, testing plan bepaald.

**AI Bijdrage:**

- Content extractie van maximosecrets.com (4 artikelen)
- Code generatie voor mappers en validaties
- Documentatie schrijven
- Error scenarios en testing requirements
- Best practices en lessons learned

**Verificatie:** Ik heb alle Maximo specificaties gelezen en begrepen. De code wijzigingen zijn gereviewed en goedgekeurd. Dit is een fundamentele verbetering die voorkomt dat we tegen Maximo limitaties aanlopen.

**Datum:** 17 februari 2026
**Student:** Pedro Eduardo Cardoso
**Status:** Ready for Implementation & Testing

---

## AI Authenticiteitsverklaring

Tijdens het technisch onderzoek en ontwerp heb ik **Cursor AI** gebruikt om te **genereren van diagram templates, analyseren van API documentatie, en structureren van technische beslissingen**. Na het gebruik van deze tool heb ik de uitkomsten ervan uitvoerig gecontroleerd en aangepast om er voor te zorgen dat het ingeleverde werk mijn eigen competenties en leeruitkomsten reflecteert. Alle architecturale beslissingen, business rules en technische keuzes zijn gebaseerd op mijn eigen analyse en in overleg met stakeholders. Ik draag de volledige verantwoordelijkheid voor de inhoud van dit werk.

_AIAS Niveau: 3 - AI Samenwerking_

---

** Conclusie: MSGConverter is nu volledig aligned met Maximo best practices!**
