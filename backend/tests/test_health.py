from fastapi.testclient import TestClient

from qtlab.api.main import app

client = TestClient(app)


def test_application_starts():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "running"