from pydantic import BaseModel


class MenuItem(BaseModel):
    id: int
    title: str
    description: str
    price: float
    restaurant_id: int