import unittest
from unittest.mock import *
from practica4 import peticion_api



@patch('requests.post')
def test_practica4(self, mockpst):
    test = (   ("julio",   200, """{"INPUT":"julio", "OUTPUT":"JULIO"}""", "JULIO"),
                ("cesar", 200, """{"INPUT":"cesar", "OUTPUT":"CESAR"}""", "CESAR"),
                ("perez", 404, "404 page not found", "ERROR") )
    for input, st, mocktxt, expected in test:
        mockpst.return_value.status_code = st
        mockpst.return_value.text = mocktxt
        outpt = peticion_api(input)
        self.assertSequenceEqual(outpt, expected)


if __name__ == '__main__':
    unittest.main()