"""
MSG-3 Validator - Hoofd validatie logic

Valideert MSG-3 data op structuur, datatypes, Maximo veldlimieten
en business rules.

Auteur: Pedro (met Cursor AI assistentie)
Datum: 4 februari 2026
Dependencies: pydantic
"""

import logging
import re
from typing import Dict, List, Any
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)

# Maximo veldlimieten
MAXIMO_LIMITS = {
    "ITEMNUM": 30,
    "DESCRIPTION": 100,
    "COMMODITY_GROUP": 8,
    "COMMODITY_CODE": 8,
    "PMNUM": 30,
    "JPNUM": 30,
}

# Geldige waarden
VALID_TASK_TYPES = {"INS", "LUB", "SVC", "RST", "FNC", "OPC", "DET", "GVI", "SDI"}
VALID_INTERVAL_UNITS = {"FH", "FC", "MO", "WK", "YR", "DY"}


@dataclass
class ValidationError:
    """
    Representeert een validatie fout.

    Attributes:
        field: Veld naam waar de fout optrad
        error_type: Type fout (required, invalid_type, invalid_value, etc.)
        message: Foutmelding
        severity: Severity (error, warning, info)
        task_code: Optioneel - de taakcode waar de fout bij hoort
    """
    field: str
    error_type: str
    message: str
    severity: str = "error"
    task_code: str = ""


@dataclass
class ValidationResult:
    """
    Resultaat van een validatie.

    Attributes:
        is_valid: True als er geen errors zijn (warnings zijn OK)
        errors: Lijst van ValidationError objecten (blokkeren pipeline)
        warnings: Lijst van warnings (niet blokkerend)
        info_messages: Lijst van info messages
    """
    is_valid: bool
    errors: List[ValidationError]
    warnings: List[ValidationError]
    info_messages: List[str]

    def get_error_summary(self) -> str:
        """Genereer een tekstuele samenvatting van fouten."""
        if self.is_valid and not self.warnings:
            return "Validatie geslaagd"

        lines = []
        if not self.is_valid:
            lines.append(f"Validatie gefaald: {len(self.errors)} error(s)")
            for error in self.errors:
                prefix = f"[{error.task_code}] " if error.task_code else ""
                lines.append(f"  ERROR  {prefix}{error.field}: {error.message}")

        if self.warnings:
            lines.append(f"Waarschuwingen: {len(self.warnings)}")
            for w in self.warnings:
                prefix = f"[{w.task_code}] " if w.task_code else ""
                lines.append(f"  WARN   {prefix}{w.field}: {w.message}")

        return "\n".join(lines)

    @property
    def total_issues(self) -> int:
        return len(self.errors) + len(self.warnings)


