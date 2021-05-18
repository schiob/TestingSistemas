from typing import Union
from unittest.mock import MagicMock, patch
import unittest
from badwords import bad_words, check_badwords


class TestBadWords(unittest.TestCase):
    def test_badwords(self):

        cases  = (	((["popo", "sangre", "muerte", "maldito"], "El animal maldito se acercó con una mirada de muerte. Manchas de sangre cubrían el suelo", "kawai"), "El animal kawai se acercó con una mirada de kawai. Manchas de kawai cubrían el suelo"),
                    ((["popo", "sangre", "muerte", "maldito"], "El animal maldito se acercó con una mirada de muerte. Manchas de sangre cubrían el suelo", "suave"), "El animal suave se acercó con una mirada de suave. Manchas de suave cubrían el suelo"),    
                    ((["popo", "sangre", "muerte", "maldito"], "El animal maldito se acercó con una mirada de muerte. Manchas de sangre cubrían el suelo", "gei"),  "El animal gei se acercó con una mirada de gei. Manchas de gei cubrían el suelo"))   
                   
        for inptt, esp in cases:
            
            prm = bad_words(inptt[0], inptt[1], inptt[2])
            self.assertEqual(prm, esp)

    @patch("badwords.check_badwords")
    def test_check_badwords(self, mokos):

        cases  = (	( (["popo", "sangre", "muerte", "maldito"], "El animal maldito se acercó con una mirada de muerte. Manchas de sangre cubrían el suelo", "kawai", 88), "Es válido"),
                    ( (["popo", "sangre", "muerte", "maldito"], "El animal maldito se acercó con una mirada de muerte. Manchas de sangre cubrían el suelo", "suave", 89), "No es valido"),    
                    ( (["popo", "sangre", "muerte", "maldito"], "El animal maldito se acercó con una mirada de muerte. Manchas de sangre cubrían el suelo", "gei",   40), "No es valido"))  
        
        for inpt,  esp in cases:
            sgn = check_badwords(inpt[0], inpt[1], inpt[2], inpt[3])
            self.assertEqual(sgn, esp)

if __name__ == "__main__":
    unittest.main()