import unittest
import censura

class TestNT(unittest.TestCase):

    def test_f1(self):
        test_casos = [("popo sangre muerte maldito", "El animal maldito se acercó con una mirada de muerte. Manchas de sangre cubrían el suelo", "kawai", "El animal kawai se acercó con una mirada de kawai. Manchas de kawai cubrían el suelo"),
                      ("lava tina", "Anita lava la tina", "tinajera", "Anita tinajerajera la tinajera"),
                      ("el la tomate", "el tomate grande y rojo estaba en la estufa", "pepino", "pepino pepino grande y rojo estaba en pepino estufa")]

        for entrada, cadena, cambio, esperado in test_casos:
            actual = censura.censura(entrada, cadena, cambio)
            self.assertEqual(esperado, actual)

    def test_f2(self):
        test_casos = [("popo sangre muerte maldito", "El animal maldito se acercó con una mirada de muerte. Manchas de sangre cubrían el suelo", "kawai", 6, "Es una cadena valida"),
                      ("lava tina", "Anita lava la tina", "tinajera", 3, "No es una cadena valida"),
                      ("el la tomate", "el tomate grande y rojo estaba en la estufa", "pepino", 10, "Es una cadena valida")]

        for entrada, cadena, cambio, diferencia, esperado in test_casos:
            actual = censura.limite_censura(entrada, cadena, cambio, diferencia)
            self.assertEqual(esperado, actual)


if __name__ == '__main__':
    unittest.main()
