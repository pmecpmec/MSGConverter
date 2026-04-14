"""
Unit tests voor Parser module

Auteur: Pedro (met Cursor AI assistentie)
Datum: 4 februari 2026
"""

import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
from src.parser.msg3_parser import MSG3Parser, MSG3Task, ParseError, VALID_TASK_TYPES, VALID_INTERVAL_UNITS
from src.parser.excel_reader import ExcelReader

FIXTURE_DIR = Path(__file__).parent.parent / "fixtures"
REDESIGN_EXCEL = FIXTURE_DIR / "test_msg3_redesign.xlsx"


class TestMSG3Parser:
    """Test cases voor MSG3Parser."""

    def setup_method(self):
        self.parser = MSG3Parser()

    def test_parser_initialization(self):
        assert self.parser is not None
        assert len(self.parser.supported_versions) == 2
        assert self.parser.reader is not None

    def test_msg3_task_creation(self):
        task = MSG3Task(
            task_code="32-11-01-001",
            description="Visual inspection",
            task_type="INS",
            interval=500,
            interval_unit="FH",
        )
        assert task.task_code == "32-11-01-001"
        assert task.description == "Visual inspection"
        assert task.interval == 500
        assert task.zone is None
        assert task.skills == []

    def test_msg3_task_to_dict(self):
        task = MSG3Task(
            task_code="32-11-01-001",
            description="Visual inspection",
            task_type="INS",
            interval=500,
            interval_unit="FH",
            zone="Z100",
            ata_chapter="32",
            ata_system="11",
            man_hours=1.5,
            skills=["MECH", "NDT"],
        )
        d = task.to_dict()
        assert isinstance(d, dict)
        assert d["task_code"] == "32-11-01-001"
        assert d["zone"] == "Z100"
        assert d["ata_system"] == "11"
        assert d["skills"] == ["MECH", "NDT"]
        assert d["man_hours"] == 1.5

    def test_parse_redesign_file(self):
        data = self.parser.parse(REDESIGN_EXCEL)
        assert data["metadata"]["version"] == "redesign"
        assert len(data["tasks"]) == 10
        assert data["metadata"]["total_tasks"] == 10

    def test_parse_file_not_found(self):
        with pytest.raises(FileNotFoundError):
            self.parser.parse(Path("does_not_exist.xlsx"))

    def test_detect_version_redesign(self):
        version = self.parser._detect_version(REDESIGN_EXCEL)
        assert version == "redesign"

    def test_parse_redesign_row_valid(self):
        row = {
            "TASK_CODE": "32-11-01-099",
            "DESCRIPTION": "Test inspection task",
            "TASK_TYPE": "INS",
            "INTERVAL": 500,
            "INTERVAL_UNIT": "FH",
            "ZONE": "Z100",
            "ATA_CHAPTER": "32",
            "MAN_HOURS": 2.0,
            "SKILLS": "MECH,NDT",
            "_row_number": 5,
        }
        task, errors = self.parser._parse_redesign_row(row, 5, set())
        assert task is not None
        assert task.task_code == "32-11-01-099"
        assert task.task_type == "INS"
        assert task.skills == ["MECH", "NDT"]

    def test_parse_redesign_row_missing_task_code(self):
        row = {
            "TASK_CODE": None,
            "DESCRIPTION": "Test",
            "TASK_TYPE": "INS",
            "INTERVAL": 500,
            "INTERVAL_UNIT": "FH",
            "_row_number": 5,
        }
        task, errors = self.parser._parse_redesign_row(row, 5, set())
        assert task is None
        assert any(e.field == "TASK_CODE" for e in errors)

    def test_parse_redesign_row_duplicate_code(self):
        row = {
            "TASK_CODE": "DUP-001",
            "DESCRIPTION": "Test",
            "TASK_TYPE": "INS",
            "INTERVAL": 100,
            "INTERVAL_UNIT": "FH",
            "_row_number": 5,
        }
        task, errors = self.parser._parse_redesign_row(row, 5, {"DUP-001"})
        assert task is None
        assert any("Dubbele" in e.message for e in errors)

    def test_parse_redesign_row_missing_description(self):
        row = {
            "TASK_CODE": "32-99-99-001",
            "DESCRIPTION": "",
            "TASK_TYPE": "INS",
            "INTERVAL": 500,
            "INTERVAL_UNIT": "FH",
            "_row_number": 5,
        }
        task, errors = self.parser._parse_redesign_row(row, 5, set())
        assert task is None
        assert any(e.field == "DESCRIPTION" for e in errors)

    def test_parse_redesign_row_invalid_interval(self):
        row = {
            "TASK_CODE": "32-99-99-002",
            "DESCRIPTION": "Valid description",
            "TASK_TYPE": "INS",
            "INTERVAL": "abc",
            "INTERVAL_UNIT": "FH",
            "_row_number": 5,
        }
        task, errors = self.parser._parse_redesign_row(row, 5, set())
        assert task is None
        assert any(e.field == "INTERVAL" for e in errors)

    def test_parse_redesign_row_zero_interval(self):
        row = {
            "TASK_CODE": "32-99-99-003",
            "DESCRIPTION": "Valid description",
            "TASK_TYPE": "INS",
            "INTERVAL": 0,
            "INTERVAL_UNIT": "FH",
            "_row_number": 5,
        }
        task, errors = self.parser._parse_redesign_row(row, 5, set())
        assert task is None

    def test_parse_redesign_row_default_task_type(self):
        row = {
            "TASK_CODE": "32-99-99-004",
            "DESCRIPTION": "Missing task type",
            "TASK_TYPE": None,
            "INTERVAL": 100,
            "INTERVAL_UNIT": "FH",
            "_row_number": 5,
        }
        task, errors = self.parser._parse_redesign_row(row, 5, set())
        assert task is not None
        assert task.task_type == "INS"

    def test_parse_redesign_row_invalid_task_type(self):
        row = {
            "TASK_CODE": "32-99-99-005",
            "DESCRIPTION": "Invalid type",
            "TASK_TYPE": "XYZ",
            "INTERVAL": 100,
            "INTERVAL_UNIT": "FH",
            "_row_number": 5,
        }
        task, errors = self.parser._parse_redesign_row(row, 5, set())
        assert task is not None
        assert any(e.field == "TASK_TYPE" for e in errors)

    def test_parse_redesign_row_default_interval_unit(self):
        row = {
            "TASK_CODE": "32-99-99-006",
            "DESCRIPTION": "Missing interval unit",
            "TASK_TYPE": "INS",
            "INTERVAL": 100,
            "INTERVAL_UNIT": None,
            "_row_number": 5,
        }
        task, errors = self.parser._parse_redesign_row(row, 5, set())
        assert task is not None
        assert task.interval_unit == "FH"

    def test_parse_redesign_row_invalid_interval_unit(self):
        row = {
            "TASK_CODE": "32-99-99-007",
            "DESCRIPTION": "Bad unit",
            "TASK_TYPE": "INS",
            "INTERVAL": 100,
            "INTERVAL_UNIT": "XX",
            "_row_number": 5,
        }
        task, errors = self.parser._parse_redesign_row(row, 5, set())
        assert task is not None
        assert any(e.field == "INTERVAL_UNIT" for e in errors)

    def test_ata_extracted_from_task_code(self):
        row = {
            "TASK_CODE": "27-11-01-001",
            "DESCRIPTION": "Test",
            "TASK_TYPE": "INS",
            "INTERVAL": 100,
            "INTERVAL_UNIT": "FH",
            "ATA_CHAPTER": None,
            "_row_number": 5,
        }
        task, _ = self.parser._parse_redesign_row(row, 5, set())
        assert task is not None
        assert task.ata_chapter == "27"


