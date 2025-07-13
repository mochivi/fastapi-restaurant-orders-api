from pydantic import BaseModel, ConfigDict, Field


class MenuItemBase(BaseModel):
    title: str
    description: str = Field(max_length=1000)
    price: float = Field(gt=0)
    
class MenuItemCreate(MenuItemBase):
    pass

class MenuItemUpdate(BaseModel):
    id: int
    title: str | None = Field(default=None, max_length=100)
    description: str | None = Field(default=None, max_length=1000)
    price: float | None = Field(default=None, gt=0)

class MenuItemResponse(MenuItemBase):
    id: int
    restaurant_id: int

    model_config = ConfigDict(from_attributes=True)