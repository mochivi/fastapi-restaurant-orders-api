from typing import Any

from fastapi import APIRouter, status

from app.api.dependencies import OrderServiceDep
from app.models.schemas.order import OrderUpdate, OrderResponse

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.get(
    path="/{order_id}",
    status_code=status.HTTP_200_OK,
    summary="Get an order",
    response_model=OrderResponse
)
def get(
    order_id: int,
    order_service: OrderServiceDep
) -> Any:
    return order_service.get(order_id)

@router.patch(
    path="/",
    status_code=status.HTTP_200_OK,
    summary="Update an order",
    response_model=OrderResponse
)
def update(
    order_update: OrderUpdate,
    order_service: OrderServiceDep
) -> Any:
    return order_service.update(order_update)


@router.delete(
    path="/{order_id}",
    status_code=status.HTTP_200_OK,
    summary="Delete an order",
)
def delete(
    order_id: int,
    order_service: OrderServiceDep
) -> None:
    order_service.delete(order_id)