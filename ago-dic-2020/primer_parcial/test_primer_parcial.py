import unittest
import mock
import primer_parcial
####### Test ######
class Test_primer_parcial(unittest.TestCase):
    def test_TestEquilatero(self):
        ######### Usando mock ###################
        with mock.patch("builtins.open", mock.mock_open(read_data="3 3 3"), create=True) as mock_file:
            result = primer_parcial.tri_from_file("path")
        mock_file.assert_called_once_with("path")
          ######### Usando archivo ###################
        resultf = primer_parcial.tri_from_file("equi2.txt")
        
        self.assertEqual(result,"Equilátero")
        self.assertEqual(resultf,"Equilátero")

    
    def test_TestNoTri(self):
        ######### Usando mock ###################
        with mock.patch("builtins.open", mock.mock_open(read_data="0 0 0"), create=True) as mock_file:
            result = primer_parcial.tri_from_file("path")
        mock_file.assert_called_once_with("path")
         ######### Usando archivo ###################
        resultf = primer_parcial.tri_from_file("notri2.txt")
        ######### Usando mock ###################
        with mock.patch("builtins.open", mock.mock_open(read_data="1 2 3"), create=True) as mock_file:
            resulta = primer_parcial.tri_from_file("path")
        mock_file.assert_called_once_with("path")
        
        self.assertEqual(resulta,"No triángulo")
        self.assertEqual(result,"No triángulo")
        self.assertEqual(resultf,"No triángulo")

       
    def test_TestIsoceles(self):
        ######### Usando archivo ###################
        resulta = primer_parcial.tri_from_file("iso1.txt")
        ######### Usando mock ###################
        with mock.patch("builtins.open", mock.mock_open(read_data="4 5 4"), create=True) as mock_file:
            result = primer_parcial.tri_from_file("path")
        mock_file.assert_called_once_with("path")
        
        self.assertEqual(resulta,"Isóceles")
        self.assertEqual(result,"Isóceles")

        
    def test_TestEscaleno(self):
        ######### Usando mock ###################
        with mock.patch("builtins.open", mock.mock_open(read_data="8 6 5"), create=True) as mock_file:
            result = primer_parcial.tri_from_file("path")
        mock_file.assert_called_once_with("path")
        self.assertEqual(result,"Escaleno")

    
        
if __name__ == '__main__':
    unittest.main()
    
    
    
    
