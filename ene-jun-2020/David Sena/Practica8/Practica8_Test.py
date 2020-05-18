import unittest
class TestCensura(unittest.TestCase):
       def censura_test(self):
        test = [
            {
                
                "texto": "El animal maldito se acercó con una mirada de muerte. Manchas de sangre cubrían el suelo",
                "palabras_malas": ("popo", "sangre", "muerte", "maldito"),
                "reemplazo": "kawaii",
                "diferencia": 4,
                "expect_out": "Es valido"
            }
        ]
        for tc in test:
            actual= censura2(tc["texto"],tc["palabras_malas"],tc["reemplazo"],tc["diferencia"])
            actual= censura2("No es el text", "palabras_malas", "bye",1)
            self.assertEqual(tc["expect_out"], actual)

if __name__ == "__main__":
   unittest.main()
