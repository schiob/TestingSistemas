import unittest
from unittest import mock
from unittest.mock import patch
from parcial_2 import get_averages, get_names

class segundo_parcial_unit_tests(unittest.TestCase):
    mock_data = [['Jose_Lopez', 'quimica', '89.00'], ['Jose_Lopez', 'matematicas', '85.34'], ['Maria_Martinez', 'fisica', '95.50'], ['Maria_Martinez', 'español', '90.00']]
    @patch('parcial_2.read_alumn_data', return_value= mock_data)
    def test_get_names(self,read_alumn_data):
        set1 = ['Jose_Lopez', 'Maria_Martinez']
        list1 = read_alumn_data("mock")
        list_names = get_names(list1)
        self.assertEqual(set1,list_names)
    
    mock_data = [['Jose_Lopez', 'quimica', '89.00'], ['Jose_Lopez', 'matematicas', '85.34'], ['Maria_Martinez', 'fisica', '95.50'], ['Maria_Martinez', 'español', '90.00']]
    @patch('parcial_2.read_alumn_data', return_value= mock_data)
    def test_promedios(self,read_alumn_data):
        set1 = {'Jose_Lopez': 87.17, 'Maria_Martinez': 92.75}
        list1 = read_alumn_data("mock")
        test1 = get_averages(list1)
        self.assertEqual(set1,test1)
    
    mock_data = [['Jose_Lopez', 'quimica', '0'], ['Jose_Lopez', 'matematicas', '0'], ['Maria_Martinez', 'fisica', '0'], ['Maria_Martinez', 'español', '0']]
    @patch('parcial_2.read_alumn_data', return_value= mock_data)
    def test_calificaciones_con_cero(self,read_alumn_data):
        set1 = {'Jose_Lopez': 0.0, 'Maria_Martinez': 0.0}
        list1 = read_alumn_data("mock")
        test1 = get_averages(list1)
        self.assertEqual(set1,test1)

    mock_data = []
    @patch('parcial_2.read_alumn_data', return_value= mock_data)
    def test_calificaciones_vacias(self,read_alumn_data):
        set1 = {}
        list1 = read_alumn_data("mock")
        test1 = get_averages(list1)
        self.assertEqual(set1,test1)
       





if __name__=='__main__':
    unittest.main()