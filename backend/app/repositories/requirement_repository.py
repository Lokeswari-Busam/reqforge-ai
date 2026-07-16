from sqlalchemy.orm import Session

from app.models.requirement import Requirement


class RequirementRepository:

    def create_requirement(
        self,
        db: Session,
        requirement: Requirement,
    ) -> Requirement:

        db.add(requirement)
        db.commit()
        db.refresh(requirement)

        return requirement
    

    def get_requirement_by_uuid(
        self,
        db: Session,
        requirement_uuid: str,
    ) -> Requirement | None:

        return (
            db.query(Requirement)
            .filter(
                Requirement.uuid == requirement_uuid,
            )
            .first()
        )
    
    def get_requirements_by_project(
        self,
        db: Session,
        project_uuid: str,
    ) -> list[Requirement]:

        return (
            db.query(Requirement)
            .filter(
                Requirement.project_uuid == project_uuid,
            )
            .order_by(
                Requirement.created_at.desc(),
            )
            .all()
        )
    
    def get_requirements_by_document(
        self,
        db: Session,
        document_uuid: str,
    ) -> list[Requirement]:

        return (
            db.query(Requirement)
            .filter(
                Requirement.document_uuid == document_uuid,
            )
            .order_by(
                Requirement.created_at.desc(),
            )
            .all()
        )
    
    def update_requirement(
        self,
        db: Session,
        requirement: Requirement,
    ) -> Requirement:

        db.commit()
        db.refresh(requirement)

        return requirement
    
    def delete_requirement(
        self,
        db: Session,
        requirement: Requirement,
    ):

        db.delete(requirement)
        db.commit()