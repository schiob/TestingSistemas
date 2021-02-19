import unittest
import NSPE

class TestNumero(unittest.TestCase):
    def test_tipo(self):
        test =       [((51, -12, -3, 0, 2),"2 número positivo\n2 número negativo\n3 número par\n2 número impar"),
                      ((-89, 31, 6, 32, 9),"4 número positivo\n1 número negativo\n2 número par\n3 número impar"),
                      ((-99, 72, -158), "1 número positivo\n2 número negativo\n2 número par\n1 número impar")]

        for lista, esperado in test:
            actual = NSPE.practica1(lista)
            self.assertEqual(esperado,actual)

if __name__ == '__main__':
    unittest.main()