class TestParserHelpers:
    """Test helper/static methods."""

    def test_clean_str_none(self):
        assert MSG3Parser._clean_str(None) is None

    def test_clean_str_empty(self):
        assert MSG3Parser._clean_str("") is None
        assert MSG3Parser._clean_str("   ") is None

    def test_clean_str_value(self):
        assert MSG3Parser._clean_str("  hello  ") == "hello"

    def test_parse_int_valid(self):
        assert MSG3Parser._parse_int(42) == 42
        assert MSG3Parser._parse_int("42") == 42
        assert MSG3Parser._parse_int(42.7) == 42

    def test_parse_int_invalid(self):
        assert MSG3Parser._parse_int(None) is None
        assert MSG3Parser._parse_int("abc") is None

    def test_parse_float_valid(self):
        assert MSG3Parser._parse_float(1.5) == 1.5
        assert MSG3Parser._parse_float("2.5") == 2.5

    def test_parse_float_invalid(self):
        assert MSG3Parser._parse_float(None) is None
        assert MSG3Parser._parse_float("xyz") is None

    def test_parse_skills_none(self):
        assert MSG3Parser._parse_skills(None) == []

    def test_parse_skills_empty(self):
        assert MSG3Parser._parse_skills("") == []

    def test_parse_skills_single(self):
        assert MSG3Parser._parse_skills("MECH") == ["MECH"]

    def test_parse_skills_multiple(self):
        assert MSG3Parser._parse_skills("MECH, NDT, ELEC") == ["MECH", "NDT", "ELEC"]

    def test_extract_ata_valid(self):
        assert MSG3Parser._extract_ata_from_task_code("32-11-01-001") == "32"
        assert MSG3Parser._extract_ata_from_task_code("27-11-01-001") == "27"

    def test_extract_ata_invalid(self):
        assert MSG3Parser._extract_ata_from_task_code("ABC-11") is None
        assert MSG3Parser._extract_ata_from_task_code("1-11") is None

    def test_extract_ata_system_valid(self):
        assert MSG3Parser._extract_ata_system_from_task_code("32-11-01-001") == "11"
        assert MSG3Parser._extract_ata_system_from_task_code("27-21-01-001") == "21"

    def test_extract_ata_system_invalid(self):
        assert MSG3Parser._extract_ata_system_from_task_code("32") is None
        assert MSG3Parser._extract_ata_system_from_task_code("32-ABC") is None
        assert MSG3Parser._extract_ata_system_from_task_code("32-1") is None


