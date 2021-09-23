import unittest
from taquitos import *

class TestCuenta (unittest.TestCase):
    def test_cuenta (self):
        test_cases = [
            #No contiene cosas en el menu
            ('carnitas pozole','Total a pagar: 0'),
            #No contiene tacos
            ('','Por favor, ingrese un pedido mayor a 0 y menor a 30.'),
            #Contiene más de 30 tacos
            ('cachete cachete cachete cachete cachete cachete cachete cachete cachete cachete cachete cachete cachete cachete cachete cachete cachete cachete cachete cachete cachete cachete cachete cachete cachete cachete cachete cachete cachete cachete cachete cachete','Por favor, ingrese un pedido mayor a 0 y menor a 30.'),
            #Orden normal
            ('cachete lengua cachete tripitas machito machito machito cachete lengua','Total a pagar: 110'),
            #Contiene caracteres extra
            ('lengua*','Total a pagar: 0'),
            ]

        for tc in test_cases:
            resultado = cuenta (tc[0])
            self.assertEqual(resultado,tc[1])
            
if __name__ == '__main__':
    unittest.main()  