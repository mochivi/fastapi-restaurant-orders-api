from app.models.domain.order import Order
from app.models.enums import OrderStatus
from app.models.schemas.order import RestaurantOrderCreate
from app.repositories.dependencies import MockMenuItemRepositoryDep, MockOrderRepositoryDep, MockRestaurantRepositoryDep, MockUserRepositoryDep
from app.repositories.interfaces import user_repository

class RestaurantOrderService:
    def __init__(
        self, 
        order_repository: MockOrderRepositoryDep,
        restaurant_repository: MockRestaurantRepositoryDep,
        user_repository: MockUserRepositoryDep,
        menu_item_repository: MockMenuItemRepositoryDep 
    ) -> None:
        self.order_repository = order_repository
        self.restaurant_repository = restaurant_repository
        self.user_repository = user_repository
        self.menu_item_repository = menu_item_repository

    def create(self, restaurant_id: int, restaurant_order_create: RestaurantOrderCreate) -> Order:
        self.restaurant_repository.get(restaurant_id)
        self.user_repository.get(restaurant_order_create.user_id)
        
        total_price = 0
        for menu_item_id in restaurant_order_create.menu_item_ids:
            menu_item = self.menu_item_repository.get(menu_item_id)
            total_price += menu_item.price

        order: Order = Order(
            **restaurant_order_create.model_dump(),
            restaurant_id=restaurant_id,
            status=OrderStatus.pending_payment,
            total_price=total_price,
        )

        return self.order_repository.create(order)