import unittest
from unittest import mock
from practica1 import numbers



class TestNumbers(unittest.TestCase):
    def test_practica(self):
        cases = [   
            ("51 -12 -3 0 2", "2 número(s) positivo(s)\n2 número(s) negativo(s)\n3 número(s) par(es)\n2 número(s) impar(es)"),
            ("0 1 2 3 4", "4 número(s) positivo(s)\n0 número(s) negativo(s)\n3 número(s) par(es)\n2 número(s) impar(es)"),
            ("-1 -2 -3", "0 número(s) positivo(s)\n3 número(s) negativo(s)\n1 número(s) par(es)\n2 número(s) impar(es)"),
            ("0", "0 número(s) positivo(s)\n0 número(s) negativo(s)\n1 número(s) par(es)\n0 número(s) impar(es)")
                    ]

        for n in cases:
            esp = n[1]
            act = numbers(n[0])
            self.assertEquals(esp, act)   


if __name__=="__main__":
    unittest.main()
