from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:

    def create_user(self, db: Session, user: User) -> User:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def get_by_email(self, db: Session, email: str) -> User | None:
        return (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

    def get_by_uuid(self, db: Session, user_uuid: str) -> User | None:
        return (
            db.query(User)
            .filter(User.uuid == user_uuid)
            .first()
        )