from pydantic import BaseModel

from app.models.enums import OrderStatus

class Order(BaseModel):
    id: int
    user_id: int
    restaurant_id: int
    menu_item_ids: list[int]
    total_price: float
    status: OrderStatus
    