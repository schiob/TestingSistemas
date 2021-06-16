import unittest
from suma_de_numeros import *

class tests(unittest.TestCase):

    def test_numeros(self):
        
        tc = [ 
            ((6, -5), 5),
            ((12, 15), 13),
            ((12, 12), 0),
            ((123, 321), 21756),
            ((4321, 1234), 4284911),
            ((-19289, 7853), -77593260),
            ((1, 2, 3), "Dame 2 numeros ni mas ni menos compadre")
        ]

        for i in tc:
            self.assertEqual(suma_de_impares(i[0]), i[1])

if __name__ == '__main__':
    unittest.main()