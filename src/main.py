"""
MSG-3 -> Maximo Integration - Main Application

Entry point voor de MSG-3 naar Maximo integratie applicatie.
Orkestreert de volledige pipeline: parsing, validatie, change detection,
mapping en JSON output.

Auteur: Pedro (met Cursor AI assistentie)
Datum: 4 februari 2026
Organisatie: Babcock Schiphol
Project: Comakership ADSD - MSG-3 Maximo Integration
"""

import sys
import json
import logging
import argparse
from pathlib import Path
from typing import Optional, Dict, Any
from datetime import datetime

from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from rich.table import Table
from rich import box
from rich.text import Text

from . import __version__
from .parser import MSG3Parser
from .validator.msg3_validator import MSG3Validator, ValidationResult
from .change_detection.change_detector import ChangeDetector
from .mapping.msg3_maximo_mapper import MSG3MaximoMapper

logger = logging.getLogger(__name__)
console = Console()


class MSG3MaximoIntegration:
    """
    Hoofdapplicatie voor MSG-3 -> Maximo integratie.

    Orkestreert de volledige pipeline:
    1. Excel parsing (MSG-3 -> JSON)
    2. Data validatie
    3. Change detection (vergelijking met vorige versie)
    4. Mapping (MSG-3 -> Maximo objecten)
    5. Maximo upload (via REST API) [toekomstig]
    """

    def __init__(self, config_path: Optional[Path] = None):
        logger.info("MSG-3 Maximo Integration gestart")
        self.config_path = config_path
        self._initialize_components()

    def _initialize_components(self) -> None:
        logger.info("Componenten initialiseren...")
        self.parser = MSG3Parser()
        self.validator = MSG3Validator()
        self.change_detector = ChangeDetector()
        self.mapper = MSG3MaximoMapper()

    def process_msg3_file(
        self,
        excel_path: Path,
        previous_data: Optional[Dict[str, Any]] = None,
        skip_validation: bool = False,
        quiet: bool = False,
    ) -> Dict[str, Any]:
        """
        Verwerk een MSG-3 Excel bestand volledig.

        Pipeline: Parse -> Validate -> Change Detection -> Map

        Args:
            excel_path: Pad naar MSG-3 Excel bestand
            previous_data: Optioneel: vorige versie voor change detection
            skip_validation: Sla validatie over (niet aanbevolen)
            quiet: Geen rich output, alleen logging

        Returns:
            Dictionary met resultaten van elke stap
        """
        result = {
            "success": False,
            "file": str(excel_path),
            "timestamp": datetime.now().isoformat(),
            "version": __version__,
            "parsed_data": None,
            "validation": None,
            "changes": None,
            "maximo_objects": None,
            "errors": [],
        }

        steps = [
            ("Excel parsing",          self._step_parse,    (excel_path, result)),
            ("Data validatie",         self._step_validate, (result, skip_validation)),
            ("Change detection",       self._step_changes,  (result, previous_data)),
            ("Mapping naar Maximo",    self._step_map,      (result,)),
        ]

        if quiet:
            for _label, fn, args in steps:
                if not fn(*args):
                    return result
        else:
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(bar_width=30),
                TaskProgressColumn(),
                console=console,
                transient=True,
            ) as progress:
                task = progress.add_task("Pipeline...", total=len(steps))
                for label, fn, args in steps:
                    progress.update(task, description=f"[cyan]{label}[/cyan]...")
                    ok = fn(*args)
                    progress.advance(task)
                    if not ok:
                        return result

        return result

    # ------------------------------------------------------------------ steps

    def _step_parse(self, excel_path: Path, result: Dict[str, Any]) -> bool:
        logger.info("Stap 1/4: Excel parsing...")
        try:
            parsed_data = self.parser.parse(excel_path)
        except Exception as e:
            logger.error(f"Parse fout: {e}", exc_info=True)
            result["errors"].append(str(e))
            return False

        result["parsed_data"] = parsed_data
        task_count = len(parsed_data.get("tasks", []))
        parse_errors = len(parsed_data.get("parse_errors", []))
        logger.info(f"  {task_count} taken geparseerd, {parse_errors} parse fouten")

        if task_count == 0:
            result["errors"].append("Geen taken gevonden in het bestand")
            return False
        return True

    def _step_validate(self, result: Dict[str, Any], skip: bool) -> bool:
        if skip:
            logger.info("Stap 2/4: Validatie overgeslagen")
            return True

        logger.info("Stap 2/4: Data validatie...")
        try:
            validation = self.validator.validate(result["parsed_data"])
        except Exception as e:
            logger.error(f"Validatie fout: {e}", exc_info=True)
            result["errors"].append(str(e))
            return False

        result["validation"] = {
            "is_valid": validation.is_valid,
            "error_count": len(validation.errors),
            "warning_count": len(validation.warnings),
            "summary": validation.get_error_summary(),
        }

        if not validation.is_valid:
            logger.warning(f"  Validatie gefaald: {len(validation.errors)} errors")
            result["errors"].append("Validatie gefaald")
            return False

        logger.info(f"  Validatie geslaagd ({len(validation.warnings)} warnings)")
        return True

    def _step_changes(
        self, result: Dict[str, Any], previous_data: Optional[Dict[str, Any]]
    ) -> bool:
        if not previous_data:
            logger.info("Stap 3/4: Geen vorige versie, change detection overgeslagen")
            return True

        logger.info("Stap 3/4: Wijzigingen detecteren...")
        try:
            changes = self.change_detector.detect_changes(
                previous_data, result["parsed_data"]
            )
            result["changes"] = changes.get_summary()
            logger.info(f"  {result['changes']}")
        except Exception as e:
            logger.error(f"Change detection fout: {e}", exc_info=True)
            result["errors"].append(str(e))
            return False
        return True

    def _step_map(self, result: Dict[str, Any]) -> bool:
        logger.info("Stap 4/4: Mapping naar Maximo objecten...")
        try:
            maximo_objects = self.mapper.map(result["parsed_data"])
        except Exception as e:
            logger.error(f"Mapping fout: {e}", exc_info=True)
            result["errors"].append(str(e))
            return False

        result["maximo_objects"] = maximo_objects
        obj_counts = {
            k: len(v) for k, v in maximo_objects.items() if isinstance(v, list)
        }
        logger.info(f"  Maximo objecten: {obj_counts}")
        result["success"] = True
        logger.info("Verwerking succesvol afgerond")
        return True

    def validate_only(self, excel_path: Path) -> ValidationResult:
        """Valideer een MSG-3 Excel bestand zonder mapping."""
        logger.info(f"Validatie van bestand: {excel_path}")
        parsed_data = self.parser.parse(excel_path)
        return self.validator.validate(parsed_data)

    def parse_only(self, excel_path: Path) -> Dict[str, Any]:
        """Alleen parsen, zonder validatie of mapping."""
        logger.info(f"Parsing van bestand: {excel_path}")
        return self.parser.parse(excel_path)


