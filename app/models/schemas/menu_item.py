from pydantic import BaseModel, ConfigDict


class MenuItemBase(BaseModel):
    title: str
    description: str
    price: float
    
class MenuItemCreate(MenuItemBase):
    restaurant_id: int

class MenuItemUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    price: str | None = None

class MenuItemResponse(MenuItemBase):
    id: int

    model_config = ConfigDict(from_attributes=True)