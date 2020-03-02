import unittest
from parcial1 import convertidor12to24

class TestParcial(unittest.TestCase):
    def test_convertidor(self):
        test = [
            {'input':"02:23p.m",
             'expect_out':"14:23hrs"},
            {'input':"11:42p.m",
             'expect_out':"23:42hrs"},
            {'input':"11:42a.m",
             'expect_out':"11:42hrs"},
             {'input':"12:00p.m",
             'expect_out':"12:00hrs"},
             {'input':"12:00a.m",
             'expect_out':"00:00hrs"},
             {'input':"01:05a.m",
             'expect_out':"01:05hrs"},
             {'input':"11:59p.m",
             'expect_out':"23:59hrs"},
        ]
        for tc in test:
            actual = convertidor12to24(tc['input'])
            self.assertEqual(tc['expect_out'],actual)

if __name__ == "__main__":
    unittest.main()