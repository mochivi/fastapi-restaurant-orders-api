from typing import Annotated, Any

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.models.schemas.user_login import TokenResponse, UserLogin
from app.api.dependencies import AuthServiceDep
from app.services import auth_service

router = APIRouter(prefix="/login", tags=["Login"])

@router.post("/token")
def login_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    auth_service: AuthServiceDep
):
    user_login = UserLogin(email=form_data.username, password=form_data.password) 
    return auth_service.authenticate(user_login)