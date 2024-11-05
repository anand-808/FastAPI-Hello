from fastapi.testclient import TestClient
from Fastapi.app.main import app  # Absolute import instead of relative

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_invalid_route():
    response = client.get("/invalid")
    assert response.status_code == 404

def test_get_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Ensure the response is a list
