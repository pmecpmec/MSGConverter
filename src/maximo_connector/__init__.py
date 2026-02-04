"""
Maximo Connector Module - Maximo REST API communicatie

Deze module verzorgt de communicatie met IBM Maximo via de REST API:
- Authentication & authorization
- CRUD operaties op Maximo objecten
- Error handling & retry logic
- Batch operations

Auteur: Pedro (met Cursor AI assistentie)
Datum: 4 februari 2026
"""

from .maximo_client import MaximoClient
from .rest_client import RestClient

__all__ = ["MaximoClient", "RestClient"]
