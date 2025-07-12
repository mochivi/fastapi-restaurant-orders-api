from pydantic import BaseModel, Field


class Restaurant(BaseModel):
    id: int
    name: str = Field(max_length=255)
    owner_id: int
    menu_item_ids: list[int] = []