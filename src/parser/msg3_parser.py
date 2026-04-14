"""
MSG-3 Parser - Excel naar JSON conversie

Deze module parseert MSG-3 Excel bestanden naar een gestructureerd JSON formaat
dat gebruikt kan worden door de rest van de pipeline.

Auteur: Pedro (met Cursor AI assistentie)
Datum: 4 februari 2026
Dependencies: openpyxl, pandas
"""

import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field

from .excel_reader import ExcelReader

logger = logging.getLogger(__name__)

# Verwachte headers per versie
REDESIGN_HEADERS = [
    "TASK_CODE", "DESCRIPTION", "TASK_TYPE", "INTERVAL",
    "INTERVAL_UNIT", "ZONE", "ATA_CHAPTER", "MAN_HOURS", "SKILLS",
]
ORIGINAL_HEADERS = ["TASK CODE", "DESCRIPTION", "INTERVAL"]

# Geldige waarden
VALID_TASK_TYPES = {"INS", "LUB", "SVC", "RST", "FNC", "OPC", "DET", "GVI", "SDI"}
VALID_INTERVAL_UNITS = {"FH", "FC", "MO", "WK", "YR", "DY"}


@dataclass
class MSG3Task:
    """
    Representeert een MSG-3 taak.

    Dit is de basis datastructuur voor een MSG-3 maintenance taak
    zoals gedefinieerd in de ATA MSG-3 specificatie.

    Attributes:
        task_code: Unieke taak code (bijv. "32-11-01-001")
        description: Beschrijving van de taak
        task_type: Type taak (INS=Inspection, LUB=Lubrication, etc.)
        interval: Interval waarde (numeriek)
        interval_unit: Eenheid (FH=Flight Hours, FC=Flight Cycles, MO=Months)
        zone: Toegangszone op het vliegtuig
        ata_chapter: ATA hoofdstuk nummer
        man_hours: Geschatte man-uren
        skills: Benodigde vaardigheden/certificeringen
    """
    task_code: str
    description: str
    task_type: str
    interval: int
    interval_unit: str
    zone: Optional[str] = None
    ata_chapter: Optional[str] = None
    ata_system: Optional[str] = None
    man_hours: Optional[float] = None
    skills: Optional[List[str]] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        """Converteer naar dictionary voor JSON serialisatie."""
        return {
            "task_code": self.task_code,
            "description": self.description,
            "task_type": self.task_type,
            "interval": self.interval,
            "interval_unit": self.interval_unit,
            "zone": self.zone,
            "ata_chapter": self.ata_chapter,
            "ata_system": self.ata_system,
            "man_hours": self.man_hours,
            "skills": self.skills,
        }


@dataclass
class ParseError:
    """Fout tijdens het parsen van een rij."""
    row_number: int
    field: str
    message: str


