import unittest
from primer_parcial import tipo_triangulo

class TestParcial(unittest.TestCase):
    def test_Equilatero(self):
        entrada='C:/Users/Crist/Documents/equi1.txt'
        salida_esperada="Equilatero"
        salida_real=tipo_triangulo(entrada)
        self.assertEqual(salida_real,salida_esperada)

        entrada='C:/Users/Crist/Documents/equi2.txt'
        salida_esperada="Equilatero"
        salida_real=tipo_triangulo(entrada)
        self.assertEqual(salida_real,salida_esperada)
    
    def test_Notri(self):
        entrada='C:/Users/Crist/Documents/notri1.txt'
        salida_esperada="No triángulo"
        salida_real=tipo_triangulo(entrada)
        self.assertEqual(salida_real,salida_esperada)

        entrada='C:/Users/Crist/Documents/notri2.txt'
        salida_esperada="No triángulo"
        salida_real=tipo_triangulo(entrada)
        self.assertEqual(salida_real,salida_esperada)

        entrada='C:/Users/Crist/Documents/notri3.txt'
        salida_esperada="No triángulo"
        salida_real=tipo_triangulo(entrada)
        self.assertEqual(salida_real,salida_esperada)

    def test_Isosceles(self):
        entrada='C:/Users/Crist/Documents/iso1.txt'
        salida_esperada="Isóceles"
        salida_real=tipo_triangulo(entrada)
        self.assertEqual(salida_real,salida_esperada)

        entrada='C:/Users/Crist/Documents/iso2.txt'
        salida_esperada="Isóceles"
        salida_real=tipo_triangulo(entrada)
        self.assertEqual(salida_real,salida_esperada)

    def test_Escaleno(self):

        entrada='C:/Users/Crist/Documents/esca1.txt'
        salida_esperada="Escaleno"
        salida_real=tipo_triangulo(entrada)
        self.assertEqual(salida_real,salida_esperada)

    
           
            

if __name__=="__main__":
    unittest.main()

    