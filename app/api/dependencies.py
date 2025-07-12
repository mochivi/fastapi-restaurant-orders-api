from typing import Annotated, TypeAlias

from fastapi import Depends

from app.services import (
    user_service,
    restaurant_service,
    order_service,
    menu_item_service
)

UserServiceDep: TypeAlias = Annotated[user_service.UserService, Depends()]
RestaurantServiceDep: TypeAlias = Annotated[restaurant_service.RestaurantService, Depends()]
OrderServiceDep: TypeAlias = Annotated[order_service.OrderService, Depends()]
MenuItemServiceDep: TypeAlias = Annotated[menu_item_service.MenuItemService, Depends()]