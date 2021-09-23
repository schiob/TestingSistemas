import unittest
from taquitos import total_pedido, crear_lista

class Parcial1(unittest.TestCase):
   #cachete lengua tripitas pastor machito
    def test_prueba1(self):
        lista = crear_lista('cachete lengua tripitas pastor machito')
        resultado_real = total_pedido(lista)
        self.assertEqual(resultado_real, 61)
    
    def test_prueba2(self):
        lista = crear_lista('cachete cachete lengua tripitas pastor pastor machito')
        resultado_real = total_pedido(lista)
        self.assertEqual(resultado_real, 89)

    def test_prueba3(self):
        lista = crear_lista('cachete cachete machito')
        resultado_real = total_pedido(lista)
        self.assertEqual(resultado_real, 4)

    def test_prueba4(self):
        lista = crear_lista('pastor pastor pastor pastor pastor')
        resultado_real = total_pedido(lista)
        self.assertEqual(resultado_real, 60)

if __name__ == '__main__':
    unittest.main()