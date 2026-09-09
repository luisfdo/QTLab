from uuid import UUID

from qtlab.domain.study.entities import Study


class InMemoryStudyRepository:
    def __init__(self) -> None:
        self._studies: dict[UUID, Study] = {}

    def save(self, study: Study) -> None:
        self._studies[study.id] = study

    def get(self, study_id: UUID) -> Study | None:
        return self._studies.get(study_id)

    def list(self) -> list[Study]:
        return list(self._studies.values())
