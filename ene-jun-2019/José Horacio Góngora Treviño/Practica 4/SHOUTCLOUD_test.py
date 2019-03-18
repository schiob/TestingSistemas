import unittest
import SHOUTCLOUD
from unittest.mock import patch

class ShoutCloud(unittest.TestCase):
    @patch('requests.post')

    def test_Shout(self, mock_post):
        test_cases = (("hola", "HOLA"),
                      ("adios", "ADIOS"),
                      ("tacos", "TACOS"),
                      ("hamburquesa", "HAMBURQUESA")
                      )

        for entrada,esperado in test_cases:
            mock_post.return_value.text = entrada
            SHOUTCLOUD.mayusculas(esperado)

if __name__ == '__main__':
    unittest.main()