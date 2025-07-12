class DomainException(Exception):
    pass

class NotFoundException(DomainException):
    _context: str
    _id: str

    def __init__(self, id: int, *args: object) -> None:
        self.id = id
        super().__init__(f"{self._context} with id '{self.id}' not found", *args)

class UserNotFoundException(NotFoundException):
    _context: str = "User"