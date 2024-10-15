import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_publish_message():
    response = client.post("/publish", json={"msg": "Test message"})
    assert response.status_code == 200
    assert response.json() == {"status": "Message published"}
