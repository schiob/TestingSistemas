import unittest
import Parcial_1

class TestHora(unittest.TestCase):
    def test_hora(self):
        test_casos = (("14:23hrs", "02:23P.M."),
                     ("23:43hrs", "11:43P.M."),
                     ("11:42hrs", "11:42A.M."),
                     ("00:00hrs", "12:00A.M."),
                     ("12:00hrs", "12:00P.M."),
                     ("01:05hrs", "01:05A.M"),
                     ("23:59hrs", "11:59P.M"))

        for hrs, esperado in test_casos:
            actual = Parcial_1.convertir24a12(hrs)
            self.assertEqual(esperado, actual)

if __name__ == '__main__':
    unittest.main()