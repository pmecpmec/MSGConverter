# 🚨 BUSINESS RULES FIRST - Critical Development Guideline

**⚠️ LEES DIT EERST VOORDAT JE BEGINT MET DEVELOPMENT**

---

## 📋 Core Principle

> **"Alle ontwikkeling moet compliant zijn met de 80 Babcock @ Schiphol business rules"**

Dit is **NIET OPTIONEEL**. De business rules zijn de basis van:
- ✅ Alle validaties
- ✅ Alle data transformaties
- ✅ Alle workflows
- ✅ Alle integraties
- ✅ Alle beslissingen

---

## 🎯 Waarom Dit Zo Belangrijk Is

### Veiligheid
- **11 CRITICAL rules** die directe veiligheidsrisico's blokkeren
- Airside access vereist strikte compliance
- PBM, VGB-screening, certificeringen zijn niet negocieerbaar

### Compliance
- ISO 9001 en ISO 45001 verplicht
- GDPR compliance
- NEN-normen
- Schiphol-specifieke regelgeving

### Operationele Continuïteit
- SLA compliance voorkomt boetes
- Correcte planning voorkomt verstoringen
- Kwaliteitscontroles voorkomen uitval

### Juridische Bescherming
- Documentatie van naleving
- Audit trail
- Liability protection

---

## 📚 Business Rules Locaties

### 1. Implementation
```
src/validator/business_rules.py
```
- Alle 80 rules gedefinieerd
- Validatie framework
- Production-ready code

### 2. Complete Documentation
```
docs/technisch-ontwerp/business-rules.md
```
- Volledige beschrijvingen
- Validatie voorbeelden
- Implementation guide

### 3. Quick Reference
```
docs/technisch-ontwerp/business-rules-quick-reference.md
```
- Snelle lookup
- Code voorbeelden
- Critical rules lijst

---

## 🔴 11 Critical Rules - ALTIJD CHECKEN

Deze rules blokkeren processing en MOETEN worden gevalideerd:

| ID | Rule | Categorie |
|----|------|-----------|
| **SEC-1.1** | Geldige Schiphol-pas vereist | Security |
| **SEC-1.2** | VGB-screening voor airside | Security |
| **SEC-1.8** | PBM verplicht in operationele zones | Security |
| **OPS-2.4** | Alleen gecertificeerde elektriciens | Operations |
| **OPS-2.8** | PTW voor risicovol werk | Operations |
| **OPS-2.9** | TRA verplicht | Operations |
| **QUA-3.10** | Geldige certificeringen vereist | Quality |
| **PLN-5.3** | Werkvergunning vereist voor start | Planning |
| **IT-6.3** | GDPR-richtlijnen | IT Systems |
| **HR-7.8** | Alcohol/drugs verboden | HR |
| **HR-7.10** | Schiphol-pas verlies direct melden | HR |

---

## 💻 Development Workflow

### Bij Elk Development Task

#### ✅ STAP 1: Identificeer Relevante Rules
```python
# Vraag jezelf af:
# - Welke business rules zijn van toepassing?
# - Welke categorie(ën) zijn relevant?
# - Zijn er critical rules die ik moet checken?
```

#### ✅ STAP 2: Implementeer Validatie
```python
from src.validator.business_rules import BusinessRulesValidator, RuleCategory

validator = BusinessRulesValidator()

# Valideer je data
violations = validator.validate(data)

# Of specifieke categorie
violations = validator.validate_by_category(data, RuleCategory.SECURITY)
```

#### ✅ STAP 3: Handle Violations
```python
if violations:
    critical_violations = [v for v in violations 
                          if v.rule.severity == RuleSeverity.CRITICAL]
    
    if critical_violations:
        # BLOKKEER PROCESSING
        raise CriticalRuleViolation(critical_violations)
    
    # Log andere violations
    for violation in violations:
        logger.warning(f"{violation.rule.rule_id}: {violation.message}")
```

#### ✅ STAP 4: Documenteer Compliance
```python
# In je code documentatie:
"""
Business Rules Compliance:
- SEC-1.1: Schiphol-pas validated ✅
- SEC-1.2: VGB-screening checked ✅
- OPS-2.8: PTW verification implemented ✅
"""
```

---

## 🏗️ Per Module Guidelines

### Parser Module
**Relevante Rules:** IT-6.1, QUA-3.2, IT-6.8

```python
# Bij het parsen van MSG-3 Excel:
# - IT-6.1: Data moet in centrale systeem (Maximo)
# - QUA-3.2: Documentatie binnen 24 uur
# - IT-6.8: Foto's toevoegen (INFO level)
```

