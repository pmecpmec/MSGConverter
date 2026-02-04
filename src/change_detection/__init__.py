"""
Change Detection Module - Wijzigingsdetectie tussen MSG-3 versies

Deze module detecteert wijzigingen tussen twee versies van MSG-3 data:
- Toegevoegde taken
- Gewijzigde taken
- Verwijderde taken
- Field-level changes

Auteur: Pedro (met Cursor AI assistentie)
Datum: 4 februari 2026
"""

from .change_detector import ChangeDetector
from .diff_engine import DiffEngine

__all__ = ["ChangeDetector", "DiffEngine"]
