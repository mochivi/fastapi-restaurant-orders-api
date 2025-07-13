from typing import Annotated, TypeAlias

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from app.core.security import verify_access_token
from app.models.domain.user import User
from app.models.schemas.user_login import TokenData
from app.repositories.dependencies import MockUserRepositoryDep
from app.services import (
    auth_service,
    user_service,
    restaurant_service,
    order_service,
    restaurant_order_service,
    menu_item_service
)

UserServiceDep: TypeAlias = Annotated[user_service.UserService, Depends()]
RestaurantServiceDep: TypeAlias = Annotated[restaurant_service.RestaurantService, Depends()]
OrderServiceDep: TypeAlias = Annotated[order_service.OrderService, Depends()]
RestaurantOrderServiceDep: TypeAlias = Annotated[restaurant_order_service.RestaurantOrderService, Depends()]
MenuItemServiceDep: TypeAlias = Annotated[menu_item_service.MenuItemService, Depends()]
AuthServiceDep: TypeAlias = Annotated[auth_service.AuthService, Depends()]

oauth2_scheme: OAuth2PasswordBearer = OAuth2PasswordBearer(tokenUrl="/api/v1/login/token")

# Receive the user's access token, validate user
def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], user_repository: MockUserRepositoryDep) -> User:
    token_data: TokenData = verify_access_token(token)    
    user: User = user_repository.get_by_email(token_data.sub)
    return user

CurrentUserDep: TypeAlias = Annotated[User, Depends(get_current_user)]