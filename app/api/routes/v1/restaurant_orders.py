from typing import Any
from fastapi import APIRouter, status

from app.api.dependencies import RestaurantOrderServiceDep
from app.models.schemas.order import RestaurantOrderCreate, OrderResponse

router: APIRouter = APIRouter(prefix="/restaurants/{restaurant_id}/orders", tags=["Restaurant Orders"])

@router.post(
    path="/",
    status_code=status.HTTP_201_CREATED,
    summary="Create an order",
    response_model=OrderResponse
)
def create(
    restaurant_id: int,
    restaurant_order_create: RestaurantOrderCreate,
    restaurant_order_service: RestaurantOrderServiceDep
) -> Any:
    return restaurant_order_service.create(restaurant_id, restaurant_order_create)