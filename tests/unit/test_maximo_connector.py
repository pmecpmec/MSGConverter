"""
Unit tests voor Maximo Connector module

Tests met gemockte HTTP calls — geen echte Maximo server nodig.

Auteur: Pedro (met Cursor AI assistentie)
Datum: april 2026
"""

import pytest
from unittest.mock import patch, MagicMock, PropertyMock
import json

from src.maximo_connector.rest_client import RestClient, MaximoAPIError
from src.maximo_connector.maximo_client import MaximoClient, ENDPOINTS


class TestRestClient:
    """Test cases voor RestClient."""

    def setup_method(self):
        self.client = RestClient(base_url="https://maximo.test.com")

    def test_initialization(self):
        assert self.client.base_url == "https://maximo.test.com"
        assert self.client.session is not None
        assert "application/json" in self.client.headers["Accept"]

    def test_initialization_strip_trailing_slash(self):
        client = RestClient(base_url="https://maximo.test.com/")
        assert client.base_url == "https://maximo.test.com"

    def test_set_auth(self):
        self.client.set_auth({"apikey": "test-key-123"})
        assert self.client.headers["apikey"] == "test-key-123"

    @patch("src.maximo_connector.rest_client.RestClient._handle_response")
    def test_get_success(self, mock_handle):
        mock_handle.return_value = {"member": []}
        with patch.object(self.client.session, "get") as mock_get:
            mock_get.return_value = MagicMock()
            result = self.client.get("/maximo/oslc/os/mxpm")
            mock_get.assert_called_once()
            assert result == {"member": []}

    @patch("src.maximo_connector.rest_client.RestClient._handle_response")
    def test_post_success(self, mock_handle):
        mock_handle.return_value = {"PMNUM": "MSG3-TEST"}
        with patch.object(self.client.session, "post") as mock_post:
            mock_post.return_value = MagicMock()
            result = self.client.post("/maximo/oslc/os/mxpm", {"PMNUM": "MSG3-TEST"})
            mock_post.assert_called_once()
            assert result["PMNUM"] == "MSG3-TEST"

    @patch("src.maximo_connector.rest_client.RestClient._handle_response")
    def test_patch_uses_method_override(self, mock_handle):
        mock_handle.return_value = {"status": "ok"}
        with patch.object(self.client.session, "post") as mock_post:
            mock_post.return_value = MagicMock()
            self.client.patch("/maximo/oslc/os/mxpm/123", {"DESCRIPTION": "Updated"})
            call_kwargs = mock_post.call_args
            assert call_kwargs[1]["headers"]["x-method-override"] == "PATCH"

    @patch("src.maximo_connector.rest_client.RestClient._handle_response")
    def test_delete_success(self, mock_handle):
        mock_handle.return_value = {"status": "ok"}
        with patch.object(self.client.session, "delete") as mock_del:
            mock_del.return_value = MagicMock()
            result = self.client.delete("/maximo/oslc/os/mxpm/123")
            assert result["status"] == "ok"

    def test_get_connection_error(self):
        import requests
        with patch.object(self.client.session, "get", side_effect=requests.ConnectionError("refused")):
            with pytest.raises(MaximoAPIError, match="Connection failed"):
                self.client.get("/test")

    def test_post_timeout(self):
        import requests
        with patch.object(self.client.session, "post", side_effect=requests.Timeout("timed out")):
            with pytest.raises(MaximoAPIError, match="timed out"):
                self.client.post("/test", {})

    def test_handle_response_200(self):
        resp = MagicMock()
        resp.status_code = 200
        resp.content = b'{"PMNUM": "TEST"}'
        resp.json.return_value = {"PMNUM": "TEST"}
        result = self.client._handle_response(resp)
        assert result["PMNUM"] == "TEST"

    def test_handle_response_201(self):
        resp = MagicMock()
        resp.status_code = 201
        resp.content = b'{"PMNUM": "NEW"}'
        resp.json.return_value = {"PMNUM": "NEW"}
        result = self.client._handle_response(resp)
        assert result["PMNUM"] == "NEW"

    def test_handle_response_204_no_content(self):
        resp = MagicMock()
        resp.status_code = 204
        resp.content = b""
        result = self.client._handle_response(resp)
        assert result["status"] == "ok"

    def test_handle_response_400_error(self):
        resp = MagicMock()
        resp.status_code = 400
        resp.json.return_value = {"Error": {"message": "Bad request"}}
        resp.text = "Bad request"
        with pytest.raises(MaximoAPIError) as exc_info:
            self.client._handle_response(resp)
        assert exc_info.value.status_code == 400

    def test_handle_response_500_text_error(self):
        resp = MagicMock()
        resp.status_code = 500
        resp.json.side_effect = ValueError("not json")
        resp.text = "Internal Server Error"
        with pytest.raises(MaximoAPIError) as exc_info:
            self.client._handle_response(resp)
        assert "500" in str(exc_info.value)


