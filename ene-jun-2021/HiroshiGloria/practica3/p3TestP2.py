import unittest
from practica2 import triangulos as trian

class practica2TestingMethods(unittest.TestCase):
    ### solo para tener algo que hacer commit
    def testEquilatero(self):
        l = [3,3,3]
        a = trian(l)
        self.assertEqual(a,"Es equilatero.")

    def testIsoceles(self):
        l = [3,3,1]
        a = trian(l)
        self.assertEqual(a,"Es isoceles.")

    def testEscaleno(self):
        l = [2,3,4]
        a = trian(l)
        self.assertEqual(a,"Es escaleno.")

    def testNotBuildable(self):
        l = [1,1,2]
        a = trian(l)
        self.assertEqual(a,"No se puede construír.")

    def testNotBuildableCeros(self):
        l = [0,3,2]
        a = trian(l)
        self.assertEqual(a,"No se puede construír.")

if __name__ == '__main__':
    unittest.main()