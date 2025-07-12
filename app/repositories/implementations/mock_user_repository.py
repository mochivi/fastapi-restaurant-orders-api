from app.repositories.interfaces.user_repository import BaseUserRepository
from app.models.domain.user import User
from app.models.domain.exceptions.exceptions import UserNotFoundException, UserAlreadyExistsException

_users: dict[int, User] = {}

class MockUserRepository(BaseUserRepository):
    def get(self, id: int) -> User:
        user: User | None = _users.get(id, None)
        if not user:
            raise UserNotFoundException(id)
        return user
    
    def create(self, item: User) -> User:
        user: User | None = _users.get(item.id, None)
        if user:
            raise UserAlreadyExistsException(item.id)
        
        # Also check by the user's email
        for k, v in _users.items():
            if v.email == item.email:
                raise UserAlreadyExistsException(item.id)

        _users[item.id] = item
        return _users[item.id]

    def update(self, item: User) -> User:
        user = _users.get(item.id, None)
        if not user:
            raise UserNotFoundException(item.id)
        _users[item.id] = item
        return item
    
    def delete(self, id: int) -> None:
        user: User | None = _users.get(id, None)
        if not user:
            raise UserNotFoundException(id)
        _users.pop(id)