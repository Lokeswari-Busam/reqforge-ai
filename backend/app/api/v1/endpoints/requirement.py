from fastapi import (
    APIRouter,
    Depends,
    status,
)

from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.database.dependencies import get_db

from app.models.user import User

from app.schemas.requirement import (
    RequirementCreate,
    RequirementUpdate,
    RequirementResponse,
    RequirementListResponse,
)

from app.AI.services.requirement_service import RequirementService 

router = APIRouter(
    prefix="/requirements",
    tags=["Requirements"],
)

requirement_service = RequirementService()

@router.post(
    "/projects/{project_uuid}/documents/{document_uuid}",
    response_model=RequirementResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_requirement(
    project_uuid: str,
    document_uuid: str,
    requirement_data: RequirementCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return requirement_service.create_requirement(
        db=db,
        project_uuid=project_uuid,
        document_uuid=document_uuid,
        requirement_data=requirement_data,
        current_user=current_user,
    )

@router.get(
    "/{requirement_uuid}",
    response_model=RequirementResponse,
)
def get_requirement(
    requirement_uuid: str,
    db: Session = Depends(get_db),
):

    return requirement_service.get_requirement(
        db=db,
        requirement_uuid=requirement_uuid,
    )

@router.get(
    "/projects/{project_uuid}",
    response_model=RequirementListResponse,
)
def get_project_requirements(
    project_uuid: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return requirement_service.get_project_requirements(
        db=db,
        project_uuid=project_uuid,
        current_user=current_user,
    )

@router.patch(
    "/{requirement_uuid}",
    response_model=RequirementResponse,
)
def update_requirement(
    requirement_uuid: str,
    requirement_data: RequirementUpdate,
    db: Session = Depends(get_db),
):

    return requirement_service.update_requirement(
        db=db,
        requirement_uuid=requirement_uuid,
        requirement_data=requirement_data,
    )

@router.delete(
    "/{requirement_uuid}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_requirement(
    requirement_uuid: str,
    db: Session = Depends(get_db),
):

    requirement_service.delete_requirement(
        db=db,
        requirement_uuid=requirement_uuid,
    )