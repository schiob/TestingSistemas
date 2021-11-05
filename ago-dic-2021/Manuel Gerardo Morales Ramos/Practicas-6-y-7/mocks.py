import abc

# I/O interface.
class IO(abc.ABC):
    @abc.abstractmethod
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


class MockInput(IO):
    def __init__(self, input_value: str) -> None:
        self.input_value = input_value

    def Read(self) -> str:
        return self.input_value