from app.repositories.interfaces.user_repository import BaseUserRepository
from app.models.domain.user import User
from app.models.domain.exceptions import UserNotFoundException

class MockUserRepository(BaseUserRepository):
    _users: dict[int, User] = {}
    _next_id = 1

    def get(self, id: int) -> User:
        user = self._users.get(id, None)
        if not user:
            raise UserNotFoundException(id)
        return user
    
    def create(self, item: User) -> User:
        ...    

    def update(self, item: User) -> User:
        ...
    
    def delete(self, id: int) -> User:
        ...