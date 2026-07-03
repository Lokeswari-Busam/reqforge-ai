from fastapi import status


class AppException(Exception):

    def __init__(
        self,
        message: str,
        status_code: int = status.HTTP_400_BAD_REQUEST,
        error_code: str = "APPLICATION_ERROR",
    ):
        super().__init__(message)
        
        self.message = message
        self.status_code = status_code
        self.error_code = error_code