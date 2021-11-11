import abc

# I/O interface
class Escritor(abc.ABC):
    @abc.abstractmethod
    def Read(self) -> str:
        pass
    
    @abc.abstractmethod
    def Write(self, data: str) -> None:
        pass

# Implementation
class File(Escritor):
    def __init__(self, file_name: str) -> None:
        self.__file_name = file_name

    def Read(self) -> str:
        with open(self.__file_name, 'r') as f:
            return f.read()

    def Write(self, data: str) -> None:
        with open(self.file_name, 'a') as f:
            return f.write(data)

# Mock
class MockInput(Escritor):
    def __init__(self, input_value: str) -> None:
        self.input_value = input_value

    def Read(self) -> str:
        return self.input_value