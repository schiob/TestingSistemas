import unittest
from Contenedores import *

class TestContenedores(unittest.TestCase):
    
    def test_cont(self):
        test = [
            {
            'input' : 3,
            'expect_out' : 27
        },
        {
            'input' : 5,
            'expect_out' : 125
        }
    ]

    for tc in test:
        r = volumen(tc['input'])
        self.assertEquals(tc['expect_out'], r)

