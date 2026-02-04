"""
JobPlan Mapper - MSG-3 naar Maximo JobPlan mapping

Mapt MSG-3 taken naar Maximo JobPlan records.

Auteur: Pedro (met Cursor AI assistentie)
Datum: 4 februari 2026
"""

import logging
from typing import Dict, List, Any

logger = logging.getLogger(__name__)


class JobPlanMapper:
    """
    Mapt MSG-3 taken naar Maximo JobPlan objects.
    
    JobPlan records in Maximo bevatten de gedetailleerde
    werkinstructies, benodigde tools, skills en materialen.
    """
    
    def __init__(self):
        """Initialiseer de JobPlan mapper."""
        logger.debug("JobPlanMapper geïnitialiseerd")
    
    def map_task(self, msg3_task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Map een MSG-3 taak naar een Maximo JobPlan object.
        
        Args:
            msg3_task: MSG-3 taak dictionary
            
        Returns:
            Maximo JobPlan object dictionary
        """
        jobplan_record = {
            "JPNUM": msg3_task.get("task_code"),
            "DESCRIPTION": msg3_task.get("description"),
            "PLUSCJPREVDUR": msg3_task.get("man_hours", 0),
            # Meer mappings...
        }
        
        return jobplan_record
    
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
