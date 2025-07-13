from datetime import timedelta, datetime

from pydantic import BaseModel, EmailStr

from app.models.enums import UserRole

class UserLogin(BaseModel):
    email: EmailStr
    password: str

# The information encoded into the token
class TokenData(BaseModel):
    sub: EmailStr
    role: UserRole
    exp: datetime

# We reply back with the token + expiry details
class TokenResponse(BaseModel):
    access_token: str
    expires_in: int