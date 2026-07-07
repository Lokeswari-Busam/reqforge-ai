import os
import re
from datetime import datetime

from fastapi import UploadFile
from sqlalchemy.orm import Session


from app.models.document import Document
from app.models.user import User
from app.repositories.document_repository import DocumentRepository
from app.repositories.project_repository import ProjectRepository
from app.exceptions.project_exception import (
    ProjectNotFoundException,
    ProjectAccessDeniedException,
)
from app.models.project import Project
from app.exceptions.document_exception import (
    DocumentNotFoundException,
    UnsupportedFileTypeException,
    FileSizeExceededException,
)

class DocumentService:

    def __init__(self):
        self.document_repository = DocumentRepository()
        self.project_repository = ProjectRepository()
    
    ALLOWED_EXTENSIONS = {
        ".pdf",
        ".doc",
        ".docx",
        ".txt",
    }

    MAX_FILE_SIZE = 10 * 1024 * 1024

    UPLOAD_DIRECTORY = "uploads"

    def __init__(self):
        os.makedirs(
            self.UPLOAD_DIRECTORY,
            exist_ok=True,
        )

        self.document_repository = DocumentRepository()
        self.project_repository = ProjectRepository()

    def _get_project(
        self,
        db: Session,
        project_uuid: str,
        current_user: User,
    ) -> Project:

        project = self.project_repository.get_project_by_uuid(
            db,
            project_uuid,
        )

        if project is None:
            raise ProjectNotFoundException()

        if project.user_uuid != current_user.uuid:
            raise ProjectAccessDeniedException()

        return project
    
    def _validate_extension(
        self,
        filename: str,
    ):

        extension = os.path.splitext(filename)[1].lower()

        if extension not in self.ALLOWED_EXTENSIONS:
            raise UnsupportedFileTypeException()

        return extension
    
    def _validate_file_size(
        self,
        file_size: int,
    ):

        if file_size > self.MAX_FILE_SIZE:
            raise FileSizeExceededException()
        
    
    def _generate_filename(
        self,
        document_type: str,
        project_name: str,
        extension: str,
    ) -> str:

        safe_project_name = re.sub(
            r"[^a-zA-Z0-9]+",
            "_",
            project_name.strip().lower(),
        ).strip("_")

        current_datetime = datetime.now().strftime(
            "%Y-%m-%d_%H-%M-%S"
        )

        return (
            f"{document_type}_"
            f"{safe_project_name}_"
            f"{current_datetime}"
            f"{extension}"
        )
    
    def upload_document(
        self,
        db: Session,
        project_uuid: str,
        file: UploadFile,
        current_user: User,
    ) -> Document:

        project = self._get_project(
            db,
            project_uuid,
            current_user,
        )

        extension = self._validate_extension(
            file.filename,
        )

        file_content = file.file.read()
        file.file.seek(0)
        if not file_content:
            raise UnsupportedFileTypeException()

        self._validate_file_size(
            len(file_content),
        )

        stored_filename = self._generate_filename(
            document_type="requirements",
            project_name=project.name,
            extension=extension,
        )

        storage_path = os.path.join(
            self.UPLOAD_DIRECTORY,
            stored_filename,
        )

        with open(
            storage_path,
            "wb",
        ) as buffer:
            buffer.write(file_content)

        document = Document(
            project_uuid=project.uuid,
            original_filename=file.filename,
            stored_filename=stored_filename,
            file_extension=extension,
            mime_type=file.content_type,
            file_size=len(file_content),
            storage_path=storage_path,
        )

        return self.document_repository.create_document(
            db,
            document,
        )
    
    def get_documents_by_project(
        self,
        db: Session,
        project_uuid: str,
        current_user: User,
    ) -> list[Document]:

        self._get_project(
            db,
            project_uuid,
            current_user,
        )

        return self.document_repository.get_documents_by_project(
            db,
            project_uuid,
        )
    
    def get_document(
        self,
        db: Session,
        document_uuid: str,
        current_user: User,
    ) -> Document:

        document = self.document_repository.get_document_by_uuid(
            db,
            document_uuid,
        )

        if document is None:
            raise DocumentNotFoundException()

        self._get_project(
            db,
            document.project_uuid,
            current_user,
        )

        return document
    
    def delete_document(
        self,
        db: Session,
        document_uuid: str,
        current_user: User,
    ) -> None:

        document = self.document_repository.get_document_by_uuid(
            db,
            document_uuid,
        )

        if document is None:
            raise DocumentNotFoundException()

        self._get_project(
            db,
            document.project_uuid,
            current_user,
        )

        if os.path.exists(document.storage_path):
            os.remove(document.storage_path)

        self.document_repository.delete_document(
            db,
            document,
        )
