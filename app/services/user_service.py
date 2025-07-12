from app.core.security import hash_password
from app.models.domain.user import User
from app.models.schemas.user import UserCreate, UserUpdate
from app.repositories.dependencies import MockUserRepositoryDep

class UserService:
    def __init__(self, user_repository: MockUserRepositoryDep) -> None:
        self.user_repository = user_repository

    def get(self, user_id: int) -> User:
        return self.user_repository.get(user_id)

    def create(self, user_create: UserCreate) -> User:
        password_hash = hash_password(user_create.password)
        
        user_dump = user_create.model_dump()
        user_dump["password"] = password_hash
        
        user: User = User(**user_dump)
        return self.user_repository.create(user)

    def update(self, user_update: UserUpdate) -> User:

        # Fails with not found if user doesn't exist
        db_user: User = self.user_repository.get(user_update.id)
        
        user_dump = user_update.model_dump()
        for k, v in user_dump.items():
            if v is not None:
                setattr(db_user, k, v)

        return self.user_repository.update(db_user)

    def delete(self, user_id: int) -> None:
        self.user_repository.delete(user_id)