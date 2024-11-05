from fastapi.testclient import TestClient
from main import app  # Absolute import instead of relative

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_invalid_route():
    response = client.get("/invalid")
    assert response.status_code == 404
