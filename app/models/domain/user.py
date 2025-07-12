from typing import Generator

from pydantic import BaseModel, EmailStr, Field

from app.models.enums import UserRole

def _id_generator():
    i = 1
    while True:
        yield i
        i += 1
_id_gen = _id_generator()

def generate_next() -> int:
    return next(_id_gen)

class User(BaseModel):
    id: int = Field(default_factory=generate_next, gt=0)
    password_hash: str = Field(alias="password")
    email: EmailStr
    name: str = Field(max_length=255)
    role: UserRole