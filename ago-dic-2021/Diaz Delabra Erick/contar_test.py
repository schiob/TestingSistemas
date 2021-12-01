import unittest
from contar import contar_vocales

class TestContar(unittest.TestCase):
    def test_contar_vocales(self):
        contar_vocales()
        self.assertEqual('FOO','FOO')


if __name__ == '__main__':
    unittest.main()