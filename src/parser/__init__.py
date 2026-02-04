"""
Parser Module - MSG-3 Excel naar JSON conversie

Deze module is verantwoordelijk voor het inlezen van MSG-3 Excel bestanden
en het converteren naar een gestandaardiseerd JSON formaat.

Auteur: Pedro (met Cursor AI assistentie)
Datum: 4 februari 2026
"""

from .msg3_parser import MSG3Parser
from .excel_reader import ExcelReader

__all__ = ["MSG3Parser", "ExcelReader"]
