from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.enums import (
    RequirementPriority,
    RequirementStatus,
    RequirementType,
)


class RequirementCreate(BaseModel):

    title: str

    description: str

    type: RequirementType

    priority: RequirementPriority


class RequirementUpdate(BaseModel):

    title: str | None = None

    description: str | None = None

    type: RequirementType | None = None

    priority: RequirementPriority | None = None

    status: RequirementStatus | None = None


class RequirementResponse(BaseModel):

    uuid: str

    project_uuid: str

    document_uuid: str

    requirement_id: str

    title: str

    description: str

    type: RequirementType

    priority: RequirementPriority

    status: RequirementStatus

    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )


class RequirementListResponse(BaseModel):

    requirements: list[RequirementResponse]

    total: int