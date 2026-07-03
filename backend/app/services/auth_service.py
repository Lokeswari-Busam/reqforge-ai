from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import (
    UserLoginRequest,
    UserRegisterRequest,
)
from app.utils.security import (
    create_access_token,
    hash_password,
    verify_password,
)


class AuthService:

    def __init__(self):
        self.user_repository = UserRepository()

    def register_user(
        self,
        db: Session,
        request: UserRegisterRequest,
    ) -> User:

        existing_user = self.user_repository.get_by_email(
            db,
            request.email,
        )

        if existing_user:
            raise ValueError(
                "Email already registered."
            )

        user = User(
            first_name=request.first_name,
            last_name=request.last_name,
            email=request.email,
            password_hash=hash_password(
                request.password
            ),
        )

        return self.user_repository.create_user(
            db,
            user,
        )

    def login_user(
        self,
        db: Session,
        request: UserLoginRequest,
    ) -> str:

        user = self.user_repository.get_by_email(
            db,
            request.email,
        )

        if not user:
            raise ValueError(
                "Invalid email or password."
            )

        if not verify_password(
            request.password,
            user.password_hash,
        ):
            raise ValueError(
                "Invalid email or password."
            )

        return create_access_token(
            {
                "sub": user.email,
                "uuid": user.uuid,
            }
        )