"""
Item Mapper - MSG-3 naar Maximo Item Master mapping

Mapt MSG-3 taken naar Maximo Item Master records.

Items moeten EERST worden aangemaakt voordat ze in PM's of JobPlans worden gebruikt!

Gebaseerd op Maximo Secrets specificaties:
- Item Master: https://maximosecrets.com/2026/02/11/item-master/
- Item Statuses: https://maximosecrets.com/2026/02/13/item-statuses-2/
- Item Sets & Organizations: https://maximosecrets.com/2026/02/02/item-sets-and-organizations-and-item-types/
- Commodity Groups: https://maximosecrets.com/2026/02/04/commodity-groups-and-codes/

Auteur: Pedro (met Cursor AI assistentie)
Datum: 17 februari 2026
"""

import logging
from typing import Dict, List, Any, Optional, Tuple

logger = logging.getLogger(__name__)


class ItemMapper:
    """
    Mapt MSG-3 taken naar Maximo Item Master objects.
    
    CRITICAL Maximo Rules (from maximosecrets.com):
    - ITEMNUM max 30 characters, UPPERCASE only
    - ITEMNUM is IMMUTABLE after save (cannot be changed!)
    - NO DELETE action available (use OBSOLETE status instead)
    - Description max 100 characters, must be unique and clear
    - Status hierarchy: PENDING → PLANNING → ACTIVE → PENDOBS → OBSOLETE
    - OBSOLETE is IRREVERSIBLE and requires PENDOBS first
    - Commodity Group/Code HIGHLY RECOMMENDED (max 8 chars, UPPERCASE)
    - MSG-3 items are Non-Stocked (STOCKCATEGORY = NS)
    
    Item Types:
    - ITEM - Standard items (can be stocked)
    - TOOL - Tool items  
    - STDSERVICE - Standard service (no inventory)
    
    MSG-3 Mapping Strategy:
    - Task Code → ITEMNUM (format: MSG3-{task_code})
    - Description → DESCRIPTION (max 100 chars)
    - ATA Chapter → Commodity Group (format: ATA-{chapter})
    - ATA System → Commodity Code (format: {chapter}-{system})
    - Status: PLANNING (initial) → ACTIVE (after approval)
    - Stock Category: NS (Non-Stocked, tasks not physical items)
    """
    
    def __init__(self, item_set_id: str = "MSG3-MAINT", org_id: Optional[str] = None):
        """
        Initialiseer de Item mapper.
        
        Args:
            item_set_id: Item Set ID voor MSG-3 items (default: "MSG3-MAINT")
            org_id: Organization ID (optioneel, moet geconfigureerd worden)
        """
        logger.debug("ItemMapper geïnitialiseerd")
        self.item_set_id = item_set_id
        self.org_id = org_id
        
        # Maximo limits
        self.max_itemnum_length = 30
        self.max_description_length = 100
        self.max_commodity_length = 8
        self.recommended_itemnum_length = 12  # For UI readability
        
        # Item statuses
        self.valid_statuses = ["PENDING", "PLANNING", "ACTIVE", "PENDOBS", "OBSOLETE"]
        self.default_status = "PLANNING"  # Best practice for new items
        
        # Stock categories
        self.stock_categories = ["STK", "NS", "SP"]
        self.default_stock_category = "NS"  # MSG-3 items are Non-Stocked
    
    def map_task_to_item(self, msg3_task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Map MSG-3 taak naar Maximo Item Master record.
        
        Args:
            msg3_task: MSG-3 taak dictionary met fields:
                - task_code: MSG-3 task nummer (required)
                - description: Task beschrijving (required)
                - ata_chapter: ATA chapter nummer (required for commodity)
                - ata_system: ATA system nummer (required for commodity)
                - status: Status override (optioneel)
                
        Returns:
            Maximo Item Master record dictionary
            
        Raises:
            ValueError: Als verplichte velden ontbreken of validatie faalt
            
        Example:
            >>> item_mapper = ItemMapper(item_set_id="MSG3-MAINT", org_id="SCHIPHOL")
            >>> msg3_task = {
            ...     "task_code": "32-11-01-001",
            ...     "description": "Inspection - Landing Gear - Door - Visual Check",
            ...     "ata_chapter": "32",
            ...     "ata_system": "11"
            ... }
            >>> item_record = item_mapper.map_task_to_item(msg3_task)
            >>> print(item_record['ITEMNUM'])
            MSG3-32-11-01-001
            >>> print(item_record['STATUS'])
            PLANNING
            >>> print(item_record['STOCKCATEGORY'])
            NS
        """
        # Valideer verplichte velden
        self._validate_required_fields(msg3_task)
        
        # Generate ITEMNUM
        itemnum = self._generate_itemnum(msg3_task.get("task_code"))
        
        # Valideer ITEMNUM (CRITICAL - immutable after save!)
        self._validate_itemnum(itemnum)
        
        # Format en valideer description
        description = self._format_description(msg3_task.get("description"))
        
        # Map commodity group/code van ATA
        commodity_group = self._map_commodity_group(msg3_task.get("ata_chapter"))
        commodity_code = self._map_commodity_code(
            msg3_task.get("ata_chapter"),
            msg3_task.get("ata_system")
        )
        
        # Valideer commodities (max 8 chars, uppercase)
        self._validate_commodity(commodity_group, "group")
        self._validate_commodity(commodity_code, "code")
        
        # Build Maximo Item Master record
        item_record = {
            # ========== KEY FIELDS (IMMUTABLE) ==========
            "ITEMNUM": itemnum,  # CRITICAL: Cannot be changed after save!
            "ITEMSETID": self.item_set_id,  # Link to Item Set
            
            # ========== REQUIRED FIELDS ==========
            "DESCRIPTION": description,  # Max 100 chars
            "ITEMTYPE": "ITEM",  # MSG-3 tasks are type ITEM
            "STATUS": msg3_task.get("status", self.default_status),  # PLANNING initially
            
            # ========== ITEM CHARACTERISTICS ==========
            "STOCKCATEGORY": self.default_stock_category,  # NS = Non-Stocked
            "ROTATING": False,  # MSG-3 items are not rotating assets
            "LOTTYPE": None,  # No lot tracking
            "CONDITIONENABLED": False,  # No condition tracking
            "ISKIT": False,  # Not a kit
            "CAPITALIZED": False,  # Not capitalized
            
            # ========== COMMODITY FIELDS (REQUIRED for search & reporting) ==========
            "COMMODITY": commodity_group,  # ATA Chapter (e.g., "ATA-32")
            "COMMODITYCODE": commodity_code,  # ATA System (e.g., "32-11")
            
            # ========== FINANCIAL FIELDS ==========
            "TAXEXEMPT": False,  # Not tax exempt by default
            
            # ========== OPERATIONAL FIELDS ==========
            "INSPECTIONREQUIRED": msg3_task.get("inspection_required", False),
            "ADDASSPAREPAT": False,  # Don't auto-add as spare part
            
            # ========== MSG-3 SPECIFIC (custom fields) ==========
            "PLUSCMSG3TASKCODE": msg3_task.get("task_code"),
            "PLUSCMSG3ATA": msg3_task.get("ata_chapter"),
            "PLUSCMSG3SYSTEM": msg3_task.get("ata_system"),
            "PLUSCMSG3TYPE": msg3_task.get("task_type"),
        }
        
        logger.debug(f"Mapped MSG-3 task {msg3_task.get('task_code')} → Item {itemnum}")
        return item_record
    
    def map_task_to_item_org(self, msg3_task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Map MSG-3 taak naar Maximo Item/Organization Details record.
        
        Dit record linkt het item aan een specifieke organization.
        Wordt automatisch aangemaakt door Maximo maar kan custom fields hebben.
        
        Args:
            msg3_task: MSG-3 taak dictionary
            
        Returns:
            Item/Organization Details record
            
        Raises:
            ValueError: Als organization ID niet is geconfigureerd
        """
        if not self.org_id:
            raise ValueError("Organization ID not configured in ItemMapper")
        
        itemnum = self._generate_itemnum(msg3_task.get("task_code"))
        
        item_org_record = {
            # Key fields
            "ITEMNUM": itemnum,
            "ORGID": self.org_id,
            
            # Status (defaults from organization settings)
            "STATUS": msg3_task.get("status", self.default_status),
            
            # Stock category
            "STOCKCATEGORY": self.default_stock_category,  # NS
            
            # Receipt tolerance (not applicable for non-stocked items)
            "RECEIPTOL": 0,
            
            # Tax fields
            "TAXEXEMPT": False,
            "TAXCODE": None,  # Default from organization
            
            # Hazard (for MSDS reference if hazardous material)
            "HAZARD": None,  # Not applicable for MSG-3 tasks
        }
        
        logger.debug(f"Mapped Item/Org record for {itemnum} in org {self.org_id}")
        return item_org_record
    
    def validate_item_for_obsolete(
        self, 
        itemnum: str, 
        level: str = "ITEM"
    ) -> Tuple[bool, List[str]]:
        """
        Valideer of item kan worden ge-OBSOLETE.
        
        Maximo Rules voor OBSOLETE (from maximosecrets.com):
        - Status must be PENDOBS first
        - Cannot have work plan references
        - Cannot have job plan references
        - Cannot have desktop requisition lines (MRLINE)
        - Cannot have purchase requisition lines
        - Cannot have purchase order lines
        - Cannot have item balance (inventory level only)
        - OBSOLETE is IRREVERSIBLE!
        
        Args:
            itemnum: Item number to validate
            level: Level to check ("ITEM", "ITEMORG", or "INVENTORY")
            
        Returns:
            Tuple of (can_obsolete: bool, blocking_reasons: List[str])
            
        Example:
            >>> item_mapper = ItemMapper()
            >>> can_obsolete, reasons = item_mapper.validate_item_for_obsolete("MSG3-32-11-001")
            >>> if not can_obsolete:
            ...     print(f"Cannot OBSOLETE: {', '.join(reasons)}")
        """
        blocking_reasons = []
        
        # NOTE: Actual reference checks require database queries
        # This is a template showing what needs to be checked
        
        logger.info(f"Validating OBSOLETE for {itemnum} at {level} level")
        
        # TODO: Implement actual database checks
        # if has_workplan_references(itemnum, level):
        #     blocking_reasons.append(f"Item exists on work plan at {level} level")
        
        # if has_jobplan_references(itemnum, level):
        #     blocking_reasons.append(f"Item exists on job plan at {level} level")
        
        # if has_mrline_references(itemnum, level):
        #     blocking_reasons.append(f"Item exists on desktop requisition at {level} level")
        
        # if has_pr_references(itemnum, level):
        #     blocking_reasons.append(f"Item exists on purchase requisition at {level} level")
        
        # if has_po_references(itemnum, level):
        #     blocking_reasons.append(f"Item exists on purchase order at {level} level")
        
        # if level == "INVENTORY" and has_balance(itemnum):
        #     blocking_reasons.append("Item has remaining balance")
        
        can_obsolete = len(blocking_reasons) == 0
        
        if can_obsolete:
            logger.info(f"Item {itemnum} can be set to OBSOLETE")
        else:
            logger.warning(f"Item {itemnum} cannot be OBSOLETE: {blocking_reasons}")
        
        return (can_obsolete, blocking_reasons)
    
    # ========================================================================
    # PRIVATE HELPER METHODS
    # ========================================================================
    
    def _validate_required_fields(self, msg3_task: Dict[str, Any]) -> None:
        """Valideer verplichte MSG-3 velden."""
        required_fields = {
            "task_code": "Task Code",
            "description": "Description",
            "ata_chapter": "ATA Chapter"
        }
        
        missing = [name for field, name in required_fields.items() if not msg3_task.get(field)]
        
        if missing:
            raise ValueError(f"Missing required fields: {', '.join(missing)}")
    
    def _generate_itemnum(self, task_code: str) -> str:
        """
        Genereer Maximo ITEMNUM van MSG-3 task code.
        
        Format: MSG3-{task_code}
        Example: MSG3-32-11-01-001
        """
        if not task_code:
            raise ValueError("Task code is required for ITEMNUM generation")
        
        itemnum = f"MSG3-{task_code}".upper()
        return itemnum
    
    def _validate_itemnum(self, itemnum: str) -> None:
        """
        Valideer ITEMNUM volgens Maximo regels.
        
        Rules:
        - Max 30 characters (CRITICAL)
        - Uppercase only (convention)
        - Recommend max 12 for UI readability (warning only)
        - No spaces (best practice)
        
        Raises:
            ValueError: Als ITEMNUM invalid is
        """
        if not itemnum:
            raise ValueError("ITEMNUM is required")
        
        if len(itemnum) > self.max_itemnum_length:
            raise ValueError(
                f"ITEMNUM too long: {len(itemnum)} > {self.max_itemnum_length} chars"
            )
        
        if itemnum != itemnum.upper():
            raise ValueError(f"ITEMNUM must be uppercase: {itemnum}")
        
        if " " in itemnum:
            raise ValueError(f"ITEMNUM cannot contain spaces: {itemnum}")
        
        # Warning voor UI readability (niet een error)
        if len(itemnum) > self.recommended_itemnum_length:
            logger.warning(
                f"ITEMNUM {itemnum} exceeds recommended length "
                f"({len(itemnum)} > {self.recommended_itemnum_length}), "
                "may require horizontal scrolling in UI"
            )
    
    def _format_description(self, description: str) -> str:
        """
        Format en valideer description voor Maximo.
        
        Maximo Rules:
        - Max 100 characters (CRITICAL)
        - Should be unique and clear (10,000+ items in system)
        - Recommend min 10 chars for clarity
        """
        if not description:
            raise ValueError("Description is required")
        
        # Trim whitespace
        description = description.strip()
        
        # Check max length (CRITICAL)
        if len(description) > self.max_description_length:
            logger.error(
                f"Description too long ({len(description)} chars), "
                f"truncating to {self.max_description_length}"
            )
            description = description[:97] + "..."
        
        # Warn if too short
        if len(description) < 10:
            logger.warning(
                f"Description very short ({len(description)} chars): '{description}' "
                "- may be hard to distinguish in 10,000+ items"
            )
        
        return description
    
    def _map_commodity_group(self, ata_chapter: str) -> str:
        """
        Map ATA Chapter naar Maximo Commodity Group.
        
        Format: ATA-{chapter}
        Example: ATA-32 (Landing Gear)
        Max: 8 characters (Maximo UPPER 8)
        """
        if not ata_chapter:
            logger.warning("No ATA chapter provided for commodity group")
            return ""
        
        commodity_group = f"ATA-{ata_chapter}".upper()
        return commodity_group
    
    def _map_commodity_code(self, ata_chapter: str, ata_system: str) -> str:
        """
        Map ATA Chapter + System naar Maximo Commodity Code.
        
        Format: {chapter}-{system}
        Example: 32-11 (Landing Gear Doors)
        Max: 8 characters (Maximo UPPER 8)
        """
        if not ata_chapter or not ata_system:
            logger.warning("Incomplete ATA codes for commodity code")
            return ""
        
        commodity_code = f"{ata_chapter}-{ata_system}".upper()
        return commodity_code
    
    def _validate_commodity(self, commodity: str, commodity_type: str) -> None:
        """
        Valideer commodity group/code volgens Maximo regels.
        
        Rules:
        - Max 8 characters (CRITICAL)
        - Uppercase only (convention)
        - Required for search & reporting (highly recommended)
        
        Args:
            commodity: Commodity group or code
            commodity_type: "group" or "code" (for error messages)
            
        Raises:
            ValueError: Als commodity invalid is
        """
        if not commodity:
            logger.warning(f"No commodity {commodity_type} - HIGHLY RECOMMENDED for search & reporting")
            return
        
        if len(commodity) > self.max_commodity_length:
            raise ValueError(
                f"Commodity {commodity_type} too long: "
                f"'{commodity}' ({len(commodity)} > {self.max_commodity_length} chars)"
            )
        
        if commodity != commodity.upper():
            raise ValueError(
                f"Commodity {commodity_type} must be uppercase: {commodity}"
            )


if __name__ == "__main__":
    # Test de mapper
    logging.basicConfig(level=logging.DEBUG)
    
    item_mapper = ItemMapper(item_set_id="MSG3-MAINT", org_id="SCHIPHOL")
    
    # Test task
    test_task = {
        "task_code": "32-11-01-001",
        "description": "Inspection - Landing Gear - Door - Visual Check",
        "ata_chapter": "32",
        "ata_system": "11",
        "task_type": "Inspection"
    }
    
    # Map to item
    item_record = item_mapper.map_task_to_item(test_task)
    print("Item Master Record:")
    for key, value in item_record.items():
        print(f"  {key}: {value}")
    
    # Map to item/org
    item_org_record = item_mapper.map_task_to_item_org(test_task)
    print("\nItem/Organization Record:")
    for key, value in item_org_record.items():
        print(f"  {key}: {value}")
    
    # Test OBSOLETE validation
    can_obsolete, reasons = item_mapper.validate_item_for_obsolete("MSG3-32-11-01-001")
    print(f"\nCan OBSOLETE: {can_obsolete}")
    if not can_obsolete:
        print(f"Reasons: {reasons}")
