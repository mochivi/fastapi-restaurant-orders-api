from pydantic import BaseModel, EmailStr, ConfigDict, Field

from app.models.enums import UserRole

class UserBase(BaseModel):
    email: EmailStr
    name: str = Field(max_length=255)
    role: UserRole

class UserCreate(UserBase):
    password: str
    
class UserUpdate(BaseModel):
    id: int
    password: str | None = None
    email: EmailStr | None = None
    name: str | None = Field(default=None, max_length=255)
    role: UserRole | None = None

class UserResponse(UserBase):
    id: int = Field(gt=0)

    model_config = ConfigDict(from_attributes=True)