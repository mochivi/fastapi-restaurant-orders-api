from pydantic import BaseModel, ConfigDict

from app.models.enums import OrderStatus


class RestaurantOrderBase(BaseModel):
    pass

class RestaurantOrderCreate(RestaurantOrderBase):
    total_price: float
    user_id: int
    menu_item_ids: list[int]

class RestaurantOrderUpdate():
    status: OrderStatus | None = None

class RestaurantOrderResponse(RestaurantOrderBase):
    id: int
    restaurant_id: int
    user_id: int
    menu_item_ids: list[int]
    status: OrderStatus
    total_price: float

    model_config = ConfigDict(from_attributes=True)