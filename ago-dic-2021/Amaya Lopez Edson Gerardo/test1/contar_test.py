import unittest
from contar import contar_vocales

class TestContar(unittest.TestCase):
    def test_contar_vocales(self):
        resultado_real= contar_vocales("aeiortyr")

        self.assertEqual(resultado_real,4)


if __name__ == '__main__':
    unittest.main()

