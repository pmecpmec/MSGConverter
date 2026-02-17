"""
JobPlan Mapper - MSG-3 naar Maximo JobPlan mapping

Mapt MSG-3 taken naar Maximo JobPlan records.

JobPlans bevatten gedetailleerde werkinstructies, materials, tools, en labor.

Gebaseerd op Maximo Secrets specificaties:
- Item Master: https://maximosecrets.com/2026/02/11/item-master/
  (JobPlans kunnen items als materials refereren)

Auteur: Pedro (met Cursor AI assistentie)
Datum: 4 februari 2026
Laatste Update: 17 februari 2026 (Maximo specificaties toegevoegd)
"""

import logging
from typing import Dict, List, Any, Optional

logger = logging.getLogger(__name__)


class JobPlanMapper:
    """
    Mapt MSG-3 taken naar Maximo JobPlan objects.
    
    JobPlan records in Maximo bevatten de gedetailleerde
    werkinstructies, benodigde tools, skills en materialen.
    
    CRITICAL Maximo Rules:
    - JPNUM (Job Plan Number) is key field
    - Description max 100 characters
    - Status: DRAFT → ACTIVE → OBSOLETE
    - Items referenced in materials MUST exist in Item Master
    - Labor must reference valid craft codes
    - Tools must exist in Tools application
    
    MSG-3 Mapping:
    - Task Code → JPNUM
    - Description → DESCRIPTION
    - Man Hours → Duration estimate
    - Work Instructions → Task list
    - Required Parts → Materials list
    - Required Tools → Tools list
    """
    
    def __init__(self):
        """Initialiseer de JobPlan mapper."""
        logger.debug("JobPlanMapper geïnitialiseerd")
        
        # Status mapping
        self.status_mapping = {
            "draft": "DRAFT",
            "active": "ACTIVE",
            "obsolete": "OBSOLETE"
        }
        
        # Default values
        self.default_status = "ACTIVE"
        self.default_work_type = "PM"
    
    def map_task(self, msg3_task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Map een MSG-3 taak naar een Maximo JobPlan object.
        
        Args:
            msg3_task: MSG-3 taak dictionary met:
                - task_code: MSG-3 task nummer
                - description: Task beschrijving
                - man_hours: Geschatte uren
                - work_instructions: Werkinstructies (optioneel)
                - required_parts: Benodigde onderdelen (optioneel)
                - required_tools: Benodigde tools (optioneel)
                
        Returns:
            Maximo JobPlan object dictionary
            
        Example:
            >>> jp_mapper = JobPlanMapper()
            >>> msg3_task = {
            ...     "task_code": "32-11-01-001",
            ...     "description": "Visual inspection landing gear door",
            ...     "man_hours": 2.5,
            ...     "work_instructions": "1. Visual check\\n2. Report findings"
            ... }
            >>> jobplan = jp_mapper.map_task(msg3_task)
            >>> print(jobplan['JPNUM'])
            MSG3-32-11-01-001
        """
        # Generate JPNUM (same format as ITEMNUM/PMNUM)
        jpnum = self._generate_jpnum(msg3_task.get("task_code"))
        
        # Validate JPNUM length
        if len(jpnum) > 30:
            raise ValueError(f"JPNUM too long: {jpnum}")
        
        # Format description
        description = self._format_description(msg3_task.get("description"))
        
        # Build JobPlan record
        jobplan_record = {
            # Key fields
            "JPNUM": jpnum,
            "DESCRIPTION": description,
            
            # Status
            "STATUS": msg3_task.get("status", self.default_status),
            
            # Work Type
            "WORKTYPE": self.default_work_type,
            
            # Duration (man hours)
            "PLUSCJPREVDUR": msg3_task.get("man_hours", 0),
            
            # Work instructions (stored as tasks in JPTASK table)
            # NOTE: This will be handled separately by task lines
            
            # MSG-3 Specific custom fields
            "PLUSCMSG3TASKCODE": msg3_task.get("task_code"),
            "PLUSCMSG3ATA": msg3_task.get("ata_chapter"),
        }
        
        # TODO: Add materials (JOBMATERIAL table)
        # TODO: Add tools (JOBTOOL table)
        # TODO: Add labor (JOBLABOR table)
        # TODO: Add task instructions (JPTASK table)
        
        logger.debug(f"Mapped MSG-3 task {msg3_task.get('task_code')} → JobPlan {jpnum}")
        return jobplan_record
    
    def _generate_jpnum(self, task_code: str) -> str:
        """
        Genereer JPNUM van MSG-3 task code.
        
        Format: MSG3-{task_code}
        Same as ITEMNUM/PMNUM voor consistency
        """
        if not task_code:
            raise ValueError("Task code required for JPNUM")
        
        return f"MSG3-{task_code}".upper()
    
    def _format_description(self, description: str) -> str:
        """
        Format description volgens Maximo regels.
        
        Max 100 characters (same as Item/PM)
        """
        if not description:
            raise ValueError("Description is required")
        
        description = description.strip()
        
        if len(description) > 100:
            logger.warning(f"Description too long, truncating to 100 chars")
            description = description[:97] + "..."
        
        return description
    
    def map_tasks(self, msg3_tasks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Map meerdere MSG-3 taken naar JobPlan objects."""
        jobplan_records = []
        for task in msg3_tasks:
            try:
                jobplan_record = self.map_task(task)
                jobplan_records.append(jobplan_record)
            except Exception as e:
                logger.error(f"Fout bij mappen taak {task.get('task_code')}: {e}")
        
        return jobplan_records