### Validator Module
**Relevante Rules:** ALLE 80 RULES

```python
# Validator MOET alle rules kunnen valideren
# - Implementeer validation_func voor elke rule
# - Check critical rules eerst
# - Log alle violations
```

### Mapping Module
**Relevante Rules:** QUA-3.4, LOG-4.2, IT-6.1

```python
# Bij mapping MSG-3 → Maximo:
# - QUA-3.4: Alleen goedgekeurde materialen
# - LOG-4.2: Materialen op juiste werkorder
# - IT-6.1: Gebruik Maximo als centrale systeem
```

### Change Detection Module
**Relevante Rules:** QUA-3.3, COM-8.9, QUA-3.2

```python
# Bij detecteren van wijzigingen:
# - QUA-3.3: Registreer afwijkingen
# - COM-8.9: Meld afwijkingen direct
# - QUA-3.2: Update documentatie binnen 24 uur
```

### Maximo Connector Module
**Relevante Rules:** IT-6.1, IT-6.3, IT-6.7, IT-6.9

```python
# Bij Maximo integratie:
# - IT-6.1: Alle werkorders in Maximo
# - IT-6.3: GDPR compliance
# - IT-6.7: Offline werk binnen 4 uur sync
# - IT-6.9: Onjuiste data binnen 24 uur fix
```

---

## 📝 Code Review Checklist

Bij elke code review, check:

- [ ] Zijn relevante business rules geïdentificeerd?
- [ ] Is validatie geïmplementeerd?
- [ ] Worden critical violations geblokkeerd?
- [ ] Zijn violations gedocumenteerd?
- [ ] Is error handling correct?
- [ ] Zijn tests geschreven voor rule compliance?
- [ ] Is documentatie bijgewerkt?

---

## 🧪 Testing Requirements

### Elke Feature MOET Tests Hebben Voor:

1. **Happy Path met Rule Compliance**
```python
def test_work_order_with_valid_ptw():
    """Test OPS-2.8: PTW voor risicovol werk"""
    work_order = create_work_order(has_ptw=True)
    violations = validator.validate(work_order)
    assert len(violations) == 0
```

2. **Rule Violations**
```python
def test_work_order_without_ptw_fails():
    """Test OPS-2.8: PTW ontbreekt"""
    work_order = create_work_order(has_ptw=False)
    violations = validator.validate(work_order)
    assert any(v.rule.rule_id == "OPS-2.8" for v in violations)
```

3. **Critical Rule Blocking**
```python
def test_critical_violation_blocks_processing():
    """Test dat critical violations processing blokkeren"""
    data_without_schiphol_pass = {...}
    with pytest.raises(CriticalRuleViolation):
        process_employee_access(data_without_schiphol_pass)
```

---

## 🎯 Praktische Voorbeelden

### Voorbeeld 1: MSG-3 Parsing

```python
def parse_msg3_file(file_path: str) -> Dict[str, Any]:
    """
    Parse MSG-3 Excel file.
    
    Business Rules Compliance:
    - IT-6.1: Output voor Maximo systeem
    - QUA-3.2: Parsing binnen 24 uur na ontvangst
    - IT-6.8: Foto's van source file toevoegen
    """
    validator = BusinessRulesValidator()
    
    # Parse file
    data = excel_reader.read(file_path)
    
    # Validate parsed data
    violations = validator.validate(data)
    
    # Check for critical violations
    critical = [v for v in violations 
                if v.rule.severity == RuleSeverity.CRITICAL]
    
    if critical:
        raise ParseError(f"Critical rules violated: {critical}")
    
    # Add metadata for IT-6.8 (photos)
    data['attachments'] = get_source_file_metadata(file_path)
    
    return data
```

### Voorbeeld 2: Work Order Creation

```python
def create_work_order(task_data: Dict) -> WorkOrder:
    """
    Create Maximo work order from MSG-3 task.
    
    Business Rules Compliance:
    - PLN-5.3: Werkvergunning vereist voor start
    - OPS-2.8: PTW voor risicovol werk
    - QUA-3.10: Geldige certificeringen
    """
    validator = BusinessRulesValidator()
    
    # Validate task data
    violations = validator.validate(task_data)
    
    # Check critical security rules
    security_violations = validator.validate_by_category(
        task_data, 
        RuleCategory.SECURITY
    )
    
    if security_violations:
        logger.error(f"Security violations: {security_violations}")
        raise SecurityException(security_violations)
    
    # Check operations rules
    ops_violations = validator.validate_by_category(
        task_data,
        RuleCategory.OPERATIONS
    )
    
    # Create work order
    work_order = WorkOrder(**task_data)
    
    # Add compliance metadata
    work_order.compliance_check = {
        'validated_at': datetime.now(),
        'rules_checked': 80,
        'violations': len(violations)
    }
    
    return work_order
```

