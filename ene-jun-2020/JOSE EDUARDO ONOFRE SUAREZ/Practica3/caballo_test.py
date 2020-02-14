import unittest
from caballoE import calcular_mov

class TestCaballo(unittest.TestCase):
    def test_caballo_mov(self):
        tc = [
            {
                "nombre": "centro",
                "entrada": "d4",
                "salida_esperada": 8
            },
            {
                "nombre": "izq",
                "entrada": "a4",
                "salida_esperada": 4
            },
            {
                "nombre": "abajo",
                "entrada": "d1",
                "salida_esperada": 4
            },
            {
                "nombre": "arriba",
                "entrada": "d8",
                "salida_esperada": 4
            },
            {
                "nombre": "der",
                "entrada": "h4",
                "salida_esperada": 4
            },
            {
                "nombre": "esq",
                "entrada": "h1",
                "salida_esperada": 2
            },
            {
                "nombre": "esq2",
                "entrada": "h8",
                "salida_esperada": 2
            },
            {
                "nombre": "esq3",
                "entrada": "a8",
                "salida_esperada": 2
            },
            {
                "nombre": "casiesq",
                "entrada": "a2",
                "salida_esperada": 3
            },
            {
                "nombre": "casiesq",
                "entrada": "b1",
                "salida_esperada": 3
            },
            {
                "nombre": "casiesq2",
                "entrada": "g2",
                "salida_esperada": 4
            },
            {
                "nombre": "casiesq2",
                "entrada": "g5",
                "salida_esperada": 6
            },
            {
                "nombre": "casiesq2",
                "entrada": "b4",
                "salida_esperada": 6
            },
            {
                "nombre": "casiesq2",
                "entrada": "d2",
                "salida_esperada": 6
            },
            {
                "nombre": "casiesq2",
                "entrada": "d2",
                "salida_esperada": 6
            }

        ]

        for test in tc:
            mov = calcular_mov(test["entrada"], "")
            self.assertEqual(mov, test["salida_esperada"], msg="error en {}, entrada: {}, esperado: {} real {}".format(test["nombre"], test["entrada"], test["salida_esperada"], mov))

if __name__ == "__main__":
    unittest.main()