"""
PM Mapper - MSG-3 naar Maximo PM object mapping

Mapt MSG-3 taken naar Maximo PM (Preventive Maintenance) records.

Auteur: Pedro (met Cursor AI assistentie)
Datum: 4 februari 2026
"""

import logging
from typing import Dict, List, Any

logger = logging.getLogger(__name__)


class PMMapper:
    """
    Mapt MSG-3 taken naar Maximo PM objects.
    
    PM (Preventive Maintenance) records in Maximo representeren
    de onderhoudstaken met intervals en routing.
    
    Mapping:
    - MSG-3 Task Code → PM.PMNUM
    - MSG-3 Description → PM.DESCRIPTION
    - MSG-3 Interval → PM.FREQUENCY + PM.FREQUNIT
    - MSG-3 Zone → PM.LOCATION
    - MSG-3 ATA Chapter → PM.WORKTYPE (of custom field)
    """
    
    def __init__(self):
        """Initialiseer de PM mapper."""
        logger.debug("PMMapper geïnitialiseerd")
        self._load_mapping_config()
    
    def _load_mapping_config(self) -> None:
        """Laad mapping configuratie."""
        # TODO: Laad field mapping config van file
        pass
    
    def map_task(self, msg3_task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Map een MSG-3 taak naar een Maximo PM object.
        
        Args:
            msg3_task: MSG-3 taak dictionary
            
        Returns:
            Maximo PM object dictionary
            
        Example:
            >>> pm_mapper = PMMapper()
            >>> msg3_task = {
            ...     "task_code": "32-11-01-001",
            ...     "description": "Visual inspection landing gear",
            ...     "interval": 500,
            ...     "interval_unit": "FH"
            ... }
            >>> pm_record = pm_mapper.map_task(msg3_task)
            >>> print(pm_record['PMNUM'])
            32-11-01-001
        """
        pm_record = {
            "PMNUM": msg3_task.get("task_code"),
            "DESCRIPTION": msg3_task.get("description"),
            "FREQUENCY": msg3_task.get("interval"),
            "FREQUNIT": self._map_interval_unit(msg3_task.get("interval_unit")),
            "LOCATION": msg3_task.get("zone"),
            # Meer mappings...
        }
        
        return pm_record
    
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
