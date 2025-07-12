from typing import Annotated, TypeAlias

from fastapi import Depends

from app.repositories.implementations import (
    mock_user_repository,
    mock_restaurant_repository,
    mock_order_repository,
    mock_menu_item_repository
)

MockUserRepositoryDep: TypeAlias = Annotated[mock_user_repository.MockUserRepository, Depends()]
MockRestaurantRepositoryDep: TypeAlias = Annotated[mock_restaurant_repository.MockRestaurantRepository, Depends()]
MockOrderRepositoryDep: TypeAlias = Annotated[mock_order_repository.MockOrderRepository, Depends()]
MockMenuItemRepositoryDep: TypeAlias = Annotated[mock_menu_item_repository.MockMenuItemRepository, Depends()]
