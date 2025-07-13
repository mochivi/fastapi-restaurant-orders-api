from app.models.domain import menu_item

from app.models.domain.menu_item import MenuItem
from app.models.schemas.menu_item import MenuItemCreate, MenuItemUpdate
from app.repositories.dependencies import MockMenuItemRepositoryDep



class MenuItemService:
    def __init__(self, menu_item_repository: MockMenuItemRepositoryDep) -> None:
        self.menu_item_repository = menu_item_repository

    def get(self, restaurant_id: int, menu_item_id: int) -> MenuItem:
        return self.menu_item_repository.get(menu_item_id)

    def create(self, restaurant_id: int, menu_item_create: MenuItemCreate) -> MenuItem:
        menu_item: MenuItem = MenuItem(**menu_item_create.model_dump(), restaurant_id=restaurant_id)
        return self.menu_item_repository.create(menu_item)

    def update(self, restaurant_id: int, menu_item_update: MenuItemUpdate) -> MenuItem:
        db_menu_item: MenuItem = self.menu_item_repository.get(menu_item_update.id)
        
        for k, v in menu_item_update.model_dump().items():
            if v is not None:
                setattr(db_menu_item, k, v)

        return self.menu_item_repository.update(db_menu_item)

    def delete(self, restaurant_id: int, menu_item_id: int) -> None:
        self.menu_item_repository.delete(menu_item_id)