import unittest
import Practica3

class TestNTriangulo(unittest.TestCase):
    def test_triangulo(self):
#Caso Prueba1
        total=Practica3.Prueba3NTriangulo(4)
        self.assertEqual(total, 10)

#Caso Prueba2
        total=Practica3.Prueba3NTriangulo(6)
        self.assertEqual(total, 21)

#Caso Prueba3
        total=Practica3.Prueba3NTriangulo(1)
        self.assertEqual(total, 1)

#Caso Prueba4
        total=Practica3.Prueba3NTriangulo(5)
        self.assertEqual(total, 15)

#Caso Prueba5
        total=Practica3.Prueba3NTriangulo(3)
        self.assertEqual(total, 6)

if __name__=='__main__':
    unittest.main()