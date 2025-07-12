from pydantic import BaseModel, EmailStr, Field

from app.models.enums import UserRole

class User(BaseModel):
    id: int = Field(gt=0)
    password_hash: str = Field(alias="password")
    email: EmailStr
    name: str = Field(max_length=255)
    role: UserRole