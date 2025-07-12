from app.models.domain.menu_item import MenuItem
from app.repositories.dependencies import MockMenuItemRepositoryDep


class MenuItemService:
    def __init__(self, MenuItem_repository: MockMenuItemRepositoryDep) -> None:
        self.MenuItem_repository = MenuItem_repository

    def get(self) -> MenuItem:
        ...

    def create(self) -> MenuItem:
        ...

    def update(self) -> MenuItem:
        ...

    def delete(self) -> MenuItem:
        ...