from sqlalchemy.orm import Session

from app.models.project import Project
from app.enums import ProjectStatus


class ProjectRepository:

    def create_project(
        self,
        db: Session,
        project: Project,
    ) -> Project:

        db.add(project)
        db.commit()
        db.refresh(project)

        return project

    def get_project_by_uuid(
        self,
        db: Session,
        project_uuid: str,
    ) -> Project | None:

        return (
            db.query(Project)
            .filter(Project.uuid == project_uuid)
            .first()
        )
    
    def get_active_projects_by_user(
        self,
        db: Session,
        user_uuid: str,
    ) -> list[Project]:

        return (
            db.query(Project)
            .filter(
                Project.user_uuid == user_uuid,
                Project.status == ProjectStatus.ACTIVE,
            )
            .order_by(Project.created_at.desc())
            .all()
        )

    def update_project(
        self,
        db: Session,
        project: Project,
    ) -> Project:

        db.commit()
        db.refresh(project)

        return project

    def archive_project(
        self,
        db: Session,
        project: Project,
    ) -> Project:

        project.status = ProjectStatus.ARCHIVED

        db.commit()
        db.refresh(project)

        return project