from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"name": "Alice", "email": "alice@example.com"})
    assert response.status_code == 200
    assert response.json()["name"] == "Alice"

def test_get_user():
    response = client.get("/users/1")
    assert response.status_code == 200