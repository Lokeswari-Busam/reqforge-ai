from enum import Enum


class ProjectStatus(str, Enum):
    DRAFT = "DRAFT"
    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"



class UserRole(str, Enum):
    ADMIN = "ADMIN"
    BUSINESS_ANALYST = "BUSINESS_ANALYST"
    REVIEWER = "REVIEWER"


class UserStatus(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class RequirementStatus(str, Enum):
    DRAFT = "DRAFT"
    GENERATED = "GENERATED"
    APPROVED = "APPROVED"


class DocumentType(str, Enum):
    BRD = "BRD"
    SRS = "SRS"
    USER_STORY = "USER_STORY"
    API_SPEC = "API_SPEC"