from app.models.domain.restaurant import Restaurant
from app.repositories.dependencies import MockRestaurantRepositoryDep


class RestaurantService:
    def __init__(self, Restaurant_repository: MockRestaurantRepositoryDep) -> None:
        self.Restaurant_repository = Restaurant_repository

    def get(self) -> Restaurant:
        ...

    def create(self) -> Restaurant:
        ...

    def update(self) -> Restaurant:
        ...

    def delete(self) -> Restaurant:
        ...