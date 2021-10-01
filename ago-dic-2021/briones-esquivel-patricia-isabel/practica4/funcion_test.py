import unittest
from funcion import calc_prom

class NuevoMock ():
    def __init__(self, return_value): 
        self.return_value = return_value

    def leer(self) -> str: 
        return self.return_value

class TestMock(unittest.TestCase):         
    def test_mock(self):
        mi_mock = NuevoMock("1\n1") 
        self.assertEqual(calc_prom(mi_mock), 1)
        
if __name__ == "__main__":
    unittest.main()