class MSG3Parser:
    """
    Parser voor MSG-3 Excel bestanden.

    Deze class leest MSG-3 Excel bestanden en converteert ze naar
    gestructureerde JSON data. Ondersteunt zowel het originele MSG-3
    formaat als het herontworpen formaat.

    Example:
        >>> parser = MSG3Parser()
        >>> data = parser.parse(Path("msg3.xlsx"))
        >>> print(f"Gevonden {len(data['tasks'])} taken")
    """

    def __init__(self):
        """Initialiseer de MSG-3 parser."""
        logger.info("MSG3Parser geïnitialiseerd")
        self.reader = ExcelReader()
        self.supported_versions = ["original", "redesign"]

    def parse(self, excel_path: Path) -> Dict[str, Any]:
        """
        Parse een MSG-3 Excel bestand naar JSON.

        Args:
            excel_path: Pad naar het MSG-3 Excel bestand

        Returns:
            Dictionary met geparseerde MSG-3 data:
            {
                "metadata": {...},
                "tasks": [...],
                "parse_errors": [...],
                "version": str
            }

        Raises:
            FileNotFoundError: Als het bestand niet bestaat
            ValueError: Als het bestand geen geldig MSG-3 formaat heeft
        """
        logger.info(f"Parsing MSG-3 bestand: {excel_path}")
        excel_path = Path(excel_path)

        if not excel_path.exists():
            raise FileNotFoundError(f"Bestand niet gevonden: {excel_path}")

        # Detecteer MSG-3 versie (original vs redesign)
        version = self._detect_version(excel_path)
        logger.info(f"Gedetecteerde versie: {version}")

        # Parse gebaseerd op versie
        if version == "redesign":
            tasks, errors = self._parse_redesign(excel_path)
        elif version == "original":
            tasks, errors = self._parse_original(excel_path)
        else:
            raise ValueError(f"Onbekende MSG-3 versie: {version}")

        data = {
            "metadata": {
                "version": version,
                "source_file": str(excel_path.resolve()),
                "file_name": excel_path.name,
                "parsed_at": datetime.now().isoformat(),
                "total_tasks": len(tasks),
                "parse_errors": len(errors),
            },
            "tasks": [t.to_dict() for t in tasks],
            "parse_errors": [
                {"row": e.row_number, "field": e.field, "message": e.message}
                for e in errors
            ],
        }

        logger.info(
            f"Parsing compleet: {len(tasks)} taken gevonden, "
            f"{len(errors)} fouten"
        )
        return data

    def _detect_version(self, excel_path: Path) -> str:
        """
        Detecteer de MSG-3 versie (original of redesign).

        Kijkt naar de headers in de eerste sheet om te bepalen
        welk formaat het bestand heeft.

        Args:
            excel_path: Pad naar Excel bestand

        Returns:
            "original" of "redesign"
        """
        logger.debug("Versie detectie...")

        sheets = self.reader.get_sheet_names(excel_path)
        if not sheets:
            raise ValueError("Excel bestand bevat geen sheets")

        # Probeer redesign headers te vinden
        header_row = self.reader.find_header_row(
            excel_path, sheets[0], REDESIGN_HEADERS
        )
        if header_row is not None:
            logger.info(f"Redesign formaat gedetecteerd (headers op rij {header_row})")
            return "redesign"

        # Probeer origineel formaat headers
        header_row = self.reader.find_header_row(
            excel_path, sheets[0], ORIGINAL_HEADERS
        )
        if header_row is not None:
            logger.info(f"Origineel formaat gedetecteerd (headers op rij {header_row})")
            return "original"

        # Fallback: als er data staat, behandel als origineel
        logger.warning(
            "Geen herkenbare headers gevonden, fallback naar origineel formaat"
        )
        return "original"

    def _parse_redesign(self, excel_path: Path) -> tuple:
        """
        Parse herontworpen MSG-3 Excel formaat.

        Kolommen (redesign):
            A: TASK_CODE (verplicht, uniek)
            B: DESCRIPTION (verplicht)
            C: TASK_TYPE (INS/LUB/SVC/etc.)
            D: INTERVAL (numeriek)
            E: INTERVAL_UNIT (FH/FC/MO/WK)
            F: ZONE (optioneel)
            G: ATA_CHAPTER (optioneel)
            H: MAN_HOURS (optioneel)
            I: SKILLS (optioneel, comma separated)

        Args:
            excel_path: Pad naar Excel bestand

        Returns:
            Tuple van (lijst MSG3Task, lijst ParseError)
        """
        logger.debug("Parsing redesign MSG-3 formaat...")

        sheets = self.reader.get_sheet_names(excel_path)
        header_row = self.reader.find_header_row(
            excel_path, sheets[0], REDESIGN_HEADERS
        )
        if header_row is None:
            header_row = 1

        rows = self.reader.read_sheet(
            excel_path, sheet_name=sheets[0], header_row=header_row
        )

        tasks: List[MSG3Task] = []
        errors: List[ParseError] = []
        seen_codes: set = set()

        for row in rows:
            row_num = row.get("_row_number", 0)
            try:
                task, row_errors = self._parse_redesign_row(row, row_num, seen_codes)
                errors.extend(row_errors)
                if task is not None:
                    tasks.append(task)
                    seen_codes.add(task.task_code)
            except Exception as e:
                errors.append(ParseError(row_num, "general", str(e)))
                logger.warning(f"Rij {row_num}: onverwachte fout - {e}")

        return tasks, errors

    def _parse_redesign_row(
        self, row: Dict[str, Any], row_num: int, seen_codes: set
    ) -> tuple:
        """Parse een enkele rij uit het redesign formaat."""
        errors: List[ParseError] = []

        # Verplichte velden
        task_code = self._clean_str(row.get("TASK_CODE"))
        description = self._clean_str(row.get("DESCRIPTION"))
        task_type = self._clean_str(row.get("TASK_TYPE"))
        interval_raw = row.get("INTERVAL")
        interval_unit = self._clean_str(row.get("INTERVAL_UNIT"))

        if not task_code:
            errors.append(ParseError(row_num, "TASK_CODE", "Verplicht veld ontbreekt"))
            return None, errors

        if task_code in seen_codes:
            errors.append(ParseError(row_num, "TASK_CODE", f"Dubbele taakcode: {task_code}"))
            return None, errors

        if not description:
            errors.append(ParseError(row_num, "DESCRIPTION", "Verplicht veld ontbreekt"))
            return None, errors

        # Task type validatie
        if not task_type:
            task_type = "INS"  # Default
            errors.append(ParseError(row_num, "TASK_TYPE", "Ontbreekt, standaard INS gebruikt"))
        elif task_type.upper() not in VALID_TASK_TYPES:
            errors.append(
                ParseError(row_num, "TASK_TYPE", f"Ongeldig type '{task_type}', verwacht: {VALID_TASK_TYPES}")
            )

        # Interval parsing
        interval = self._parse_int(interval_raw)
        if interval is None or interval <= 0:
            errors.append(ParseError(row_num, "INTERVAL", f"Ongeldige waarde: {interval_raw}"))
            return None, errors

        # Interval unit validatie
        if not interval_unit:
            interval_unit = "FH"  # Default
            errors.append(ParseError(row_num, "INTERVAL_UNIT", "Ontbreekt, standaard FH gebruikt"))
        elif interval_unit.upper() not in VALID_INTERVAL_UNITS:
            errors.append(
                ParseError(row_num, "INTERVAL_UNIT", f"Ongeldig: '{interval_unit}', verwacht: {VALID_INTERVAL_UNITS}")
            )

        # Optionele velden
        zone = self._clean_str(row.get("ZONE"))
        ata_chapter = self._clean_str(row.get("ATA_CHAPTER"))
        man_hours = self._parse_float(row.get("MAN_HOURS"))
        skills = self._parse_skills(row.get("SKILLS"))

        # ATA chapter + system afleiden uit task_code als ze ontbreken
        if not ata_chapter and task_code:
            ata_chapter = self._extract_ata_from_task_code(task_code)

        ata_system = self._clean_str(row.get("ATA_SYSTEM"))
        if not ata_system and task_code:
            ata_system = self._extract_ata_system_from_task_code(task_code)

        task = MSG3Task(
            task_code=task_code.upper(),
            description=description,
            task_type=task_type.upper(),
            interval=interval,
            interval_unit=interval_unit.upper(),
            zone=zone.upper() if zone else None,
            ata_chapter=ata_chapter,
            ata_system=ata_system,
            man_hours=man_hours,
            skills=skills,
        )
        return task, errors

    def _parse_original(self, excel_path: Path) -> tuple:
        """
        Parse originele MSG-3 Excel formaat.

        Het originele formaat heeft minder gestandaardiseerde kolommen.
        We proberen de meest gangbare structuur te herkennen.

        Args:
            excel_path: Pad naar Excel bestand

        Returns:
            Tuple van (lijst MSG3Task, lijst ParseError)
        """
        logger.debug("Parsing origineel MSG-3 formaat...")

        sheets = self.reader.get_sheet_names(excel_path)
        header_row = self.reader.find_header_row(
            excel_path, sheets[0], ORIGINAL_HEADERS
        )
        if header_row is None:
            header_row = 1

        rows = self.reader.read_sheet(
            excel_path, sheet_name=sheets[0], header_row=header_row
        )

        tasks: List[MSG3Task] = []
        errors: List[ParseError] = []
        seen_codes: set = set()

        # Kolomnaam mapping: origineel -> redesign
        column_map = self._build_original_column_map(rows)

        for row in rows:
            row_num = row.get("_row_number", 0)
            try:
                # Map originele kolomnamen naar standaard namen
                mapped_row = self._map_original_columns(row, column_map)
                task, row_errors = self._parse_redesign_row(mapped_row, row_num, seen_codes)
                errors.extend(row_errors)
                if task is not None:
                    tasks.append(task)
                    seen_codes.add(task.task_code)
            except Exception as e:
                errors.append(ParseError(row_num, "general", str(e)))

        return tasks, errors

    def _build_original_column_map(self, rows: List[Dict]) -> Dict[str, str]:
        """
        Bouw een mapping van originele kolomnamen naar standaard namen.

        Zoekt naar bekende variaties van kolomnamen.
        """
        if not rows:
            return {}

        available = set(rows[0].keys())
        mapping = {}

        # Bekende variaties per standaard veld
        variations = {
            "TASK_CODE": ["TASK CODE", "TASK_CODE", "TASKCODE", "CODE", "TASK NR", "TASK_NR"],
            "DESCRIPTION": ["DESCRIPTION", "DESC", "OMSCHRIJVING", "TASK DESCRIPTION"],
            "TASK_TYPE": ["TASK_TYPE", "TASK TYPE", "TYPE", "TASKTYPE"],
            "INTERVAL": ["INTERVAL", "INT", "FREQUENCY"],
            "INTERVAL_UNIT": ["INTERVAL_UNIT", "INTERVAL UNIT", "UNIT", "FREQ UNIT"],
            "ZONE": ["ZONE", "ACCESS ZONE", "AREA"],
            "ATA_CHAPTER": ["ATA_CHAPTER", "ATA CHAPTER", "ATA", "CHAPTER"],
            "MAN_HOURS": ["MAN_HOURS", "MAN HOURS", "MANHOURS", "MH", "HOURS"],
            "SKILLS": ["SKILLS", "SKILL", "CERTIFICATION", "CERT"],
        }

        for standard_name, variants in variations.items():
            for variant in variants:
                if variant in available:
                    mapping[variant] = standard_name
                    break

        logger.debug(f"Kolom mapping: {mapping}")
        return mapping

    def _map_original_columns(
        self, row: Dict[str, Any], column_map: Dict[str, str]
    ) -> Dict[str, Any]:
        """Map originele kolomnamen naar standaard namen."""
        mapped = {}
        for key, value in row.items():
            standard_name = column_map.get(key, key)
            mapped[standard_name] = value
        return mapped

    # --- Helper methodes ---

    @staticmethod
    def _clean_str(value: Any) -> Optional[str]:
        """Clean en strip een string waarde."""
        if value is None:
            return None
        s = str(value).strip()
        return s if s else None

    @staticmethod
    def _parse_int(value: Any) -> Optional[int]:
        """Parse een waarde naar int."""
        if value is None:
            return None
        try:
            return int(float(str(value)))
        except (ValueError, TypeError):
            return None

    @staticmethod
    def _parse_float(value: Any) -> Optional[float]:
        """Parse een waarde naar float."""
        if value is None:
            return None
        try:
            return float(str(value))
        except (ValueError, TypeError):
            return None

    @staticmethod
    def _parse_skills(value: Any) -> List[str]:
        """Parse comma-separated skills naar een lijst."""
        if value is None:
            return []
        skills_str = str(value).strip()
        if not skills_str:
            return []
        return [s.strip() for s in skills_str.split(",") if s.strip()]

    @staticmethod
    def _extract_ata_from_task_code(task_code: str) -> Optional[str]:
        """
        Probeer ATA chapter af te leiden uit de task code.

        Voorbeeld: "32-11-01-001" -> "32"
        """
        parts = task_code.split("-")
        if parts and parts[0].isdigit() and len(parts[0]) == 2:
            return parts[0]
        return None

    @staticmethod
    def _extract_ata_system_from_task_code(task_code: str) -> Optional[str]:
        """
        Probeer ATA system af te leiden uit de task code.

        MSG-3 task code formaat: {chapter}-{system}-{subsystem}-{sequence}
        Voorbeeld: "32-11-01-001" -> "11"
        """
        parts = task_code.split("-")
        if len(parts) >= 2 and parts[1].isdigit() and len(parts[1]) == 2:
            return parts[1]
        return None


if __name__ == "__main__":
    # Test de parser
    logging.basicConfig(level=logging.DEBUG)
    parser = MSG3Parser()
    print("MSG3Parser ready for testing")
