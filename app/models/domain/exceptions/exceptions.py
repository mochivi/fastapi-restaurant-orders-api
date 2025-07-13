from app.models.domain.exceptions.interfaces import NotFoundException, ConflictException

class UserNotFoundException(NotFoundException):
    _context: str = "User"

    def __init__(self, id: int | None = None, email: str | None = None, *args: object) -> None:
        if id is not None:
            super().__init__(id, *args)
        elif email is not None:
            super().__init__(None, f"User with email {email} not found")

class RestaurantNotFoundException(NotFoundException):
    _context: str = "Restaurant"

class OrderNotFoundException(NotFoundException):
    _context: str = "Order"

class MenuItemNotFoundException(NotFoundException):
    _context: str = "Menu Item"


class UserAlreadyExistsException(ConflictException):
    _context: str = "User"

class RestaurantAlreadyExistsException(ConflictException):
    _context: str = "Restaurant"

class OrderAlreadyExistsException(ConflictException):
    _context: str = "Order"

class MenuItemAlreadyExistsException(ConflictException):
    _context: str = "Menu Item"