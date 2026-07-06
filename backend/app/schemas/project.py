from pydantic import BaseModel, Field

from app.enums import ProjectStatus

class ProjectCreateRequest(BaseModel):
    name: str = Field(
        min_length=3,
        max_length=200,
    )

    description: str | None = Field(
        default=None,
        max_length=1000,
    )
class ProjectUpdateRequest(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=3,
        max_length=200,
    )

    description: str | None = Field(
        default=None,
        max_length=1000,
    )

    status: ProjectStatus | None = None

from datetime import datetime


class ProjectResponse(BaseModel):
    uuid: str
    user_uuid: str
    name: str
    description: str | None
    status: ProjectStatus

    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }