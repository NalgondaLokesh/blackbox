import pytest
import requests
import base64
import hashlib

BASE_URL = "http://localhost:5010"

def test_ping():
    response = requests.get(f"{BASE_URL}/ping")
    assert response.status_code == 200
    assert "status" in response.json()

def test_obfuscate():
    data = {"data": "hello123"}
    response = requests.post(f"{BASE_URL}/v1/obfuscate", json=data)
    assert response.status_code == 200
    assert "result" in response.json()
    
    # Verify it's valid base64
    base64.b64decode(response.json()["result"])

# [Add similar tests for all endpoints...]