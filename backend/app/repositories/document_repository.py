from sqlalchemy.orm import Session

from app.models.document import Document


class DocumentRepository:

    def create_document(
        self,
        db: Session,
        document: Document,
    ) -> Document:

        db.add(document)
        db.commit()
        db.refresh(document)

        return document

    def get_document_by_uuid(
        self,
        db: Session,
        document_uuid: str,
    ) -> Document | None:

        return (
            db.query(Document)
            .filter(Document.uuid == document_uuid)
            .first()
        )

    def get_documents_by_project(
        self,
        db: Session,
        project_uuid: str,
    ) -> list[Document]:

        return (
            db.query(Document)
            .filter(Document.project_uuid == project_uuid)
            .order_by(Document.created_at.desc())
            .all()
        )

    def update_document(
        self,
        db: Session,
        document: Document,
    ) -> Document:

        db.commit()
        db.refresh(document)

        return document

    def delete_document(
        self,
        db: Session,
        document: Document,
    ) -> None:

        db.delete(document)
        db.commit()