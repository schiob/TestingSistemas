import unittest

def sumImpares(x, y):
    sum = 0
    y2 = x
    x2 = y
    if x<y:
        for i in range(x+1, y):
            if i%2!=0:
               sum +=i
        print(sum)
        return sum
    else:
        for i in range(x2+1, y2):
            if i%2!=0:
               sum += i
        print(sum)
        return sum

class Pruebas(unittest.TestCase):
    def test1(self):
        self.assertEqual(sumImpares(6, -5), 5)
    def test2(self):
        self.assertEqual(sumImpares(12, 15), 13)
    def test3(self):
        self.assertEqual(sumImpares(12, 12), 0)
    def test4(self):
        self.assertEqual(sumImpares(123, 321), 21756)
    def test5(self):
        self.assertEqual(sumImpares(4321, 1234), 4284911)
    def test6(self):
        self.assertEqual(sumImpares(-19289, 7853), -77593260)

if __name__ == "__main__":
    unittest.main()

