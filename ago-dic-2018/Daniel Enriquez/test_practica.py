import unittest
import practica

class TestJuanita(unittest.TestCase):

    def test_contar(self):
        resultado=practica.contar([0,3,42,5,6])
        self.assertEqual(resultado[0],3)
        self.assertEqual(resultado[1],2)
        self.assertEqual(resultado[2],4)#En esta prueba estamos verificando que haya 4 negativos y 0 positivos y
        # al compilar el programa nos dice que no es verdad que son 0 y que es diferente de 4
        self.assertEqual(resultado[3],0)
if __name__ == "__main__":
    unittest.main()
