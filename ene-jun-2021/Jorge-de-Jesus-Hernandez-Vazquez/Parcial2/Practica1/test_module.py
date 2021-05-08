import unittest
import requests
from unittest.mock import patch
from module import file_method, upper_case, main_method
 

class testFile(unittest.TestCase):


    def test_file(self, mockss):
        param = """ 
    El archivito no estaba pero mientras ve este bonito perrito:
                   ▄              ▄
                  ▌▒█           ▄▀▒▌
                  ▌▒▒█        ▄▀▒▒▒▐
                 ▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐
               ▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐
             ▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌
            ▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌
            ▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐
           ▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌
           ▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌
          ▌▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐
          ▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌
          ▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐
           ▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌
           ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐
            ▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌
              ▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀
                ▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀
                   ▒▒▒▒▒▒▒▒▒▒▀▀     
        """
        cases = (   ("other.txt", "other.txt, ['AYUDAAAAAAAAAAAAAAAAAAAAAAAAaaa']", ['AYUDAAAAAAAAAAAAAAAAAAAAAAAAaaa']),
                    ("whatever",  f"whatever, {param}", param)  )
        for inp, mock, esp in cases:
            mockss.return_value = mock
            outputs = file_method(inp)
            self.assertRaises(outputs, esp)

class testRequests(unittest.TestCase):

    @patch('requests.post')
    def test_mock(self, mockpst):
        cases = (   ("hola",   200, """{"INPUT":"hola",   "OUTPUT":"HOLA"}""", "HOLA"),
                    ("sabado", 200, """{"INPUT":"sabado", "OUTPUT":"SABADO"}""", "SABADO"),
                    ("jorge",  404, "404 page not found", "****ERROR****") )

        for inp, st, mock, esp in cases:
            mockpst.return_value.status_code = st
            mockpst.return_value.text = mock
            outpt = upper_case(inp)
            self.assertSequenceEqual(outpt, esp)


class testMain(unittest.TestCase):
    pass



if __name__=="__main__":
    unittest.main()