"""
Unit tests voor Parser module

Auteur: Pedro (met Cursor AI assistentie)
Datum: 4 februari 2026
"""

import pytest
from pathlib import Path
from src.parser.msg3_parser import MSG3Parser, MSG3Task


class TestMSG3Parser:
    """Test cases voor MSG3Parser."""
    
    def setup_method(self):
        """Setup voor elke test."""
        self.parser = MSG3Parser()
    
    def test_parser_initialization(self):
        """Test of parser correct geïnitialiseerd wordt."""
        assert self.parser is not None
        assert len(self.parser.supported_versions) == 2
    
    def test_msg3_task_creation(self):
        """Test MSG3Task dataclass."""
        task = MSG3Task(
            task_code="32-11-01-001",
            description="Visual inspection",
            task_type="INS",
            interval=500,
            interval_unit="FH"
        )
        
        assert task.task_code == "32-11-01-001"
        assert task.description == "Visual inspection"
        assert task.interval == 500
    
    def test_msg3_task_to_dict(self):
        """Test MSG3Task to_dict conversie."""
        task = MSG3Task(
            task_code="32-11-01-001",
            description="Visual inspection",
            task_type="INS",
            interval=500,
            interval_unit="FH"
        )
        
        task_dict = task.to_dict()
        assert isinstance(task_dict, dict)
        assert task_dict["task_code"] == "32-11-01-001"
    
    # TODO: Meer tests toevoegen na implementatie
    # - test_parse_original_format
    # - test_parse_redesign_format
    # - test_invalid_file
    # - test_empty_file
    # - test_detect_version


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
