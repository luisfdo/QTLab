from fastapi.testclient import TestClient

from qtlab.api.main import app
from qtlab.api.studies import get_session
from qtlab.domain.study.entities import Study

from backend.src.qtlab.infrastructure.sqlite_study_repository import SQLiteStudyRepository

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


def test_study_survives_persistence():
    session = get_session()
    repository = SQLiteStudyRepository(session)
    study = Study.create(
        observation="Broad ETFs often recover after large daily declines."
    )

    repository.save(study)

    restored = repository.get(study.id)

    assert restored is not None
    assert restored.id == study.id
    assert restored.observation.text == study.observation.text
    assert restored.status == study.status