"""
Unit tests voor Validator module

Auteur: Pedro (met Cursor AI assistentie)
Datum: 5 februari 2026
"""

import pytest
from src.validator.msg3_validator import MSG3Validator, ValidationResult, ValidationError
from src.validator.business_rules import (
    BusinessRulesValidator,
    BusinessRule,
    RuleViolation,
    RuleCategory,
    RuleSeverity
)


VALID_TASK = {
    "task_code": "32-11-01-001",
    "description": "Visual inspection landing gear main fitting",
    "task_type": "INS",
    "interval": 500,
    "interval_unit": "FH",
    "zone": "Z100",
    "ata_chapter": "32",
    "ata_system": "11",
    "man_hours": 1.5,
    "skills": ["MECH"],
}

VALID_DATA = {
    "metadata": {"version": "redesign", "total_tasks": 1},
    "tasks": [VALID_TASK],
}


class TestMSG3Validator:
    """Test cases voor MSG3Validator."""

    def setup_method(self):
        self.validator = MSG3Validator()

    def test_validator_initialization(self):
        assert self.validator is not None

    def test_validation_result_creation(self):
        result = ValidationResult(
            is_valid=True, errors=[], warnings=[], info_messages=[]
        )
        assert result.is_valid is True
        assert result.total_issues == 0

    def test_validation_error_creation(self):
        error = ValidationError(
            field="task_code",
            error_type="required",
            message="Task code is verplicht",
            severity="error",
        )
        assert error.field == "task_code"
        assert error.severity == "error"

    def test_validate_valid_data(self):
        result = self.validator.validate(VALID_DATA)
        assert result.is_valid
        assert len(result.errors) == 0

    def test_validate_missing_tasks_key(self):
        result = self.validator.validate({"metadata": {}})
        assert not result.is_valid
        assert any(e.field == "tasks" for e in result.errors)

    def test_validate_missing_metadata(self):
        result = self.validator.validate({"tasks": [VALID_TASK]})
        assert not result.is_valid
        assert any(e.field == "metadata" for e in result.errors)

    def test_validate_tasks_not_list(self):
        result = self.validator.validate({"metadata": {}, "tasks": "bad"})
        assert not result.is_valid

    def test_validate_not_dict(self):
        result = self.validator.validate("not a dict")
        assert not result.is_valid

    def test_validate_duplicate_task_codes(self):
        data = {
            "metadata": {},
            "tasks": [VALID_TASK, VALID_TASK],
        }
        result = self.validator.validate(data)
        assert not result.is_valid
        assert any("Dubbele" in e.message for e in result.errors)

    def test_validate_missing_required_field(self):
        task = VALID_TASK.copy()
        task["description"] = None
        data = {"metadata": {}, "tasks": [task]}
        result = self.validator.validate(data)
        assert not result.is_valid

    def test_validate_invalid_interval(self):
        task = VALID_TASK.copy()
        task["interval"] = -10
        data = {"metadata": {}, "tasks": [task]}
        result = self.validator.validate(data)
        assert not result.is_valid

    def test_validate_invalid_interval_unit(self):
        task = VALID_TASK.copy()
        task["interval_unit"] = "INVALID"
        data = {"metadata": {}, "tasks": [task]}
        result = self.validator.validate(data)
        assert not result.is_valid

    def test_validate_maximo_itemnum_too_long(self):
        task = VALID_TASK.copy()
        task["task_code"] = "A" * 30
        data = {"metadata": {}, "tasks": [task]}
        result = self.validator.validate(data)
        assert any(e.error_type == "maximo_limit" for e in result.errors)

    def test_validate_description_too_long_warning(self):
        task = VALID_TASK.copy()
        task["description"] = "X" * 150
        data = {"metadata": {}, "tasks": [task]}
        result = self.validator.validate(data)
        assert any(w.error_type == "maximo_limit" for w in result.warnings)

    def test_validate_short_description_warning(self):
        task = VALID_TASK.copy()
        task["description"] = "Short"
        data = {"metadata": {}, "tasks": [task]}
        result = self.validator.validate(data)
        assert any(w.error_type == "quality" for w in result.warnings)

    def test_validate_missing_ata_chapter_warning(self):
        task = VALID_TASK.copy()
        task["ata_chapter"] = None
        data = {"metadata": {}, "tasks": [task]}
        result = self.validator.validate(data)
        assert any(w.field == "ata_chapter" for w in result.warnings)

    def test_validate_high_fh_interval_warning(self):
        task = VALID_TASK.copy()
        task["interval"] = 60000
        data = {"metadata": {}, "tasks": [task]}
        result = self.validator.validate(data)
        assert any("ongebruikelijk" in w.message for w in result.warnings)

    def test_validate_high_mo_interval_warning(self):
        task = VALID_TASK.copy()
        task["interval"] = 150
        task["interval_unit"] = "MO"
        data = {"metadata": {}, "tasks": [task]}
        result = self.validator.validate(data)
        assert any("ongebruikelijk" in w.message for w in result.warnings)

    def test_validate_negative_man_hours_warning(self):
        task = VALID_TASK.copy()
        task["man_hours"] = -5
        data = {"metadata": {}, "tasks": [task]}
        result = self.validator.validate(data)
        assert any(w.field == "man_hours" for w in result.warnings)

    def test_error_summary_valid(self):
        result = ValidationResult(True, [], [], [])
        assert "geslaagd" in result.get_error_summary()

    def test_error_summary_with_errors(self):
        err = ValidationError("test", "required", "test msg", task_code="TC-001")
        result = ValidationResult(False, [err], [], [])
        summary = result.get_error_summary()
        assert "ERROR" in summary
        assert "TC-001" in summary

    def test_error_summary_with_warnings(self):
        warn = ValidationError("test", "quality", "warning msg", severity="warning")
        result = ValidationResult(True, [], [warn], [])
        summary = result.get_error_summary()
        assert "WARN" in summary


