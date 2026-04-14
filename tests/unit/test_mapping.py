"""
Unit tests voor Mapping module

Auteur: Pedro (met Cursor AI assistentie)
Datum: 4 februari 2026
"""

import pytest
from src.mapping.pm_mapper import PMMapper
from src.mapping.jobplan_mapper import JobPlanMapper
from src.mapping.item_mapper import ItemMapper
from src.mapping.msg3_maximo_mapper import MSG3MaximoMapper


SAMPLE_TASK = {
    "task_code": "32-11-01-001",
    "description": "Visual inspection landing gear main fitting",
    "task_type": "INS",
    "interval": 500,
    "interval_unit": "FH",
    "zone": "Z100",
    "ata_chapter": "32",
    "ata_system": "11",  # Now derived from task_code by parser
    "man_hours": 1.5,
    "skills": ["MECH", "NDT"],
}


def _make_task(**overrides):
    task = SAMPLE_TASK.copy()
    task.update(overrides)
    return task


class TestPMMapper:
    """Test cases voor PMMapper."""

    def setup_method(self):
        self.mapper = PMMapper()

    def test_mapper_initialization(self):
        assert self.mapper is not None
        assert self.mapper.interval_unit_mapping is not None

    def test_interval_unit_mapping(self):
        assert self.mapper._map_interval_unit("FH") == "HOURS"
        assert self.mapper._map_interval_unit("FC") == "CYCLES"
        assert self.mapper._map_interval_unit("MO") == "MONTHS"
        assert self.mapper._map_interval_unit("WK") == "WEEKS"
        assert self.mapper._map_interval_unit("UNKNOWN") == "HOURS"

    def test_map_single_task(self):
        pm = self.mapper.map_task(SAMPLE_TASK)
        assert pm["PMNUM"] == "MSG3-32-11-01-001"
        assert pm["DESCRIPTION"] == SAMPLE_TASK["description"]
        assert pm["FREQUENCY"] == 500
        assert pm["FREQUNIT"] == "HOURS"
        assert pm["STATUS"] == "PLANNING"
        assert pm["COMMODITY"] == "ATA-32"

    def test_map_multiple_tasks(self):
        tasks = [_make_task(task_code=f"32-11-01-{i:03d}") for i in range(5)]
        records = self.mapper.map_tasks(tasks)
        assert len(records) == 5

    def test_map_task_missing_required_field(self):
        with pytest.raises(ValueError, match="Missing required"):
            self.mapper.map_task({"description": "test"})

    def test_format_description_truncation(self):
        long_desc = "A" * 150
        result = self.mapper._format_description(long_desc)
        assert len(result) <= 100
        assert result.endswith("...")

    def test_format_description_empty(self):
        with pytest.raises(ValueError):
            self.mapper._format_description("")

    def test_generate_pmnum(self):
        assert self.mapper._generate_pmnum("32-11-01-001") == "MSG3-32-11-01-001"

    def test_map_commodity_group(self):
        assert self.mapper._map_commodity_group("32") == "ATA-32"

    def test_map_commodity_group_none(self):
        assert self.mapper._map_commodity_group(None) == ""

    def test_map_commodity_code(self):
        assert self.mapper._map_commodity_code("32", "11") == "32-11"

    def test_map_commodity_code_incomplete(self):
        assert self.mapper._map_commodity_code("32", None) == ""
        assert self.mapper._map_commodity_code(None, "11") == ""

    def test_map_priority_default(self):
        assert self.mapper._map_priority(None) == 3

    def test_map_priority_clamp(self):
        assert self.mapper._map_priority(0) == 1
        assert self.mapper._map_priority(10) == 5
        assert self.mapper._map_priority(3) == 3

    def test_map_tasks_handles_errors(self):
        tasks = [SAMPLE_TASK, {"bad": "task"}]
        records = self.mapper.map_tasks(tasks)
        assert len(records) == 1