def _setup_logging(verbose: bool = False, log_file: Optional[str] = None) -> None:
    """Configureer logging voor de applicatie."""
    level = logging.DEBUG if verbose else logging.INFO
    fmt = "%(asctime)s [%(levelname)8s] %(name)s: %(message)s"
    handlers: list = []
    if log_file:
        handlers.append(logging.FileHandler(log_file, encoding="utf-8"))
    else:
        handlers.append(logging.StreamHandler(sys.stdout))
    logging.basicConfig(level=level, format=fmt, handlers=handlers)


def _print_banner() -> None:
    """Print applicatie banner met rich."""
    title = Text(f"MSG-3 -> Maximo Integration  v{__version__}", style="bold cyan")
    subtitle = Text("Comakership ADSD - Babcock Schiphol", style="dim")
    combined = Text.assemble(title, "\n", subtitle)
    console.print(Panel(combined, border_style="cyan", padding=(0, 2)))
    console.print()


def _print_summary(result: Dict[str, Any]) -> None:
    """Print een rich-samenvatting van de pipeline-resultaten."""
    success = result.get("success", False)

    # Kopje
    if success:
        console.print(Panel("[bold green]RESULTAAT: SUCCESVOL[/bold green]", border_style="green"))
    else:
        errors_text = "\n".join(f"  - {e}" for e in result.get("errors", []))
        console.print(Panel(
            f"[bold red]RESULTAAT: GEFAALD[/bold red]\n{errors_text}",
            border_style="red",
        ))

    table = Table(box=box.SIMPLE, show_header=False, padding=(0, 1))
    table.add_column("Label", style="bold", min_width=18)
    table.add_column("Waarde")

    parsed = result.get("parsed_data")
    if parsed:
        tasks = parsed.get("tasks", [])
        version = parsed.get("metadata", {}).get("version", "?")
        errs = parsed.get("parse_errors", [])
        table.add_row("Formaat", version)
        table.add_row(
            "Taken",
            f"[green]{len(tasks)} geparseerd[/green], "
            f"[{'red' if errs else 'dim'}]{len(errs)} parse fouten[/{'red' if errs else 'dim'}]",
        )

    validation = result.get("validation")
    if validation:
        status_color = "green" if validation["is_valid"] else "red"
        table.add_row(
            "Validatie",
            f"[{status_color}]{'OK' if validation['is_valid'] else 'GEFAALD'}[/{status_color}] "
            f"({validation['error_count']} errors, {validation['warning_count']} warnings)",
        )

    changes = result.get("changes")
    if changes:
        table.add_row("Wijzigingen", str(changes))

    maximo = result.get("maximo_objects")
    if maximo:
        for key, val in maximo.items():
            if isinstance(val, list) and val:
                table.add_row(f"  {key}", f"[cyan]{len(val)}[/cyan] objecten")

    console.print(table)
    console.print()


