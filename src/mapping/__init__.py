"""
Mapping Module - MSG-3 naar Maximo object mapping

Deze module mapt MSG-3 taken naar Maximo objecten:
- PM (Preventive Maintenance) records
- JobPlan records
- Location records

Auteur: Pedro (met Cursor AI assistentie)
Datum: 4 februari 2026
"""

from .msg3_maximo_mapper import MSG3MaximoMapper
from .pm_mapper import PMMapper
from .jobplan_mapper import JobPlanMapper

__all__ = ["MSG3MaximoMapper", "PMMapper", "JobPlanMapper"]
