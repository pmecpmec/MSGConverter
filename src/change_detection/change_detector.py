"""
Change Detector - Hoofd change detection logic

Detecteert wijzigingen tussen MSG-3 versies en genereert changelog.

Auteur: Pedro (met Cursor AI assistentie)
Datum: 4 februari 2026
"""

import logging
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from enum import Enum

logger = logging.getLogger(__name__)


class ChangeType(Enum):
    """Types van wijzigingen."""
    ADDED = "added"
    MODIFIED = "modified"
    DELETED = "deleted"


@dataclass
class Change:
    """
    Representeert een wijziging in MSG-3 data.
    
    Attributes:
        change_type: Type wijziging (added/modified/deleted)
        task_code: Taak code die gewijzigd is
        field: Veld dat gewijzigd is (None voor hele taak)
        old_value: Oude waarde (None voor added)
        new_value: Nieuwe waarde (None voor deleted)
    """
    change_type: ChangeType
    task_code: str
    field: Optional[str] = None
    old_value: Any = None
    new_value: Any = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Converteer naar dictionary."""
        return {
            "change_type": self.change_type.value,
            "task_code": self.task_code,
            "field": self.field,
            "old_value": str(self.old_value) if self.old_value else None,
            "new_value": str(self.new_value) if self.new_value else None
        }


@dataclass
class ChangeReport:
    """
    Rapport van alle wijzigingen.
    
    Attributes:
        changes: Lijst van Change objecten
        added_count: Aantal toegevoegde taken
        modified_count: Aantal gewijzigde taken
        deleted_count: Aantal verwijderde taken
    """
    changes: List[Change]
    added_count: int
    modified_count: int
    deleted_count: int
    
    def get_summary(self) -> str:
        """Genereer tekstuele samenvatting."""
        return (
            f"Change Detection Rapport:\n"
            f"  ✚ {self.added_count} toegevoegd\n"
            f"  ✎ {self.modified_count} gewijzigd\n"
            f"  ✖ {self.deleted_count} verwijderd\n"
            f"  = {len(self.changes)} totaal aantal wijzigingen"
        )


class ChangeDetector:
    """
    Detecteert wijzigingen tussen twee MSG-3 versies.
    
    Vergelijkt twee versies van MSG-3 data en genereert een
    gedetailleerd change report met field-level differences.
    
    Example:
        >>> detector = ChangeDetector()
        >>> report = detector.detect_changes(old_data, new_data)
        >>> print(report.get_summary())
        >>> for change in report.changes:
        ...     print(f"{change.change_type}: {change.task_code}")
    """
    
    def __init__(self):
        """Initialiseer de change detector."""
        logger.info("ChangeDetector geïnitialiseerd")
        self.diff_engine = None  # TODO: Initialiseer DiffEngine
    
    def detect_changes(
        self, 
        old_data: Dict[str, Any], 
        new_data: Dict[str, Any]
    ) -> ChangeReport:
        """
        Detecteer wijzigingen tussen twee MSG-3 versies.
        
        Args:
            old_data: Vorige versie MSG-3 data
            new_data: Nieuwe versie MSG-3 data
            
        Returns:
            ChangeReport met alle gedetecteerde wijzigingen
        """
        logger.info("Change detection starten...")
        changes: List[Change] = []
        
        old_tasks = {task['task_code']: task for task in old_data.get('tasks', [])}
        new_tasks = {task['task_code']: task for task in new_data.get('tasks', [])}
        
        # Detecteer toegevoegde taken
        added = self._detect_added(old_tasks, new_tasks)
        changes.extend(added)
        
        # Detecteer verwijderde taken
        deleted = self._detect_deleted(old_tasks, new_tasks)
        changes.extend(deleted)
        
        # Detecteer gewijzigde taken
        modified = self._detect_modified(old_tasks, new_tasks)
        changes.extend(modified)
        
        report = ChangeReport(
            changes=changes,
            added_count=len(added),
            modified_count=len(modified),
            deleted_count=len(deleted)
        )
        
        logger.info(report.get_summary())
        return report
    
    def _detect_added(
        self, 
        old_tasks: Dict[str, Any], 
        new_tasks: Dict[str, Any]
    ) -> List[Change]:
        """Detecteer toegevoegde taken."""
        added = []
        for task_code in new_tasks:
            if task_code not in old_tasks:
                added.append(Change(
                    change_type=ChangeType.ADDED,
                    task_code=task_code,
                    new_value=new_tasks[task_code]
                ))
        logger.debug(f"Toegevoegde taken: {len(added)}")
        return added
    
    def _detect_deleted(
        self, 
        old_tasks: Dict[str, Any], 
        new_tasks: Dict[str, Any]
    ) -> List[Change]:
        """Detecteer verwijderde taken."""
        deleted = []
        for task_code in old_tasks:
            if task_code not in new_tasks:
                deleted.append(Change(
                    change_type=ChangeType.DELETED,
                    task_code=task_code,
                    old_value=old_tasks[task_code]
                ))
        logger.debug(f"Verwijderde taken: {len(deleted)}")
        return deleted
    
    def _detect_modified(
        self, 
        old_tasks: Dict[str, Any], 
        new_tasks: Dict[str, Any]
    ) -> List[Change]:
        """Detecteer gewijzigde taken (field-level)."""
        modified = []
        
        for task_code in old_tasks:
            if task_code in new_tasks:
                old_task = old_tasks[task_code]
                new_task = new_tasks[task_code]
                
                # Vergelijk elk veld
                for field in old_task:
                    if field in new_task and old_task[field] != new_task[field]:
                        modified.append(Change(
                            change_type=ChangeType.MODIFIED,
                            task_code=task_code,
                            field=field,
                            old_value=old_task[field],
                            new_value=new_task[field]
                        ))
        
        logger.debug(f"Gewijzigde velden: {len(modified)}")
        return modified


if __name__ == "__main__":
    # Test de change detector
    logging.basicConfig(level=logging.DEBUG)
    detector = ChangeDetector()
    print("ChangeDetector ready for testing")