def main():
    """Main entry point voor de applicatie."""
    arg_parser = argparse.ArgumentParser(
        description="MSG-3 -> Maximo Integration Tool",
        epilog="Comakership ADSD - Babcock Schiphol",
    )
    arg_parser.add_argument(
        "excel_file", type=Path,
        help="Pad naar MSG-3 Excel bestand",
    )
    arg_parser.add_argument(
        "--mode", choices=["full", "validate", "parse"],
        default="full",
        help="Verwerkingsmodus (default: full)",
    )
    arg_parser.add_argument(
        "--output", "-o", type=Path, default=None,
        help="Pad voor JSON output bestand (default: stdout)",
    )
    arg_parser.add_argument(
        "--previous", type=Path, default=None,
        help="Pad naar vorige JSON output voor change detection",
    )
    arg_parser.add_argument(
        "--skip-validation", action="store_true",
        help="Sla validatie over (niet aanbevolen)",
    )
    arg_parser.add_argument(
        "--verbose", "-v", action="store_true",
        help="Uitgebreide logging",
    )
    arg_parser.add_argument(
        "--log-file", type=str, default=None,
        help="Schrijf logs naar bestand",
    )
    arg_parser.add_argument(
        "--quiet", "-q", action="store_true",
        help="Alleen JSON output, geen banner/samenvatting",
    )
    arg_parser.add_argument(
        "--version", action="version",
        version=f"MSG-3 Maximo Integration v{__version__}",
    )

    args = arg_parser.parse_args()

    _setup_logging(verbose=args.verbose, log_file=args.log_file)

    if not args.quiet:
        _print_banner()

    if not args.excel_file.exists():
        logger.error(f"Bestand niet gevonden: {args.excel_file}")
        sys.exit(1)

    integration = MSG3MaximoIntegration()

    # Laad vorige data voor change detection
    previous_data = None
    if args.previous:
        if args.previous.exists():
            with open(args.previous, "r", encoding="utf-8") as f:
                prev_result = json.load(f)
                previous_data = prev_result.get("parsed_data")
                if previous_data:
                    logger.info(f"Vorige versie geladen: {args.previous}")
                else:
                    logger.warning("Vorige JSON bevat geen parsed_data")
        else:
            logger.warning(f"Vorig bestand niet gevonden: {args.previous}")

    # Voer de gekozen modus uit
    if args.mode == "parse":
        result = integration.parse_only(args.excel_file)
    elif args.mode == "validate":
        validation = integration.validate_only(args.excel_file)
        result = {
            "success": validation.is_valid,
            "is_valid": validation.is_valid,
            "error_count": len(validation.errors),
            "warning_count": len(validation.warnings),
            "summary": validation.get_error_summary(),
        }
        if not args.quiet:
            print(validation.get_error_summary())
    else:
        result = integration.process_msg3_file(
            args.excel_file,
            previous_data=previous_data,
            skip_validation=args.skip_validation,
            quiet=args.quiet,
        )
        if not args.quiet:
            _print_summary(result)

    # Output opslaan of naar stdout
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False, default=str)
        if not args.quiet:
            print(f"Output opgeslagen: {args.output}")
    elif args.quiet:
        print(json.dumps(result, indent=2, ensure_ascii=False, default=str))

    success = result.get("success", result.get("is_valid", False))
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
