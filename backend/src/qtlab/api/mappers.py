from qtlab.api.schemas import StudyResponse, TimelineEventResponse
from qtlab.domain.study.entities import Study


def study_to_response(study: Study) -> StudyResponse:
    return StudyResponse(
        id=study.id,
        observation=study.observation.text,
        status=study.status.value,
        created_at=study.created_at,
        updated_at=study.updated_at,
        timeline=[
            TimelineEventResponse(
                type=type(event).__name__,
                occurred_at=event.occurred_at,
            )
            for event in study.timeline
        ],
    )
