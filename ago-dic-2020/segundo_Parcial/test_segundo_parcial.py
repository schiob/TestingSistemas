
import tempfile
import unittest
import mock
import Segundo_Parcial
####### Test ######
class Test_primer_parcial(unittest.TestCase):
    def test_Prom_unitario(self):
        ######### Usando mock ###################
        
        with mock.patch("builtins.open", mock.mock_open(read_data="Laura_sanchez quimica 85.00\nLaura_sanchez espanol 85.00"), create=True) as mock_file:
            result = Segundo_Parcial.prom("path")
        mock_file.assert_called_once_with("path")
        with mock.patch("builtins.open", mock.mock_open(read_data="Laura_sanchez quimica 75.00\nRaul_martinez espanol 86.40"), create=True) as mock_file:
            resulta = Segundo_Parcial.prom("path")
        mock_file.assert_called_once_with("path")
        with mock.patch("builtins.open", mock.mock_open(read_data="Laura_sanchez quimica 75.00\nLaura_sanchez espanol 86.40\nRaul_Martinez ingles 95.20\nRaul_Martinez espanol 84.20"), create=True) as mock_file:
            resultb = Segundo_Parcial.prom("path")
        mock_file.assert_called_once_with("path")
        
        self.assertEqual(result,{'Laura_sanchez': 85.00})
        self.assertEqual(resulta,{'Laura_sanchez': 75.00, 'Raul_martinez': 86.40})
        self.assertEqual(resultb,{'Laura_sanchez': 80.70, 'Raul_Martinez': 89.70})
    def test_Prom_integracion(self):
       ###############crear y abrir el archivo#############
        f = tempfile.NamedTemporaryFile(mode='w+')
      
        f.write("Laura_sanchez quimica 75.00 Laura_sanchez espanol 86.40 Raul_Martinez ingles 95.20 Raul_Martinez espanol 84.20")
        f.seek(0)
        result = Segundo_Parcial.prom(f.name) 
        self.assertEqual(result,{'Laura_sanchez': 80.70, 'Raul_Martinez': 89.70})
      
        f.close()


        
        
if __name__ == '__main__':
    unittest.main()
    
    