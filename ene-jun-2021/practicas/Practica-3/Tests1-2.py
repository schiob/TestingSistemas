import unittest
from Practica2 import tipo_triangulo
from Practica1 import contador

class test_practica_2_cass(unittest.TestCase):
    
    def test_practica_2(self):
        casos = (
            [0, 0, 0, "No es un Triangulo"],
            [1, 1, 1, "Es un triangulo Equilatero"],
            [1, 2, 3, "Es un triangulo Escaleno"],
            [-1, 2, 3, "No es un Triangulo"],
            ["a", 2, 3, "No es un Triangulo"],
            [None, 3, 4, "No es un Triangulo"],
            [1.1, 0.1, 2.3, "Es un triangulo Escaleno"],
            [1, 1, 2, "Es un triangulo Isoseles"]
        )

        for x in casos:
            self.assertEquals(tipo_triangulo(x[0], x[1], x[2]), x[3])
class test_practica_1_class(unittest.TestCase):

    def test_practica_1(self):
        casos = (
            ["1 2 3 4 5 6", "No es la cantidad de datos pedido"],
            ["1 2 3 4", "No es la cantidad de datos pedido"],
            ["-1 2 -3 5 asd", "No es el tipo de dato pedido"],
            ["0.5 1 2 3 5", "No es el tipo de dato pedido"]
        )

        for x in casos:
            self.assertEquals(contador(0),contador(1) )

if __name__ == '__main__':
    unittest.main()
        
        