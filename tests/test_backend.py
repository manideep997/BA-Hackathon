import sys
import os
import pytest
from fastapi.testclient import TestClient

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from backend.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "Backend is running"}

def test_status():
    response = client.get("/api/status/12345")
    assert response.status_code == 200
    assert response.json() == {"task_id": "12345", "status": "completed"}
