import unittest
<<<<<<< HEAD
import Practica4
import mock

class csvTest(unittest.TestCase):
    doml = ['hotmail.com', 'protonmail.com']
    
    @mock.patch('Practica4.getDomains', return_value = doml)
    def test_acces_file(self, mock_get):
        data_expected = {'hotmail.com': 81.33, 'protonmail.com': 88.33}
        self.assertEqual(Practica4.getAverages("Practica4TData.csv"),data_expected)
       

=======
import unittest.mock
from unittest.mock import MagicMock

class csvTest(unittest.TestCase):
    def test_fake_csv(self):
        resultdict = {'hotmail.com': 81.33, 'protonmail.com': 88.33}
        fake_csv = str(
            "juan,juan@hotmail.com,85\n"
            "pedro,pedro@protonmail.com,90\n"
            "lucy,lucy@hotmail.com,89\n"
            "john,john@protonmail.com,100\n"
            "carlos,carlos@hotmail.com,70\n"
            "adriana,adriana@protonmail.com,75\n"
                                                )
        mock_csv = MagicMock(return_value = fake_csv)
        self.assertEqual(getAverages(mock_csv),resultdict)
        
if __name__=='__main__':
  unittest.main()
>>>>>>> c151a235c5fc7360b9826adcf9ef8328ec7326a8

if __name__ == '__main__':
    unittest.main()