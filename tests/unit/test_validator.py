"""
Unit tests voor Validator module

Auteur: Pedro (met Cursor AI assistentie)
Datum: 4 februari 2026
"""

import pytest
from src.validator.msg3_validator import MSG3Validator, ValidationResult, ValidationError


class TestMSG3Validator:
    """Test cases voor MSG3Validator."""
    
    def setup_method(self):
        """Setup voor elke test."""
        self.validator = MSG3Validator()
    
    def test_validator_initialization(self):
        """Test of validator correct geïnitialiseerd wordt."""
        assert self.validator is not None
    
    def test_validation_result_creation(self):
        """Test ValidationResult dataclass."""
        result = ValidationResult(
            is_valid=True,
            errors=[],
            warnings=[],
            info_messages=[]
        )
        
        assert result.is_valid is True
        assert len(result.errors) == 0
    
    def test_validation_error_creation(self):
        """Test ValidationError dataclass."""
        error = ValidationError(
            field="task_code",
            error_type="required",
            message="Task code is verplicht",
            severity="error"
        )
        
        assert error.field == "task_code"
        assert error.severity == "error"
    
    # TODO: Meer tests toevoegen na implementatie
    # - test_validate_valid_data
    # - test_validate_missing_required_field
    # - test_validate_invalid_datatype
    # - test_business_rules_validation


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
