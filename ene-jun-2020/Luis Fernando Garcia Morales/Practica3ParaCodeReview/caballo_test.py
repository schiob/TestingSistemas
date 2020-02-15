import unittest
from caballo import calcular_mov

class TestCaballo(unittest.TestCase):
    def test_caballo_mov(self):
        tc = [
            {
                "nombre": "centro",
                "entrada": "d4",
                "enrada_peon":"00",
                "salida_esperada": 8
            },
            {
                "nombre": "izq",
                "entrada": "a4",
                "enrada_peon":"00",
                "salida_esperada": 4
            },
            {
                "nombre": "abajo",
                "entrada": "d1",
                "enrada_peon":"00",
                "salida_esperada": 4
            },
            {
                "nombre": "arriba",
                "entrada": "d8",
                "enrada_peon":"00",
                "salida_esperada": 4
            },
            {
                "nombre": "der",
                "entrada": "h4",
                "enrada_peon":"00",
                "salida_esperada": 4
            },
            {
                "nombre": "esq",
                "entrada": "h1",
                "enrada_peon":"00",
                "salida_esperada": 2
            },
            {
                "nombre": "esq2",
                "entrada": "h8",
                "enrada_peon":"00",
                "salida_esperada": 2
            },
            {
                "nombre": "esq3",
                "entrada": "a8",
                "enrada_peon":"00",
                "salida_esperada": 2
            },
            {
                "nombre": "casiesq",
                "entrada": "a2",
                "enrada_peon":"00",
                "salida_esperada": 4
            },
            {
                "nombre": "casiesq",
                "entrada": "b1",
                "enrada_peon":"00",
                "salida_esperada": 3
            },
            {
                "nombre": "casiesq2",
                "entrada": "g2",
                "enrada_peon":"00",
                "salida_esperada": 4
            },
            {
                "nombre": "casiesq2",
                "entrada": "g5",
                "enrada_peon":"00",
                "salida_esperada": 6
            },
            {
                "nombre": "casiesq2",
                "entrada": "b4",
                "enrada_peon":"00",
                "salida_esperada": 6
            },
            {
                "nombre": "casiesq2",
                "entrada": "d2",
                "enrada_peon":"00",
                "salida_esperada": 6
            },
            {
                "nombre": "casiesq2",
                "entrada": "d2",
                "enrada_peon":"00",
                "salida_esperada": 6
            },
            {
                "nombre":"peon1",
                "entrada":"a1",
                "enrada_peon":"b3",
                "salida_esperada": 1
            }

        ]
        for test in tc:
            mov = calcular_mov(test["entrada"], test["enrada_peon"])
            self.assertEqual(mov, test["salida_esperada"], msg="error en {}, entrada: {}, entrada_peon{}, esperado: {} real {}".format(test["nombre"], test["entrada"], test["enrada_peon"], test["salida_esperada"], mov))

if __name__ == "__main__":
    unittest.main()