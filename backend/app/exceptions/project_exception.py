from fastapi import status

from app.exceptions.base_exception import AppException


class ProjectNotFoundException(AppException):

    def __init__(self):
        super().__init__(
            message="Project not found.",
            status_code=status.HTTP_404_NOT_FOUND,
            error_code="PROJECT_NOT_FOUND",
        )


class ProjectAccessDeniedException(AppException):

    def __init__(self):
        super().__init__(
            message="You don't have permission to access this project.",
            status_code=status.HTTP_403_FORBIDDEN,
            error_code="PROJECT_ACCESS_DENIED",
        )