class TestParserOriginalFormat:
    """Test origineel MSG-3 formaat parsing."""

    def setup_method(self):
        self.parser = MSG3Parser()

    def test_build_column_map_empty(self):
        result = self.parser._build_original_column_map([])
        assert result == {}

    def test_build_column_map_known_variations(self):
        rows = [{"TASK CODE": "X", "DESCRIPTION": "Y", "INTERVAL": 100, "_row_number": 1}]
        mapping = self.parser._build_original_column_map(rows)
        assert mapping.get("TASK CODE") == "TASK_CODE"
        assert mapping.get("DESCRIPTION") == "DESCRIPTION"

    def test_map_original_columns(self):
        row = {"TASK CODE": "32-001", "DESC": "Test", "INT": 500}
        column_map = {"TASK CODE": "TASK_CODE", "DESC": "DESCRIPTION", "INT": "INTERVAL"}
        mapped = self.parser._map_original_columns(row, column_map)
        assert mapped["TASK_CODE"] == "32-001"
        assert mapped["DESCRIPTION"] == "Test"
        assert mapped["INTERVAL"] == 500


class TestExcelReader:
    """Test ExcelReader."""

    def setup_method(self):
        self.reader = ExcelReader()

    def test_get_sheet_names(self):
        sheets = self.reader.get_sheet_names(REDESIGN_EXCEL)
        assert len(sheets) >= 1
        assert "MSG3 Tasks" in sheets

    def test_read_sheet(self):
        rows = self.reader.read_sheet(REDESIGN_EXCEL, "MSG3 Tasks")
        assert len(rows) == 10
        assert "TASK_CODE" in rows[0]

    def test_read_sheet_with_max_rows(self):
        rows = self.reader.read_sheet(REDESIGN_EXCEL, "MSG3 Tasks", max_rows=3)
        assert len(rows) == 3

    def test_find_header_row(self):
        row = self.reader.find_header_row(
            REDESIGN_EXCEL, "MSG3 Tasks",
            ["TASK_CODE", "DESCRIPTION", "INTERVAL"]
        )
        assert row == 1

    def test_find_header_row_not_found(self):
        row = self.reader.find_header_row(
            REDESIGN_EXCEL, "MSG3 Tasks",
            ["COMPLETELY_FAKE_HEADER_1", "COMPLETELY_FAKE_HEADER_2"]
        )
        assert row is None

    def test_validate_path_not_found(self):
        with pytest.raises(FileNotFoundError):
            self.reader._validate_path(Path("nonexistent.xlsx"))

    def test_validate_path_bad_extension(self):
        with pytest.raises(ValueError, match="Ongeldig bestandstype"):
            self.reader._validate_path(Path(__file__))

    def test_read_as_dataframe(self):
        df = self.reader.read_as_dataframe(REDESIGN_EXCEL)
        assert len(df) == 10
        assert "TASK_CODE" in df.columns

    def test_read_range(self):
        data = self.reader.read_range(REDESIGN_EXCEL, "MSG3 Tasks", "A1:B2")
        assert len(data) == 2
        assert data[0][0] == "TASK_CODE"


class TestParseError:
    """Test ParseError dataclass."""

    def test_creation(self):
        err = ParseError(row_number=5, field="INTERVAL", message="Ongeldige waarde")
        assert err.row_number == 5
        assert err.field == "INTERVAL"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
