import unittest
from platillo import Platillo, Ingrediente

class TestPlatillo(unittest.TestCase):
    def testAddIngrediente(self):
        testCases = [
            {
                "name": "Agregar 1 elemento",
                "input": (
                    [Ingrediente("papa", "gr", "500"), 200],
                ),
                "list_final": [
                    {"ingrediente": Ingrediente("papa", "gr", "500"), "cantidad": 200},
                ],
            },
            {
                "name": "Agregar 2 elemento",
                "input": (
                    [Ingrediente("papa", "gr", "500"), 200],
                    [Ingrediente("tomate", "gr", "250"), 545],
                ),
                "list_final": [
                    {"ingrediente": Ingrediente("papa", "gr", "500"), "cantidad": 200},
                    {"ingrediente": Ingrediente("tomate", "gr", "250"), "cantidad": 545},
                ],
            },
            {
                "name": "Agregar 2 del mismo",
                "input": (
                    [Ingrediente("papa", "gr", "500"), 200],
                    [Ingrediente("papa", "gr", "500"), 545],
                ),
                "list_final": [
                    {"ingrediente": Ingrediente("papa", "gr", "500"), "cantidad": 745},
                ],
            },
        ]

        for tc in testCases:
            plat = Platillo("mi platillo")

            # add all ingredientes
            for ing in tc["input"]:
                plat.addIngrediente(ing[0], ing[1])

            for ing in tc["list_final"]:
                inResult = False
                for ingResult in plat.ingredientes:
                    if ingResult["ingrediente"].nombre == ing["ingrediente"].nombre:
                        inResult = True
                        self.assertEqual(ing["cantidad"], ingResult["cantidad"])
                if not inResult:
                    self.fail("no se encontró el ingrediente {}".format(ing.name))
    

if __name__ == "__main__":
    unittest.main()