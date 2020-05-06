import unittest
import numpy

def lados(x, y, z):
    vol = x*y*z
    return vol

def contenedor(cont):
    total = 0
    for i in cont:
        total+= numpy.prod(i)
    return total

def main_fun(x,y,z,total):
    caja1 = lados(x,x,x)
    caja2 = lados(y,y,y)
    caja3 = lados(z,z,z)
    count = 0
    ls = []
    while total > caja1:
        total -=caja1
        count+=1
    if total < caja1:
        ls.append([count,caja1])
        count = 0
    while total > caja2:
        total -= caja2
        count += 1
    if total < caja2:
        ls.append([count,caja2])
        count=0
    while total > 0:
        total -= caja3
        count += 1
    ls.append([count,caja3])
    return ls
        
class test(unittest.TestCase):
    def test_lados(self):
        SalidaEserada=5*4*3
        self.assertEqual(SalidaEserada, lados(5,4,3))
    def test_contenedor(self):
        SalidaEsperada=(5*4)+(2*3)+(6*2)
        self.assertEqual(SalidaEsperada, contenedor(([5,4],[2,3],[6,2])))
    def main_fun(self):
        salida_esperada = [[1,4],[1,3],[2,2]]
        self.assertEqual(salida_esperada, main_fun(4,3,2,100))
if __name__ == "__main__":
    unittest.main()