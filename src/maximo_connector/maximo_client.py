"""
Maximo Client - Hoofd Maximo API client

Biedt high-level interface voor Maximo operaties via de OSLC REST API.

Maximo OSLC API endpoints:
- /maximo/oslc/os/mxitem       -> Item Master
- /maximo/oslc/os/mxpm         -> Preventive Maintenance
- /maximo/oslc/os/mxjobplan    -> Job Plans
- /maximo/oslc/os/mxcommodity  -> Commodity Groups/Codes

Auteur: Pedro (met Cursor AI assistentie)
Datum: 4 februari 2026
Dependencies: requests
"""

import logging
from typing import Dict, List, Any, Optional

from .rest_client import RestClient, MaximoAPIError

logger = logging.getLogger(__name__)

# Maximo OSLC object structure endpoints
ENDPOINTS = {
    "item": "/maximo/oslc/os/mxitem",
    "pm": "/maximo/oslc/os/mxpm",
    "jobplan": "/maximo/oslc/os/mxjobplan",
    "commodity": "/maximo/oslc/os/mxcommodity",
}


class MaximoClient:
    """
    High-level Maximo API client.

    Biedt convenience methods voor alle Maximo operaties die nodig
    zijn voor de MSG-3 integratie:
    - Item Master CRUD
    - PM (Preventive Maintenance) CRUD
    - JobPlan CRUD
    - Commodity management
    - Batch operations

    Authenticatie:
    - API Key (aanbevolen): via apikey parameter
    - Basic Auth: via username/password
    - Maximo MAXAUTH cookie: automatisch via form-based login

    Example:
        >>> client = MaximoClient(
        ...     base_url="https://maximo.babcock.nl",
        ...     apikey="your-api-key-here"
        ... )
        >>> client.authenticate()
        >>> result = client.create_item(item_data)
    """

    def __init__(
        self,
        base_url: str,
        apikey: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        verify_ssl: bool = True,
        timeout: int = 30,
    ):
        self.base_url = base_url.rstrip("/")
        self.apikey = apikey
        self.username = username
        self.password = password

        self.rest_client = RestClient(
            base_url=self.base_url,
            verify_ssl=verify_ssl,
            timeout=timeout,
        )
        self.authenticated = False

        logger.info(f"MaximoClient initialized for {self.base_url}")

    def authenticate(self) -> bool:
        """
        Authenticeer bij Maximo.

        Ondersteunt drie methoden (in volgorde van voorkeur):
        1. API Key (header: apikey)
        2. Basic Auth (header: Authorization)
        3. MAXAUTH cookie (form-based login)

        Returns:
            True als authenticatie succesvol

        Raises:
            MaximoAPIError: Bij authenticatie fout
        """
        logger.info("Authenticating with Maximo...")

        if self.apikey:
            self.rest_client.set_auth({"apikey": self.apikey})
            logger.info("Using API key authentication")
        elif self.username and self.password:
            self.rest_client.session.auth = (self.username, self.password)
            logger.info("Using Basic Auth authentication")
        else:
            raise MaximoAPIError("No credentials provided (apikey or username/password required)")

        try:
            self.rest_client.get("/maximo/oslc/os/mxpm?oslc.pageSize=1")
            self.authenticated = True
            logger.info("Authentication successful")
            return True
        except MaximoAPIError as e:
            self.authenticated = False
            logger.error(f"Authentication failed: {e}")
            raise

    def _require_auth(self) -> None:
        """Controleer dat we geauthenticeerd zijn."""
        if not self.authenticated:
            raise MaximoAPIError("Not authenticated. Call authenticate() first.")

    # ========================================================================
    # ITEM MASTER
    # ========================================================================

    def create_item(self, item_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Maak een nieuw Item Master record in Maximo.

        Args:
            item_data: Item record (moet ITEMNUM en DESCRIPTION bevatten)

        Returns:
            Created resource van Maximo

        Raises:
            MaximoAPIError: Bij API fout (bijv. duplicate ITEMNUM)
        """
        self._require_auth()
        itemnum = item_data.get("ITEMNUM", "?")
        logger.info(f"Creating Item: {itemnum}")
        return self.rest_client.post(ENDPOINTS["item"], item_data)

    def get_item(self, itemnum: str) -> Optional[Dict[str, Any]]:
        """Haal een Item op via ITEMNUM."""
        self._require_auth()
        params = {"oslc.where": f'itemnum="{itemnum}"', "oslc.select": "*"}
        result = self.rest_client.get(ENDPOINTS["item"], params=params)
        members = result.get("member", result.get("rdfs:member", []))
        return members[0] if members else None

    def item_exists(self, itemnum: str) -> bool:
        """Check of een Item bestaat."""
        return self.get_item(itemnum) is not None

    # ========================================================================
    # PREVENTIVE MAINTENANCE
    # ========================================================================

    def create_pm(self, pm_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Maak een nieuw PM record in Maximo.

        Args:
            pm_data: PM record (moet PMNUM en DESCRIPTION bevatten)

        Returns:
            Created resource van Maximo
        """
        self._require_auth()
        pmnum = pm_data.get("PMNUM", "?")
        logger.info(f"Creating PM: {pmnum}")
        return self.rest_client.post(ENDPOINTS["pm"], pm_data)

    def update_pm(self, href: str, pm_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update een bestaand PM record.

        Args:
            href: Maximo resource href (uit eerder GET response)
            pm_data: Velden om te updaten (partial update)

        Returns:
            Updated resource
        """
        self._require_auth()
        logger.info(f"Updating PM at {href}")
        return self.rest_client.patch(href, pm_data)

    def get_pm(self, pmnum: str) -> Optional[Dict[str, Any]]:
        """Haal een PM op via PMNUM."""
        self._require_auth()
        params = {"oslc.where": f'pmnum="{pmnum}"', "oslc.select": "*"}
        result = self.rest_client.get(ENDPOINTS["pm"], params=params)
        members = result.get("member", result.get("rdfs:member", []))
        return members[0] if members else None

    # ========================================================================
    # JOB PLANS
    # ========================================================================

    def create_jobplan(self, jobplan_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Maak een nieuw JobPlan record in Maximo.

        Args:
            jobplan_data: JobPlan record (moet JPNUM en DESCRIPTION bevatten)

        Returns:
            Created resource van Maximo
        """
        self._require_auth()
        jpnum = jobplan_data.get("JPNUM", "?")
        logger.info(f"Creating JobPlan: {jpnum}")
        return self.rest_client.post(ENDPOINTS["jobplan"], jobplan_data)

    def get_jobplan(self, jpnum: str) -> Optional[Dict[str, Any]]:
        """Haal een JobPlan op via JPNUM."""
        self._require_auth()
        params = {"oslc.where": f'jpnum="{jpnum}"', "oslc.select": "*"}
        result = self.rest_client.get(ENDPOINTS["jobplan"], params=params)
        members = result.get("member", result.get("rdfs:member", []))
        return members[0] if members else None

    # ========================================================================
    # COMMODITIES
    # ========================================================================

    def create_commodity(self, commodity_data: Dict[str, Any]) -> Dict[str, Any]:
        """Maak een nieuw Commodity record in Maximo."""
        self._require_auth()
        commodity = commodity_data.get("COMMODITY", "?")
        logger.info(f"Creating Commodity: {commodity}")
        return self.rest_client.post(ENDPOINTS["commodity"], commodity_data)

    # ========================================================================
    # BATCH OPERATIONS
    # ========================================================================

    def batch_create(
        self,
        object_type: str,
        records: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """
        Maak meerdere records in batch.

        Verwerkt records sequentieel met error tracking.
        Maximo heeft geen native batch endpoint, dus we doen ze een voor een.

        Args:
            object_type: Object type ("item", "pm", "jobplan", "commodity")
            records: Lijst van records om te maken

        Returns:
            Samenvatting met successes, failures en details
        """
        self._require_auth()
        logger.info(f"Batch creating {len(records)} {object_type} records")

        create_fn = {
            "item": self.create_item,
            "pm": self.create_pm,
            "jobplan": self.create_jobplan,
            "commodity": self.create_commodity,
        }.get(object_type)

        if not create_fn:
            raise MaximoAPIError(f"Unknown object type: {object_type}")

        successes = []
        failures = []

        for i, record in enumerate(records):
            try:
                result = create_fn(record)
                successes.append({"index": i, "result": result})
            except MaximoAPIError as e:
                logger.error(f"Failed to create {object_type} #{i}: {e}")
                failures.append({"index": i, "error": str(e), "record": record})

        summary = {
            "object_type": object_type,
            "total": len(records),
            "success_count": len(successes),
            "failure_count": len(failures),
            "successes": successes,
            "failures": failures,
        }

        logger.info(
            f"Batch complete: {len(successes)} succeeded, {len(failures)} failed"
        )
        return summary

    def upload_maximo_objects(
        self, maximo_objects: Dict[str, List[Dict[str, Any]]]
    ) -> Dict[str, Any]:
        """
        Upload alle Maximo objecten in de juiste volgorde.

        Volgorde is cruciaal:
        1. Commodities (moeten bestaan voor Items)
        2. Items (moeten bestaan voor PM/JobPlan)
        3. PM records
        4. JobPlans

        Args:
            maximo_objects: Output van MSG3MaximoMapper.map()

        Returns:
            Samenvatting per object type
        """
        self._require_auth()
        logger.info("=== Starting Maximo upload ===")

        results = {}
        upload_order = [
            ("commodity", "commodities"),
            ("item", "items"),
            ("pm", "pm"),
            ("jobplan", "jobplan"),
        ]

        for object_type, key in upload_order:
            records = maximo_objects.get(key, [])
            if not records:
                logger.info(f"  Skipping {key}: no records")
                results[key] = {"total": 0, "success_count": 0, "failure_count": 0}
                continue

            logger.info(f"  Uploading {len(records)} {key}...")
            results[key] = self.batch_create(object_type, records)

            if results[key]["failure_count"] > 0:
                logger.warning(
                    f"  {results[key]['failure_count']} {key} failed to upload"
                )

        total_success = sum(r.get("success_count", 0) for r in results.values())
        total_fail = sum(r.get("failure_count", 0) for r in results.values())
        logger.info(
            f"=== Upload complete: {total_success} succeeded, {total_fail} failed ==="
        )

        return results
