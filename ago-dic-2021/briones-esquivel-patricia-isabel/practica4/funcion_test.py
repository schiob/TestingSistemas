import unittest
from funcion import calc_prom

class NuevoMock ():
    def __init__(self, return_value): 
        self.return_value = return_value

    def leer(self) -> list: 
        datos = self.return_value.split('\n')
        return datos

class TestMock(unittest.TestCase):         
    def test_mock(self):
        mi_mock = NuevoMock("10\n15") 
        self.assertEqual(calc_prom(mi_mock), 12.5)
        
if __name__ == "__main__":
    unittest.main()