"""
Business Rules Validator - Domein-specifieke validatie regels

Valideert MSG-3 data tegen Babcock @ Schiphol business rules:
- Security & Access Control regels
- Operations & Maintenance regels
- Quality & Compliance regels
- Logistics & Inventory regels
- Planning & Workflow regels
- IT & System Usage regels
- HR & Workforce regels
- Communication & Reporting regels

Auteur: Pedro (met Cursor AI assistentie)
Datum: 5 februari 2026
"""

import logging
from typing import Dict, List, Any, Optional, Callable
from dataclasses import dataclass
from enum import Enum
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)


class RuleCategory(Enum):
    """Categorieën van business rules."""
    SECURITY = "Security & Access Control"
    OPERATIONS = "Operations & Maintenance"
    QUALITY = "Quality & Compliance"
    LOGISTICS = "Logistics & Inventory"
    PLANNING = "Planning & Workflow"
    IT_SYSTEMS = "IT & System Usage"
    HR = "HR & Workforce"
    COMMUNICATION = "Communication & Reporting"


class RuleSeverity(Enum):
    """Ernst van rule violations."""
    CRITICAL = "critical"  # Blokkeert verdere processing
    ERROR = "error"        # Must be fixed
    WARNING = "warning"    # Should be reviewed
    INFO = "info"          # Informational


@dataclass
class BusinessRule:
    """
    Definitie van een business rule.
    
    Attributes:
        rule_id: Unieke identifier (bijv. "SEC-1.1")
        category: Categorie van de rule
        title: Korte beschrijving
        description: Volledige beschrijving
        severity: Ernst bij violation
        validation_func: Optionele validatie functie
    """
    rule_id: str
    category: RuleCategory
    title: str
    description: str
    severity: RuleSeverity
    validation_func: Optional[Callable] = None
    
    def __str__(self) -> str:
        return f"[{self.rule_id}] {self.title}"


@dataclass
class RuleViolation:
    """
    Representeert een business rule violation.
    
    Attributes:
        rule: De geschonden rule
        field: Veld waar violation optrad (optioneel)
        message: Beschrijving van de violation
        value: Actuele waarde (optioneel)
        context: Extra context informatie
    """
    rule: BusinessRule
    field: Optional[str]
    message: str
    value: Optional[Any] = None
    context: Optional[Dict[str, Any]] = None
    
    def __str__(self) -> str:
        return f"{self.rule.severity.value.upper()}: {self.rule.rule_id} - {self.message}"


