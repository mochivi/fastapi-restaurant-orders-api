from pydantic import BaseModel, Field


def _id_generator():
    i = 1
    while True:
        yield i
        i+=1
_id_gen = _id_generator()

def generate_next_id() -> int:
    return next(_id_gen)

class MenuItem(BaseModel):
    id: int = Field(default_factory=generate_next_id, gt=0)
    title: str = Field(max_length=100)
    description: str = Field(max_length=1000)
    price: float = Field(gt=0)
    restaurant_id: int