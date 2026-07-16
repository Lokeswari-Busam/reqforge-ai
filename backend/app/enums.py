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
    GENERATED = "GENERATED"
    REVIEWED = "REVIEWED"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"


class DocumentType(str, Enum):
    BRD = "BRD"
    SRS = "SRS"
    USER_STORY = "USER_STORY"
    API_SPEC = "API_SPEC"

class DocumentStatus(str, Enum):
    UPLOADED = "UPLOADED"
    PROCESSING = "PROCESSING"
    PROCESSED = "PROCESSED"
    FAILED = "FAILED"

class RequirementPriority(str, Enum):

    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class RequirementType(str, Enum):

    FUNCTIONAL = "FUNCTIONAL"
    NON_FUNCTIONAL = "NON_FUNCTIONAL"
    BUSINESS = "BUSINESS"
    TECHNICAL = "TECHNICAL"