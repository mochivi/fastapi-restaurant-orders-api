from typing import Any

from fastapi import APIRouter, status

from app.api.dependencies import RestaurantServiceDep
from app.models.schemas.restaurant import RestaurantCreate, RestaurantResponse, RestaurantUpdate

router = APIRouter(prefix="/restaurants", tags=["Restaurant"])


@router.get(
    path="/{restaurant_id}",
    summary="Get a restaurant",
    status_code=status.HTTP_200_OK,
    response_model=RestaurantResponse
)
def get(
    restaurant_id: int,
    restaurant_service: RestaurantServiceDep
) -> Any:
    return restaurant_service.get(restaurant_id)


@router.post(
    path="/",
    summary="Create a restaurant",
    status_code=status.HTTP_201_CREATED,
    response_model=RestaurantResponse
)
def create(
    restaurant_create: RestaurantCreate,
    restaurant_service: RestaurantServiceDep
) -> Any:
    return restaurant_service.create(restaurant_create)


@router.patch(
    path="/",
    summary="Update a restaurant",
    status_code=status.HTTP_200_OK,
    response_model=RestaurantResponse
)
def update(
    restaurant_update: RestaurantUpdate,
    restaurant_service: RestaurantServiceDep
) -> Any:
    return restaurant_service.update(restaurant_update)

@router.delete(
    path="/{restaurant_id}",
    summary="Delete a restaurant",
    status_code=status.HTTP_200_OK,
)
def delete(
    restaurant_id: int,
    restaurant_service: RestaurantServiceDep
) -> None:
    restaurant_service.delete(restaurant_id)