import unittest
from Cajas import Volumen_Caja, Contenido, Funcion_Principal

class test(unittest.TestCase):
    def test_lados(self):
        SalidaEsperada=5*4*3
        self.assertEqual(SalidaEsperada, Volumen_Caja(1,6,5))
    def test_contenedor(self):
        Salida_Esperada=(4*2)+(5*2)+(4*4)
        self.assertEqual(SalidaEsperada, Contenido(([4,2],[5,2],[4,4])))
    def main_fun(self):
        salida_esperada = [[1,4],[1,3],[2,2]]
        self.assertEqual(salida_esperada, Funcion_Principal(4,3,2,100))
if __name__ == "__main__":
    unittest.main() 