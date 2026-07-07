from datetime import datetime
from pydantic import BaseModel, ConfigDict
from app.enums import DocumentStatus

class DocumentResponse(BaseModel):

    uuid: str
    project_uuid: str

    original_filename: str
    stored_filename: str

    file_extension: str
    mime_type: str
    file_size: int

    storage_path: str

    status: DocumentStatus

    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )