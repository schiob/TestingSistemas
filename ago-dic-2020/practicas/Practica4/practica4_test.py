import unittest
from unittest import mock, TestCase


class TestPractica4(unittest.TestCase):

    test_cases = (
            {
                "filename": "Datos.csv",
                "esperado": {'hotmail.com': 84.0, 'gmail.com': 89.0, 'outlook.com': 74.0},
                "hasError": False

            })

