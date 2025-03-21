import sys
import os
# Add the parent directory (project root) to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import requests
from query_threat_intelligence import check_ip

# Dummy response class to simulate 'requests.get' behavior
class DummyResponse:
    def __init__(self, status_code, data):
        self.status_code = status_code
        self._data = data

    def json(self):
        return self._data

def test_check_ip_success(monkeypatch):
    # Setup a dummy IP and a simulated successful response
    ip = "123.123.123.123"
    dummy_data = {
        "data": {
            "attributes": {
                "last_analysis_stats": {
                    "malicious": 5,
                    "suspicious": 2,
                    "harmless": 50
                },
                "asn": "AS12345",
                "country": "US"
            }
        }
    }
    
    # Dummy function to replace requests.get
    def dummy_get(url, headers):
        return DummyResponse(200, dummy_data)
    
    # Replace the requests.get function with dummy_get
    monkeypatch.setattr(requests, "get", dummy_get)
    
    result = check_ip(ip)
    
    # Assert that the result matches our dummy data
    assert result["IP"] == ip
    assert result["Malicious Votes"] == 5
    assert result["Suspicious Votes"] == 2
    assert result["Harmless Votes"] == 50
    assert result["ASN"] == "AS12345"
    assert result["Country"] == "US"

def test_check_ip_failure(monkeypatch):
    # Setup a dummy IP and simulate a failure response
    ip = "123.123.123.123"
    error_message = "Not found"
    
    def dummy_get(url, headers):
        return DummyResponse(404, {"error": error_message})
    
    monkeypatch.setattr(requests, "get", dummy_get)
    
    result = check_ip(ip)
    
    # Check that the error is present in the result
    assert result["IP"] == ip
    assert "Error" in result
    assert error_message in result["Error"]
    # Dummy response class to simulate 'requests.get' behavior
class DummyResponse:
    def __init__(self, status_code, data):
        self.status_code = status_code
        self._data = data
        # Set text attribute from data if available; otherwise empty string
        self.text = data.get("error", "") if isinstance(data, dict) else ""

    def json(self):
        return self._data