class MSG3Validator:
    """
    Hoofd validator voor MSG-3 data.

    Voert verschillende validaties uit:
    1. Structuur validatie (zijn de verwachte velden aanwezig?)
    2. Data type en waarde validatie
    3. Maximo veldlimiet validatie
    4. Data kwaliteit checks

    Example:
        >>> validator = MSG3Validator()
        >>> result = validator.validate(parsed_data)
        >>> if result.is_valid:
        ...     print("Data is geldig!")
        >>> else:
        ...     print(result.get_error_summary())
    """

    def __init__(self):
        """Initialiseer de validator."""
        logger.info("MSG3Validator geïnitialiseerd")

    def validate(self, data: Dict[str, Any]) -> ValidationResult:
        """
        Valideer MSG-3 data.

        Args:
            data: Geparseerde MSG-3 data (output van MSG3Parser)

        Returns:
            ValidationResult object met resultaten
        """
        logger.info("Validatie starten...")
        errors: List[ValidationError] = []
        warnings: List[ValidationError] = []
        info_messages: List[str] = []

        # 1. Structuur validatie
        logger.debug("Structuur validatie...")
        struct_errors = self._validate_structure(data)
        errors.extend(struct_errors)

        # Stop als structuur ongeldig is
        if struct_errors:
            return ValidationResult(
                is_valid=False,
                errors=errors,
                warnings=warnings,
                info_messages=["Structuur validatie gefaald, overige checks overgeslagen"],
            )

        tasks = data.get("tasks", [])
        info_messages.append(f"{len(tasks)} taken te valideren")

        # 2. Per-taak validatie
        seen_codes: set = set()
        for idx, task in enumerate(tasks):
            task_code = task.get("task_code", f"task_{idx}")

            # Dubbele taakcodes
            if task_code in seen_codes:
                errors.append(ValidationError(
                    field="task_code", error_type="duplicate",
                    message=f"Dubbele taakcode: {task_code}",
                    task_code=task_code,
                ))
            seen_codes.add(task_code)

            # Veld validatie
            task_errors, task_warnings = self._validate_task(task, task_code)
            errors.extend(task_errors)
            warnings.extend(task_warnings)

            # Maximo limiet checks
            maximo_errors, maximo_warnings = self._validate_maximo_limits(task, task_code)
            errors.extend(maximo_errors)
            warnings.extend(maximo_warnings)

        # 3. Data kwaliteit checks
        logger.debug("Data kwaliteit checks...")
        quality_warnings = self._check_data_quality(tasks)
        warnings.extend(quality_warnings)

        is_valid = len(errors) == 0

        result = ValidationResult(
            is_valid=is_valid,
            errors=errors,
            warnings=warnings,
            info_messages=info_messages,
        )

        logger.info(
            f"Validatie compleet: {'geslaagd' if is_valid else 'gefaald'} "
            f"({len(errors)} errors, {len(warnings)} warnings)"
        )
        return result

    def _validate_structure(self, data: Dict[str, Any]) -> List[ValidationError]:
        """Valideer de basis structuur van de parser output."""
        errors = []

        if not isinstance(data, dict):
            errors.append(ValidationError(
                field="data", error_type="invalid_type",
                message="Data moet een dictionary zijn",
            ))
            return errors

        if "tasks" not in data:
            errors.append(ValidationError(
                field="tasks", error_type="required",
                message="'tasks' veld ontbreekt in data",
            ))

        if "metadata" not in data:
            errors.append(ValidationError(
                field="metadata", error_type="required",
                message="'metadata' veld ontbreekt in data",
            ))

        tasks = data.get("tasks")
        if tasks is not None and not isinstance(tasks, list):
            errors.append(ValidationError(
                field="tasks", error_type="invalid_type",
                message="'tasks' moet een lijst zijn",
            ))

        return errors

    def _validate_task(
        self, task: Dict[str, Any], task_code: str
    ) -> tuple:
        """Valideer een individuele taak op verplichte velden en waarden."""
        errors: List[ValidationError] = []
        warnings: List[ValidationError] = []

        # Verplichte velden
        required_fields = ["task_code", "description", "task_type", "interval", "interval_unit"]
        for field_name in required_fields:
            value = task.get(field_name)
            if value is None or (isinstance(value, str) and not value.strip()):
                errors.append(ValidationError(
                    field=field_name, error_type="required",
                    message=f"Verplicht veld '{field_name}' ontbreekt of is leeg",
                    task_code=task_code,
                ))

        # Task type validatie
        task_type = task.get("task_type", "")
        if task_type and task_type not in VALID_TASK_TYPES:
            warnings.append(ValidationError(
                field="task_type", error_type="invalid_value",
                message=f"Onbekend taaktype '{task_type}', verwacht: {VALID_TASK_TYPES}",
                severity="warning", task_code=task_code,
            ))

        # Interval validatie
        interval = task.get("interval")
        if interval is not None:
            if not isinstance(interval, (int, float)) or interval <= 0:
                errors.append(ValidationError(
                    field="interval", error_type="invalid_value",
                    message=f"Interval moet een positief getal zijn, kreeg: {interval}",
                    task_code=task_code,
                ))

        # Interval unit validatie
        interval_unit = task.get("interval_unit", "")
        if interval_unit and interval_unit not in VALID_INTERVAL_UNITS:
            errors.append(ValidationError(
                field="interval_unit", error_type="invalid_value",
                message=f"Ongeldige interval eenheid '{interval_unit}', verwacht: {VALID_INTERVAL_UNITS}",
                task_code=task_code,
            ))

        # Task code formaat check
        if task_code and not re.match(r"^[\w\-]+$", task_code):
            errors.append(ValidationError(
                field="task_code", error_type="invalid_format",
                message=f"Taakcode bevat ongeldige tekens: {task_code}",
                task_code=task_code,
            ))

        # Man hours validatie (optioneel maar als aanwezig: positief)
        man_hours = task.get("man_hours")
        if man_hours is not None and (not isinstance(man_hours, (int, float)) or man_hours < 0):
            warnings.append(ValidationError(
                field="man_hours", error_type="invalid_value",
                message=f"Man-uren moet een positief getal zijn, kreeg: {man_hours}",
                severity="warning", task_code=task_code,
            ))

        return errors, warnings

    def _validate_maximo_limits(
        self, task: Dict[str, Any], task_code: str
    ) -> tuple:
        """Valideer Maximo veldlimieten (voorkom fouten bij REST API upload)."""
        errors: List[ValidationError] = []
        warnings: List[ValidationError] = []

        # ITEMNUM: MSG3-{task_code} moet <= 30 tekens zijn
        itemnum = f"MSG3-{task_code}"
        if len(itemnum) > MAXIMO_LIMITS["ITEMNUM"]:
            errors.append(ValidationError(
                field="task_code", error_type="maximo_limit",
                message=(
                    f"Gegenereerd ITEMNUM '{itemnum}' is {len(itemnum)} tekens, "
                    f"max {MAXIMO_LIMITS['ITEMNUM']}"
                ),
                task_code=task_code,
            ))

        # Description <= 100 tekens
        desc = task.get("description", "")
        if desc and len(desc) > MAXIMO_LIMITS["DESCRIPTION"]:
            warnings.append(ValidationError(
                field="description", error_type="maximo_limit",
                message=(
                    f"Beschrijving is {len(desc)} tekens, "
                    f"max {MAXIMO_LIMITS['DESCRIPTION']} (wordt afgekapt)"
                ),
                severity="warning", task_code=task_code,
            ))

        # Commodity Group: ATA-{chapter} <= 8 tekens
        ata = task.get("ata_chapter")
        if ata:
            comm_group = f"ATA-{ata}"
            if len(comm_group) > MAXIMO_LIMITS["COMMODITY_GROUP"]:
                errors.append(ValidationError(
                    field="ata_chapter", error_type="maximo_limit",
                    message=(
                        f"Commodity group '{comm_group}' is {len(comm_group)} tekens, "
                        f"max {MAXIMO_LIMITS['COMMODITY_GROUP']}"
                    ),
                    task_code=task_code,
                ))

        return errors, warnings

    def _check_data_quality(self, tasks: List[Dict[str, Any]]) -> List[ValidationError]:
        """
        Voer data kwaliteit checks uit (warnings, niet blokkerend).

        Checks:
        - Korte beschrijvingen (minder dan 10 tekens)
        - Ontbrekende optionele maar nuttige velden
        - Verdacht hoge of lage interval waarden
        """
        warnings = []

        for task in tasks:
            tc = task.get("task_code", "")

            # Korte beschrijving
            desc = task.get("description", "")
            if desc and len(desc) < 10:
                warnings.append(ValidationError(
                    field="description", error_type="quality",
                    message=f"Beschrijving is erg kort ({len(desc)} tekens)",
                    severity="warning", task_code=tc,
                ))

            # Ontbrekend ATA chapter
            if not task.get("ata_chapter"):
                warnings.append(ValidationError(
                    field="ata_chapter", error_type="quality",
                    message="ATA chapter ontbreekt, commodity mapping niet mogelijk",
                    severity="warning", task_code=tc,
                ))

            # Verdacht hoog interval
            interval = task.get("interval", 0)
            unit = task.get("interval_unit", "")
            if unit == "FH" and interval and interval > 50000:
                warnings.append(ValidationError(
                    field="interval", error_type="quality",
                    message=f"Interval {interval} FH is ongebruikelijk hoog",
                    severity="warning", task_code=tc,
                ))
            elif unit == "MO" and interval and interval > 120:
                warnings.append(ValidationError(
                    field="interval", error_type="quality",
                    message=f"Interval {interval} maanden (>10 jaar) is ongebruikelijk",
                    severity="warning", task_code=tc,
                ))

        # Globale checks
        if len(tasks) == 0:
            warnings.append(ValidationError(
                field="tasks", error_type="quality",
                message="Geen taken gevonden in het bestand",
                severity="warning",
            ))

        return warnings


if __name__ == "__main__":
    # Test de validator
    logging.basicConfig(level=logging.DEBUG)
    validator = MSG3Validator()
    print("MSG3Validator ready for testing")
