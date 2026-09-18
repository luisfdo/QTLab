from collections.abc import Generator
from uuid import UUID

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

# from qtlab.infrastructure.study_repository import InMemoryStudyRepository
from qtlab.api.schemas import StudyResponse
from qtlab.infrastructure.database import SessionLocal
from qtlab.infrastructure.sqlite_study_repository import SQLiteStudyRepository
from qtlab.api.mappers import study_to_response
from qtlab.use_cases.create_study import CreateStudy, CreateStudyRequest

router = APIRouter(prefix="/studies", tags=["studies"])

# repository = InMemoryStudyRepository()


class CreateStudyPayload(BaseModel):
    observation: str


class CreateStudyResponse(BaseModel):
    id: UUID


def get_session() -> Generator:
    session = SessionLocal()

    try:
        yield session
    finally:
        session.close()


# @router.post("", response_model=CreateStudyResponse)
# def create_study(payload: CreateStudyPayload) -> CreateStudyResponse:
#     use_case = CreateStudy(repository)
#
#     study_id = use_case.execute(
#         CreateStudyRequest(
#             observation=payload.observation,
#         )
#     )
#
#     return CreateStudyResponse(id=study_id)


@router.post("")
def create_study(payload: CreateStudyPayload, session: Session = Depends(get_session),):
    repository = SQLiteStudyRepository(session)

    use_case = CreateStudy(repository)

    study_id = use_case.execute(
        CreateStudyRequest(
            observation=payload.observation,
        )
    )

    return CreateStudyResponse(id=study_id)


@router.get("/{study_id}")
def get_study(study_id: UUID, session: Session = Depends(get_session),):
    repository = SQLiteStudyRepository(session)
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


@router.get("", response_model=list[StudyResponse])
def list_studies(
    session: Session = Depends(get_session),
) -> list[StudyResponse]:
    repository = SQLiteStudyRepository(session)

    studies = repository.list()

    return [
        study_to_response(study)
        for study in studies
    ]
