"""
MSG-3 Maximo Mapper - Hoofd mapping logic

Coordineert de mapping van MSG-3 data naar Maximo objecten.

CRITICAL: Volgorde van object creatie in Maximo:
1. Commodity Groups & Codes (moet bestaan voor Items)
2. Item Master (moet bestaan voor PM/JobPlan)
3. Item/Organization Details (automatisch door Maximo)
4. PM (Preventive Maintenance)
5. JobPlan (Job Plans)

Gebaseerd op Maximo Secrets specificaties (maximosecrets.com)

Auteur: Pedro (met Cursor AI assistentie)
Datum: 4 februari 2026
Laatste Update: 17 februari 2026 (Maximo specificaties toegevoegd)
"""

import logging
from typing import Dict, List, Any, Optional

from .item_mapper import ItemMapper
from .pm_mapper import PMMapper
from .jobplan_mapper import JobPlanMapper

logger = logging.getLogger(__name__)


class MSG3MaximoMapper:
    """
    Hoofd mapper voor MSG-3 naar Maximo.
    
    Coordineert de mapping van MSG-3 taken naar verschillende
    Maximo objecten (Item, PM, JobPlan, Location, etc.).
    
    CRITICAL Maximo Rules:
    - Items MOETEN bestaan voordat ze in PM's of JobPlans worden gebruikt
    - Commodities MOETEN bestaan voordat ze aan Items worden toegewezen
    - Status workflow: PLANNING → ACTIVE (na approval)
    - ITEMNUM is immutable (kan niet worden gewijzigd na save)
    - NO DELETE actie (gebruik OBSOLETE status)
    
    Example:
        >>> mapper = MSG3MaximoMapper(
        ...     item_set_id="MSG3-MAINT",
        ...     org_id="SCHIPHOL"
        ... )
        >>> maximo_objects = mapper.map(msg3_data, changes)
        >>> print(f"Gegenereerd: {len(maximo_objects['items'])} Items")
        >>> print(f"Gegenereerd: {len(maximo_objects['pm'])} PM records")
    """
    
    def __init__(
        self, 
        item_set_id: str = "MSG3-MAINT",
        org_id: Optional[str] = None
    ):
        """
        Initialiseer de mapper.
        
        Args:
            item_set_id: Item Set ID voor MSG-3 items (default: "MSG3-MAINT")
            org_id: Organization ID (optioneel, moet geconfigureerd worden)
        """
        logger.info("MSG3MaximoMapper geïnitialiseerd")
        
        self.item_set_id = item_set_id
        self.org_id = org_id
        
        # Initialiseer sub-mappers
        self.item_mapper = ItemMapper(item_set_id=item_set_id, org_id=org_id)
        self.pm_mapper = PMMapper()
        self.jobplan_mapper = JobPlanMapper()
        
        logger.info(f"Mappers geïnitialiseerd voor Item Set: {item_set_id}, Org: {org_id}")
    
    def map(
        self, 
        msg3_data: Dict[str, Any],
        changes: Any = None
    ) -> Dict[str, List[Dict[str, Any]]]:
        """
        Map MSG-3 data naar Maximo objecten.
        
        CRITICAL: Volgorde is belangrijk!
        1. Commodities (moet bestaan voor Items)
        2. Items (moet bestaan voor PM/JobPlan)
        3. PM records
        4. JobPlan records
        
        Args:
            msg3_data: Geparseerde en gevalideerde MSG-3 data met:
                - tasks: List van MSG-3 taken
                - metadata: MSG-3 metadata (optioneel)
            changes: Optionele change report voor delta processing
            
        Returns:
            Dictionary met Maximo objecten in correcte volgorde:
            {
                "commodities": [...],      # Step 1: Commodity Groups & Codes
                "items": [...],            # Step 2: Item Master records
                "item_orgs": [...],        # Step 3: Item/Organization records
                "pm": [...],               # Step 4: PM records
                "jobplan": [...]           # Step 5: JobPlan records
            }
            
        Raises:
            ValueError: Als verplichte data ontbreekt of validatie faalt
        """
        logger.info("=== Starting MSG-3 → Maximo mapping ===")
        
        # Valideer input
        if not msg3_data or 'tasks' not in msg3_data:
            raise ValueError("MSG-3 data must contain 'tasks' key")
        
        tasks = msg3_data['tasks']
        if not tasks:
            logger.warning("No tasks found in MSG-3 data")
            return self._empty_result()
        
        logger.info(f"Mapping {len(tasks)} MSG-3 tasks to Maximo objects")
        
        # Initialize result containers
        maximo_objects = {
            "commodities": [],
            "items": [],
            "item_orgs": [],
            "pm": [],
            "jobplan": []
        }
        
        # Track errors
        mapping_errors = []
        
        # Step 1: Extract unique Commodity Groups & Codes
        logger.info("Step 1: Extracting Commodity Groups & Codes...")
        try:
            commodities = self._extract_commodities(tasks)
            maximo_objects["commodities"] = commodities
            logger.info(f"  ✓ Extracted {len(commodities)} unique commodities")
        except Exception as e:
            error_msg = f"Failed to extract commodities: {e}"
            logger.error(error_msg)
            mapping_errors.append(error_msg)
        
        # Step 2: Map taken naar Item Master records
        logger.info("Step 2: Mapping to Item Master records...")
        for task in tasks:
            try:
                item_record = self.item_mapper.map_task_to_item(task)
                maximo_objects["items"].append(item_record)
            except Exception as e:
                error_msg = f"Failed to map task {task.get('task_code')} to Item: {e}"
                logger.error(error_msg)
                mapping_errors.append(error_msg)
        
        logger.info(f"  ✓ Mapped {len(maximo_objects['items'])} Item Master records")
        
        # Step 3: Map taken naar Item/Organization records
        if self.org_id:
            logger.info("Step 3: Mapping to Item/Organization records...")
            for task in tasks:
                try:
                    item_org_record = self.item_mapper.map_task_to_item_org(task)
                    maximo_objects["item_orgs"].append(item_org_record)
                except Exception as e:
                    error_msg = f"Failed to map task {task.get('task_code')} to Item/Org: {e}"
                    logger.error(error_msg)
                    mapping_errors.append(error_msg)
            
            logger.info(f"  ✓ Mapped {len(maximo_objects['item_orgs'])} Item/Org records")
        else:
            logger.warning("Step 3: Skipping Item/Org mapping (no org_id configured)")
        
        # Step 4: Map taken naar PM records
        logger.info("Step 4: Mapping to PM records...")
        pm_records = self.pm_mapper.map_tasks(tasks)
        maximo_objects["pm"] = pm_records
        logger.info(f"  ✓ Mapped {len(maximo_objects['pm'])} PM records")
        
        # Step 5: Map taken naar JobPlan records
        logger.info("Step 5: Mapping to JobPlan records...")
        jobplan_records = self.jobplan_mapper.map_tasks(tasks)
        maximo_objects["jobplan"] = jobplan_records
        logger.info(f"  ✓ Mapped {len(maximo_objects['jobplan'])} JobPlan records")
        
        # Summary
        total_objects = sum(len(v) for v in maximo_objects.values())
        logger.info(f"=== Mapping complete: {total_objects} total objects ===")
        
        if mapping_errors:
            logger.warning(f"Mapping completed with {len(mapping_errors)} errors")
            for error in mapping_errors:
                logger.warning(f"  - {error}")
        
        return maximo_objects
    
    def _empty_result(self) -> Dict[str, List]:
        """Return empty result structure."""
        return {
            "commodities": [],
            "items": [],
            "item_orgs": [],
            "pm": [],
            "jobplan": []
        }
    
    def _extract_commodities(self, tasks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Extract unique Commodity Groups & Codes van MSG-3 taken.
        
        Returns list van commodity records die moeten worden aangemaakt:
        [
            {"COMMODITY": "ATA-32", "PARENT": None, "ISSERVICE": False},  # Group
            {"COMMODITY": "32-11", "PARENT": "ATA-32", "ISSERVICE": False}  # Code
        ]
        
        Args:
            tasks: List van MSG-3 taken
            
        Returns:
            List van unique commodity records
        """
        commodity_groups = set()
        commodity_codes = set()
        
        for task in tasks:
            ata_chapter = task.get("ata_chapter")
            ata_system = task.get("ata_system")
            
            if ata_chapter:
                # Add commodity group
                group = f"ATA-{ata_chapter}".upper()
                if len(group) <= 8:  # Maximo limit
                    commodity_groups.add((group, ata_chapter))
            
            if ata_chapter and ata_system:
                # Add commodity code
                code = f"{ata_chapter}-{ata_system}".upper()
                parent = f"ATA-{ata_chapter}".upper()
                if len(code) <= 8 and len(parent) <= 8:  # Maximo limit
                    commodity_codes.add((code, parent, ata_chapter, ata_system))
        
        # Build commodity records
        commodities = []
        
        # Add groups first
        for group, chapter in sorted(commodity_groups):
            commodities.append({
                "COMMODITY": group,
                "PARENT": None,  # Groups have no parent
                "ITEMSETID": self.item_set_id,
                "ISSERVICE": False,  # MSG-3 items are not services
                "DESCRIPTION": f"ATA Chapter {chapter}",  # Optional
            })
        
        # Add codes
        for code, parent, chapter, system in sorted(commodity_codes):
            commodities.append({
                "COMMODITY": code,
                "PARENT": parent,  # Link to group
                "ITEMSETID": self.item_set_id,
                "ISSERVICE": False,
                "DESCRIPTION": f"ATA {chapter}-{system}",  # Optional
            })
        
        logger.debug(f"Extracted {len(commodity_groups)} groups and {len(commodity_codes)} codes")
        return commodities


if __name__ == "__main__":
    # Test de mapper
    logging.basicConfig(level=logging.DEBUG)
    mapper = MSG3MaximoMapper()
    print("MSG3MaximoMapper ready for testing")
