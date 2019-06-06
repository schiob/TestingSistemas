import unittest
import Extra
class TestNumeros(unittest.TestCase):
    def test_numeros(self):
        test_cases = [('6 -5', 5), ('12 15', 13), ('12 12', 0), ('123 321', 21756), ('4321 1234', 4284911), ('-19289 7853', -77593260)]

        for enter, esperado in test_cases:
            actual = Extra.Impares(enter)
            self.assertEqual(esperado, actual)

if __name__ == '__main__':
        unittest.main()
