from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.database.dependencies import get_db
from app.models.user import User
from app.schemas.project import (
    ProjectCreateRequest,
    ProjectUpdateRequest,
    ProjectResponse,
)
from app.services.project_service import ProjectService

router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
)

project_service = ProjectService()

# Create Project
@router.post(
    "",
    response_model=ProjectResponse,
    status_code=201,
)
def create_project(
    request: ProjectCreateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return project_service.create_project(
        db,
        request,
        current_user,
    )

# Get My Projects
@router.get(
    "",
    response_model=list[ProjectResponse],
)
def get_projects(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return project_service.get_my_projects(
        db,
        current_user,
    )

# Get Project By UUID
@router.get(
    "/{project_uuid}",
    response_model=ProjectResponse,
)
def get_project(
    project_uuid: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return project_service.get_project(
        db,
        project_uuid,
        current_user,
    )

# Update Project
@router.put(
    "/{project_uuid}",
    response_model=ProjectResponse,
)
def update_project(
    project_uuid: str,
    request: ProjectUpdateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return project_service.update_project(
        db,
        project_uuid,
        request,
        current_user,
    )

# Archive Project
# Although this is a soft delete, we'll keep the REST API intuitive by using DELETE.
@router.delete(
    "/{project_uuid}",
    response_model=ProjectResponse,
)
def archive_project(
    project_uuid: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return project_service.archive_project(
        db,
        project_uuid,
        current_user,
    )