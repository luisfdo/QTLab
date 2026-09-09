from datetime import timezone

import pytest

from qtlab.domain.study.entities import Study
from qtlab.domain.study.status import StudyStatus


def test_new_study_is_under_investigation():
    study = Study.create(
        observation="Broad ETFs often recover after large daily declines."
    )

    assert study.status == StudyStatus.UNDER_INVESTIGATION


def test_new_study_has_an_observation():
    text = "Broad ETFs often recover after large daily declines."

    study = Study.create(observation=text)

    assert study.observation.text == text


def test_new_study_has_unique_id():
    study = Study.create(observation="Something interesting.")

    assert study.id is not None


def test_new_study_uses_utc_timestamps():
    study = Study.create(observation="Something interesting.")

    assert study.created_at.tzinfo == timezone.utc
    assert study.updated_at.tzinfo == timezone.utc


def test_new_study_records_creation_event():
    study = Study.create(observation="Something interesting.")

    assert len(study.timeline) == 1
    assert study.timeline[0].study_id == study.id


def test_empty_observation_is_rejected():
    with pytest.raises(ValueError, match="Observation cannot be empty"):
        Study.create(observation="   ")
