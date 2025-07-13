from pydantic import BaseModel, Field

from app.models.enums import OrderStatus

def _id_generator():
    i = 1
    while True:
        yield i
        i += 1
_id_gen = _id_generator()

def generate_next() -> int:
    return next(_id_gen)

class Order(BaseModel):
    id: int = Field(default_factory=generate_next, gt=0)
    user_id: int
    restaurant_id: int
    menu_item_ids: list[int]
    total_price: float
    status: OrderStatus
    