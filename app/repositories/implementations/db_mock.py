from app.models.domain.user import User
from app.models.domain.restaurant import Restaurant
from app.models.domain.order import Order
from app.models.domain.menu_item import MenuItem

_users: dict[int, User] = {}
_restaurants: dict[int, Restaurant] = {}
_orders: dict[int, Order] = {}
_menu_items: dict[int, MenuItem]