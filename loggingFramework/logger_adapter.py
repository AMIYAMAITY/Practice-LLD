
from abc import ABC, abstractmethod

class Adapter(ABC):

    @abstractmethod
    def append(self, message):
        pass