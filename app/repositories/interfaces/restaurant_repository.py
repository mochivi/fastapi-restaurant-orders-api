from app.repositories.base import BaseRepository
from app.models.domain.restaurant import Restaurant

class BaseRestaurantRepository(BaseRepository[Restaurant]):
    pass