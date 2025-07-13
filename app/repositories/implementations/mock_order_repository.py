from app.models.domain.exceptions.exceptions import OrderAlreadyExistsException, OrderNotFoundException
from app.repositories.interfaces.order_repository import BaseOrderRepository
from app.models.domain.order import Order
from app.repositories.implementations.db_mock import _orders

class MockOrderRepository(BaseOrderRepository):
    
    def get(self, id: int) -> Order:
        order: Order | None = _orders.get(id, None)
        if not order:
            raise OrderNotFoundException(id)
        return order

    def create(self, item: Order) -> Order:
        order: Order | None = _orders.get(item.id, None)
        if order:
            raise OrderAlreadyExistsException(item.id) 

        _orders[item.id] = item
        return item


    def update(self, item: Order) -> Order:
        order: Order | None = _orders.get(item.id, None)
        if not order:
            raise OrderNotFoundException(item.id)
        _orders[item.id] = item
        return item

    def delete(self, id: int) -> None:
        order: Order | None = _orders.get(id, None)
        if not order:
            raise OrderNotFoundException(id)
        _orders.pop(id)