class TestBusinessRulesValidator:
    """Test cases voor BusinessRulesValidator."""
    
    def setup_method(self):
        """Setup voor elke test."""
        self.validator = BusinessRulesValidator()
    
    def test_validator_initialization(self):
        """Test of business rules validator correct geïnitialiseerd wordt."""
        assert self.validator is not None
        assert len(self.validator.rules) > 0
    
    def test_all_90_rules_loaded(self):
        """Test of alle 90 business rules geladen zijn (8 categorieën + 10 Maximo Item rules)."""
        assert len(self.validator.rules) == 90, f"Expected 90 rules, but got {len(self.validator.rules)}"
    
    def test_rules_by_category(self):
        """Test het verwachte aantal rules per categorie."""
        expected = {
            RuleCategory.LOGISTICS: 20,  # 10 operationeel + 10 Maximo Item rules (LOG-4.0.*)
        }
        for category in RuleCategory:
            rules = self.validator.get_rules_by_category(category)
            expected_count = expected.get(category, 10)
            assert len(rules) == expected_count, (
                f"Category {category.value} should have {expected_count} rules, but has {len(rules)}"
            )
    
    def test_security_rules_loaded(self):
        """Test of Security & Access Control rules correct geladen zijn."""
        rules = self.validator.get_rules_by_category(RuleCategory.SECURITY)
        assert len(rules) == 10
        
        # Check eerste rule
        sec_1_1 = self.validator.get_rule("SEC-1.1")
        assert sec_1_1 is not None
        assert sec_1_1.title == "Geldige Schiphol-pas vereist"
        assert sec_1_1.severity == RuleSeverity.CRITICAL
    
    def test_operations_rules_loaded(self):
        """Test of Operations & Maintenance rules correct geladen zijn."""
        rules = self.validator.get_rules_by_category(RuleCategory.OPERATIONS)
        assert len(rules) == 10
        
        ops_2_1 = self.validator.get_rule("OPS-2.1")
        assert ops_2_1 is not None
        assert "SLA" in ops_2_1.description
    
    def test_quality_rules_loaded(self):
        """Test of Quality & Compliance rules correct geladen zijn."""
        rules = self.validator.get_rules_by_category(RuleCategory.QUALITY)
        assert len(rules) == 10
        
        qua_3_1 = self.validator.get_rule("QUA-3.1")
        assert qua_3_1 is not None
        assert "ISO 9001" in qua_3_1.description
    
    def test_logistics_rules_loaded(self):
        """Test of Logistics & Inventory rules correct geladen zijn."""
        rules = self.validator.get_rules_by_category(RuleCategory.LOGISTICS)
        assert len(rules) == 20
        
        log_4_1 = self.validator.get_rule("LOG-4.1")
        assert log_4_1 is not None
        assert "voorraad" in log_4_1.description.lower()
    
    def test_planning_rules_loaded(self):
        """Test of Planning & Workflow rules correct geladen zijn."""
        rules = self.validator.get_rules_by_category(RuleCategory.PLANNING)
        assert len(rules) == 10
        
        pln_5_1 = self.validator.get_rule("PLN-5.1")
        assert pln_5_1 is not None
        assert "prioriteit" in pln_5_1.description.lower()
    
    def test_it_rules_loaded(self):
        """Test of IT & System Usage rules correct geladen zijn."""
        rules = self.validator.get_rules_by_category(RuleCategory.IT_SYSTEMS)
        assert len(rules) == 10
        
        it_6_1 = self.validator.get_rule("IT-6.1")
        assert it_6_1 is not None
        assert "Maximo" in it_6_1.description
    
    def test_hr_rules_loaded(self):
        """Test of HR & Workforce rules correct geladen zijn."""
        rules = self.validator.get_rules_by_category(RuleCategory.HR)
        assert len(rules) == 10
        
        hr_7_1 = self.validator.get_rule("HR-7.1")
        assert hr_7_1 is not None
        assert "training" in hr_7_1.description.lower()
    
    def test_communication_rules_loaded(self):
        """Test of Communication & Reporting rules correct geladen zijn."""
        rules = self.validator.get_rules_by_category(RuleCategory.COMMUNICATION)
        assert len(rules) == 10
        
        com_8_1 = self.validator.get_rule("COM-8.1")
        assert com_8_1 is not None
        assert "storingen" in com_8_1.description.lower()
    
    def test_get_rules_by_severity(self):
        """Test filtering van rules op severity."""
        critical_rules = self.validator.get_rules_by_severity(RuleSeverity.CRITICAL)
        error_rules = self.validator.get_rules_by_severity(RuleSeverity.ERROR)
        warning_rules = self.validator.get_rules_by_severity(RuleSeverity.WARNING)
        info_rules = self.validator.get_rules_by_severity(RuleSeverity.INFO)
        
        # Check dat we rules hebben in verschillende severities
        assert len(critical_rules) > 0
        assert len(error_rules) > 0
        assert len(warning_rules) > 0
        
        # Check totaal
        total = len(critical_rules) + len(error_rules) + len(warning_rules) + len(info_rules)
        assert total == 90
    
    def test_critical_rules_identification(self):
        """Test of critical rules correct geïdentificeerd zijn."""
        critical_rules = self.validator.get_rules_by_severity(RuleSeverity.CRITICAL)
        
        # Er moeten meerdere critical rules zijn
        assert len(critical_rules) >= 5
        
        # Check enkele bekende critical rules
        critical_ids = list(critical_rules.keys())
        assert "SEC-1.1" in critical_ids  # Schiphol-pas
        assert "SEC-1.8" in critical_ids  # PBM
        assert "OPS-2.4" in critical_ids  # Gecertificeerde elektriciens
    
    def test_rule_summary_generation(self):
        """Test het genereren van een rule summary."""
        summary = self.validator.get_rule_summary()
        
        assert summary["total_rules"] == 90
        assert "by_category" in summary
        assert "by_severity" in summary
        assert "rules" in summary
        assert len(summary["rules"]) == 90
    
    def test_validate_empty_data(self):
        """Test validatie met lege data."""
        data = {}
        violations = self.validator.validate(data)
        
        # Moet een lijst returnen (mogelijk leeg als geen validation_func's geïmplementeerd)
        assert isinstance(violations, list)
    
    def test_validate_with_context(self):
        """Test validatie met context informatie."""
        data = {"task_code": "TEST-001"}
        context = {"user": "test_user", "permissions": ["read", "write"]}
        
        violations = self.validator.validate(data, context)
        assert isinstance(violations, list)
    
    def test_validate_by_category(self):
        """Test validatie van specifieke categorie."""
        data = {"task_code": "TEST-001"}
        
        # Valideer alleen security rules
        violations = self.validator.validate_by_category(
            data, 
            RuleCategory.SECURITY
        )
        
        assert isinstance(violations, list)
    
    def test_business_rule_creation(self):
        """Test het maken van een BusinessRule object."""
        rule = BusinessRule(
            rule_id="TEST-1.1",
            category=RuleCategory.SECURITY,
            title="Test Rule",
            description="Dit is een test regel",
            severity=RuleSeverity.WARNING
        )
        
        assert rule.rule_id == "TEST-1.1"
        assert rule.category == RuleCategory.SECURITY
        assert rule.severity == RuleSeverity.WARNING
        assert str(rule) == "[TEST-1.1] Test Rule"
    
    def test_rule_violation_creation(self):
        """Test het maken van een RuleViolation object."""
        rule = BusinessRule(
            rule_id="TEST-1.1",
            category=RuleCategory.SECURITY,
            title="Test Rule",
            description="Test beschrijving",
            severity=RuleSeverity.ERROR
        )
        
        violation = RuleViolation(
            rule=rule,
            field="test_field",
            message="Test violation message",
            value="invalid_value",
            context={"extra": "info"}
        )
        
        assert violation.rule.rule_id == "TEST-1.1"
        assert violation.field == "test_field"
        assert violation.value == "invalid_value"
        assert "ERROR" in str(violation)
    
    def test_rule_categories_enum(self):
        """Test RuleCategory enum."""
        assert len(RuleCategory) == 8
        assert RuleCategory.SECURITY.value == "Security & Access Control"
        assert RuleCategory.OPERATIONS.value == "Operations & Maintenance"
        assert RuleCategory.QUALITY.value == "Quality & Compliance"
    
    def test_rule_severity_enum(self):
        """Test RuleSeverity enum."""
        assert len(RuleSeverity) == 4
        assert RuleSeverity.CRITICAL.value == "critical"
        assert RuleSeverity.ERROR.value == "error"
        assert RuleSeverity.WARNING.value == "warning"
        assert RuleSeverity.INFO.value == "info"
    
    def test_rule_ids_format(self):
        """Test of alle rule IDs het juiste format hebben."""
        all_rules = self.validator.get_all_rules()
        
        for rule_id, rule in all_rules.items():
            # Check format: XXX-N.M (prefix can be 2-3 chars)
            parts = rule_id.split('-')
            assert len(parts) == 2, f"Rule ID {rule_id} has wrong format"
            
            prefix, number = parts
            assert len(prefix) in [2, 3], f"Rule prefix {prefix} should be 2-3 chars"
            assert '.' in number, f"Rule number {number} should contain a dot"


