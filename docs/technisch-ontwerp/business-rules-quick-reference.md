# 📘 Business Rules Quick Reference

**Versie:** 1.0  
**Datum:** 5 februari 2026

---

## 🚀 Quick Usage

```python
from src.validator.business_rules import BusinessRulesValidator, RuleCategory

# Initialize validator (loads all 80 rules)
validator = BusinessRulesValidator()

# Validate data
data = {"employee": "John Doe", "task": "PM-001"}
violations = validator.validate(data)

# Check for violations
if violations:
    for violation in violations:
        print(f"{violation.rule.severity.value}: {violation.message}")
```

---

## 📊 Rule Categories Overview

| Code | Category | Rules | Focus |
|------|----------|-------|-------|
| **SEC** | Security & Access Control | 10 | Passes, screening, incidents |
| **OPS** | Operations & Maintenance | 10 | PM/CM, certifications, PTW |
| **QUA** | Quality & Compliance | 10 | ISO, audits, RCA |
| **LOG** | Logistics & Inventory | 10 | Stock, materials, waste |
| **PLN** | Planning & Workflow | 10 | Scheduling, SLA, escalation |
| **IT** | IT & System Usage | 10 | Maximo, GDPR, sync |
| **HR** | HR & Workforce | 10 | Training, onboarding, conduct |
| **COM** | Communication & Reporting | 10 | Incidents, reports, feedback |

---

## 🚨 Critical Rules (11 total)

These rules are **CRITICAL** and will block further processing:

### Security (3)
- **SEC-1.1**: Geldige Schiphol-pas vereist
- **SEC-1.2**: VGB-screening voor airside
- **SEC-1.8**: PBM verplicht

### Operations (3)
- **OPS-2.4**: Gecertificeerde elektriciens
- **OPS-2.8**: PTW voor risicovol werk
- **OPS-2.9**: TRA verplicht

### Quality (1)
- **QUA-3.10**: Geldige certificeringen

### Planning (1)
- **PLN-5.3**: Werkvergunning vereist

### IT (1)
- **IT-6.3**: GDPR-richtlijnen

### HR (2)
- **HR-7.8**: Alcohol en drugs verboden
- **HR-7.10**: Schiphol-pas verlies melden

---

## 🔍 Common Validations

### Employee Access Check
```python
# Check: SEC-1.1, SEC-1.2, SEC-1.3
violations = validator.validate_by_category(
    {"employee": employee_data},
    RuleCategory.SECURITY
)
```

### Work Order Validation
```python
# Check: OPS-2.1, PLN-5.1, PLN-5.5
violations = validator.validate(work_order_data)
```

### Material Tracking
```python
# Check: LOG-4.2, LOG-4.7, LOG-4.9
violations = validator.validate_by_category(
    {"material": material_data},
    RuleCategory.LOGISTICS
)
```

---

## 📋 Severity Levels

| Symbol | Level | Count | Action Required |
|--------|-------|-------|-----------------|
| 🔴 | CRITICAL | 11 | Block immediately |
| 🟠 | ERROR | 48 | Must fix |
| 🟡 | WARNING | 19 | Should review |
| 🔵 | INFO | 2 | Optional |

---

## 🔧 Getting Specific Rules

```python
# Get one rule
rule = validator.get_rule("SEC-1.1")
print(rule.title)
print(rule.description)

# Get all security rules
security_rules = validator.get_rules_by_category(RuleCategory.SECURITY)

# Get all critical rules
critical_rules = validator.get_rules_by_severity(RuleSeverity.CRITICAL)

# Get summary
summary = validator.get_rule_summary()
print(f"Total rules: {summary['total_rules']}")
```

---

## 📖 Complete Rule List

### Security & Access Control (SEC)
1. **SEC-1.1** 🔴 - Geldige Schiphol-pas vereist
2. **SEC-1.2** 🔴 - VGB-screening voor airside toegang
3. **SEC-1.3** 🟠 - Jaarlijkse herkeuring toegangspassen
4. **SEC-1.4** 🟠 - Beperkte toegang technische ruimtes
5. **SEC-1.5** 🟠 - Gereedschap registratie
6. **SEC-1.6** 🟠 - Airside materialen vooraf aanmelden
7. **SEC-1.7** 🟠 - Bezoekers begeleiden
8. **SEC-1.8** 🔴 - PBM verplicht
9. **SEC-1.9** 🟠 - Snelle incident melding (15 min)
10. **SEC-1.10** 🟡 - Foto's en video's verboden

### Operations & Maintenance (OPS)
1. **OPS-2.1** 🟠 - Preventief onderhoud binnen SLA
2. **OPS-2.2** 🟠 - Correctief onderhoud responstijd
3. **OPS-2.3** 🟠 - Kwaliteitscontrole voor afsluiten
4. **OPS-2.4** 🔴 - Gecertificeerde elektriciens
5. **OPS-2.5** 🟠 - OEM-specificaties volgen
6. **OPS-2.6** 🟠 - Jaarlijkse NEN-keuring
7. **OPS-2.7** 🟠 - Afstemming operationele impact
8. **OPS-2.8** 🔴 - PTW voor risicovol werk
9. **OPS-2.9** 🔴 - TRA verplicht
10. **OPS-2.10** 🟠 - 24-uur vooraf aanmelden kritieke zones

