from datetime import datetime
import uuid

from sqlalchemy import (
    String,
    Text,
    DateTime,
    Enum,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from app.database.base import Base
from app.enums import (
    RequirementPriority,
    RequirementType,
    RequirementStatus,
)


class Requirement(Base):

    __tablename__ = "requirements"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    uuid: Mapped[str] = mapped_column(
        String(36),
        default=lambda: str(uuid.uuid4()),
        unique=True,
        index=True,
    )

    project_uuid: Mapped[str] = mapped_column(
        String(36),
        index=True,
    )

    document_uuid: Mapped[str] = mapped_column(
        String(36),
        index=True,
    )

    requirement_id: Mapped[str] = mapped_column(
        String(20),
        unique=True,
    )

    title: Mapped[str] = mapped_column(
        String(255),
    )

    description: Mapped[str] = mapped_column(
        Text,
    )

    type: Mapped[RequirementType] = mapped_column(
        Enum(RequirementType),
    )

    priority: Mapped[RequirementPriority] = mapped_column(
        Enum(RequirementPriority),
    )

    status: Mapped[RequirementStatus] = mapped_column(
        Enum(RequirementStatus),
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )