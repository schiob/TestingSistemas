import unittest
from unittest.mock import MagicMock
from platillo import Platillo, Ingrediente
from comida import Comida
from main import CalcCaloriasPlatillo, CalcCaloriasComida, SePuedeComer


class TestMain(unittest.TestCase):
    def testCalcCaloriasPlatillo(self):
        testCases = [
            {
                "name": "Agregar 1 elemento",
                "in_platillo": (
                    [Ingrediente("papa", "gr", 500), 200],
                    [Ingrediente("tomate", "gr", 250), 300],
                    [Ingrediente("aguacate", "gr", 700), 100],
                    [Ingrediente("lechuga", "gr", 100), 850],
                ),
                "salida_esperada": 330000,
            },
        ]

        for tc in testCases:
            plat = Platillo("lo que sea")

            # add all ingredientes
            for ing in tc["in_platillo"]:
                plat.addIngrediente(ing[0], ing[1])

            self.assertEqual(CalcCaloriasPlatillo(plat), tc["salida_esperada"])

    def testCalcCaloriasComida(self):
        testCases = [
            {
                "name": "Agregar 1 elemento",
                "in_platillos": (
                    {
                        "nombre": "ensalada",
                        "ingredientes": [
                            [Ingrediente("papa", "gr", 500), 200],
                            [Ingrediente("tomate", "gr", 250), 300],
                            [Ingrediente("aguacate", "gr", 700), 100],
                            [Ingrediente("lechuga", "gr", 100), 850],
                        ]
                    },
                    {
                        "nombre": "carne con pasta",
                        "ingredientes": [
                            [Ingrediente("carne", "gr", 675), 400],
                            [Ingrediente("tomate", "gr", 250), 300],
                            [Ingrediente("pasta", "gr", 200), 300],
                        ]
                    },
                ),
                "salida_esperada": 735000,
            },
        ]
        
        for tc in testCases:
            platillos = []

            for plat_dic in tc["in_platillos"]:
                plat = Platillo(plat_dic["nombre"])
                # add all ingredientes
                for ing in plat_dic["ingredientes"]:
                    plat.addIngrediente(ing[0], ing[1])

                platillos.append(plat)
            
            comida = Comida(platillos)

            self.assertEqual(CalcCaloriasComida(comida), tc["salida_esperada"])
        
    def testSePuedeComer(self):
        testCases = [
            {
                "name": "con dieta mock",
                "dieta_mock_lleva": 50000,
                "dieta_mock_max": 600000,
                "in_platillos": (
                    {
                        "nombre": "ensalada",
                        "ingredientes": [
                            [Ingrediente("papa", "gr", 500), 200],
                            [Ingrediente("tomate", "gr", 250), 300],
                            [Ingrediente("aguacate", "gr", 700), 100],
                            [Ingrediente("lechuga", "gr", 100), 850],
                        ]
                    },
                    {
                        "nombre": "carne con pasta",
                        "ingredientes": [
                            [Ingrediente("carne", "gr", 675), 400],
                            [Ingrediente("tomate", "gr", 250), 300],
                            [Ingrediente("pasta", "gr", 200), 300],
                        ]
                    },
                    # TOTAL 735000
                ),
                "salida_esperada": False,
            },
        ]
        
        for tc in testCases:
            platillos = []

            for plat_dic in tc["in_platillos"]:
                plat = Platillo(plat_dic["nombre"])
                # add all ingredientes
                for ing in plat_dic["ingredientes"]:
                    plat.addIngrediente(ing[0], ing[1])

                platillos.append(plat)
            
            comida = Comida(platillos)

            dieta_mock = MagicMock()
            dieta_mock.calcularCuantoLleva.return_value = tc["dieta_mock_lleva"]
            dieta_mock.max_calorias = tc["dieta_mock_max"]

            self.assertEqual(SePuedeComer(dieta_mock, comida), tc["salida_esperada"])


if __name__ == "__main__":
    unittest.main()