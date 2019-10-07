from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def search_element(self, name):
        # Return an Element object or None
        pass