from typing import Any
from datetime import datetime, timezone

import jwt
from passlib.context import CryptContext
from fastapi import HTTPException, status
from pydantic import ValidationError

from app.core.config import settings
from app.models.domain.user import User
from app.models.enums import UserRole
from app.models.schemas.user_login import TokenData, TokenResponse
from app.services.exceptions.interfaces import BadRequestException, UnauthorizedException

_pwd_context = CryptContext('bcrypt')

def hash_password(password: str) -> str:
    return _pwd_context.hash(password, "bcrypt")

def verify_password(password: str, password_hash: str) -> bool:
    return _pwd_context.verify(password, password_hash, "bcrypt")

def create_access_token(data: dict) -> TokenResponse:    
    encoded_jwt = jwt.encode(
        payload=data,
        key=settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM
    )

    return TokenResponse(
        access_token=encoded_jwt,
        expires_in=settings.JWT_EXPIRES_IN.seconds
    )

def verify_access_token(access_token: str) -> TokenData:
    try:
        claims = jwt.decode(access_token, key=settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
    except jwt.InvalidTokenError:
        raise UnauthorizedException("invalid access token")
    except:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="something went wrong")

    try:
        token_data: TokenData = TokenData.model_validate(claims)
    except ValidationError:
        raise BadRequestException("invalid token")
    except Exception:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="something went wrong")

    return token_data