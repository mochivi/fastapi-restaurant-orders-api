from pydantic import BaseModel, ConfigDict, Field


class RestaurantBase(BaseModel):
    name: str = Field(max_length=255)
    owner_id: int = Field(gt=0)

class RestaurantCreate(RestaurantBase):
    pass

class RestaurantUpdate(BaseModel):
    name: str | None = None

class RestaurantResponse(RestaurantBase):
    id: int
    menu_item_ids: list[int]

    model_config = ConfigDict(from_attributes=True)