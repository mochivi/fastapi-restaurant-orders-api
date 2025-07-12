
# Base ServiceException class
class ServiceException(Exception):
    pass

class BadRequestException(ServiceException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)