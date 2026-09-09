from uuid import UUID

from fastapi import APIRouter
from pydantic import BaseModel

from qtlab.infrastructure.study_repository import InMemoryStudyRepository
from qtlab.use_cases.create_study import CreateStudy, CreateStudyRequest


router = APIRouter(prefix="/studies", tags=["studies"])

repository = InMemoryStudyRepository()


class CreateStudyPayload(BaseModel):
    observation: str


class CreateStudyResponse(BaseModel):
    id: UUID


@router.post("", response_model=CreateStudyResponse)
def create_study(payload: CreateStudyPayload) -> CreateStudyResponse:
    use_case = CreateStudy(repository)

    study_id = use_case.execute(
        CreateStudyRequest(
            observation=payload.observation,
        )
    )

    return CreateStudyResponse(id=study_id)


@router.get("/{study_id}")
def get_study(study_id: UUID):
    study = repository.get(study_id)

    if study is None:
        raise HTTPException(
            status_code=404,
            detail="Study not found",
        )

    return {
        "id": study.id,
        "observation": study.observation.text,
        "status": study.status,
        "created_at": study.created_at,
        "updated_at": study.updated_at,
        "timeline": [
            {
                "type": type(event).__name__,
                "occurred_at": event.occurred_at,
            }
            for event in study.timeline
        ],
    }