class TestBusinessRulesIntegration:
    """Integratie tests voor Business Rules."""
    
    def setup_method(self):
        """Setup voor elke test."""
        self.validator = BusinessRulesValidator()
    
    def test_all_categories_have_expected_rules(self):
        """Test dat alle categorieën het verwachte aantal rules hebben."""
        expected = {"Logistics & Inventory": 20}

        for category in RuleCategory:
            rules = self.validator.get_rules_by_category(category)
            expected_count = expected.get(category.value, 10)
            assert len(rules) == expected_count, (
                f"Category {category.value} has {len(rules)} rules instead of {expected_count}"
            )
    
    def test_no_duplicate_rule_ids(self):
        """Test dat er geen duplicate rule IDs zijn."""
        all_rules = self.validator.get_all_rules()
        rule_ids = list(all_rules.keys())
        
        # Check voor duplicates
        assert len(rule_ids) == len(set(rule_ids)), "Found duplicate rule IDs"
    
    def test_all_rules_have_descriptions(self):
        """Test dat alle rules een beschrijving hebben."""
        all_rules = self.validator.get_all_rules()
        
        for rule_id, rule in all_rules.items():
            assert rule.title, f"Rule {rule_id} has no title"
            assert rule.description, f"Rule {rule_id} has no description"
            assert len(rule.description) > 10, f"Rule {rule_id} description too short"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
