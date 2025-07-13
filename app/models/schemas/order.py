from pydantic import BaseModel, ConfigDict

from app.models.enums import OrderStatus


class OrderBase(BaseModel):
    pass

# Used in /restaurants/{restaurant_id}/create
class RestaurantOrderCreate(OrderBase):
    user_id: int
    menu_item_ids: list[int]

class OrderUpdate(BaseModel):
    id: int
    status: OrderStatus | None = None

class OrderResponse(OrderBase):
    id: int
    restaurant_id: int
    user_id: int
    menu_item_ids: list[int]
    status: OrderStatus
    total_price: float

    model_config = ConfigDict(from_attributes=True)