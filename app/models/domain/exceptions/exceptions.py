from app.models.domain.exceptions.interfaces import NotFoundException, ConflictException

class UserNotFoundException(NotFoundException):
    _context: str = "User"

class RestaurantNotFoundException(NotFoundException):
    _context: str = "Restaurant"

class UserAlreadyExistsException(ConflictException):
    _context: str = "User"

class RestaurantAlreadyExistsException(ConflictException):
    _context: str = "Restaurant"