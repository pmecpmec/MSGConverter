"""
Integration tests voor volledige pipeline

Test de complete flow van Excel parsing tot Maximo mapping.

Auteur: Pedro (met Cursor AI assistentie)
Datum: 4 februari 2026
"""

import pytest
from pathlib import Path

from src.parser.msg3_parser import MSG3Parser
from src.validator.msg3_validator import MSG3Validator
from src.change_detection.change_detector import ChangeDetector
from src.mapping.msg3_maximo_mapper import MSG3MaximoMapper
from src.main import MSG3MaximoIntegration

FIXTURE_DIR = Path(__file__).parent.parent / "fixtures"
REDESIGN_EXCEL = FIXTURE_DIR / "test_msg3_redesign.xlsx"


@pytest.fixture
def integration():
    return MSG3MaximoIntegration()


@pytest.fixture
def parser():
    return MSG3Parser()


@pytest.fixture
def validator():
    return MSG3Validator()


@pytest.fixture
def mapper():
    return MSG3MaximoMapper()


class TestParseValidateMapPipeline:
    """Test de flow: Parse -> Validate -> Map."""

    @pytest.mark.integration
    def test_parse_redesign_excel(self, parser):
        """Test dat het redesign Excel bestand correct geparseerd wordt."""
        assert REDESIGN_EXCEL.exists(), f"Test fixture niet gevonden: {REDESIGN_EXCEL}"

        data = parser.parse(REDESIGN_EXCEL)

        assert "metadata" in data
        assert "tasks" in data
        assert "parse_errors" in data
        assert data["metadata"]["version"] == "redesign"
        assert len(data["tasks"]) == 10

    @pytest.mark.integration
    def test_parsed_task_fields(self, parser):
        """Test dat geparseerde taken alle verwachte velden bevatten."""
        data = parser.parse(REDESIGN_EXCEL)
        task = data["tasks"][0]

        assert task["task_code"] == "32-11-01-001"
        assert task["description"] == "Visual inspection landing gear main fitting"
        assert task["task_type"] == "INS"
        assert task["interval"] == 500
        assert task["interval_unit"] == "FH"
        assert task["zone"] == "Z100"
        assert task["ata_chapter"] == "32"
        assert task["ata_system"] == "11"
        assert task["man_hours"] == 1.5
        assert task["skills"] == ["MECH", "NDT"]

    @pytest.mark.integration
    def test_validate_parsed_data(self, parser, validator):
        """Test dat geparseerde data validatie doorkomt."""
        data = parser.parse(REDESIGN_EXCEL)
        result = validator.validate(data)

        assert result.is_valid, f"Validatie gefaald:\n{result.get_error_summary()}"
        assert len(result.errors) == 0

    @pytest.mark.integration
    def test_map_validated_data(self, parser, validator, mapper):
        """Test dat gevalideerde data correct gemapt wordt naar Maximo objecten."""
        data = parser.parse(REDESIGN_EXCEL)
        result = validator.validate(data)
        assert result.is_valid

        maximo_objects = mapper.map(data)

        assert "items" in maximo_objects
        assert "pm" in maximo_objects
        assert "jobplan" in maximo_objects
        assert "commodities" in maximo_objects

        assert len(maximo_objects["items"]) == 10
        assert len(maximo_objects["pm"]) == 10
        assert len(maximo_objects["jobplan"]) == 10

    @pytest.mark.integration
    def test_maximo_item_fields(self, parser, mapper):
        """Test dat Maximo Item records de juiste velden bevatten."""
        data = parser.parse(REDESIGN_EXCEL)
        maximo_objects = mapper.map(data)

        item = maximo_objects["items"][0]
        assert "ITEMNUM" in item
        assert "DESCRIPTION" in item
        assert item["ITEMNUM"].startswith("MSG3-")

    @pytest.mark.integration
    def test_maximo_pm_fields(self, parser, mapper):
        """Test dat Maximo PM records de juiste velden bevatten."""
        data = parser.parse(REDESIGN_EXCEL)
        maximo_objects = mapper.map(data)

        pm = maximo_objects["pm"][0]
        assert "PMNUM" in pm
        assert "DESCRIPTION" in pm
        assert "FREQUENCY" in pm

    @pytest.mark.integration
    def test_full_pipeline_via_integration_class(self, integration):
        """Test de volledige pipeline via MSG3MaximoIntegration."""
        result = integration.process_msg3_file(REDESIGN_EXCEL)

        assert result["success"], f"Pipeline gefaald: {result['errors']}"
        assert result["parsed_data"] is not None
        assert result["validation"] is not None
        assert result["validation"]["is_valid"]
        assert result["maximo_objects"] is not None
        assert len(result["errors"]) == 0

    @pytest.mark.integration
    def test_pipeline_skip_validation(self, integration):
        """Test pipeline met skip_validation flag."""
        result = integration.process_msg3_file(
            REDESIGN_EXCEL, skip_validation=True
        )

        assert result["success"]
        assert result["validation"] is None
        assert result["maximo_objects"] is not None


