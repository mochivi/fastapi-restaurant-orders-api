from app.models.domain.exceptions.interfaces import NotFoundException, ConflictException

class UserNotFoundException(NotFoundException):
    _context: str = "User"

class UserAlreadyExistsException(ConflictException):
    _context: str = "User"
    
    def __init__(self, id: int, *args: object) -> None:
        super().__init__(id, *args)