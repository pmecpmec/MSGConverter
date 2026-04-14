# Business Rules - Babcock @ Schiphol

**Versie:** 1.0
**Datum:** 5 februari 2026
**Status:** Actief
**Auteur:** Pedro (met Cursor AI assistentie)

---

## Inhoudsopgave

1. [Overzicht](#overzicht)
2. [Rule Structuur](#rule-structuur)
3. [Severity Levels](#severity-levels)
4. [Rule Categorieën](#rule-categorieën)
5. [Implementatie](#implementatie)
6. [Validatie Process](#validatie-process)
7. [Alle Business Rules](#alle-business-rules)

---

## Overzicht

Dit document bevat alle **80 business rules** voor Babcock operaties op Schiphol. Deze regels zijn essentieel voor:

- **Veiligheid**: Bescherming van medewerkers en passagiers
- **Compliance**: Voldoen aan wet- en regelgeving
- **Kwaliteit**: Waarborgen van hoge kwaliteit onderhoud
- **Efficiency**: Optimaliseren van werkprocessen

### Statistieken

- **Totaal Rules:** 80
- **Categorieën:** 8
- **Rules per Categorie:** 10
- **Critical Rules:** ~10
- **Error Rules:** ~45
- **Warning Rules:** ~23
- **Info Rules:** ~2

---

## Rule Structuur

Elke business rule heeft de volgende structuur:

```python
BusinessRule(
 rule_id: str, # Unieke ID (bijv. "SEC-1.1")
 category: RuleCategory, # Categorie (bijv. SECURITY)
 title: str, # Korte beschrijving
 description: str, # Volledige beschrijving
 severity: RuleSeverity, # Ernst niveau
 validation_func: Optional[Callable] # Validatie functie
)
```

### Rule ID Format

Format: `XXX-N.M`

- **XXX**: Categorie prefix (3 letters)
 - `SEC`: Security
 - `OPS`: Operations
 - `QUA`: Quality
 - `LOG`: Logistics
 - `PLN`: Planning
 - `IT`: IT Systems
 - `HR`: Human Resources
 - `COM`: Communication

- **N**: Categorie nummer (1-8)
- **M**: Rule nummer binnen categorie (1-10)

**Voorbeelden:**
- `SEC-1.1`: Security regel 1
- `OPS-2.5`: Operations regel 5
- `QUA-3.10`: Quality regel 10

---

## Severity Levels

### CRITICAL
- **Blokkeert verder processing**
- Moet onmiddellijk worden opgelost
- Kan leiden tot gevaarlijke situaties
- Voorbeelden: Geen VGB-screening, geen PBM, alcohol/drugs gebruik

### ERROR
- **Must be fixed**
- Werk mag niet worden voortgezet
- Non-compliance met regelgeving
- Voorbeelden: Geen certificering, geen werkvergunning, gemiste SLA

### WARNING
- **Should be reviewed**
- Werk kan voortgaan maar review vereist
- Best practice violations
- Voorbeelden: Late registratie, incomplete rapportage

### INFO
- **Informational**
- Geen directe actie vereist
- Aanbevelingen voor verbetering
- Voorbeelden: Foto's toevoegen, feedback registreren

---

## Rule Categorieën

### 1. Security & Access Control (SEC)
**Focus:** Veiligheid en toegangsbeveiliging

- Toegangspassen en screening
- Airside security
- Incident management
- PBM compliance

**Aantal Rules:** 10 (SEC-1.1 t/m SEC-1.10)

---

### 2. Operations & Maintenance (OPS)
**Focus:** Onderhoudswerkzaamheden en operationele processen

- Preventief en correctief onderhoud
- SLA compliance
- Certificeringen en kwalificaties
- Werkvergunningen (PTW)
- Risico analyses (TRA)

**Aantal Rules:** 10 (OPS-2.1 t/m OPS-2.10)

---

### 3. Quality & Compliance (QUA)
**Focus:** Kwaliteit en naleving van standaarden

- ISO 9001 en ISO 45001
- Documentatie en registratie
- Audit compliance
- Safety trainingen
- Root Cause Analysis (RCA)

**Aantal Rules:** 10 (QUA-3.1 t/m QUA-3.10)

---

### 4. Logistics & Inventory (LOG)
**Focus:** Magazijnbeheer en logistiek

- Voorraadniveaus
- Materiaal tracking
- Leveringen en retourzendingen
- Afvalscheiding
- Serienummer registratie

**Aantal Rules:** 10 (LOG-4.1 t/m LOG-4.10)

---

### 5. Planning & Workflow (PLN)
**Focus:** Werkplanning en proces management

- SLA-based planning
- Urenregistratie
- Werkorder afhandeling
- Taak dependencies
- Escalatie procedures

**Aantal Rules:** 10 (PLN-5.1 t/m PLN-5.10)

---

### 6. IT & System Usage (IT)
**Focus:** IT systemen en data management

- Maximo compliance
- GDPR compliance
- Data synchronisatie
- Documentatie management
- Access control

**Aantal Rules:** 10 (IT-6.1 t/m IT-6.10)

---

### 7. HR & Workforce (HR)
**Focus:** Personeelszaken en workforce management

- Trainingen en certificeringen
- Onboarding
- Gedragscode
- Toolboxmeetings
- Ziekteverzuim

**Aantal Rules:** 10 (HR-7.1 t/m HR-7.10)

---

### 8. Communication & Reporting (COM)
**Focus:** Communicatie en rapportage

- Incident reporting
- Klantcommunicatie
- Shiftlogs
- Escalaties
- Feedback management

**Aantal Rules:** 10 (COM-8.1 t/m COM-8.10)

---

## Implementatie

### Gebruik in Code

```python
from src.validator.business_rules import (
 BusinessRulesValidator,
 RuleCategory,
 RuleSeverity
)

# Initialiseer validator
validator = BusinessRulesValidator()

# Valideer data tegen alle rules
data = {"task_code": "PM-001", "technician": "John Doe"}
violations = validator.validate(data)

# Valideer specifieke categorie
security_violations = validator.validate_by_category(
 data,
 RuleCategory.SECURITY
)

# Haal specifieke rule op
rule = validator.get_rule("SEC-1.1")
print(f"Rule: {rule.title}")
print(f"Severity: {rule.severity.value}")

# Genereer summary
summary = validator.get_rule_summary()
print(f"Total rules: {summary['total_rules']}")
```

### Custom Validatie Functies

Regels kunnen custom validatie functies hebben:

```python
def validate_schiphol_pass(data: Dict, context: Dict) -> Optional[RuleViolation]:
 """Valideer of medewerker geldige Schiphol-pas heeft."""
 employee = data.get("employee")

 if not employee or not employee.get("schiphol_pass_valid"):
 rule = validator.get_rule("SEC-1.1")
 return RuleViolation(
 rule=rule,
 field="employee.schiphol_pass",
 message="Medewerker heeft geen geldige Schiphol-pas",
 value=employee.get("schiphol_pass_id") if employee else None
 )

 return None
```

---

## Validatie Process

### Flow Diagram

```
┌─────────────────┐
│ Input Data │
└────────┬────────┘
 │
 ▼
┌─────────────────┐
│ Load All Rules │
│ (80 rules) │
└────────┬────────┘
 │
 ▼
┌─────────────────┐
│ For Each Rule │
│ with func │
└────────┬────────┘
 │
 ▼
┌─────────────────┐ Yes ┌──────────────┐
│ Execute │────────────>│ Add to │
│ validation_ │ │ Violations │
│ func() │ │ List │
└────────┬────────┘ └──────────────┘
 │ No
 ▼
┌─────────────────┐
│ Return All │
│ Violations │
└─────────────────┘
```

### Validatie Output

```python
[
 RuleViolation(
 rule=BusinessRule(...),
 field="employee.vgb_screening",
 message="VGB-screening is verlopen",
 value="2025-12-01",
 context={"expires": "2025-12-01", "today": "2026-02-05"}
 ),
 # ... meer violations
]
```

---

## Alle Business Rules

### 1. Security & Access Control

#### SEC-1.1: Geldige Schiphol-pas vereist CRITICAL
**Beschrijving:** Alleen medewerkers met een geldige Schiphol-pas mogen beveiligde zones betreden.

**Validatie:**
- Check of medewerker een Schiphol-pas heeft
- Verify dat pas geldig is (niet verlopen)
- Check dat pas geregistreerd is in systeem

---

#### SEC-1.2: VGB-screening voor airside toegang CRITICAL
**Beschrijving:** Airside toegang vereist een geldige VGB‑screening.

**Validatie:**
- Check VGB-screening status
- Verify screening niet verlopen
- Check screening voor specifieke zone

---

#### SEC-1.3: Jaarlijkse herkeuring toegangspassen ERROR
**Beschrijving:** Alle toegangspassen moeten jaarlijks worden herkeurd.

**Validatie:**
- Check laatste herkeuring datum
- Verify < 1 jaar geleden
- Waarschuwing bij naderende vervaldatum

---

#### SEC-1.4: Beperkte toegang technische ruimtes ERROR
**Beschrijving:** Toegang tot technische ruimtes is beperkt tot geautoriseerd personeel.

**Validatie:**
- Check autorisatie voor specifieke ruimte
- Verify certificering indien nodig
- Check toestemmingslijst

---

#### SEC-1.5: Gereedschap registratie ERROR
**Beschrijving:** Gereedschap moet worden geregistreerd bij in- en uitchecken.

**Validatie:**
- Check in-checkout record
- Verify complete tool list
- Match in/out items

---

#### SEC-1.6: Airside materialen vooraf aanmelden ERROR
**Beschrijving:** Materialen die airside worden gebracht moeten vooraf worden aangemeld.

**Validatie:**
- Check pre-notification
- Verify security approval
- Check timing (minimaal X uur vooraf)

---

#### SEC-1.7: Bezoekers begeleiden ERROR
**Beschrijving:** Bezoekers moeten altijd worden begeleid door een gecertificeerde medewerker.

**Validatie:**
- Check bezoeker registratie
- Verify begeleider aanwezig
- Check begeleider certificering

---

#### SEC-1.8: PBM verplicht CRITICAL
**Beschrijving:** Persoonlijke beschermingsmiddelen (PBM) zijn verplicht in alle operationele zones.

**Validatie:**
- Check required PBM voor zone
- Verify PBM compliance
- Check PBM certificering/inspectie

---

#### SEC-1.9: Snelle incident melding ERROR
**Beschrijving:** Incidenten moeten binnen 15 minuten worden gemeld aan de duty manager.

**Validatie:**
- Check incident timestamp
- Verify melding timestamp
- Calculate delta < 15 minuten

---

#### SEC-1.10: Foto's en video's verboden WARNING
**Beschrijving:** Foto's en video's zijn verboden zonder expliciete toestemming.

**Validatie:**
- Check photography permission
- Verify zone restrictions
- Check approval document

---

### 2. Operations & Maintenance

#### OPS-2.1: Preventief onderhoud binnen SLA ERROR
**Beschrijving:** Preventief onderhoud moet worden uitgevoerd binnen de SLA-deadlines.

**Validatie:**
- Check planned date
- Compare with SLA deadline
- Check completion date

---

#### OPS-2.2: Correctief onderhoud responstijd ERROR
**Beschrijving:** Correctief onderhoud moet worden opgepakt binnen de afgesproken responstijd.

**Validatie:**
- Check failure report time
- Check response time
- Compare with SLA

---

#### OPS-2.3: Kwaliteitscontrole voor afsluiten ERROR
**Beschrijving:** Werkorders mogen alleen worden afgesloten na kwaliteitscontrole.

**Validatie:**
- Check QC performed
- Verify QC approval
- Check QC signature

---

#### OPS-2.4: Gecertificeerde elektriciens CRITICAL
**Beschrijving:** Alleen gecertificeerde technici mogen werken aan elektrische installaties.

**Validatie:**
- Check work type
- Verify technician certification
- Check certification validity

---

#### OPS-2.5: OEM-specificaties volgen ERROR
**Beschrijving:** Werkzaamheden moeten worden uitgevoerd volgens OEM-specificaties.

**Validatie:**
- Check OEM doc reference
- Verify procedure followed
- Check deviations documented

---

#### OPS-2.6: Jaarlijkse NEN-keuring ERROR
**Beschrijving:** Alle installaties moeten jaarlijks worden gekeurd volgens NEN‑normen.

**Validatie:**
- Check last inspection date
- Verify NEN compliance
- Check certificate validity

---

#### OPS-2.7: Afstemming operationele impact ERROR
**Beschrijving:** Werkzaamheden met operationele impact moeten vooraf worden afgestemd met Schiphol Operations.

**Validatie:**
- Check impact assessment
- Verify coordination
- Check approval document

---

#### OPS-2.8: PTW voor risicovol werk CRITICAL
**Beschrijving:** Werkvergunningen (PTW) zijn verplicht voor risicovolle werkzaamheden.

**Validatie:**
- Check work risk level
- Verify PTW issued
- Check PTW validity

---

#### OPS-2.9: TRA verplicht CRITICAL
**Beschrijving:** Taken mogen niet worden uitgevoerd zonder goedgekeurde TRA (Taak Risico Analyse).

**Validatie:**
- Check TRA exists
- Verify TRA approved
- Check TRA up-to-date

---

#### OPS-2.10: 24-uur vooraf aanmelden kritieke zones ERROR
**Beschrijving:** Werkzaamheden in kritieke zones moeten minimaal 24 uur vooraf worden aangemeld.

**Validatie:**
- Check notification time
- Verify zone criticality
- Check approval received

---

### 3. Quality & Compliance

#### QUA-3.1: ISO 9001 en ISO 45001 compliance ERROR
**Beschrijving:** Alle werkzaamheden moeten voldoen aan ISO 9001 en ISO 45001.

**Validatie:**
- Check ISO procedure reference
- Verify documentation
- Check audit trail

---

#### QUA-3.2: Documentatie binnen 24 uur bijwerken ERROR
**Beschrijving:** Documentatie moet binnen 24 uur worden bijgewerkt in het onderhoudssysteem.

**Validatie:**
- Check work completion time
- Check documentation time
- Calculate delta < 24 uur

---

#### QUA-3.3: Afwijkingen registreren ERROR
**Beschrijving:** Afwijkingen moeten worden geregistreerd in het kwaliteitsmanagementsysteem.

**Validatie:**
- Check for deviations
- Verify registration
- Check follow-up actions

---

#### QUA-3.4: Goedgekeurde materialen en leveranciers ERROR
**Beschrijving:** Alleen goedgekeurde materialen en leveranciers mogen worden gebruikt.

**Validatie:**
- Check supplier on approved list
- Verify material certification
- Check approval validity

---

#### QUA-3.5: Wekelijkse rapportages WARNING
**Beschrijving:** Rapportages moeten wekelijks worden aangeleverd aan de contractmanager.

**Validatie:**
- Check report submission
- Verify weekly frequency
- Check completeness

---

#### QUA-3.6: Up-to-date tekeningen ERROR
**Beschrijving:** Alle technische tekeningen moeten up‑to‑date zijn voordat werk start.

**Validatie:**
- Check drawing revision
- Verify latest version used
- Check drawing approval

---

#### QUA-3.7: Auditbevindingen binnen 30 dagen ERROR
**Beschrijving:** Auditbevindingen moeten binnen 30 dagen worden opgelost.

**Validatie:**
- Check finding date
- Verify resolution date
- Calculate delta < 30 dagen

---

#### QUA-3.8: RCA voor veiligheidsincidenten ERROR
**Beschrijving:** Veiligheidsincidenten moeten worden geëvalueerd met een RCA (root cause analysis).

**Validatie:**
- Check incident severity
- Verify RCA performed
- Check corrective actions

---

#### QUA-3.9: Jaarlijkse veiligheidstrainingen ERROR
**Beschrijving:** Alle medewerkers moeten jaarlijkse veiligheidstrainingen volgen.

**Validatie:**
- Check last training date
- Verify training type
- Check certificate validity

---

#### QUA-3.10: Geldige certificeringen vereist CRITICAL
**Beschrijving:** Werk mag niet worden uitgevoerd zonder geldige certificeringen.

**Validatie:**
- Check required certificates
- Verify validity
- Check certificate scope

---

### 4. Logistics & Inventory

#### LOG-4.1: Voorraadniveaus binnen min/max WARNING
**Beschrijving:** Voorraadniveaus moeten binnen minimum- en maximumwaarden blijven.

**Validatie:**
- Check current stock level
- Compare with min/max
- Generate alerts

---

#### LOG-4.2: Materialen op juiste werkorder boeken ERROR
**Beschrijving:** Materialen moeten worden geboekt op de juiste werkorder.

**Validatie:**
- Check work order validity
- Verify material assignment
- Check authorization

---

#### LOG-4.3: Spoedbestellingen goedkeuring WARNING
**Beschrijving:** Spoedbestellingen vereisen goedkeuring van de supervisor.

**Validatie:**
- Check order priority
- Verify supervisor approval
- Check justification

---

#### LOG-4.4: Retourmaterialen binnen 48 uur WARNING
**Beschrijving:** Retourmaterialen moeten binnen 48 uur worden verwerkt.

**Validatie:**
- Check return date
- Check processing date
- Calculate delta < 48 uur

---

#### LOG-4.5: Afvalscheiding Schiphol regels ERROR
**Beschrijving:** Afval moet worden gescheiden volgens Schiphol‑milieuregels.

**Validatie:**
- Check waste category
- Verify proper disposal
- Check environmental compliance

---

#### LOG-4.6: Airside leveringen aanmelden ERROR
**Beschrijving:** Leveringen airside moeten vooraf worden aangemeld bij security.

**Validatie:**
- Check delivery notification
- Verify security clearance
- Check timing

---

#### LOG-4.7: Serienummers registreren ERROR
**Beschrijving:** Materialen met serienummers moeten worden geregistreerd in het systeem.

**Validatie:**
- Check if item requires S/N
- Verify S/N recorded
- Check S/N uniqueness

---

#### LOG-4.8: Defecte onderdelen apart opslaan WARNING
**Beschrijving:** Defecte onderdelen moeten worden gemarkeerd en apart opgeslagen.

**Validatie:**
- Check defect marking
- Verify quarantine location
- Check documentation

---

#### LOG-4.9: Realtime magazijnbewegingen WARNING
**Beschrijving:** Magazijnbewegingen moeten realtime worden bijgewerkt.

**Validatie:**
- Check transaction timestamp
- Verify immediate update
- Check synchronization

---

#### LOG-4.10: Geautoriseerd magazijnpersoneel ERROR
**Beschrijving:** Alleen geautoriseerd personeel mag magazijnsystemen bedienen.

**Validatie:**
- Check user authorization
- Verify permissions
- Check access level

---

### 5. Planning & Workflow

#### PLN-5.1: Planning op basis prioriteit en SLA ERROR
**Beschrijving:** Werkopdrachten moeten worden ingepland op basis van prioriteit en SLA.

**Validatie:**
- Check work order priority
- Verify SLA compliance
- Check scheduling logic

---

#### PLN-5.2: Dagelijks uren registreren WARNING
**Beschrijving:** Medewerkers moeten hun uren dagelijks registreren.

**Validatie:**
- Check timesheet entries
- Verify daily submission
- Check completeness

---

#### PLN-5.3: Werkvergunning vereist voor start CRITICAL
**Beschrijving:** Werk mag niet starten zonder goedgekeurde werkvergunning.

**Validatie:**
- Check permit status
- Verify approval
- Check validity period

---

#### PLN-5.4: Geen taken overslaan ERROR
**Beschrijving:** Taken mogen niet worden overgeslagen zonder supervisor‑goedkeuring.

**Validatie:**
- Check task sequence
- Verify skipped tasks
- Check approval for skips

---

#### PLN-5.5: Volledige werkorder invulling ERROR
**Beschrijving:** Werkorders moeten volledig worden ingevuld voordat ze worden afgesloten.

**Validatie:**
- Check required fields
- Verify completeness
- Check signatures

---

#### PLN-5.6: Taken in juiste volgorde ERROR
**Beschrijving:** Taken met afhankelijkheden moeten in de juiste volgorde worden uitgevoerd.

**Validatie:**
- Check task dependencies
- Verify sequence
- Check prerequisites

---

#### PLN-5.7: Werk overdragen bij einde shift WARNING
**Beschrijving:** Werk dat niet binnen de shift kan worden afgerond moet worden overgedragen.

**Validatie:**
- Check work status at shift end
- Verify handover documented
- Check next shift assignment

---

#### PLN-5.8: Spoedwerk na escalatie ERROR
**Beschrijving:** Spoedwerk mag alleen worden uitgevoerd na escalatie.

**Validatie:**
- Check work urgency
- Verify escalation
- Check approval level

---

#### PLN-5.9: Afstemming passagiersstromen ERROR
**Beschrijving:** Werk dat impact heeft op passagiersstromen moet worden afgestemd met Operations.

**Validatie:**
- Check passenger impact
- Verify coordination
- Check operations approval

---

#### PLN-5.10: Planning 1 week vooruit WARNING
**Beschrijving:** Werkplanning moet minimaal 1 week vooruit worden bijgewerkt.

**Validatie:**
- Check planning horizon
- Verify 7+ days planned
- Check update frequency

---

### 6. IT & System Usage

#### IT-6.1: Centrale onderhoudssysteem verplicht ERROR
**Beschrijving:** Alle werkorders moeten worden verwerkt in het centrale onderhoudssysteem (bijv. Maximo).

**Validatie:**
- Check WO in Maximo
- Verify synchronization
- Check data completeness

---

#### IT-6.2: Eigen accounts gebruiken ERROR
**Beschrijving:** Medewerkers mogen alleen hun eigen accounts gebruiken.

**Validatie:**
- Check user ID
- Verify authentication
- Check shared account usage

---

#### IT-6.3: GDPR-richtlijnen CRITICAL
**Beschrijving:** Data moet worden opgeslagen volgens GDPR‑richtlijnen.

**Validatie:**
- Check data classification
- Verify encryption
- Check retention policy

---

#### IT-6.4: Mobiele apparaten vergrendelen WARNING
**Beschrijving:** Mobiele apparaten moeten worden vergrendeld bij het verlaten van de werkplek.

**Validatie:**
- Check device lock status
- Verify auto-lock settings
- Check security policy

---

#### IT-6.5: Geautoriseerde documentatie wijzigingen ERROR
**Beschrijving:** Alleen geautoriseerde medewerkers mogen technische documentatie wijzigen.

**Validatie:**
- Check user permissions
- Verify change authorization
- Check approval workflow

---

#### IT-6.6: IT-beheer voor systeemupdates ERROR
**Beschrijving:** Systeemupdates mogen alleen worden uitgevoerd door IT‑beheer.

**Validatie:**
- Check update initiator
- Verify IT approval
- Check change management

---

#### IT-6.7: Offline werk binnen 4 uur synchroniseren WARNING
**Beschrijving:** Offline werk moet binnen 4 uur worden gesynchroniseerd.

**Validatie:**
- Check offline timestamp
- Check sync timestamp
- Calculate delta < 4 uur

---

#### IT-6.8: Foto's toevoegen aan werkorder INFO
**Beschrijving:** Foto's van installaties moeten worden toegevoegd aan de werkorder.

**Validatie:**
- Check attachments
- Verify photo quality
- Check photo metadata

---

#### IT-6.9: Onjuiste data binnen 24 uur corrigeren ERROR
**Beschrijving:** Onjuiste data moet binnen 24 uur worden gecorrigeerd.

**Validatie:**
- Check error detection time
- Check correction time
- Calculate delta < 24 uur

---

#### IT-6.10: Toegang intrekken bij inactiviteit WARNING
**Beschrijving:** Toegang tot systemen wordt ingetrokken bij inactiviteit van 30 dagen.

**Validatie:**
- Check last login date
- Calculate inactivity period
- Check access status

---

### 7. HR & Workforce

#### HR-7.1: Jaarlijkse veiligheidstrainingen ERROR
**Beschrijving:** Medewerkers moeten jaarlijkse veiligheidstrainingen volgen.

**Validatie:**
- Check last training date
- Verify training completion
- Check certificate

---

#### HR-7.2: Onboarding-proces ERROR
**Beschrijving:** Nieuwe medewerkers moeten een onboarding-proces doorlopen.

**Validatie:**
- Check onboarding completion
- Verify all steps done
- Check documentation

---

#### HR-7.3: Ziekmeldingen voor dienst WARNING
**Beschrijving:** Ziekmeldingen moeten vóór aanvang van de dienst worden doorgegeven.

**Validatie:**
- Check notification time
- Check shift start time
- Verify notification method

---

#### HR-7.4: Overuren goedkeuren WARNING
**Beschrijving:** Overuren moeten vooraf worden goedgekeurd.

**Validatie:**
- Check overtime hours
- Verify approval
- Check approval timing

---

#### HR-7.5: Schiphol-gedragscode ERROR
**Beschrijving:** Medewerkers moeten voldoen aan de Schiphol‑gedragscode.

**Validatie:**
- Check code of conduct signed
- Verify compliance training
- Check violations

---

#### HR-7.6: Up-to-date certificeringen ERROR
**Beschrijving:** Certificeringen moeten up‑to‑date blijven.

**Validatie:**
- Check certificate expiry
- Verify renewals
- Check validity

---

#### HR-7.7: Toolboxmeetings WARNING
**Beschrijving:** Medewerkers moeten deelnemen aan toolboxmeetings.

**Validatie:**
- Check attendance
- Verify participation
- Check frequency

---

#### HR-7.8: Alcohol en drugs verboden CRITICAL
**Beschrijving:** Alcohol- en drugsgebruik is verboden tijdens werktijd.

**Validatie:**
- Check compliance
- Verify testing policy
- Check violations

---

#### HR-7.9: Ongewenst gedrag melden ERROR
**Beschrijving:** Ongewenst gedrag moet worden gemeld bij HR.

**Validatie:**
- Check incident report
- Verify HR notification
- Check follow-up

---

#### HR-7.10: Schiphol-pas verlies melden CRITICAL
**Beschrijving:** Medewerkers moeten hun Schiphol-pas direct melden bij verlies.

**Validatie:**
- Check loss report
- Verify timing (immediately)
- Check security notification

---

### 8. Communication & Reporting

#### COM-8.1: Storingen direct melden ERROR
**Beschrijving:** Storingen moeten direct worden gemeld via het officiële meldpunt.

**Validatie:**
- Check failure detection
- Verify immediate reporting
- Check reporting method

---

#### COM-8.2: Klantcommunicatie via contractmanager WARNING
**Beschrijving:** Klantcommunicatie verloopt via de contractmanager of teamleider.

**Validatie:**
- Check communication initiator
- Verify approval
- Check communication log

---

#### COM-8.3: Dagelijkse voortgang in shiftlog WARNING
**Beschrijving:** Dagelijkse voortgang moet worden gerapporteerd in het shiftlog.

**Validatie:**
- Check shiftlog entry
- Verify daily submission
- Check completeness

---

#### COM-8.4: Escalaties volgens escalatiemodel ERROR
**Beschrijving:** Escalaties moeten worden opgevolgd volgens het escalatiemodel.

**Validatie:**
- Check escalation level
- Verify correct path
- Check response time

---

#### COM-8.5: Volledige rapportages WARNING
**Beschrijving:** Rapportages moeten volledig en foutloos zijn.

**Validatie:**
- Check required sections
- Verify data accuracy
- Check completeness

---

#### COM-8.6: Planning wijzigingen communiceren WARNING
**Beschrijving:** Wijzigingen in planning moeten worden gecommuniceerd naar alle betrokkenen.

**Validatie:**
- Check change notification
- Verify stakeholders informed
- Check timing

---

#### COM-8.7: Incidentrapporten binnen 24 uur ERROR
**Beschrijving:** Incidentrapporten moeten binnen 24 uur worden ingediend.

**Validatie:**
- Check incident time
- Check report submission time
- Calculate delta < 24 uur

---

#### COM-8.8: Professionele communicatie WARNING
**Beschrijving:** Communicatie moet professioneel en conform bedrijfsrichtlijnen zijn.

**Validatie:**
- Check communication tone
- Verify policy compliance
- Check documentation

---

#### COM-8.9: Afwijkingen direct melden ERROR
**Beschrijving:** Afwijkingen moeten direct worden gemeld.

**Validatie:**
- Check deviation detection
- Verify immediate reporting
- Check notification method

---

#### COM-8.10: Klantfeedback registreren INFO
**Beschrijving:** Klantfeedback moet worden geregistreerd en opgevolgd.

**Validatie:**
- Check feedback registration
- Verify follow-up actions
- Check resolution

---

## Rule Statistieken

### Per Categorie

| Categorie | Prefix | Rules | Critical | Error | Warning | Info |
|-----------|--------|-------|----------|-------|---------|------|
| Security & Access Control | SEC | 10 | 3 | 6 | 1 | 0 |
| Operations & Maintenance | OPS | 10 | 3 | 7 | 0 | 0 |
| Quality & Compliance | QUA | 10 | 1 | 8 | 1 | 0 |
| Logistics & Inventory | LOG | 10 | 0 | 4 | 6 | 0 |
| Planning & Workflow | PLN | 10 | 1 | 7 | 2 | 0 |
| IT & System Usage | IT | 10 | 1 | 5 | 3 | 1 |
| HR & Workforce | HR | 10 | 2 | 6 | 2 | 0 |
| Communication & Reporting | COM | 10 | 0 | 5 | 4 | 1 |
| **TOTAAL** | | **80** | **11** | **48** | **19** | **2** |

### Per Severity

- **CRITICAL**: 11 rules (13.75%)
- **ERROR**: 48 rules (60%)
- **WARNING**: 19 rules (23.75%)
- **INFO**: 2 rules (2.5%)

---

## Onderhoud

### Rule Updates

Wanneer rules moeten worden bijgewerkt:

1. **Update `business_rules.py`**
 - Wijzig rule definitie
 - Update validation_func indien nodig
 - Update docstrings

2. **Update Tests**
 - Pas tests aan in `test_validator.py`
 - Run test suite
 - Check coverage

3. **Update Documentatie**
 - Update dit document
 - Update docs/readme-docs.md
 - Update technisch ontwerp

4. **Communicatie**
 - Informeer stakeholders
 - Update training materiaal
 - Versie bump

### Versioning

Format: `MAJOR.MINOR.PATCH`

- **MAJOR**: Breaking changes in rules
- **MINOR**: Nieuwe rules toegevoegd
- **PATCH**: Bug fixes, clarifications

---

## Contact

Voor vragen over business rules:

- **Technical**: Pedro (Developer)
- **Functional**: Babcock Operations Manager
- **Compliance**: Quality Manager
- **Security**: Security Officer

---

## AI Authenticiteitsverklaring

Tijdens het technisch onderzoek en ontwerp heb ik **Cursor AI** gebruikt om te **genereren van diagram templates, analyseren van API documentatie, en structureren van technische beslissingen**. Na het gebruik van deze tool heb ik de uitkomsten ervan uitvoerig gecontroleerd en aangepast om er voor te zorgen dat het ingeleverde werk mijn eigen competenties en leeruitkomsten reflecteert. Alle architecturale beslissingen, business rules en technische keuzes zijn gebaseerd op mijn eigen analyse en in overleg met stakeholders. Ik draag de volledige verantwoordelijkheid voor de inhoud van dit werk.

*AIAS Niveau: 3 - AI Samenwerking*

---

**Document Einde** - Versie 1.0 - 5 februari 2026
