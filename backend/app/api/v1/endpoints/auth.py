from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.user import (
    UserLoginRequest,
    UserRegisterRequest,
    UserResponse,
)
from app.services.auth_service import AuthService
from app.core.security import get_current_user
from app.exceptions.auth_exception import InvalidCredentialsException

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

auth_service = AuthService()
@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    request: UserRegisterRequest,
    db: Session = Depends(get_db),
):
    return auth_service.register_user(
        db,
        request,
    )
    
@router.post("/login")
def login(
    request: UserLoginRequest,
    db: Session = Depends(get_db),
):

        token = auth_service.login_user(
            db,
            request,
        )

        return {
            "access_token": token,
            "token_type": "bearer",
        }

    
@router.get(
    "/me",
    response_model=UserResponse,
)
def get_profile(
    current_user=Depends(get_current_user),
):
    return current_user