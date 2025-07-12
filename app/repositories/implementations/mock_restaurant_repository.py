from app.repositories.interfaces.restaurant_repository import BaseRestaurantRepository
from app.models.domain.restaurant import Restaurant
from app.models.domain.exceptions.exceptions import RestaurantAlreadyExistsException, RestaurantNotFoundException
from app.repositories.implementations.db_mock import _restaurants

class MockRestaurantRepository(BaseRestaurantRepository):

    def get(self, id: int) -> Restaurant:
        restaurant: Restaurant | None = _restaurants.get(id, None)
        if not restaurant:
            raise RestaurantNotFoundException(id)
        return restaurant
    
    def create(self, item: Restaurant) -> Restaurant:
        restaurant: Restaurant | None = _restaurants.get(item.id, None)
        if restaurant:
            raise RestaurantAlreadyExistsException(item.id)
        _restaurants[item.id] = item
        return item

    def update(self, item: Restaurant) -> Restaurant:
        restaurant: Restaurant | None = _restaurants.get(item.id, None)
        if not restaurant:
            raise RestaurantNotFoundException(item.id)
        _restaurants[item.id] = item
        return restaurant
    
    def delete(self, id: int) -> None:
        restaurant: Restaurant | None = _restaurants.get(id, None)
        if not restaurant:
            raise RestaurantNotFoundException(id)
        _restaurants.pop(id)