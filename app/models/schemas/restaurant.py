from pydantic import BaseModel, ConfigDict, Field


class RestaurantBase(BaseModel):
    name: str = Field(max_length=255)
    owner_id: int = Field(gt=0)

class RestaurantCreate(RestaurantBase):
    pass

class RestaurantUpdate(BaseModel):
    id: int
    name: str | None = Field(default=None, max_length=255)

class RestaurantResponse(RestaurantBase):
    id: int
    menu_item_ids: list[int] | None = None

    model_config = ConfigDict(from_attributes=True)