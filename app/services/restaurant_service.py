from app.models.domain.exceptions.exceptions import UserNotFoundException
from app.models.domain.restaurant import Restaurant
from app.models.schemas.restaurant import RestaurantCreate, RestaurantUpdate
from app.repositories.dependencies import MockRestaurantRepositoryDep, MockUserRepositoryDep
from app.services.exceptions.interfaces import BadRequestException


class RestaurantService:
    def __init__(
        self,
        restaurant_repository: MockRestaurantRepositoryDep,
        user_repository: MockUserRepositoryDep
    ) -> None:
        self.restaurant_repository = restaurant_repository
        self.user_repository = user_repository

    def get(self, restaurant_id: int) -> Restaurant:
        return self.restaurant_repository.get(restaurant_id)

    def create(self, restaurant_create: RestaurantCreate) -> Restaurant:
        try:
            user = self.user_repository.get(restaurant_create.owner_id)
        except UserNotFoundException:
            raise BadRequestException("trying to create restaurant under non-existent user")

        restaurant_create_dump = restaurant_create.model_dump()
        print(restaurant_create_dump)
        db_restaurant: Restaurant = Restaurant(**restaurant_create_dump, menu_item_ids=None)
        
        return self.restaurant_repository.create(db_restaurant)

    def update(self, restaurant_update: RestaurantUpdate) -> Restaurant:
        
        restaurant_update_dump = restaurant_update.model_dump()
        
        if len(restaurant_update_dump) == 0:
            raise BadRequestException("At least one field must be provided")
        
        db_restaurant: Restaurant = self.restaurant_repository.get(restaurant_update.id)
        for k, v in restaurant_update_dump.items():
            if v is not None:
                setattr(db_restaurant, k, v)

        return self.restaurant_repository.update(db_restaurant)

    # Check user's authorization for performing this
    # Business logic -> is user an admin? is user the restaurant owner?
    def delete(self, restaurant_id: int) -> None:
        self.restaurant_repository.delete(restaurant_id)