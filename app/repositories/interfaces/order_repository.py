from app.repositories.base import BaseRepository
from app.models.domain.order import Order

class BaseOrderRepository(BaseRepository[Order]):
    pass