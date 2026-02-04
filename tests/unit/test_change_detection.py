"""
Unit tests voor Change Detection module

Auteur: Pedro (met Cursor AI assistentie)
Datum: 4 februari 2026
"""

import pytest
from src.change_detection.change_detector import ChangeDetector, Change, ChangeType, ChangeReport


class TestChangeDetector:
    """Test cases voor ChangeDetector."""
    
    def setup_method(self):
        """Setup voor elke test."""
        self.detector = ChangeDetector()
    
    def test_detector_initialization(self):
        """Test of detector correct geïnitialiseerd wordt."""
        assert self.detector is not None
    
    def test_change_creation(self):
        """Test Change dataclass."""
        change = Change(
            change_type=ChangeType.ADDED,
            task_code="32-11-01-001",
            new_value={"description": "New task"}
        )
        
        assert change.change_type == ChangeType.ADDED
        assert change.task_code == "32-11-01-001"
    
    def test_change_report_summary(self):
        """Test ChangeReport summary generatie."""
        report = ChangeReport(
            changes=[],
            added_count=5,
            modified_count=3,
            deleted_count=2
        )
        
        summary = report.get_summary()
        assert "5 toegevoegd" in summary
        assert "3 gewijzigd" in summary
        assert "2 verwijderd" in summary
    
    # TODO: Meer tests toevoegen na implementatie
    # - test_detect_added_tasks
    # - test_detect_deleted_tasks
    # - test_detect_modified_tasks
    # - test_field_level_changes


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
