import unittest
from unittest.main import main
from taquitos import tacosCheco
class testTacos(unittest.TestCase):
    def test1(self):
        orden = ["pastor", "cachete", "machito", "pastor", "tripita", "cachete"]
        entrada = tacosCheco(orden)
        self.assertEqual(entrada, 79)

    def test2(self):
        orden = ["cachete", "lengua", "tripita", "pastor", "machito"]
        entrada = tacosCheco(orden)
        self.assertEqual(entrada, 61)

    def test3(self):
        orden = ["pastor", "cachete", "pastor", "lengua", "pastor", "lengua", "machito", "machito", "pastor"]
        entrada = tacosCheco(orden)
        self.assertEqual(entrada, 121)

if __name__ == "__main__":
    unittest.main()