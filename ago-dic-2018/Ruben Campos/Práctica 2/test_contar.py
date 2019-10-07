import unittest
import contar

class TestContar(unittest.TestCase):

    def test_contar(self):
        #Caso de prueba 1
        resultado = contar.funcionpro(4,[1,2,3,4])
        self.assertEqual(resultado[0], 4)
        self.assertEqual(resultado[1], 0)
        self.assertEqual(resultado[2], 2)
        self.assertEqual(resultado[3], 2)
        self.assertEqual(resultado[4], 4)

        #Caso de prueba 2
        resultado = contar.funcionpro(5,[1,3,7,-4,-2])
        self.assertEqual(resultado[0], 3)
        self.assertEqual(resultado[1], 2)
        self.assertEqual(resultado[2], 2)
        self.assertEqual(resultado[3], 3)
        self.assertEqual(resultado[4], 5)

        #Caso de prueba 3 -- Probando error de len(numeros) != n, o sea, que la cantidad de numeros que me
        #dieron de input sea desigual a la cantidad de numeros en la lista de numeros que ingresaron de input
        with self.assertRaises(SystemExit):
            resultado = contar.funcionpro(6,[1,-2,-4,6,9]) #Se pasan 5 numeros en lugar de 6
            self.assertEqual(resultado[0], 3)
            self.assertEqual(resultado[1], 2)
            self.assertEqual(resultado[2], 3)
            self.assertEqual(resultado[3], 2)
            self.assertEqual(resultado[4], 6)

        #Caso de prueba 4
        resultado = contar.funcionpro(3,[-2,2,3])
        self.assertEqual(resultado[0], 2)
        self.assertEqual(resultado[1], 1)
        self.assertEqual(resultado[2], 2)
        self.assertEqual(resultado[3], 1)
        self.assertEqual(resultado[4], 3)



if __name__ == '__main__':
    unittest.main()
