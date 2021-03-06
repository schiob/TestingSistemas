import unittest
import requests
from unittest.mock import patch
from pract4 import reQst 


class TestReQst(unittest.TestCase):

    @patch('requests.post')
    def test_mock(self, mockpst):
        cases = (   ("marte",   200, """{"INPUT":"marte", "OUTPUT":"MARTE"}""", "MARTE"),
                    ("jupiter", 200, """{"INPUT":"jupiter", "OUTPUT":"JUPITER"}""", "JUPITER"),
                    ("saturno", 404, "404 page not found", "****ERROR****") )

        for inp, st, mocktxt, esp in cases:
            mockpst.return_value.status_code = st
            mockpst.return_value.text = mocktxt
            outpt = reQst(inp)
            self.assertSequenceEqual(outpt, esp)



if __name__ == '__main__':
    unittest.main()