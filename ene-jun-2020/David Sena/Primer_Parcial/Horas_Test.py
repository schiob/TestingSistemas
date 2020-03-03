import unittest
from Horas import convertir

class TestHora(unittest.TestCase):
    def test_hora(self):
        casos=(
        ("14:23", "02:23P.M"),
        ("23:43", "11:43P.M"),
        ("11:42", "11:42A.M"),
        ("12:00", "12:00P.M"),
        ("01:05", "01:05A.M"),
        ("23:59", "11:59P.M")
        )

        for hora, salida_esperada in casos:
            actual = convertir(hora)
            self.assertEqual(actual, salida_esperada)
        
if __name__ == '__main__':
    unittest.main()




    