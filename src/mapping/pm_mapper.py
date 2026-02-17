"""
PM Mapper - MSG-3 naar Maximo PM object mapping

Mapt MSG-3 taken naar Maximo PM (Preventive Maintenance) records.

Gebaseerd op Maximo Secrets specificaties:
- Item Master: https://maximosecrets.com/2026/02/11/item-master/
- Item Statuses: https://maximosecrets.com/2026/02/13/item-statuses-2/
- Commodity Groups: https://maximosecrets.com/2026/02/04/commodity-groups-and-codes/

Auteur: Pedro (met Cursor AI assistentie)
Datum: 4 februari 2026
Laatste Update: 17 februari 2026 (Maximo specificaties toegevoegd)
"""

import logging
from typing import Dict, List, Any, Optional

logger = logging.getLogger(__name__)


class PMMapper:
    """
    Mapt MSG-3 taken naar Maximo PM objects.
    
    PM (Preventive Maintenance) records in Maximo representeren
    de onderhoudstaken met intervals en routing.
    
    Mapping MSG-3 → Maximo:
    - MSG-3 Task Code → PM.PMNUM
    - MSG-3 Description → PM.DESCRIPTION
    - MSG-3 Interval → PM.FREQUENCY + PM.FREQUNIT
    - MSG-3 Zone → PM.LOCATION
    - MSG-3 ATA Chapter → PM.WORKTYPE (of custom field)
    
    CRITICAL Maximo Rules (from maximosecrets.com):
    - PMNUM is immutable after save (cannot be changed)
    - Description max 100 characters
    - Status: PENDING → PLANNING → ACTIVE → PENDOBS → OBSOLETE
    - OBSOLETE is irreversible and requires PENDOBS first
    - No delete action available, use OBSOLETE status instead
    """
    
    def __init__(self):
        """Initialiseer de PM mapper."""
        logger.debug("PMMapper geïnitialiseerd")
        self._load_mapping_config()
        
        # Maximo Item Set voor MSG-3 items
        self.item_set_id = "MSG3-MAINT"
        
        # Default organization (wordt geconfigureerd)
        self.default_org_id = None  # TODO: Configure from settings
    
    def _load_mapping_config(self) -> None:
        """Laad mapping configuratie."""
        # Interval unit mapping (MSG-3 → Maximo)
        self.interval_unit_mapping = {
            "FH": "HOURS",      # Flight Hours
            "FC": "CYCLES",     # Flight Cycles
            "MO": "MONTHS",     # Months
            "WK": "WEEKS",      # Weeks
            "DA": "DAYS"        # Days (extra)
        }
        
        # Status mapping
        self.status_mapping = {
            "draft": "PLANNING",
            "active": "ACTIVE",
            "retired": "OBSOLETE"
        }
    
    def map_task(self, msg3_task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Map een MSG-3 taak naar een Maximo PM object.
        
        Args:
            msg3_task: MSG-3 taak dictionary met fields:
                - task_code: MSG-3 task nummer
                - description: Task beschrijving
                - interval: Onderhoud interval
                - interval_unit: Unit (FH, FC, MO, WK)
                - ata_chapter: ATA chapter nummer
                - ata_system: ATA system nummer
                - zone: Aircraft zone
                - man_hours: Geschatte uren
                
        Returns:
            Maximo PM object dictionary
            
        Raises:
            ValueError: Als verplichte velden ontbreken of validatie faalt
            
        Example:
            >>> pm_mapper = PMMapper()
            >>> msg3_task = {
            ...     "task_code": "32-11-01-001",
            ...     "description": "Visual inspection landing gear door",
            ...     "interval": 500,
            ...     "interval_unit": "FH",
            ...     "ata_chapter": "32",
            ...     "ata_system": "11",
            ...     "zone": "NOSE"
            ... }
            >>> pm_record = pm_mapper.map_task(msg3_task)
            >>> print(pm_record['PMNUM'])
            MSG3-32-11-01-001
        """
        # Valideer verplichte velden
        self._validate_required_fields(msg3_task)
        
        # Generate PMNUM (format: MSG3-{task_code})
        pmnum = self._generate_pmnum(msg3_task.get("task_code"))
        
        # Valideer PMNUM length (max 30 chars)
        if len(pmnum) > 30:
            raise ValueError(f"PMNUM too long ({len(pmnum)} > 30): {pmnum}")
        
        # Description validatie en formatting
        description = self._format_description(msg3_task.get("description"))
        
        # Commodity mapping van ATA codes
        commodity_group = self._map_commodity_group(msg3_task.get("ata_chapter"))
        commodity_code = self._map_commodity_code(
            msg3_task.get("ata_chapter"),
            msg3_task.get("ata_system")
        )
        
        # Build Maximo PM record
        pm_record = {
            # Key Fields
            "PMNUM": pmnum,
            "DESCRIPTION": description,
            
            # Interval Fields
            "FREQUENCY": msg3_task.get("interval"),
            "FREQUNIT": self._map_interval_unit(msg3_task.get("interval_unit")),
            
            # Location & Zone
            "LOCATION": msg3_task.get("zone"),
            
            # Status (new items start as PLANNING per Maximo best practice)
            "STATUS": "PLANNING",
            
            # Work Type (derived from ATA or custom field)
            "WORKTYPE": "PM",  # TODO: Map from ATA chapter
            
            # Commodity (for reporting & analysis)
            "COMMODITY": commodity_group,
            "COMMODITYCODE": commodity_code,
            
            # Duration Estimate
            "SCHEDCALDAYS": msg3_task.get("man_hours", 0),
            
            # Item Master Integration
            "ITEMNUM": pmnum,  # Reference to Item Master record
            "ITEMSETID": self.item_set_id,
            
            # Priority (default, can be overridden)
            "PRIORITY": self._map_priority(msg3_task.get("priority")),
            
            # Additional Fields
            "JPNUM": pmnum,  # Reference to Job Plan
            "ROUTE": msg3_task.get("route", False),
            
            # MSG-3 Specific (custom fields - configured in Maximo)
            "PLUSCMSG3TASKCODE": msg3_task.get("task_code"),
            "PLUSCMSG3ATA": msg3_task.get("ata_chapter"),
            "PLUSCMSG3SYSTEM": msg3_task.get("ata_system"),
        }
        
        logger.debug(f"Mapped MSG-3 task {msg3_task.get('task_code')} → PM {pmnum}")
        return pm_record
    
    def _validate_required_fields(self, msg3_task: Dict[str, Any]) -> None:
        """
        Valideer verplichte MSG-3 velden.
        
        Args:
            msg3_task: MSG-3 taak dictionary
            
        Raises:
            ValueError: Als verplichte velden ontbreken
        """
        required_fields = ["task_code", "description", "ata_chapter"]
        missing = [f for f in required_fields if not msg3_task.get(f)]
        
        if missing:
            raise ValueError(f"Missing required fields: {', '.join(missing)}")
    
    def _generate_pmnum(self, task_code: str) -> str:
        """
        Genereer Maximo PMNUM van MSG-3 task code.
        
        Format: MSG3-{task_code}
        Max: 30 characters (Maximo limit)
        Uppercase only (Maximo convention)
        
        Args:
            task_code: MSG-3 task code (bijv. "32-11-01-001")
            
        Returns:
            Maximo PMNUM (bijv. "MSG3-32-11-01-001")
        """
        pmnum = f"MSG3-{task_code}".upper()
        return pmnum
    
    def _format_description(self, description: str) -> str:
        """
        Format en valideer description voor Maximo.
        
        Maximo Rules:
        - Max 100 characters (CRITICAL)
        - Should be unique and clear for search
        - Min 10 chars recommended
        
        Args:
            description: MSG-3 task description
            
        Returns:
            Formatted description
            
        Raises:
            ValueError: Als description te lang
        """
        if not description:
            raise ValueError("Description is required")
        
        # Trim whitespace
        description = description.strip()
        
        # Check length
        if len(description) > 100:
            logger.warning(f"Description too long ({len(description)} chars), truncating to 100")
            description = description[:97] + "..."
        
        if len(description) < 10:
            logger.warning(f"Description very short ({len(description)} chars): {description}")
        
        return description
    
    def _map_commodity_group(self, ata_chapter: str) -> str:
        """
        Map ATA Chapter naar Maximo Commodity Group.
        
        Format: ATA-{chapter}
        Max: 8 characters (Maximo UPPER 8)
        
        Args:
            ata_chapter: ATA chapter nummer (bijv. "32")
            
        Returns:
            Commodity Group (bijv. "ATA-32")
        """
        if not ata_chapter:
            logger.warning("No ATA chapter provided for commodity group")
            return ""
        
        commodity_group = f"ATA-{ata_chapter}".upper()
        
        if len(commodity_group) > 8:
            raise ValueError(f"Commodity Group too long: {commodity_group}")
        
        return commodity_group
    
    def _map_commodity_code(self, ata_chapter: str, ata_system: str) -> str:
        """
        Map ATA Chapter + System naar Maximo Commodity Code.
        
        Format: {chapter}-{system}
        Max: 8 characters (Maximo UPPER 8)
        
        Args:
            ata_chapter: ATA chapter nummer (bijv. "32")
            ata_system: ATA system nummer (bijv. "11")
            
        Returns:
            Commodity Code (bijv. "32-11")
        """
        if not ata_chapter or not ata_system:
            logger.warning("Incomplete ATA codes for commodity code")
            return ""
        
        commodity_code = f"{ata_chapter}-{ata_system}".upper()
        
        if len(commodity_code) > 8:
            raise ValueError(f"Commodity Code too long: {commodity_code}")
        
        return commodity_code
    
    def _map_priority(self, priority: Optional[int]) -> int:
        """
        Map MSG-3 priority naar Maximo priority.
        
        Args:
            priority: MSG-3 priority (optioneel)
            
        Returns:
            Maximo priority (default 3 = medium)
        """
        if priority is None:
            return 3  # Medium priority
        
        # Ensure priority is within Maximo range (typically 1-5)
        return max(1, min(5, priority))
    
    def map_tasks(self, msg3_tasks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Map meerdere MSG-3 taken naar PM objects.
        
        Args:
            msg3_tasks: Lijst van MSG-3 taken
            
        Returns:
            Lijst van Maximo PM objects
        """
        pm_records = []
        for task in msg3_tasks:
            try:
                pm_record = self.map_task(task)
                pm_records.append(pm_record)
            except Exception as e:
                logger.error(f"Fout bij mappen taak {task.get('task_code')}: {e}")
        
        return pm_records
    
    def _map_interval_unit(self, msg3_unit: str) -> str:
        """
        Map MSG-3 interval unit naar Maximo FREQUNIT.
        
        MSG-3 units:
        - FH = Flight Hours
        - FC = Flight Cycles
        - MO = Months
        - WK = Weeks
        
        Maximo FREQUNIT:
        - HOURS
        - CYCLES  
        - MONTHS
        - WEEKS
        
        Args:
            msg3_unit: MSG-3 interval unit
            
        Returns:
            Maximo FREQUNIT value
        """
        unit_mapping = {
            "FH": "HOURS",
            "FC": "CYCLES",
            "MO": "MONTHS",
            "WK": "WEEKS"
        }
        
        return unit_mapping.get(msg3_unit, "HOURS")
