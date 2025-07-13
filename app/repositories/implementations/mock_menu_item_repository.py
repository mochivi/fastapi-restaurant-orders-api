from app.repositories.interfaces.menu_item_repository import BaseMenuItemRepository
from app.models.domain.menu_item import MenuItem
from app.models.domain.exceptions.exceptions import MenuItemAlreadyExistsException, MenuItemNotFoundException
from app.repositories.implementations.db_mock import _menu_items

class MockMenuItemRepository(BaseMenuItemRepository):
    
    def get(self, id: int) -> MenuItem:
        menu_item: MenuItem | None = _menu_items.get(id, None)
        if not menu_item:
            raise MenuItemNotFoundException(id)
        return menu_item

    def create(self, item: MenuItem) -> MenuItem:
        menu_item: MenuItem | None = _menu_items.get(item.id, None)
        if menu_item:
            raise MenuItemAlreadyExistsException(item.id) 
        _menu_items[item.id] = item
        return item

    def update(self, item: MenuItem) -> MenuItem:
        menu_item: MenuItem | None = _menu_items.get(item.id, None)
        if not menu_item:
            raise MenuItemNotFoundException(item.id)
        _menu_items[item.id] = item
        return item
    
    def delete(self, id: int) -> None:
        menu_item: MenuItem | None = _menu_items.get(id, None)
        if not menu_item:
            raise MenuItemNotFoundException(id)
        _menu_items.pop(id)