class BusinessRulesValidator:
    """
    Valideert MSG-3 data tegen Babcock @ Schiphol business rules.
    
    Implementeert 80 business rules verdeeld over 8 categorieën:
    1. Security & Access Control (10 rules)
    2. Operations & Maintenance (10 rules)
    3. Quality & Compliance (10 rules)
    4. Logistics & Inventory (10 rules)
    5. Planning & Workflow (10 rules)
    6. IT & System Usage (10 rules)
    7. HR & Workforce (10 rules)
    8. Communication & Reporting (10 rules)
    """
    
    def __init__(self):
        """Initialiseer de business rules validator."""
        logger.debug("BusinessRulesValidator geïnitialiseerd")
        self.rules: Dict[str, BusinessRule] = {}
        self._load_rules()
        logger.info(f"Loaded {len(self.rules)} business rules")
    
    def _load_rules(self) -> None:
        """Laad alle business rules."""
        # 1. Security & Access Control
        self._load_security_rules()
        
        # 2. Operations & Maintenance
        self._load_operations_rules()
        
        # 3. Quality & Compliance
        self._load_quality_rules()
        
        # 4. Logistics & Inventory
        self._load_logistics_rules()
        
        # 5. Planning & Workflow
        self._load_planning_rules()
        
        # 6. IT & System Usage
        self._load_it_rules()
        
        # 7. HR & Workforce
        self._load_hr_rules()
        
        # 8. Communication & Reporting
        self._load_communication_rules()
    
    def _add_rule(self, rule: BusinessRule) -> None:
        """Voeg een rule toe aan de validator."""
        self.rules[rule.rule_id] = rule
    
    # ========================================================================
    # 1. SECURITY & ACCESS CONTROL RULES
    # ========================================================================
    
    def _load_security_rules(self) -> None:
        """Laad Security & Access Control rules."""
        self._add_rule(BusinessRule(
            rule_id="SEC-1.1",
            category=RuleCategory.SECURITY,
            title="Geldige Schiphol-pas vereist",
            description="Alleen medewerkers met een geldige Schiphol-pas mogen beveiligde zones betreden.",
            severity=RuleSeverity.CRITICAL
        ))
        
        self._add_rule(BusinessRule(
            rule_id="SEC-1.2",
            category=RuleCategory.SECURITY,
            title="VGB-screening voor airside toegang",
            description="Airside toegang vereist een geldige VGB‑screening.",
            severity=RuleSeverity.CRITICAL
        ))
        
        self._add_rule(BusinessRule(
            rule_id="SEC-1.3",
            category=RuleCategory.SECURITY,
            title="Jaarlijkse herkeuring toegangspassen",
            description="Alle toegangspassen moeten jaarlijks worden herkeurd.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="SEC-1.4",
            category=RuleCategory.SECURITY,
            title="Beperkte toegang technische ruimtes",
            description="Toegang tot technische ruimtes is beperkt tot geautoriseerd personeel.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="SEC-1.5",
            category=RuleCategory.SECURITY,
            title="Gereedschap registratie",
            description="Gereedschap moet worden geregistreerd bij in- en uitchecken.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="SEC-1.6",
            category=RuleCategory.SECURITY,
            title="Airside materialen vooraf aanmelden",
            description="Materialen die airside worden gebracht moeten vooraf worden aangemeld.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="SEC-1.7",
            category=RuleCategory.SECURITY,
            title="Bezoekers begeleiden",
            description="Bezoekers moeten altijd worden begeleid door een gecertificeerde medewerker.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="SEC-1.8",
            category=RuleCategory.SECURITY,
            title="PBM verplicht",
            description="Persoonlijke beschermingsmiddelen (PBM) zijn verplicht in alle operationele zones.",
            severity=RuleSeverity.CRITICAL
        ))
        
        self._add_rule(BusinessRule(
            rule_id="SEC-1.9",
            category=RuleCategory.SECURITY,
            title="Snelle incident melding",
            description="Incidenten moeten binnen 15 minuten worden gemeld aan de duty manager.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="SEC-1.10",
            category=RuleCategory.SECURITY,
            title="Foto's en video's verboden",
            description="Foto's en video's zijn verboden zonder expliciete toestemming.",
            severity=RuleSeverity.WARNING
        ))
    
    # ========================================================================
    # 2. OPERATIONS & MAINTENANCE RULES
    # ========================================================================
    
    def _load_operations_rules(self) -> None:
        """Laad Operations & Maintenance rules."""
        self._add_rule(BusinessRule(
            rule_id="OPS-2.1",
            category=RuleCategory.OPERATIONS,
            title="Preventief onderhoud binnen SLA",
            description="Preventief onderhoud moet worden uitgevoerd binnen de SLA-deadlines.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="OPS-2.2",
            category=RuleCategory.OPERATIONS,
            title="Correctief onderhoud responstijd",
            description="Correctief onderhoud moet worden opgepakt binnen de afgesproken responstijd.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="OPS-2.3",
            category=RuleCategory.OPERATIONS,
            title="Kwaliteitscontrole voor afsluiten",
            description="Werkorders mogen alleen worden afgesloten na kwaliteitscontrole.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="OPS-2.4",
            category=RuleCategory.OPERATIONS,
            title="Gecertificeerde elektriciens",
            description="Alleen gecertificeerde technici mogen werken aan elektrische installaties.",
            severity=RuleSeverity.CRITICAL
        ))
        
        self._add_rule(BusinessRule(
            rule_id="OPS-2.5",
            category=RuleCategory.OPERATIONS,
            title="OEM-specificaties volgen",
            description="Werkzaamheden moeten worden uitgevoerd volgens OEM-specificaties.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="OPS-2.6",
            category=RuleCategory.OPERATIONS,
            title="Jaarlijkse NEN-keuring",
            description="Alle installaties moeten jaarlijks worden gekeurd volgens NEN‑normen.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="OPS-2.7",
            category=RuleCategory.OPERATIONS,
            title="Afstemming operationele impact",
            description="Werkzaamheden met operationele impact moeten vooraf worden afgestemd met Schiphol Operations.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="OPS-2.8",
            category=RuleCategory.OPERATIONS,
            title="PTW voor risicovol werk",
            description="Werkvergunningen (PTW) zijn verplicht voor risicovolle werkzaamheden.",
            severity=RuleSeverity.CRITICAL
        ))
        
        self._add_rule(BusinessRule(
            rule_id="OPS-2.9",
            category=RuleCategory.OPERATIONS,
            title="TRA verplicht",
            description="Taken mogen niet worden uitgevoerd zonder goedgekeurde TRA (Taak Risico Analyse).",
            severity=RuleSeverity.CRITICAL
        ))
        
        self._add_rule(BusinessRule(
            rule_id="OPS-2.10",
            category=RuleCategory.OPERATIONS,
            title="24-uur vooraf aanmelden kritieke zones",
            description="Werkzaamheden in kritieke zones moeten minimaal 24 uur vooraf worden aangemeld.",
            severity=RuleSeverity.ERROR
        ))
    
    # ========================================================================
    # 3. QUALITY & COMPLIANCE RULES
    # ========================================================================
    
    def _load_quality_rules(self) -> None:
        """Laad Quality & Compliance rules."""
        self._add_rule(BusinessRule(
            rule_id="QUA-3.1",
            category=RuleCategory.QUALITY,
            title="ISO 9001 en ISO 45001 compliance",
            description="Alle werkzaamheden moeten voldoen aan ISO 9001 en ISO 45001.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="QUA-3.2",
            category=RuleCategory.QUALITY,
            title="Documentatie binnen 24 uur bijwerken",
            description="Documentatie moet binnen 24 uur worden bijgewerkt in het onderhoudssysteem.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="QUA-3.3",
            category=RuleCategory.QUALITY,
            title="Afwijkingen registreren",
            description="Afwijkingen moeten worden geregistreerd in het kwaliteitsmanagementsysteem.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="QUA-3.4",
            category=RuleCategory.QUALITY,
            title="Goedgekeurde materialen en leveranciers",
            description="Alleen goedgekeurde materialen en leveranciers mogen worden gebruikt.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="QUA-3.5",
            category=RuleCategory.QUALITY,
            title="Wekelijkse rapportages",
            description="Rapportages moeten wekelijks worden aangeleverd aan de contractmanager.",
            severity=RuleSeverity.WARNING
        ))
        
        self._add_rule(BusinessRule(
            rule_id="QUA-3.6",
            category=RuleCategory.QUALITY,
            title="Up-to-date tekeningen",
            description="Alle technische tekeningen moeten up‑to‑date zijn voordat werk start.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="QUA-3.7",
            category=RuleCategory.QUALITY,
            title="Auditbevindingen binnen 30 dagen",
            description="Auditbevindingen moeten binnen 30 dagen worden opgelost.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="QUA-3.8",
            category=RuleCategory.QUALITY,
            title="RCA voor veiligheidsincidenten",
            description="Veiligheidsincidenten moeten worden geëvalueerd met een RCA (root cause analysis).",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="QUA-3.9",
            category=RuleCategory.QUALITY,
            title="Jaarlijkse veiligheidstrainingen",
            description="Alle medewerkers moeten jaarlijkse veiligheidstrainingen volgen.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="QUA-3.10",
            category=RuleCategory.QUALITY,
            title="Geldige certificeringen vereist",
            description="Werk mag niet worden uitgevoerd zonder geldige certificeringen.",
            severity=RuleSeverity.CRITICAL
        ))
    
    # ========================================================================
    # 4. LOGISTICS & INVENTORY RULES (incl. Maximo Item Rules)
    # ========================================================================
    
    def _load_logistics_rules(self) -> None:
        """Laad Logistics & Inventory rules (incl. Maximo Item Master regels)."""
        # Maximo Item Master Rules (from maximosecrets.com)
        self._add_rule(BusinessRule(
            rule_id="LOG-4.0.1",
            category=RuleCategory.LOGISTICS,
            title="ITEMNUM max 30 characters uppercase",
            description="Item Number moet max 30 characters zijn en uppercase. Best practice: max 12 voor UI readability.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="LOG-4.0.2",
            category=RuleCategory.LOGISTICS,
            title="Item Description verplicht en uniek",
            description="Description is verplicht (max 100 chars) en moet uniek en duidelijk zijn voor zoekbaarheid in 10,000+ items.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="LOG-4.0.3",
            category=RuleCategory.LOGISTICS,
            title="Commodity Group en Code toewijzen",
            description="ALTIJD commodity group en code toewijzen voor zoekbaarheid en reporting. Format: ATA Chapter → Group, ATA System → Code.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="LOG-4.0.4",
            category=RuleCategory.LOGISTICS,
            title="Item Status correct instellen",
            description="Items starten als PLANNING, worden ACTIVE na goedkeuring. OBSOLETE is irreversible en requires PENDOBS eerst.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="LOG-4.0.5",
            category=RuleCategory.LOGISTICS,
            title="Stock Category NS voor MSG-3 items",
            description="MSG-3 items zijn Non-Stocked (NS) omdat het taken zijn, geen fysieke voorraad items.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="LOG-4.0.6",
            category=RuleCategory.LOGISTICS,
            title="ITEMNUM is immutable",
            description="Item Number kan NIET worden gewijzigd na save. Oude item OBSOLETE maken en nieuw item aanmaken indien nodig.",
            severity=RuleSeverity.CRITICAL
        ))
        
        self._add_rule(BusinessRule(
            rule_id="LOG-4.0.7",
            category=RuleCategory.LOGISTICS,
            title="Item kan niet worden verwijderd",
            description="Er is geen Delete Item actie. Gebruik status OBSOLETE om items te retiren.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="LOG-4.0.8",
            category=RuleCategory.LOGISTICS,
            title="Commodity max 8 characters uppercase",
            description="Commodity Groups en Codes zijn max 8 characters en uppercase. Format: UPPER 8.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="LOG-4.0.9",
            category=RuleCategory.LOGISTICS,
            title="Item Status transitions valideren",
            description="Status wijzigingen valideren: OBSOLETE requires PENDOBS, OBSOLETE is irreversible, anderen kunnen vrij transitioneren.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="LOG-4.0.10",
            category=RuleCategory.LOGISTICS,
            title="Geen OBSOLETE bij active references",
            description="Item mag niet OBSOLETE worden als er references zijn in work plans, job plans, PR/PO lines, of item balance bestaat.",
            severity=RuleSeverity.CRITICAL
        ))
        
        # Original LOG-4.1 rule
        self._add_rule(BusinessRule(
            rule_id="LOG-4.1",
            category=RuleCategory.LOGISTICS,
            title="Voorraadniveaus binnen min/max",
            description="Voorraadniveaus moeten binnen minimum- en maximumwaarden blijven.",
            severity=RuleSeverity.WARNING
        ))
        
        self._add_rule(BusinessRule(
            rule_id="LOG-4.2",
            category=RuleCategory.LOGISTICS,
            title="Materialen op juiste werkorder boeken",
            description="Materialen moeten worden geboekt op de juiste werkorder.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="LOG-4.3",
            category=RuleCategory.LOGISTICS,
            title="Spoedbestellingen goedkeuring",
            description="Spoedbestellingen vereisen goedkeuring van de supervisor.",
            severity=RuleSeverity.WARNING
        ))
        
        self._add_rule(BusinessRule(
            rule_id="LOG-4.4",
            category=RuleCategory.LOGISTICS,
            title="Retourmaterialen binnen 48 uur",
            description="Retourmaterialen moeten binnen 48 uur worden verwerkt.",
            severity=RuleSeverity.WARNING
        ))
        
        self._add_rule(BusinessRule(
            rule_id="LOG-4.5",
            category=RuleCategory.LOGISTICS,
            title="Afvalscheiding Schiphol regels",
            description="Afval moet worden gescheiden volgens Schiphol‑milieuregels.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="LOG-4.6",
            category=RuleCategory.LOGISTICS,
            title="Airside leveringen aanmelden",
            description="Leveringen airside moeten vooraf worden aangemeld bij security.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="LOG-4.7",
            category=RuleCategory.LOGISTICS,
            title="Serienummers registreren",
            description="Materialen met serienummers moeten worden geregistreerd in het systeem.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="LOG-4.8",
            category=RuleCategory.LOGISTICS,
            title="Defecte onderdelen apart opslaan",
            description="Defecte onderdelen moeten worden gemarkeerd en apart opgeslagen.",
            severity=RuleSeverity.WARNING
        ))
        
        self._add_rule(BusinessRule(
            rule_id="LOG-4.9",
            category=RuleCategory.LOGISTICS,
            title="Realtime magazijnbewegingen",
            description="Magazijnbewegingen moeten realtime worden bijgewerkt.",
            severity=RuleSeverity.WARNING
        ))
        
        self._add_rule(BusinessRule(
            rule_id="LOG-4.10",
            category=RuleCategory.LOGISTICS,
            title="Geautoriseerd magazijnpersoneel",
            description="Alleen geautoriseerd personeel mag magazijnsystemen bedienen.",
            severity=RuleSeverity.ERROR
        ))
    
    # ========================================================================
    # 5. PLANNING & WORKFLOW RULES
    # ========================================================================
    
    def _load_planning_rules(self) -> None:
        """Laad Planning & Workflow rules."""
        self._add_rule(BusinessRule(
            rule_id="PLN-5.1",
            category=RuleCategory.PLANNING,
            title="Planning op basis prioriteit en SLA",
            description="Werkopdrachten moeten worden ingepland op basis van prioriteit en SLA.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="PLN-5.2",
            category=RuleCategory.PLANNING,
            title="Dagelijks uren registreren",
            description="Medewerkers moeten hun uren dagelijks registreren.",
            severity=RuleSeverity.WARNING
        ))
        
        self._add_rule(BusinessRule(
            rule_id="PLN-5.3",
            category=RuleCategory.PLANNING,
            title="Werkvergunning vereist voor start",
            description="Werk mag niet starten zonder goedgekeurde werkvergunning.",
            severity=RuleSeverity.CRITICAL
        ))
        
        self._add_rule(BusinessRule(
            rule_id="PLN-5.4",
            category=RuleCategory.PLANNING,
            title="Geen taken overslaan",
            description="Taken mogen niet worden overgeslagen zonder supervisor‑goedkeuring.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="PLN-5.5",
            category=RuleCategory.PLANNING,
            title="Volledige werkorder invulling",
            description="Werkorders moeten volledig worden ingevuld voordat ze worden afgesloten.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="PLN-5.6",
            category=RuleCategory.PLANNING,
            title="Taken in juiste volgorde",
            description="Taken met afhankelijkheden moeten in de juiste volgorde worden uitgevoerd.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="PLN-5.7",
            category=RuleCategory.PLANNING,
            title="Werk overdragen bij einde shift",
            description="Werk dat niet binnen de shift kan worden afgerond moet worden overgedragen.",
            severity=RuleSeverity.WARNING
        ))
        
        self._add_rule(BusinessRule(
            rule_id="PLN-5.8",
            category=RuleCategory.PLANNING,
            title="Spoedwerk na escalatie",
            description="Spoedwerk mag alleen worden uitgevoerd na escalatie.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="PLN-5.9",
            category=RuleCategory.PLANNING,
            title="Afstemming passagiersstromen",
            description="Werk dat impact heeft op passagiersstromen moet worden afgestemd met Operations.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="PLN-5.10",
            category=RuleCategory.PLANNING,
            title="Planning 1 week vooruit",
            description="Werkplanning moet minimaal 1 week vooruit worden bijgewerkt.",
            severity=RuleSeverity.WARNING
        ))
    
    # ========================================================================
    # 6. IT & SYSTEM USAGE RULES
    # ========================================================================
    
    def _load_it_rules(self) -> None:
        """Laad IT & System Usage rules."""
        self._add_rule(BusinessRule(
            rule_id="IT-6.1",
            category=RuleCategory.IT_SYSTEMS,
            title="Centrale onderhoudssysteem verplicht",
            description="Alle werkorders moeten worden verwerkt in het centrale onderhoudssysteem (bijv. Maximo).",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="IT-6.2",
            category=RuleCategory.IT_SYSTEMS,
            title="Eigen accounts gebruiken",
            description="Medewerkers mogen alleen hun eigen accounts gebruiken.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="IT-6.3",
            category=RuleCategory.IT_SYSTEMS,
            title="GDPR-richtlijnen",
            description="Data moet worden opgeslagen volgens GDPR‑richtlijnen.",
            severity=RuleSeverity.CRITICAL
        ))
        
        self._add_rule(BusinessRule(
            rule_id="IT-6.4",
            category=RuleCategory.IT_SYSTEMS,
            title="Mobiele apparaten vergrendelen",
            description="Mobiele apparaten moeten worden vergrendeld bij het verlaten van de werkplek.",
            severity=RuleSeverity.WARNING
        ))
        
        self._add_rule(BusinessRule(
            rule_id="IT-6.5",
            category=RuleCategory.IT_SYSTEMS,
            title="Geautoriseerde documentatie wijzigingen",
            description="Alleen geautoriseerde medewerkers mogen technische documentatie wijzigen.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="IT-6.6",
            category=RuleCategory.IT_SYSTEMS,
            title="IT-beheer voor systeemupdates",
            description="Systeemupdates mogen alleen worden uitgevoerd door IT‑beheer.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="IT-6.7",
            category=RuleCategory.IT_SYSTEMS,
            title="Offline werk binnen 4 uur synchroniseren",
            description="Offline werk moet binnen 4 uur worden gesynchroniseerd.",
            severity=RuleSeverity.WARNING
        ))
        
        self._add_rule(BusinessRule(
            rule_id="IT-6.8",
            category=RuleCategory.IT_SYSTEMS,
            title="Foto's toevoegen aan werkorder",
            description="Foto's van installaties moeten worden toegevoegd aan de werkorder.",
            severity=RuleSeverity.INFO
        ))
        
        self._add_rule(BusinessRule(
            rule_id="IT-6.9",
            category=RuleCategory.IT_SYSTEMS,
            title="Onjuiste data binnen 24 uur corrigeren",
            description="Onjuiste data moet binnen 24 uur worden gecorrigeerd.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="IT-6.10",
            category=RuleCategory.IT_SYSTEMS,
            title="Toegang intrekken bij inactiviteit",
            description="Toegang tot systemen wordt ingetrokken bij inactiviteit van 30 dagen.",
            severity=RuleSeverity.WARNING
        ))
    
    # ========================================================================
    # 7. HR & WORKFORCE RULES
    # ========================================================================
    
    def _load_hr_rules(self) -> None:
        """Laad HR & Workforce rules."""
        self._add_rule(BusinessRule(
            rule_id="HR-7.1",
            category=RuleCategory.HR,
            title="Jaarlijkse veiligheidstrainingen",
            description="Medewerkers moeten jaarlijkse veiligheidstrainingen volgen.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="HR-7.2",
            category=RuleCategory.HR,
            title="Onboarding-proces",
            description="Nieuwe medewerkers moeten een onboarding-proces doorlopen.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="HR-7.3",
            category=RuleCategory.HR,
            title="Ziekmeldingen voor dienst",
            description="Ziekmeldingen moeten vóór aanvang van de dienst worden doorgegeven.",
            severity=RuleSeverity.WARNING
        ))
        
        self._add_rule(BusinessRule(
            rule_id="HR-7.4",
            category=RuleCategory.HR,
            title="Overuren goedkeuren",
            description="Overuren moeten vooraf worden goedgekeurd.",
            severity=RuleSeverity.WARNING
        ))
        
        self._add_rule(BusinessRule(
            rule_id="HR-7.5",
            category=RuleCategory.HR,
            title="Schiphol-gedragscode",
            description="Medewerkers moeten voldoen aan de Schiphol‑gedragscode.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="HR-7.6",
            category=RuleCategory.HR,
            title="Up-to-date certificeringen",
            description="Certificeringen moeten up‑to‑date blijven.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="HR-7.7",
            category=RuleCategory.HR,
            title="Toolboxmeetings",
            description="Medewerkers moeten deelnemen aan toolboxmeetings.",
            severity=RuleSeverity.WARNING
        ))
        
        self._add_rule(BusinessRule(
            rule_id="HR-7.8",
            category=RuleCategory.HR,
            title="Alcohol en drugs verboden",
            description="Alcohol- en drugsgebruik is verboden tijdens werktijd.",
            severity=RuleSeverity.CRITICAL
        ))
        
        self._add_rule(BusinessRule(
            rule_id="HR-7.9",
            category=RuleCategory.HR,
            title="Ongewenst gedrag melden",
            description="Ongewenst gedrag moet worden gemeld bij HR.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="HR-7.10",
            category=RuleCategory.HR,
            title="Schiphol-pas verlies melden",
            description="Medewerkers moeten hun Schiphol-pas direct melden bij verlies.",
            severity=RuleSeverity.CRITICAL
        ))
    
    # ========================================================================
    # 8. COMMUNICATION & REPORTING RULES
    # ========================================================================
    
    def _load_communication_rules(self) -> None:
        """Laad Communication & Reporting rules."""
        self._add_rule(BusinessRule(
            rule_id="COM-8.1",
            category=RuleCategory.COMMUNICATION,
            title="Storingen direct melden",
            description="Storingen moeten direct worden gemeld via het officiële meldpunt.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="COM-8.2",
            category=RuleCategory.COMMUNICATION,
            title="Klantcommunicatie via contractmanager",
            description="Klantcommunicatie verloopt via de contractmanager of teamleider.",
            severity=RuleSeverity.WARNING
        ))
        
        self._add_rule(BusinessRule(
            rule_id="COM-8.3",
            category=RuleCategory.COMMUNICATION,
            title="Dagelijkse voortgang in shiftlog",
            description="Dagelijkse voortgang moet worden gerapporteerd in het shiftlog.",
            severity=RuleSeverity.WARNING
        ))
        
        self._add_rule(BusinessRule(
            rule_id="COM-8.4",
            category=RuleCategory.COMMUNICATION,
            title="Escalaties volgens escalatiemodel",
            description="Escalaties moeten worden opgevolgd volgens het escalatiemodel.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="COM-8.5",
            category=RuleCategory.COMMUNICATION,
            title="Volledige rapportages",
            description="Rapportages moeten volledig en foutloos zijn.",
            severity=RuleSeverity.WARNING
        ))
        
        self._add_rule(BusinessRule(
            rule_id="COM-8.6",
            category=RuleCategory.COMMUNICATION,
            title="Planning wijzigingen communiceren",
            description="Wijzigingen in planning moeten worden gecommuniceerd naar alle betrokkenen.",
            severity=RuleSeverity.WARNING
        ))
        
        self._add_rule(BusinessRule(
            rule_id="COM-8.7",
            category=RuleCategory.COMMUNICATION,
            title="Incidentrapporten binnen 24 uur",
            description="Incidentrapporten moeten binnen 24 uur worden ingediend.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="COM-8.8",
            category=RuleCategory.COMMUNICATION,
            title="Professionele communicatie",
            description="Communicatie moet professioneel en conform bedrijfsrichtlijnen zijn.",
            severity=RuleSeverity.WARNING
        ))
        
        self._add_rule(BusinessRule(
            rule_id="COM-8.9",
            category=RuleCategory.COMMUNICATION,
            title="Afwijkingen direct melden",
            description="Afwijkingen moeten direct worden gemeld.",
            severity=RuleSeverity.ERROR
        ))
        
        self._add_rule(BusinessRule(
            rule_id="COM-8.10",
            category=RuleCategory.COMMUNICATION,
            title="Klantfeedback registreren",
            description="Klantfeedback moet worden geregistreerd en opgevolgd.",
            severity=RuleSeverity.INFO
        ))
    
    # ========================================================================
    # VALIDATION METHODS
    # ========================================================================
    
    def validate(self, data: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> List[RuleViolation]:
        """
        Valideer data tegen alle relevante business rules.
        
        Args:
            data: MSG-3 data of andere te valideren data
            context: Optionele context informatie (bijv. user info, permissions)
            
        Returns:
            Lijst van RuleViolation objecten
        """
        violations = []
        context = context or {}
        
        logger.debug(f"Starting business rules validation with {len(self.rules)} rules")
        
        # Valideer alle rules die een validation_func hebben
        for rule_id, rule in self.rules.items():
            if rule.validation_func:
                try:
                    violation = rule.validation_func(data, context)
                    if violation:
                        violations.append(violation)
                except Exception as e:
                    logger.error(f"Error validating rule {rule_id}: {e}")
        
        logger.info(f"Business rules validation complete. Found {len(violations)} violations")
        return violations
    
    def validate_by_category(self, 
                            data: Dict[str, Any], 
                            category: RuleCategory,
                            context: Optional[Dict[str, Any]] = None) -> List[RuleViolation]:
        """
        Valideer data tegen rules van een specifieke categorie.
        
        Args:
            data: Te valideren data
            category: Rule categorie om te valideren
            context: Optionele context
            
        Returns:
            Lijst van violations voor de gegeven categorie
        """
        violations = []
        context = context or {}
        
        category_rules = {rid: r for rid, r in self.rules.items() if r.category == category}
        logger.debug(f"Validating {len(category_rules)} rules in category {category.value}")
        
        for rule_id, rule in category_rules.items():
            if rule.validation_func:
                try:
                    violation = rule.validation_func(data, context)
                    if violation:
                        violations.append(violation)
                except Exception as e:
                    logger.error(f"Error validating rule {rule_id}: {e}")
        
        return violations
    
    def get_rule(self, rule_id: str) -> Optional[BusinessRule]:
        """Haal een specifieke rule op."""
        return self.rules.get(rule_id)
    
    def get_rules_by_category(self, category: RuleCategory) -> Dict[str, BusinessRule]:
        """Haal alle rules van een categorie op."""
        return {rid: r for rid, r in self.rules.items() if r.category == category}
    
    def get_rules_by_severity(self, severity: RuleSeverity) -> Dict[str, BusinessRule]:
        """Haal alle rules van een bepaalde severity op."""
        return {rid: r for rid, r in self.rules.items() if r.severity == severity}
    
    def get_all_rules(self) -> Dict[str, BusinessRule]:
        """Haal alle rules op."""
        return self.rules.copy()
    
    def get_rule_summary(self) -> Dict[str, Any]:
        """
        Genereer een samenvatting van alle rules.
        
        Returns:
            Dictionary met statistieken over de rules
        """
        summary = {
            "total_rules": len(self.rules),
            "by_category": {},
            "by_severity": {},
            "rules": []
        }
        
        # Count by category
        for category in RuleCategory:
            count = len(self.get_rules_by_category(category))
            summary["by_category"][category.value] = count
        
        # Count by severity
        for severity in RuleSeverity:
            count = len(self.get_rules_by_severity(severity))
            summary["by_severity"][severity.value] = count
        
        # List all rules
        for rule_id, rule in self.rules.items():
            summary["rules"].append({
                "rule_id": rule.rule_id,
                "category": rule.category.value,
                "severity": rule.severity.value,
                "title": rule.title
            })
        
        return summary
