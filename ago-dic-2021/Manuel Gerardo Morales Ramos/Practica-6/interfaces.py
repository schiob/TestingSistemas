from abc import ABC, abstractmethod

# Interface for test ways to code this practice.
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args: any, **kwargs: any) -> any:
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

# I/O interface.
class IO(ABC):
    @abstractmethod
    def Read(self) -> str:
        pass 
    """ @abstractmethod
    def Write(self, data: str) -> None:
        pass """

# --- Implementation ---

class Terminal(IO):
    def Read(self) -> str:
        return input()

class File(IO):
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def Read(self) -> str:
        with open(self.file_name, 'r') as f:
            return f.read()

    """ def Write(self, data: str) -> None:
        with open(self.file_name, 'w') as f:
            return f.write(data) """
