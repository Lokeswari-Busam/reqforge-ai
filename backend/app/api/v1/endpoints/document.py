from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.database.dependencies import get_db
from app.models.user import User
from app.schemas.document import (
    DocumentResponse,
    
)
from app.services.document_service import DocumentService

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)

document_service = DocumentService()

# Upload Endpoint
@router.post(
    "/projects/{project_uuid}",
    response_model=DocumentResponse,
)
def upload_document(
    project_uuid: str,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return document_service.upload_document(
        db=db,
        project_uuid=project_uuid,
        file=file,
        current_user=current_user,
    )

# List Documents
@router.get(
    "/projects/{project_uuid}",
    response_model=list[DocumentResponse],
)
def get_documents(
    project_uuid: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return document_service.get_documents_by_project(
        db=db,
        project_uuid=project_uuid,
        current_user=current_user,
    )

# Get Document by UUID
@router.get(
    "/{document_uuid}",
    response_model=DocumentResponse,
)
def get_document(
    document_uuid: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return document_service.get_document(
        db=db,
        document_uuid=document_uuid,
        current_user=current_user,
    )

# Delete Document
@router.delete(
    "/{document_uuid}",
    status_code=204,
)
def delete_document(
    document_uuid: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    document_service.delete_document(
        db=db,
        document_uuid=document_uuid,
        current_user=current_user,
    )