class TestJobPlanMapper:
    """Test cases voor JobPlanMapper."""

    def setup_method(self):
        self.mapper = JobPlanMapper()

    def test_mapper_initialization(self):
        assert self.mapper is not None
        assert self.mapper.default_status == "ACTIVE"

    def test_map_single_task(self):
        jp = self.mapper.map_task(SAMPLE_TASK)
        assert jp["JPNUM"] == "MSG3-32-11-01-001"
        assert jp["DESCRIPTION"] == SAMPLE_TASK["description"]
        assert jp["PLUSCJPREVDUR"] == 1.5
        assert jp["WORKTYPE"] == "PM"

    def test_map_multiple_tasks(self):
        tasks = [_make_task(task_code=f"32-11-01-{i:03d}") for i in range(5)]
        records = self.mapper.map_tasks(tasks)
        assert len(records) == 5

    def test_generate_jpnum(self):
        assert self.mapper._generate_jpnum("32-11-01-001") == "MSG3-32-11-01-001"

    def test_generate_jpnum_empty(self):
        with pytest.raises(ValueError):
            self.mapper._generate_jpnum(None)

    def test_format_description_truncation(self):
        result = self.mapper._format_description("X" * 150)
        assert len(result) <= 100
        assert result.endswith("...")

    def test_format_description_empty(self):
        with pytest.raises(ValueError):
            self.mapper._format_description(None)

    def test_map_tasks_handles_errors(self):
        tasks = [SAMPLE_TASK, {"bad": True}]
        records = self.mapper.map_tasks(tasks)
        assert len(records) == 1


class TestItemMapper:
    """Test cases voor ItemMapper."""

    def setup_method(self):
        self.mapper = ItemMapper(item_set_id="MSG3-MAINT", org_id="SCHIPHOL")

    def test_initialization(self):
        assert self.mapper.item_set_id == "MSG3-MAINT"
        assert self.mapper.org_id == "SCHIPHOL"

    def test_map_task_to_item(self):
        item = self.mapper.map_task_to_item(SAMPLE_TASK)
        assert item["ITEMNUM"] == "MSG3-32-11-01-001"
        assert item["DESCRIPTION"] == SAMPLE_TASK["description"]
        assert item["ITEMSETID"] == "MSG3-MAINT"
        assert item["STATUS"] == "PLANNING"
        assert item["STOCKCATEGORY"] == "NS"
        assert item["COMMODITY"] == "ATA-32"
        assert item["COMMODITYCODE"] == "32-11"

    def test_map_task_to_item_org(self):
        item_org = self.mapper.map_task_to_item_org(SAMPLE_TASK)
        assert item_org["ITEMNUM"] == "MSG3-32-11-01-001"
        assert item_org["ORGID"] == "SCHIPHOL"
        assert item_org["STATUS"] == "PLANNING"

    def test_map_task_to_item_org_no_org(self):
        mapper = ItemMapper(org_id=None)
        with pytest.raises(ValueError, match="Organization ID"):
            mapper.map_task_to_item_org(SAMPLE_TASK)

    def test_map_task_missing_required(self):
        with pytest.raises(ValueError, match="Missing required"):
            self.mapper.map_task_to_item({"description": "test"})

    def test_generate_itemnum(self):
        assert self.mapper._generate_itemnum("32-11-01-001") == "MSG3-32-11-01-001"

    def test_generate_itemnum_empty(self):
        with pytest.raises(ValueError):
            self.mapper._generate_itemnum("")

    def test_validate_itemnum_too_long(self):
        with pytest.raises(ValueError, match="too long"):
            self.mapper._validate_itemnum("X" * 31)

    def test_validate_itemnum_not_uppercase(self):
        with pytest.raises(ValueError, match="uppercase"):
            self.mapper._validate_itemnum("msg3-test")

    def test_validate_itemnum_spaces(self):
        with pytest.raises(ValueError, match="spaces"):
            self.mapper._validate_itemnum("MSG3 TEST")

    def test_validate_itemnum_empty(self):
        with pytest.raises(ValueError):
            self.mapper._validate_itemnum("")

    def test_format_description_truncation(self):
        result = self.mapper._format_description("Y" * 150)
        assert len(result) <= 100
        assert result.endswith("...")

    def test_format_description_empty(self):
        with pytest.raises(ValueError):
            self.mapper._format_description("")

    def test_map_commodity_group(self):
        assert self.mapper._map_commodity_group("32") == "ATA-32"

    def test_map_commodity_group_none(self):
        assert self.mapper._map_commodity_group(None) == ""

    def test_map_commodity_code(self):
        assert self.mapper._map_commodity_code("32", "11") == "32-11"

    def test_map_commodity_code_incomplete(self):
        assert self.mapper._map_commodity_code(None, "11") == ""

    def test_validate_commodity_too_long(self):
        with pytest.raises(ValueError, match="too long"):
            self.mapper._validate_commodity("TOOLONGXX", "group")

    def test_validate_commodity_not_uppercase(self):
        with pytest.raises(ValueError, match="uppercase"):
            self.mapper._validate_commodity("ata-32", "group")

    def test_validate_commodity_empty_ok(self):
        self.mapper._validate_commodity("", "group")
        self.mapper._validate_commodity(None, "code")

    def test_validate_item_for_obsolete(self):
        can, reasons = self.mapper.validate_item_for_obsolete("MSG3-32-11-01-001")
        assert can is True
        assert reasons == []


