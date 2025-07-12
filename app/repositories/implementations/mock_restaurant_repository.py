from app.repositories.interfaces.restaurant_repository import BaseRestaurantRepository
from app.models.domain.restaurant import Restaurant

class MockRestaurantRepository(BaseRestaurantRepository):
    _restaurants: dict[int, Restaurant] = {}
    _next_id = 1

    def get(self, id: int) -> Restaurant:
        ...
    
    def create(self, item: Restaurant) -> Restaurant:
        ...    

    def update(self, item: Restaurant) -> Restaurant:
        ...
    
    def delete(self, id: int) -> Restaurant:
        ...