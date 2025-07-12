from app.repositories.interfaces.menu_item_repository import BaseMenuItemRepository
from app.models.domain.menu_item import MenuItem

class MockMenuItemRepository(BaseMenuItemRepository):
    _menu_items: dict[int, MenuItem] = {}
    _next_id = 1
    
    def get(self, id: int) -> MenuItem:
        ...
    
    def create(self, item: MenuItem) -> MenuItem:
        ...    

    def update(self, item: MenuItem) -> MenuItem:
        ...
    
    def delete(self, id: int) -> MenuItem:
        ...