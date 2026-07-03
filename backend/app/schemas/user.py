from pydantic import BaseModel, EmailStr, Field


class UserRegisterRequest(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=100)
    last_name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=100)


class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    uuid: str
    first_name: str
    last_name: str
    email: EmailStr
    is_active: bool
    is_verified: bool

    model_config = {
        "from_attributes": True
    }