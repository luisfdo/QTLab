from fastapi.testclient import TestClient

from qtlab.api.main import app


client = TestClient(app)


def test_create_and_retrieve_study():
    response = client.post(
        "/studies",
        json={
            "observation": (
                "Broad ETFs often recover after large daily declines."
            )
        },
    )

    assert response.status_code == 200

    study_id = response.json()["id"]

    response = client.get(f"/studies/{study_id}")

    assert response.status_code == 200

    study = response.json()

    assert study["id"] == study_id
    assert study["observation"] == (
        "Broad ETFs often recover after large daily declines."
    )
    assert study["status"] == "under_investigation"
    assert len(study["timeline"]) == 1
