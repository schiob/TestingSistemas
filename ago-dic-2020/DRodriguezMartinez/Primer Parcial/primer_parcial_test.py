from  unittest import mock, TestCase
from primer_parcial import Tri_from_file

class Test_primer_parcial(TestCase):
    mocks = {"equi1": "3 3 3",
             "equi2": "5 5 5",
             "notri1": "0 0 0",
             "notri2": "0 5 7",
             "notri3": "1 2 3",
             "iso1": "10 7 7",
             "iso2": "4 5 4",
             "esca1": "8 6 5"
            }

#############
    def testEquilatero(self):
        esperado = "Equilátero"
        
        with mock.patch('primer_parcial.open') as mock_open:
            
            for m in [v for i,v in self.mocks.items() if "equi" in i]:           
                mock_open.return_value.__enter__.return_value.read.return_value = m
                real = Tri_from_file("mock")

                assert esperado == real

#############
    def testNoTri(self):
        esperado = "No triángulo"

        with mock.patch('primer_parcial.open') as mock_open:
            
            for m in [v for i,v in self.mocks.items() if "notri" in i]:                  
                mock_open.return_value.__enter__.return_value.read.return_value = m
                real = Tri_from_file("mock")

                assert esperado == real

#############
    def testIsoceles(self):
        esperado = "Isóceles"

        with mock.patch('primer_parcial.open') as mock_open:
            
            for m in [v for i,v in self.mocks.items() if "iso" in i]:                  
                mock_open.return_value.__enter__.return_value.read.return_value = m
                real = Tri_from_file("mock")

                assert esperado == real

#############
    def testEscaleno(self):
        esperado = "Escaleno"

        with mock.patch('primer_parcial.open') as mock_open:
            
            for m in [v for i,v in self.mocks.items() if "esca" in i]:                  
                mock_open.return_value.__enter__.return_value.read.return_value = m
                real = Tri_from_file("mock")

                assert esperado == real