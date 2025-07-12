from pydantic import BaseModel, Field


def _id_generator():
    i = 1
    while True:
        yield i
        i += 1
_id_gen = _id_generator()

def generate_next() -> int:
    return next(_id_gen)

class Restaurant(BaseModel):
    id: int = Field(default_factory=generate_next, gt=0)
    name: str = Field(max_length=255)
    owner_id: int
    menu_item_ids: list[int] | None