from unittest import TestCase, mock
import unittest
from Parcial_2 import leer_archivo
class TestMockValue(TestCase):


    @mock.patch("__main__.leer_archivo")
    def test_get_text(self, mock_response):
        mock_response.return_value = "Jose_Lopez quimica 89.00"
        response = leer_archivo()
        self.assertEqual(response, "Jose_Lopez 89.00")

if __name__=="__main__":
    unittest.main()