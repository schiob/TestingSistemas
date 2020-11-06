from  unittest import mock, TestCase
from regression import Tri_from_file

class Test_Hola(TestCase):
    mocks = {"equi1": "3 3 3"}

    def testHolaEquilatero(self):
        usuario = "drdz"
        esperado = f"Hola, {usuario}, tu triangulo es Equilátero"
        
        with mock.patch('regression.open') as mock_open:
            
            for m in [v for i,v in self.mocks.items() if "equi" in i]:           
                mock_open.return_value.__enter__.return_value.read.return_value = m
                real = Tri_from_file("mock", "drdz")

                assert esperado == real