from fastapi import status

from app.exceptions.base_exception import AppException


class DocumentNotFoundException(AppException):

    def __init__(self):
        super().__init__(
            message="Document not found.",
            status_code=status.HTTP_404_NOT_FOUND,
            error_code="DOCUMENT_NOT_FOUND",
        )


class DocumentAccessDeniedException(AppException):

    def __init__(self):
        super().__init__(
            message="You don't have permission to access this document.",
            status_code=status.HTTP_403_FORBIDDEN,
            error_code="DOCUMENT_ACCESS_DENIED",
        )


class UnsupportedFileTypeException(AppException):

    def __init__(self):
        super().__init__(
            message="Unsupported file type.",
            status_code=status.HTTP_400_BAD_REQUEST,
            error_code="UNSUPPORTED_FILE_TYPE",
        )


class FileSizeExceededException(AppException):

    def __init__(self):
        super().__init__(
            message="File size exceeds the allowed limit.",
            status_code=status.HTTP_400_BAD_REQUEST,
            error_code="FILE_SIZE_EXCEEDED",
        )