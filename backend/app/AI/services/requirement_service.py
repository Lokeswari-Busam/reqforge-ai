from sqlalchemy.orm import Session

from app.models.user import User
from app.models.requirement import Requirement

from app.repositories.requirement_repository import RequirementRepository
from app.repositories.project_repository import ProjectRepository
from app.repositories.document_repository import DocumentRepository

from app.schemas.requirement import (
    RequirementCreate,
    RequirementUpdate,
)

from app.enums import RequirementStatus

from app.exceptions.project_exception import (
    ProjectNotFoundException,
    ProjectAccessDeniedException,
)

from app.exceptions.document_exception import (
    DocumentNotFoundException,
)

from app.exceptions.requirement_exception import (
    RequirementNotFoundException,
)

class RequirementService:

    def __init__(self):

        self.requirement_repository = RequirementRepository()
        self.project_repository = ProjectRepository()
        self.document_repository = DocumentRepository()

    def _get_project(
        self,
        db: Session,
        project_uuid: str,
        current_user: User,
    ):

        project = self.project_repository.get_project_by_uuid(
            db,
            project_uuid,
        )

        if project is None:
            raise ProjectNotFoundException()

        if project.user_uuid != current_user.uuid:
            raise ProjectAccessDeniedException()

        return project
    
    def _get_document(
        self,
        db: Session,
        document_uuid: str,
    ):

        document = self.document_repository.get_document_by_uuid(
            db,
            document_uuid,
        )

        if document is None:
            raise DocumentNotFoundException()

        return document
    
    def _get_requirement(
        self,
        db: Session,
        requirement_uuid: str,
    ):

        requirement = self.requirement_repository.get_requirement_by_uuid(
            db,
            requirement_uuid,
        )

        if requirement is None:
            raise RequirementNotFoundException()

        return requirement
    
    def create_requirement(
        self,
        db: Session,
        project_uuid: str,
        document_uuid: str,
        requirement_data: RequirementCreate,
        current_user: User,
    ):

        project = self._get_project(
            db,
            project_uuid,
            current_user,
        )

        self._get_document(
            db,
            document_uuid,
        )

        total = len(
            self.requirement_repository.get_requirements_by_project(
                db,
                project.uuid,
            )
        )

        requirement = Requirement(

            project_uuid=project.uuid,

            document_uuid=document_uuid,

            requirement_id=f"REQ-{total + 1:03d}",

            title=requirement_data.title,

            description=requirement_data.description,

            type=requirement_data.type,

            priority=requirement_data.priority,

            status=RequirementStatus.GENERATED,
        )

        return self.requirement_repository.create_requirement(
            db,
            requirement,
        )
    
    def get_requirement(
        self,
        db: Session,
        requirement_uuid: str,
    ):

        return self._get_requirement(
            db,
            requirement_uuid,
        )
    
    def get_project_requirements(
        self,
        db: Session,
        project_uuid: str,
        current_user: User,
    ):

        self._get_project(
            db,
            project_uuid,
            current_user,
        )

        requirements = (
            self.requirement_repository.get_requirements_by_project(
                db,
                project_uuid,
            )
        )

        return {
            "requirements": requirements,
            "total": len(requirements),
        }
    
    def update_requirement(
        self,
        db: Session,
        requirement_uuid: str,
        requirement_data: RequirementUpdate,
    ):

        requirement = self._get_requirement(
            db,
            requirement_uuid,
        )

        update_data = requirement_data.model_dump(
            exclude_unset=True,
        )

        for key, value in update_data.items():
            setattr(
                requirement,
                key,
                value,
            )

        return self.requirement_repository.update_requirement(
            db,
            requirement,
        )
    
    def delete_requirement(
        self,
        db: Session,
        requirement_uuid: str,
    ):

        requirement = self._get_requirement(
            db,
            requirement_uuid,
        )

        self.requirement_repository.delete_requirement(
            db,
            requirement,
        )