from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.core.config import settings
from app.database.dependencies import get_db
from app.repositories.user_repository import UserRepository
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.exceptions.auth_exception import InvalidTokenException

security = HTTPBearer(auto_error=False)


user_repository = UserRepository()

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db),
):
    if credentials is None:
        raise InvalidTokenException()

    try:
        payload = jwt.decode(
            credentials.credentials,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )

        email = payload.get("sub")

        if email is None:
            raise InvalidTokenException()

    except JWTError:
        raise InvalidTokenException()

    user = user_repository.get_by_email(
        db,
        email,
    )

    if user is None:
        raise InvalidTokenException()

    return user