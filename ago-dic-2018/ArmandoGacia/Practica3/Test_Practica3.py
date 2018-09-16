import unittest
import Practica3

class Prueba_Numerostriangulares(unittest.TestCase):
    def prueba(self):
        #Caso de Prueba 1
        res=Practica3.Triangulares(4)
        self.assertEqual(res[0],4)
        self.assertEqual(res[1],10)

        #Caso de Prueba 2
        res=Practica3.Triangulares(1)
        self.assertEqual(res[0],1)
        self.assertEqual(res[1],3)

        #Caso de Prueba 3
        res=Practica3.Triangulares(2)
        self.assertEqual(res[0],2)
        self.assertEqual(res[1],6)

        #Caso de Prueba 4
        res=Practica3.Triangulares(100)
        self.assertEqual(res[0],100)
        self.assertEqual(res[1],5050)

if __name__ == '__main__':
    unittest.main()
