from datetime import datetime, timezone

from app.core.security import create_access_token, verify_password
from app.models.schemas.user_login import TokenData, TokenResponse, UserLogin
from app.repositories.dependencies import MockUserRepositoryDep
from app.services.exceptions.interfaces import UnauthorizedException
from app.core.config import settings

class AuthService:
    def __init__(self, user_repository: MockUserRepositoryDep) -> None:
        self.user_repository = user_repository

    def authenticate(self, user_login: UserLogin) -> TokenResponse:
        user = self.user_repository.get_by_email(user_login.email)

        if not verify_password(user_login.password, user.password_hash):
            raise UnauthorizedException()


        token_data = TokenData(
            sub=user.email, 
            role=user.role,
            exp=datetime.now(timezone.utc) + settings.JWT_EXPIRES_IN
        )

        # Create access token for user
        return create_access_token(token_data.model_dump())