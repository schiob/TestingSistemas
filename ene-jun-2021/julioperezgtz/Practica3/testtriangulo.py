import unittest


from triangulo import tri

class Testtria(unittest.testcase):
    def test_triangulos(self):
        tcs=(
            [4,4,4,"Equilatero"],
            [1,3,3,"Isoceles"],
            [2,3,4,"Escaleno"],
            [3,3,4,"Isoceles"],
            [0,4,3,"No triangulo"],
            [0,0,0,"No triangulo"],
            [1,2,-1,"no triangulo"]
        )
        for t in tcs:
            self.assertEqual(tri(t[0],t[1],t[2],t[3]))

if __name__ == '__main__':
    unittest.main()