class TestMaximoAPIError:
    """Test MaximoAPIError exception."""

    def test_basic(self):
        err = MaximoAPIError("test error")
        assert str(err) == "test error"
        assert err.status_code == 0

    def test_with_status(self):
        err = MaximoAPIError("not found", status_code=404, response_body='{"msg":"nope"}')
        assert err.status_code == 404
        assert err.response_body == '{"msg":"nope"}'


class TestMaximoClient:
    """Test cases voor MaximoClient."""

    def setup_method(self):
        self.client = MaximoClient(
            base_url="https://maximo.test.com",
            apikey="test-key-123",
        )

    def test_initialization(self):
        assert self.client.base_url == "https://maximo.test.com"
        assert self.client.apikey == "test-key-123"
        assert not self.client.authenticated

    def test_authenticate_apikey(self):
        with patch.object(self.client.rest_client, "get", return_value={"member": []}):
            result = self.client.authenticate()
            assert result is True
            assert self.client.authenticated

    def test_authenticate_basic_auth(self):
        client = MaximoClient(
            base_url="https://maximo.test.com",
            username="admin",
            password="secret",
        )
        with patch.object(client.rest_client, "get", return_value={"member": []}):
            result = client.authenticate()
            assert result is True

    def test_authenticate_no_credentials(self):
        client = MaximoClient(base_url="https://maximo.test.com")
        with pytest.raises(MaximoAPIError, match="No credentials"):
            client.authenticate()

    def test_authenticate_failure(self):
        with patch.object(
            self.client.rest_client, "get",
            side_effect=MaximoAPIError("401 Unauthorized", 401)
        ):
            with pytest.raises(MaximoAPIError):
                self.client.authenticate()
            assert not self.client.authenticated

    def test_require_auth_not_authenticated(self):
        with pytest.raises(MaximoAPIError, match="Not authenticated"):
            self.client._require_auth()

    def _auth(self):
        """Helper: stel client in als geauthenticeerd."""
        self.client.authenticated = True

    def test_create_item(self):
        self._auth()
        with patch.object(self.client.rest_client, "post", return_value={"ITEMNUM": "MSG3-TEST"}) as mock:
            result = self.client.create_item({"ITEMNUM": "MSG3-TEST", "DESCRIPTION": "Test"})
            assert result["ITEMNUM"] == "MSG3-TEST"
            mock.assert_called_once_with(ENDPOINTS["item"], {"ITEMNUM": "MSG3-TEST", "DESCRIPTION": "Test"})

    def test_get_item_found(self):
        self._auth()
        with patch.object(self.client.rest_client, "get", return_value={"member": [{"ITEMNUM": "MSG3-TEST"}]}):
            result = self.client.get_item("MSG3-TEST")
            assert result["ITEMNUM"] == "MSG3-TEST"

    def test_get_item_not_found(self):
        self._auth()
        with patch.object(self.client.rest_client, "get", return_value={"member": []}):
            result = self.client.get_item("NONEXISTENT")
            assert result is None

    def test_item_exists(self):
        self._auth()
        with patch.object(self.client, "get_item", return_value={"ITEMNUM": "X"}):
            assert self.client.item_exists("X") is True
        with patch.object(self.client, "get_item", return_value=None):
            assert self.client.item_exists("X") is False

    def test_create_pm(self):
        self._auth()
        with patch.object(self.client.rest_client, "post", return_value={"PMNUM": "MSG3-PM"}) as mock:
            result = self.client.create_pm({"PMNUM": "MSG3-PM"})
            assert result["PMNUM"] == "MSG3-PM"
            mock.assert_called_once_with(ENDPOINTS["pm"], {"PMNUM": "MSG3-PM"})

    def test_update_pm(self):
        self._auth()
        with patch.object(self.client.rest_client, "patch", return_value={"status": "ok"}) as mock:
            self.client.update_pm("/maximo/oslc/os/mxpm/123", {"DESCRIPTION": "Updated"})
            mock.assert_called_once()

    def test_get_pm(self):
        self._auth()
        with patch.object(self.client.rest_client, "get", return_value={"member": [{"PMNUM": "X"}]}):
            result = self.client.get_pm("X")
            assert result is not None

    def test_create_jobplan(self):
        self._auth()
        with patch.object(self.client.rest_client, "post", return_value={"JPNUM": "MSG3-JP"}) as mock:
            result = self.client.create_jobplan({"JPNUM": "MSG3-JP"})
            assert result["JPNUM"] == "MSG3-JP"

    def test_get_jobplan(self):
        self._auth()
        with patch.object(self.client.rest_client, "get", return_value={"member": []}):
            result = self.client.get_jobplan("NONEXISTENT")
            assert result is None

    def test_create_commodity(self):
        self._auth()
        with patch.object(self.client.rest_client, "post", return_value={"COMMODITY": "ATA-32"}):
            result = self.client.create_commodity({"COMMODITY": "ATA-32"})
            assert result["COMMODITY"] == "ATA-32"

    def test_batch_create_success(self):
        self._auth()
        with patch.object(self.client, "create_pm", return_value={"PMNUM": "X"}):
            result = self.client.batch_create("pm", [{"PMNUM": "X"}, {"PMNUM": "Y"}])
            assert result["total"] == 2
            assert result["success_count"] == 2
            assert result["failure_count"] == 0

    def test_batch_create_partial_failure(self):
        self._auth()
        with patch.object(
            self.client, "create_pm",
            side_effect=[{"PMNUM": "X"}, MaximoAPIError("duplicate")]
        ):
            result = self.client.batch_create("pm", [{"PMNUM": "X"}, {"PMNUM": "X"}])
            assert result["success_count"] == 1
            assert result["failure_count"] == 1

    def test_batch_create_unknown_type(self):
        self._auth()
        with pytest.raises(MaximoAPIError, match="Unknown object type"):
            self.client.batch_create("unknown", [{}])

    def test_upload_maximo_objects(self):
        self._auth()
        maximo_objects = {
            "commodities": [{"COMMODITY": "ATA-32"}],
            "items": [{"ITEMNUM": "MSG3-TEST"}],
            "pm": [{"PMNUM": "MSG3-TEST"}],
            "jobplan": [{"JPNUM": "MSG3-TEST"}],
        }
        with patch.object(self.client, "batch_create", return_value={
            "total": 1, "success_count": 1, "failure_count": 0,
            "successes": [], "failures": [],
        }) as mock:
            results = self.client.upload_maximo_objects(maximo_objects)
            assert mock.call_count == 4
            assert "commodities" in results
            assert "items" in results
            assert "pm" in results
            assert "jobplan" in results

    def test_upload_maximo_objects_empty(self):
        self._auth()
        results = self.client.upload_maximo_objects({"commodities": [], "items": [], "pm": [], "jobplan": []})
        assert results["pm"]["total"] == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
