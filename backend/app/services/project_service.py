from sqlalchemy.orm import Session

from app.models.project import Project
from app.models.user import User
from app.repositories.project_repository import ProjectRepository
from app.schemas.project import (
    ProjectCreateRequest,
    ProjectUpdateRequest,
)
from app.exceptions.project_exception import (
    ProjectNotFoundException,
    ProjectAccessDeniedException,
)

class ProjectService:

    def __init__(self):
        self.project_repository = ProjectRepository()

    def create_project(
        self,
        db: Session,
        request: ProjectCreateRequest,
        current_user: User,
    ) -> Project:

        project = Project(
            user_uuid=current_user.uuid,
            name=request.name,
            description=request.description,
        )

        return self.project_repository.create_project(
            db,
            project,
        )
    
    def get_my_projects(
        self,
        db: Session,
        current_user: User,
    ) -> list[Project]:

        return self.project_repository.get_active_projects_by_user(
            db,
            current_user.uuid,
        )
    
    def _get_user_project(
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
    
    def get_project(
        self,
        db: Session,
        project_uuid: str,
        current_user: User,
    ) -> Project:

        return self._get_user_project(
            db,
            project_uuid,
            current_user,
        )
    
    def update_project(
        self,
        db: Session,
        project_uuid: str,
        request: ProjectUpdateRequest,
        current_user: User,
    ) -> Project:

        project = self._get_user_project(
            db,
            project_uuid,
            current_user,
        )

        if request.name is not None:
            project.name = request.name

        if request.description is not None:
            project.description = request.description

        if request.status is not None:
            project.status = request.status

        return self.project_repository.update_project(
            db,
            project,
        )
    
    def archive_project(
        self,
        db: Session,
        project_uuid: str,
        current_user: User,
    ) -> Project:

        project = self._get_user_project(
            db,
            project_uuid,
            current_user,
        )

        return self.project_repository.archive_project(
            db,
            project,
        )