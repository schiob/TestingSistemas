import unittest
from primer_parcial import triangulo

class TestPrimerParcial(unittest.TestCase):

    def setUp(self):
            equi1 = open("equi1.txt","w").write("3 3 3")
            equi2 = open("equi2.txt","w").write("5 5 5")
            notri1 = open("notri1.txt","w").write("0 0 0")
            notri2 = open("notri2.txt","w").write("0 5 7")
            notri3 = open("notri3.txt","w").write("1 2 3")
            iso1 = open("iso1.txt","w").write("10 7 7")
            iso2 = open("iso2.txt", "w").write("4 5 4")
            esca1 = open("esca1.txt","w").write("8 6 5")


    def testEquilatero(self):
        self.assertEqual(triangulo("equi1.txt"),"Equilatero")

        self.assertEqual(triangulo("equi2.txt"),"Equilatero")


    def testNoTri(self):
        self.assertEqual(triangulo("notri1.txt"),"No triangulo")

        self.assertEqual(triangulo("notri2.txt"),"No triangulo")

        self.assertEqual(triangulo("notri3.txt"),"No triangulo")


    def testIsoceles(self):
        self.assertEqual(triangulo("iso1.txt"),"Isosceles")

        self.assertEqual(triangulo("iso2.txt"),"Isosceles")

    def testEscaleno(self):
        self.assertEqual(triangulo("esca1.txt"),"Escaleno")



if __name__ == '__main__':
    unittest.main()
