"""
REST Client - Low-level HTTP client voor Maximo REST API

Biedt basis HTTP operaties met error handling en retry logic.

Auteur: Pedro (met Cursor AI assistentie)
Datum: 4 februari 2026
Dependencies: requests
"""

import logging
import time
from typing import Dict, Any, Optional

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

logger = logging.getLogger(__name__)


class MaximoAPIError(Exception):
    """Fout bij communicatie met Maximo REST API."""

    def __init__(self, message: str, status_code: int = 0, response_body: str = ""):
        super().__init__(message)
        self.status_code = status_code
        self.response_body = response_body


class RestClient:
    """
    Low-level REST client voor Maximo OSLC API.

    Verzorgt HTTP requests met:
    - Automatic retry met exponential backoff
    - Timeout handling
    - CSRF token management (Maximo vereist dit)
    - Request/response logging
    """

    DEFAULT_TIMEOUT = 30
    MAX_RETRIES = 3

    def __init__(
        self,
        base_url: str,
        verify_ssl: bool = True,
        timeout: int = DEFAULT_TIMEOUT,
        max_retries: int = MAX_RETRIES,
    ):
        self.base_url = base_url.rstrip("/")
        self.verify_ssl = verify_ssl
        self.timeout = timeout
        self.headers: Dict[str, str] = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        self.session = requests.Session()
        self.session.verify = verify_ssl

        retry_strategy = Retry(
            total=max_retries,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET", "POST", "PATCH"],
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

        logger.debug(f"RestClient initialized: {self.base_url}")

    def set_auth(self, auth_headers: Dict[str, str]) -> None:
        """Stel authenticatie headers in (API key, cookie, etc.)."""
        self.headers.update(auth_headers)

    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        """
        GET request naar Maximo OSLC API.

        Args:
            endpoint: API endpoint (bijv. "/maximo/oslc/os/mxpm")
            params: Query parameters (oslc.where, oslc.select, etc.)

        Returns:
            Response body als dictionary
        """
        url = f"{self.base_url}{endpoint}"
        logger.debug(f"GET {url} params={params}")

        try:
            response = self.session.get(
                url, headers=self.headers, params=params, timeout=self.timeout
            )
            return self._handle_response(response)
        except requests.ConnectionError as e:
            raise MaximoAPIError(f"Connection failed: {e}")
        except requests.Timeout as e:
            raise MaximoAPIError(f"Request timed out: {e}")

    def post(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        POST request naar Maximo OSLC API (create resource).

        Args:
            endpoint: API endpoint
            data: Request body

        Returns:
            Response body als dictionary (created resource)
        """
        url = f"{self.base_url}{endpoint}"
        logger.debug(f"POST {url}")

        try:
            response = self.session.post(
                url, headers=self.headers, json=data, timeout=self.timeout
            )
            return self._handle_response(response)
        except requests.ConnectionError as e:
            raise MaximoAPIError(f"Connection failed: {e}")
        except requests.Timeout as e:
            raise MaximoAPIError(f"Request timed out: {e}")

    def patch(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        PATCH request naar Maximo OSLC API (update resource).

        Maximo OSLC API gebruikt PATCH voor partial updates.
        Vereist x-method-override header voor sommige Maximo versies.

        Args:
            endpoint: API endpoint (inclusief resource ID)
            data: Velden om te updaten

        Returns:
            Response body als dictionary
        """
        url = f"{self.base_url}{endpoint}"
        logger.debug(f"PATCH {url}")

        patch_headers = {**self.headers, "x-method-override": "PATCH"}

        try:
            response = self.session.post(
                url, headers=patch_headers, json=data, timeout=self.timeout
            )
            return self._handle_response(response)
        except requests.ConnectionError as e:
            raise MaximoAPIError(f"Connection failed: {e}")
        except requests.Timeout as e:
            raise MaximoAPIError(f"Request timed out: {e}")

    def delete(self, endpoint: str) -> Dict[str, Any]:
        """
        DELETE request naar Maximo OSLC API.

        Let op: Maximo ondersteunt vaak geen DELETE. Gebruik in plaats
        daarvan status wijziging naar OBSOLETE.

        Args:
            endpoint: API endpoint

        Returns:
            Response body als dictionary
        """
        url = f"{self.base_url}{endpoint}"
        logger.debug(f"DELETE {url}")

        try:
            response = self.session.delete(
                url, headers=self.headers, timeout=self.timeout
            )
            return self._handle_response(response)
        except requests.ConnectionError as e:
            raise MaximoAPIError(f"Connection failed: {e}")
        except requests.Timeout as e:
            raise MaximoAPIError(f"Request timed out: {e}")

    def _handle_response(self, response: requests.Response) -> Dict[str, Any]:
        """Verwerk HTTP response en raise errors bij problemen."""
        logger.debug(f"Response: {response.status_code}")

        if response.status_code in (200, 201, 204):
            if response.status_code == 204 or not response.content:
                return {"status": "ok"}
            try:
                return response.json()
            except ValueError:
                return {"status": "ok", "body": response.text}

        error_msg = f"HTTP {response.status_code}"
        try:
            error_body = response.json()
            if "Error" in error_body:
                error_msg = f"{error_msg}: {error_body['Error'].get('message', '')}"
            elif "message" in error_body:
                error_msg = f"{error_msg}: {error_body['message']}"
        except (ValueError, KeyError):
            error_msg = f"{error_msg}: {response.text[:500]}"

        raise MaximoAPIError(error_msg, response.status_code, response.text)