class TestMSG3MaximoMapper:
    """Test cases voor de hoofd mapper."""

    def setup_method(self):
        self.mapper = MSG3MaximoMapper()

    def test_initialization(self):
        assert self.mapper.item_set_id == "MSG3-MAINT"
        assert self.mapper.item_mapper is not None
        assert self.mapper.pm_mapper is not None
        assert self.mapper.jobplan_mapper is not None

    def test_map_full_data(self):
        data = {"tasks": [SAMPLE_TASK]}
        result = self.mapper.map(data)
        assert "items" in result
        assert "pm" in result
        assert "jobplan" in result
        assert "commodities" in result
        assert len(result["items"]) == 1
        assert len(result["pm"]) == 1
        assert len(result["jobplan"]) == 1

    def test_map_empty_tasks(self):
        data = {"tasks": []}
        result = self.mapper.map(data)
        assert all(len(v) == 0 for v in result.values())

    def test_map_no_tasks_key(self):
        with pytest.raises(ValueError, match="tasks"):
            self.mapper.map({})

    def test_map_none_data(self):
        with pytest.raises(ValueError):
            self.mapper.map(None)

    def test_extract_commodities(self):
        tasks = [
            {"ata_chapter": "32", "ata_system": "11"},
            {"ata_chapter": "32", "ata_system": "21"},
            {"ata_chapter": "27", "ata_system": "11"},
        ]
        commodities = self.mapper._extract_commodities(tasks)
        groups = [c for c in commodities if c["PARENT"] is None]
        codes = [c for c in commodities if c["PARENT"] is not None]
        assert len(groups) == 2  # ATA-32, ATA-27
        assert len(codes) == 3  # 32-11, 32-21, 27-11

    def test_extract_commodities_no_ata(self):
        tasks = [{"task_code": "TEST-001"}]
        commodities = self.mapper._extract_commodities(tasks)
        assert len(commodities) == 0

    def test_map_with_org_id(self):
        mapper = MSG3MaximoMapper(org_id="SCHIPHOL")
        data = {"tasks": [SAMPLE_TASK]}
        result = mapper.map(data)
        assert len(result["item_orgs"]) == 1

    def test_empty_result(self):
        result = self.mapper._empty_result()
        assert all(isinstance(v, list) and len(v) == 0 for v in result.values())


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
