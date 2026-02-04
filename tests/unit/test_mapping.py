"""
Unit tests voor Mapping module

Auteur: Pedro (met Cursor AI assistentie)
Datum: 4 februari 2026
"""

import pytest
from src.mapping.pm_mapper import PMMapper
from src.mapping.jobplan_mapper import JobPlanMapper


class TestPMMapper:
    """Test cases voor PMMapper."""
    
    def setup_method(self):
        """Setup voor elke test."""
        self.mapper = PMMapper()
    
    def test_mapper_initialization(self):
        """Test of mapper correct geïnitialiseerd wordt."""
        assert self.mapper is not None
    
    def test_interval_unit_mapping(self):
        """Test interval unit conversie."""
        assert self.mapper._map_interval_unit("FH") == "HOURS"
        assert self.mapper._map_interval_unit("FC") == "CYCLES"
        assert self.mapper._map_interval_unit("MO") == "MONTHS"
        assert self.mapper._map_interval_unit("WK") == "WEEKS"
    
    # TODO: Meer tests toevoegen na implementatie
    # - test_map_task_basic
    # - test_map_task_with_all_fields
    # - test_map_multiple_tasks


class TestJobPlanMapper:
    """Test cases voor JobPlanMapper."""
    
    def setup_method(self):
        """Setup voor elke test."""
        self.mapper = JobPlanMapper()
    
    def test_mapper_initialization(self):
        """Test of mapper correct geïnitialiseerd wordt."""
        assert self.mapper is not None
    
    # TODO: Meer tests toevoegen na implementatie


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
