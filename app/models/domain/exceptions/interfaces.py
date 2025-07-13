
# Base Domain Exception inherited by all domain exceptions
class DomainException(Exception):
    pass

# ResourceNotFound 404 exceptions
class NotFoundException(DomainException):
    _context: str
    _id: str

    def __init__(self, id: int | None = None, *args: object) -> None:
        if id is not None:
            self.id = id
            super().__init__(f"{self._context} with id '{self.id}' not found", *args)
        super().__init__(*args)
        
# Conflict 409 exceptions
class ConflictException(DomainException):
    _context: str
    _id: str

    def __init__(self, id: int, *args: object, **kwargs) -> None:
        self.id = id
               
        super().__init__(f"{self._context} with id '{self.id} already exists'", *args)