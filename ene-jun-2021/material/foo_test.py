import unittest
from foo import sumar_algo, Entrada

class EntradaMock(Entrada):
    def __init__(self, return_value):
        self.return_value = return_value

    def pedir_entrada(self) -> str:
        return self.return_value

class TestFoo(unittest.TestCase):
    def test_foo(self):
        mi_mock = EntradaMock("14")
        self.assertEqual(sumar_algo(5, mi_mock), 19)

        mi_mock = EntradaMock("0")
        self.assertEqual(sumar_algo(5, mi_mock), 5)

if __name__ == "__main__":
    unittest.main()