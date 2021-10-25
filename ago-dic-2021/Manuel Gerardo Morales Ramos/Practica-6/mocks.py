import interfaces

class MockInput(interfaces.IO):
    def __init__(self, input_value: str) -> None:
        self.input_value = input_value

    def Read(self) -> str:
        return self.input_value