import unittest
import os
from unittest.mock import MagicMock
from main import showTacos, Taco, sqlite

class TestTacos(unittest.TestCase):
    def setUp(self):
        self.db = sqlite("test.db")
        cur = self.db.conn.cursor()
        cur.execute("CREATE TABLE TACOS (id INTEGER PRIMARY KEY AUTOINCREMENT,tortilla TEXT, guiso TEXT, salsa TEXT)")

        self.db.save(Taco("harina", "bistek", "roja"))
        self.db.save(Taco("harina", "picadillo", "verde"))

    def tearDown(self):
        os.remove("test.db")

    def testShowAll(self):
        entrada = [Taco("harina", "bistek", "roja"), Taco("harina", "picadillo", "verde")]
        salida_esperada = [Taco("harina", "bistek", "roja"), Taco("harina", "picadillo", "verde")]

        dbMock = MagicMock()
        dbMock.getAllTacos.return_value = entrada

        real = showTacos(dbMock)   
        self.assertEqual(salida_esperada, real)

    def test_integration(self):
        salida_esperada = [Taco("harina", "bistek", "roja"), Taco("harina", "picadillo", "verde")]

        real = showTacos(self.db)   
        self.assertEqual(salida_esperada, real)

if __name__ == "__main__":
    unittest.main()