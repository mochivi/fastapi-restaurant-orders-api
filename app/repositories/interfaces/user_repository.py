from app.repositories.base import BaseRepository
from app.models.domain.user import User

class BaseUserRepository(BaseRepository[User]):
    pass