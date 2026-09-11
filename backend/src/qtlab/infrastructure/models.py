from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, String, Text, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from qtlab.infrastructure.database import Base


class StudyModel(Base):
    __tablename__ = "studies"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
    )

    observation: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )


class StudyEventModel(Base):
    __tablename__ = "study_events"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    study_id: Mapped[UUID] = mapped_column(
        ForeignKey("studies.id"),
        nullable=False,
        index=True,
    )

    event_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    occurred_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )
