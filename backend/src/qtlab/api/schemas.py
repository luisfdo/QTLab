from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class CreateStudyRequest(BaseModel):
    observation: str


class CreateStudyResponse(BaseModel):
    id: UUID


class TimelineEventResponse(BaseModel):
    type: str
    occurred_at: datetime


class StudyResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    observation: str
    research_question: str | None
    status: str
    created_at: datetime
    updated_at: datetime
    timeline: list[TimelineEventResponse]


class DefineResearchQuestionRequest(BaseModel):
    text: str
