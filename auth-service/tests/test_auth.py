# tests/test_auth.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_user():
    response = client.post("/register", json={
        "username": "demo",
        "email": "demo@example.com",
        "password": "password"
    })
    assert response.status_code == 200
    assert response.json()["username"] == "demo"
