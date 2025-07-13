from app.models.domain.order import Order
from app.models.schemas.order import OrderUpdate
from app.repositories.implementations.mock_order_repository import MockOrderRepository
from app.services.exceptions.interfaces import BadRequestException


class OrderService:

    def __init__(self, order_repository: MockOrderRepository) -> None:
        self.order_repository = order_repository

    def get(self, order_id: int) -> Order:
        return self.order_repository.get(order_id)

    def update(self, order_update: OrderUpdate) -> Order:
        if order_update.status is None:
            raise BadRequestException("A new status must be provided")
        
        db_order: Order = self.order_repository.get(order_update.id)

        if db_order.status == order_update.status:
            raise BadRequestException("provide status is the same as already stored")
        
        db_order.status = order_update.status
        new_order: Order = self.order_repository.update(db_order)
        
        return new_order

    def delete(self, order_id: int) -> None:
        self.order_repository.delete(order_id)