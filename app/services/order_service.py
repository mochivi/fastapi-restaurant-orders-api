from app.models.domain.order import Order
from app.repositories.dependencies import MockOrderRepositoryDep


class OrderService:
    def __init__(self, Order_repository: MockOrderRepositoryDep) -> None:
        self.Order_repository = Order_repository

    def get(self) -> Order:
        ...

    def create(self) -> Order:
        ...

    def update(self) -> Order:
        ...

    def delete(self) -> Order:
        ...