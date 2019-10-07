import impares
import unittest

class Testeo(unittest.TestCase):
    def test_cuentaimpares(self):
        res = impares.cuentaimpares('6 -5')
        self.assertEqual(res, 5)
        res = impares.cuentaimpares('12 15')
        self.assertEqual(res, 13)
        res = impares.cuentaimpares('12 12')
        self.assertEqual(res, 0)
        res = impares.cuentaimpares('123 321')
        self.assertEqual(res, 21756)
        res = impares.cuentaimpares('4321 1234')
        self.assertEqual(res, 4284911)
        res = impares.cuentaimpares('-19289 7853')
        self.assertEqual(res, -77593260)

if __name__ == '__main__':
    unittest.main()
