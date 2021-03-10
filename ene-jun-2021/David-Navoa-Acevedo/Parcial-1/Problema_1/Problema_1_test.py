import unittest
from Problema_1 import numero_triangular

class test_numero_triangular(unittest.TestCase):

    def test_case(self):

        casos = (
            #Casos dados en el problema
            [1, 1],
            [3, 6],
            [4, 10],
            [56, 1596],
            [400, 80200],
            #casos planteados adicionales
            ["striiiing", "No se permiten valores distintos al entero"],
            [1.5, "No se permiten valores distintos al entero"],
            [None, "No se permiten valores distintos al entero"],
            [-15, "No hay numeros triangulares negativos"]
        )

        for x in casos:
            self.assertEquals(numero_triangular(x[0]),x[1] )

if __name__ == '__main__':
    unittest.main()