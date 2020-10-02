import unittest
import mock
import primer_parcial
####### Test ######
class Test_primer_parcial(unittest.TestCase):
    def test_eqilatero_1(self):
        ######### Usando mock ###################
        with mock.patch("builtins.open", mock.mock_open(read_data="3 3 3"), create=True) as mock_file:
            result = primer_parcial.tri_from_file("path")
        mock_file.assert_called_once_with("path")
        self.assertEqual(result,"Equilátero")

    def test_eqilatero_2(self):
        ######### Usando archivo ###################
        result = primer_parcial.tri_from_file("equi2.txt")
        self.assertEqual(result,"Equilátero")
    
    def test_no_triangulo_1(self):
        ######### Usando mock ###################
        with mock.patch("builtins.open", mock.mock_open(read_data="0 0 0"), create=True) as mock_file:
            result = primer_parcial.tri_from_file("path")
        mock_file.assert_called_once_with("path")
        self.assertEqual(result,"No triángulo")

    def test_no_triangulo_2(self):
        ######### Usando archivo ###################
        result = primer_parcial.tri_from_file("notri2.txt")
        self.assertEqual(result,"No triángulo")

    def test_no_triangulo_3(self):
        ######### Usando mock ###################
        with mock.patch("builtins.open", mock.mock_open(read_data="1 2 3"), create=True) as mock_file:
            result = primer_parcial.tri_from_file("path")
        mock_file.assert_called_once_with("path")
        self.assertEqual(result,"No triángulo")

    def test_isoceles_1(self):
        ######### Usando archivo ###################
        result = primer_parcial.tri_from_file("iso1.txt")
        self.assertEqual(result,"Isóceles")

    def test_isoceles_2(self):
        ######### Usando mock ###################
        with mock.patch("builtins.open", mock.mock_open(read_data="4 5 4"), create=True) as mock_file:
            result = primer_parcial.tri_from_file("path")
        mock_file.assert_called_once_with("path")
        self.assertEqual(result,"Isóceles")

    def test_escaleno_1(self):
        ######### Usando mock ###################
        with mock.patch("builtins.open", mock.mock_open(read_data="8 6 5"), create=True) as mock_file:
            result = primer_parcial.tri_from_file("path")
        mock_file.assert_called_once_with("path")
        self.assertEqual(result,"Escaleno")

    
        
if __name__ == '__main__':
    unittest.main()
    
    