### Voorbeeld 3: Employee Access Validation

```python
def validate_employee_access(employee: Employee, zone: str) -> bool:
    """
    Validate employee can access zone.
    
    Business Rules Compliance:
    - SEC-1.1: Geldige Schiphol-pas
    - SEC-1.2: VGB-screening voor airside
    - SEC-1.4: Beperkte toegang technische ruimtes
    """
    validator = BusinessRulesValidator()
    
    # Prepare validation data
    data = {
        'employee': employee.to_dict(),
        'zone': zone,
        'access_type': 'entry'
    }
    
    # Validate security rules only
    violations = validator.validate_by_category(
        data,
        RuleCategory.SECURITY
    )
    
    # Critical security violations MUST block
    critical = [v for v in violations 
                if v.rule.severity == RuleSeverity.CRITICAL]
    
    if critical:
        logger.critical(
            f"Access DENIED for {employee.name} to {zone}: {critical}"
        )
        return False
    
    # Log warnings but allow access
    for violation in violations:
        if violation.rule.severity == RuleSeverity.WARNING:
            logger.warning(f"Access warning: {violation.message}")
    
    return True
```

---

## 🔄 Continuous Compliance

### Daily
- Review nieuwe violations
- Check compliance metrics
- Update violation documentation

### Weekly
- Rule compliance report
- Trend analysis
- Team review

### Monthly
- Full audit
- Rule updates indien nodig
- Training refresher

---

## 📊 Monitoring & Metrics

Track deze metrics:

```python
# Compliance Metrics
total_validations = 1000
rule_violations = 45
critical_violations = 2
compliance_rate = (total_validations - rule_violations) / total_validations
# Target: > 95%

# Per Category
security_compliance = calculate_compliance(RuleCategory.SECURITY)
operations_compliance = calculate_compliance(RuleCategory.OPERATIONS)
# etc.
```

---

## 🚨 Escalation Path

Bij rule violations:

1. **INFO** → Log en continue
2. **WARNING** → Log, notify, continue
3. **ERROR** → Log, notify, review required
4. **CRITICAL** → STOP, escalate, investigate

---

## 📞 Support

### Vragen over Business Rules?

1. **Documentatie**: `docs/technisch-ontwerp/business-rules.md`
2. **Quick Ref**: `docs/technisch-ontwerp/business-rules-quick-reference.md`
3. **Code**: `src/validator/business_rules.py`
4. **Functional**: Babcock Operations Manager
5. **Compliance**: Quality Manager
6. **Security**: Security Officer

---

## ✅ Remember

> **"If you're not sure if a business rule applies, IT PROBABLY DOES. Check it!"**

### Golden Rules:
1. 🔴 **CRITICAL rules ALWAYS block**
2. 📝 **ALWAYS validate before processing**
3. 📊 **ALWAYS log violations**
4. 🧪 **ALWAYS test rule compliance**
5. 📚 **ALWAYS document compliance**

---

## 🎓 Voor Pedro's Comakership

Deze business-rules-first approach laat zien:
- ✅ **Analyseren**: Begrip van business requirements
- ✅ **Ontwerpen**: Compliance-driven architecture
- ✅ **Realiseren**: Rule-based implementation
- ✅ **Professioneel handelen**: Safety & compliance first

---

**🚀 ALWAYS THINK: "Is this compliant with our business rules?"**

---

**Last Updated:** 5 februari 2026  
**Status:** MANDATORY READING  
**Version:** 1.0

---

## AI Authenticiteitsverklaring

Tijdens het technisch onderzoek en ontwerp heb ik **Cursor AI** gebruikt om te **genereren van diagram templates, analyseren van API documentatie, en structureren van technische beslissingen**. Na het gebruik van deze tool heb ik de uitkomsten ervan uitvoerig gecontroleerd en aangepast om er voor te zorgen dat het ingeleverde werk mijn eigen competenties en leeruitkomsten reflecteert. Alle architecturale beslissingen, business rules en technische keuzes zijn gebaseerd op mijn eigen analyse en in overleg met stakeholders. Ik draag de volledige verantwoordelijkheid voor de inhoud van dit werk.

*AIAS Niveau: 3 - AI Samenwerking*