### Quality & Compliance (QUA)
1. **QUA-3.1** 🟠 - ISO 9001 en ISO 45001 compliance
2. **QUA-3.2** 🟠 - Documentatie binnen 24 uur bijwerken
3. **QUA-3.3** 🟠 - Afwijkingen registreren
4. **QUA-3.4** 🟠 - Goedgekeurde materialen en leveranciers
5. **QUA-3.5** 🟡 - Wekelijkse rapportages
6. **QUA-3.6** 🟠 - Up-to-date tekeningen
7. **QUA-3.7** 🟠 - Auditbevindingen binnen 30 dagen
8. **QUA-3.8** 🟠 - RCA voor veiligheidsincidenten
9. **QUA-3.9** 🟠 - Jaarlijkse veiligheidstrainingen
10. **QUA-3.10** 🔴 - Geldige certificeringen vereist

### Logistics & Inventory (LOG)
1. **LOG-4.1** 🟡 - Voorraadniveaus binnen min/max
2. **LOG-4.2** 🟠 - Materialen op juiste werkorder boeken
3. **LOG-4.3** 🟡 - Spoedbestellingen goedkeuring
4. **LOG-4.4** 🟡 - Retourmaterialen binnen 48 uur
5. **LOG-4.5** 🟠 - Afvalscheiding Schiphol regels
6. **LOG-4.6** 🟠 - Airside leveringen aanmelden
7. **LOG-4.7** 🟠 - Serienummers registreren
8. **LOG-4.8** 🟡 - Defecte onderdelen apart opslaan
9. **LOG-4.9** 🟡 - Realtime magazijnbewegingen
10. **LOG-4.10** 🟠 - Geautoriseerd magazijnpersoneel

### Planning & Workflow (PLN)
1. **PLN-5.1** 🟠 - Planning op basis prioriteit en SLA
2. **PLN-5.2** 🟡 - Dagelijks uren registreren
3. **PLN-5.3** 🔴 - Werkvergunning vereist voor start
4. **PLN-5.4** 🟠 - Geen taken overslaan
5. **PLN-5.5** 🟠 - Volledige werkorder invulling
6. **PLN-5.6** 🟠 - Taken in juiste volgorde
7. **PLN-5.7** 🟡 - Werk overdragen bij einde shift
8. **PLN-5.8** 🟠 - Spoedwerk na escalatie
9. **PLN-5.9** 🟠 - Afstemming passagiersstromen
10. **PLN-5.10** 🟡 - Planning 1 week vooruit

### IT & System Usage (IT)
1. **IT-6.1** 🟠 - Centrale onderhoudssysteem verplicht
2. **IT-6.2** 🟠 - Eigen accounts gebruiken
3. **IT-6.3** 🔴 - GDPR-richtlijnen
4. **IT-6.4** 🟡 - Mobiele apparaten vergrendelen
5. **IT-6.5** 🟠 - Geautoriseerde documentatie wijzigingen
6. **IT-6.6** 🟠 - IT-beheer voor systeemupdates
7. **IT-6.7** 🟡 - Offline werk binnen 4 uur synchroniseren
8. **IT-6.8** 🔵 - Foto's toevoegen aan werkorder
9. **IT-6.9** 🟠 - Onjuiste data binnen 24 uur corrigeren
10. **IT-6.10** 🟡 - Toegang intrekken bij inactiviteit (30 dagen)

### HR & Workforce (HR)
1. **HR-7.1** 🟠 - Jaarlijkse veiligheidstrainingen
2. **HR-7.2** 🟠 - Onboarding-proces
3. **HR-7.3** 🟡 - Ziekmeldingen voor dienst
4. **HR-7.4** 🟡 - Overuren goedkeuren
5. **HR-7.5** 🟠 - Schiphol-gedragscode
6. **HR-7.6** 🟠 - Up-to-date certificeringen
7. **HR-7.7** 🟡 - Toolboxmeetings
8. **HR-7.8** 🔴 - Alcohol en drugs verboden
9. **HR-7.9** 🟠 - Ongewenst gedrag melden
10. **HR-7.10** 🔴 - Schiphol-pas verlies melden

### Communication & Reporting (COM)
1. **COM-8.1** 🟠 - Storingen direct melden
2. **COM-8.2** 🟡 - Klantcommunicatie via contractmanager
3. **COM-8.3** 🟡 - Dagelijkse voortgang in shiftlog
4. **COM-8.4** 🟠 - Escalaties volgens escalatiemodel
5. **COM-8.5** 🟡 - Volledige rapportages
6. **COM-8.6** 🟡 - Planning wijzigingen communiceren
7. **COM-8.7** 🟠 - Incidentrapporten binnen 24 uur
8. **COM-8.8** 🟡 - Professionele communicatie
9. **COM-8.9** 🟠 - Afwijkingen direct melden
10. **COM-8.10** 🔵 - Klantfeedback registreren

---

## 📞 Support

Voor vragen:
- **Documentation**: `docs/technisch-ontwerp/business-rules.md`
- **Code**: `src/validator/business_rules.py`
- **Tests**: `tests/unit/test_validator.py`

---

**Last Updated:** 5 februari 2026
