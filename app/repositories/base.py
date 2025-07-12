from abc import ABC, abstractmethod

class BaseRepository[T](ABC):

    @abstractmethod
    def get(self, id: int) -> T:
        ...

    @abstractmethod
    def create(self, item: T) -> T:
        ...    

    @abstractmethod
    def update(self, item: T) -> T:
        ...
    
    @abstractmethod
    def delete(self, id: int) -> None:
        ...