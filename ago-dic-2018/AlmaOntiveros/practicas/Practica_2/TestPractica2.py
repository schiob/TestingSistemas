import unittest
import Practica2

class TestPractica2 (unittest.TestCase):
    def test_numeros(self):
#Caso de Prueba1
        total=Practica2.calc([5,-8,32,0,4])
        self.assertEqual(total[0], 3)
        self.assertEqual(total[1], 1)
        self.assertEqual(total[2], 1)
        self.assertEqual(total[3], 3)

#Caso de Prueba2
        total=Practica2.calc([10,9,-3,1,6])
        self.assertEqual(total[0], 2)
        self.assertEqual(total[1], 3)
        self.assertEqual(total[2], 1)
        self.assertEqual(total[3], 4)

#Caso de Prueba3
        total=Practica2.calc([-5,100,-12,2,7])
        self.assertEqual(total[0], 3)
        self.assertEqual(total[1], 2)
        self.assertEqual(total[2], 2)
        self.assertEqual(total[3], 3)

#Caso de Prueba4
        total=Practica2.calc([55,21,-123,543,90])
        self.assertEqual(total[0], 1)
        self.assertEqual(total[1], 4)
        self.assertEqual(total[2], 1)
        self.assertEqual(total[3], 4)

#Caso de Prueba5
        total=Practica2.calc([0,40,-1,-1000,66])
        self.assertEqual(total[0], 3)
        self.assertEqual(total[1], 1)
        self.assertEqual(total[2], 2)
        self.assertEqual(total[3], 2)
if __name__=='__main__':
    unittest.main()