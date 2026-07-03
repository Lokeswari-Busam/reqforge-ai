from fastapi import status

from app.exceptions.base_exception import AppException


class UserAlreadyExistsException(AppException):

    def __init__(self):
        super().__init__(
            message="Email already registered.",
            status_code=status.HTTP_409_CONFLICT,
            error_code="USER_ALREADY_EXISTS",
        )