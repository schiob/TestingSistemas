import unittest
from taquitos import total_pedido, crear_lista

class Parcial1(unittest.TestCase):
   #cachete lengua tripitas pastor machito
    def test_prueba1(self):
        lista = crear_lista('cachete lengua tripitas pastor machito')
        resultado_real = total_pedido(lista)
        self.assertEqual(resultado_real, 64)

if __name__ == '__main__':
    unittest.main()