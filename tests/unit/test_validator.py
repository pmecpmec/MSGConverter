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


class TestBusinessRulesValidator:
    """Test cases voor BusinessRulesValidator."""
    
    def setup_method(self):
        """Setup voor elke test."""
        self.validator = BusinessRulesValidator()
    
    def test_validator_initialization(self):
        """Test of business rules validator correct geïnitialiseerd wordt."""
        assert self.validator is not None
        assert len(self.validator.rules) > 0
    
    def test_all_80_rules_loaded(self):
        """Test of alle 80 business rules geladen zijn."""
        assert len(self.validator.rules) == 80, f"Expected 80 rules, but got {len(self.validator.rules)}"
    
    def test_rules_by_category(self):
        """Test of elke categorie 10 rules heeft."""
        for category in RuleCategory:
            rules = self.validator.get_rules_by_category(category)
            assert len(rules) == 10, f"Category {category.value} should have 10 rules, but has {len(rules)}"
    
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
        assert len(rules) == 10
        
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
        assert total == 80
    
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
        
        assert summary["total_rules"] == 80
        assert "by_category" in summary
        assert "by_severity" in summary
        assert "rules" in summary
        assert len(summary["rules"]) == 80
    
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
    
    def test_all_categories_have_equal_rules(self):
        """Test dat alle categorieën evenveel rules hebben."""
        rule_counts = {}
        
        for category in RuleCategory:
            rules = self.validator.get_rules_by_category(category)
            rule_counts[category.value] = len(rules)
        
        # Alle categorieën moeten 10 rules hebben
        for category, count in rule_counts.items():
            assert count == 10, f"Category {category} has {count} rules instead of 10"
    
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
