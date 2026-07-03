from fastapi import status

from app.exceptions.base_exception import AppException


class InvalidCredentialsException(AppException):

    def __init__(self):
        super().__init__(
            message="Invalid email or password.",
            status_code=status.HTTP_401_UNAUTHORIZED,
            error_code="INVALID_CREDENTIALS",
        )

class InvalidTokenException(AppException):
    def __init__(self):
        super().__init__(
            message="Invalid authentication credentials.",
            status_code=status.HTTP_401_UNAUTHORIZED,
            error_code="INVALID_TOKEN",
        )