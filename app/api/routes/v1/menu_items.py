from typing import Any

from fastapi import APIRouter, status

from app.models.schemas.menu_item import MenuItemCreate, MenuItemUpdate, MenuItemResponse
from app.api.dependencies import MenuItemServiceDep

router: APIRouter = APIRouter(prefix="/restaurants/{restaurant_id}/menuitems", tags=["Menu Items"])

@router.get(
    path="/{menu_item_id}",
    status_code=status.HTTP_200_OK,
    summary="Get a menu item from a restaurant",
    response_model=MenuItemResponse
)
def get(
    restaurant_id: int,
    menu_item_id: int,
    menu_item_service: MenuItemServiceDep
) -> Any:
    return menu_item_service.get(restaurant_id, menu_item_id)


@router.post(
    path="/",
    status_code=status.HTTP_201_CREATED,
    summary="Create a menu item for a restaurant",
    response_model=MenuItemResponse
)
def create(
    restaurant_id: int,
    menu_item_create: MenuItemCreate,
    menu_item_service: MenuItemServiceDep
) -> Any:
    return menu_item_service.create(restaurant_id, menu_item_create)

@router.patch(
    path="/",
    status_code=status.HTTP_200_OK,
    summary="Update a menu item for a restaurant",
    response_model=MenuItemResponse
)
def update(
    restaurant_id: int,
    menu_item_update: MenuItemUpdate,
    menu_item_service: MenuItemServiceDep
) -> Any:
    return menu_item_service.update(restaurant_id, menu_item_update)

@router.delete(
    path="/{menu_item_id}",
    status_code=status.HTTP_200_OK,
    summary="Deletes a menu item for a restaurant",
)
def delete(
    restaurant_id: int,
    menu_item_id: int,
    menu_item_service: MenuItemServiceDep
) -> None:
    menu_item_service.delete(restaurant_id, menu_item_id)