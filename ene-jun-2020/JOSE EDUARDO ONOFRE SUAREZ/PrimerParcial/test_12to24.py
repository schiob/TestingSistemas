import unittest
from S12to24 import Tiempo

class TestConversion(unittest.TestCase):

    def test_Clock(self):
        hora = "01:00a.m."
        salida_esperada = "01:00hrs"

        salida_real = Tiempo.Hora(hora)

        self.assertEqual(salida_esperada,salida_real)


if __name__ == "__main__":
    unittest.main()
        
