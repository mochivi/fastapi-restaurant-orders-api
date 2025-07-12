from app.models.domain.user import User
from app.repositories.dependencies import MockUserRepositoryDep

class UserService:
    def __init__(self, user_repository: MockUserRepositoryDep) -> None:
        self.user_repository = user_repository

    def get(self, user_id: int) -> User:
        return self.user_repository.get(user_id)

    def create(self) -> User:
        ...

    def update(self) -> User:
        ...

    def delete(self) -> User:
        ...