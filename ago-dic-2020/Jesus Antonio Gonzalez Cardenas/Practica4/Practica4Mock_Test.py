from Practica4 import getAverages
import unittest
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

