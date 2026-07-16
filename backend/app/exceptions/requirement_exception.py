from app.exceptions.base_exception import AppException


class RequirementNotFoundException(AppException):

    def __init__(self):

        super().__init__(
            status_code=404,
            message="Requirement not found.",
            error_code="REQUIREMENT_NOT_FOUND",
        )


class RequirementAccessDeniedException(AppException):

    def __init__(self):

        super().__init__(
            status_code=403,
            message="You do not have permission to access this requirement.",
            error_code="REQUIREMENT_ACCESS_DENIED",
        )


class RequirementAlreadyExistsException(AppException):

    def __init__(self):

        super().__init__(
            status_code=409,
            message="Requirement already exists.",
            error_code="REQUIREMENT_ALREADY_EXISTS",
        )