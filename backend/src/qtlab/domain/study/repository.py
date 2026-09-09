from abc import ABC, abstractmethod
from uuid import UUID

from .entities import Study


class StudyRepository(ABC):
    @abstractmethod
    def save(self, study: Study) -> None:
        ...

    @abstractmethod
    def get(self, study_id: UUID) -> Study | None:
        ...

    @abstractmethod
    def list(self) -> list[Study]:
        ...