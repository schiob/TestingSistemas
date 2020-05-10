import unittest
from Censura import censura, censura2

class TestCensura(unittest.TestCase):
   def censura2_test(self):
        test = [
            {
                "malas": ("popo", "sangre", "muerte", "maldito"),
                "frase": "El animal maldito se acercó con una mirada de muerte. Manchas de sangre cubrían el suelo",
                "buena": "kawaii",
                "diferencia": 4,
                "expect_out": "Es valido"
            }
        ]
        for tc in test:
            actual= censura2(tc["malas"],tc["frase"],tc["buena"],tc["diferencia"])
            actual= censura2("No", "No si", "si",1)
            self.assertEqual(tc["expect_out"], actual)

if __name__ == "__main__":
   unittest.main()
    