class TestChangeDetectionPipeline:
    """Test de flow met change detection."""

    @pytest.mark.integration
    def test_change_detection_identical(self, parser):
        """Test change detection met identieke data (geen wijzigingen)."""
        detector = ChangeDetector()
        data = parser.parse(REDESIGN_EXCEL)

        report = detector.detect_changes(data, data)

        assert report.added_count == 0
        assert report.deleted_count == 0
        assert report.modified_count == 0

    @pytest.mark.integration
    def test_change_detection_with_modifications(self, parser):
        """Test change detection met gewijzigde taken."""
        import copy
        detector = ChangeDetector()
        old_data = parser.parse(REDESIGN_EXCEL)
        new_data = copy.deepcopy(old_data)

        new_data["tasks"][0]["interval"] = 600
        new_data["tasks"][0]["description"] = "Modified inspection"

        report = detector.detect_changes(old_data, new_data)

        assert report.modified_count > 0

    @pytest.mark.integration
    def test_change_detection_with_added_task(self, parser):
        """Test change detection met toegevoegde taak."""
        import copy
        detector = ChangeDetector()
        old_data = parser.parse(REDESIGN_EXCEL)
        new_data = copy.deepcopy(old_data)

        new_data["tasks"].append({
            "task_code": "99-99-99-001",
            "description": "New test task",
            "task_type": "INS",
            "interval": 100,
            "interval_unit": "FH",
            "zone": None,
            "ata_chapter": "99",
            "man_hours": 1.0,
            "skills": [],
        })

        report = detector.detect_changes(old_data, new_data)

        assert report.added_count == 1

    @pytest.mark.integration
    def test_change_detection_with_deleted_task(self, parser):
        """Test change detection met verwijderde taak."""
        import copy
        detector = ChangeDetector()
        old_data = parser.parse(REDESIGN_EXCEL)
        new_data = copy.deepcopy(old_data)

        new_data["tasks"].pop(0)

        report = detector.detect_changes(old_data, new_data)

        assert report.deleted_count == 1

    @pytest.mark.integration
    def test_full_pipeline_with_change_detection(self, integration, parser):
        """Test de volledige pipeline met change detection."""
        import copy
        previous_data = parser.parse(REDESIGN_EXCEL)
        modified_data = copy.deepcopy(previous_data)
        modified_data["tasks"][0]["interval"] = 999

        result = integration.process_msg3_file(
            REDESIGN_EXCEL, previous_data=previous_data
        )

        assert result["success"]


class TestErrorHandling:
    """Test error handling in de pipeline."""

    @pytest.mark.integration
    def test_nonexistent_file(self, integration):
        """Test met een bestand dat niet bestaat."""
        result = integration.process_msg3_file(Path("nonexistent.xlsx"))
        assert not result["success"]
        assert len(result["errors"]) > 0

    @pytest.mark.integration
    def test_parse_only_mode(self, integration):
        """Test parse-only modus."""
        data = integration.parse_only(REDESIGN_EXCEL)
        assert "tasks" in data
        assert len(data["tasks"]) == 10

    @pytest.mark.integration
    def test_validate_only_mode(self, integration):
        """Test validate-only modus."""
        result = integration.validate_only(REDESIGN_EXCEL)
        assert result.is_valid


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-m", "integration"])
