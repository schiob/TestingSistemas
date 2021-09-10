import unittest #No se te olvide que el nombre el archivo bajo ningún motivo debe de ser "Unittest.py"
from practica2 import sm

print('\n "Todo bien, todo correcto, y yo que me alegro" \n')

class TestIgualdad(unittest.TestCase):

    def test1(self):
        rr = sm(93, 7) #rr singinfica resultado real
        self.assertEqual(rr, 100)

    def test2(self):
        rr = sm(23, -5)
        self.assertEqual(rr, 18)

    def test3(self):
        rr = sm(-24, -10)
        self.assertEqual(rr, -34)

    def test4(self):
        rr = sm(-22, 11)
        self.assertEqual(rr, -11)

    def test5(self):
        rr = sm(-6.5, -13)
        self.assertEqual(rr, -19.5)

    def test6(self):
        rr = sm(0, 0)
        self.assertEqual(rr, 0)

    def test7(self):
        rr = sm(67,84)
        self.assertNotEqual(rr, -187)

    def test8(self):
        rr = sm(20.7, 56.8)
        self.assertTrue(87.5)

if __name__ == '__main__':
    unittest.main()
