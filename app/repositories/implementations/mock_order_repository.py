from app.repositories.interfaces.order_repository import BaseOrderRepository
from app.models.domain.order import Order

class MockOrderRepository(BaseOrderRepository):
    _orders: dict[int, Order] = {}
    _next_id = 1
    
    def get(self, id: int) -> Order:
        ...
    
    def create(self, item: Order) -> Order:
        ...    

    def update(self, item: Order) -> Order:
        ...
    
    def delete(self, id: int) -> None:
        ...

