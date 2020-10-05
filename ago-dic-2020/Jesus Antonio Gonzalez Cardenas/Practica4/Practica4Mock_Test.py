import unittest
import Practica4
import mock

class csvTest(unittest.TestCase):
    doml = ['hotmail.com', 'protonmail.com']
    
    @mock.patch('Practica4.getDomains', return_value = doml)
    def test_acces_file(self, mock_get):
        data_expected = {'hotmail.com': 81.33, 'protonmail.com': 88.33}
        self.assertEqual(Practica4.getAverages("Practica4TData.csv"),data_expected)
       


if __name__ == '__main__':
    unittest.main()