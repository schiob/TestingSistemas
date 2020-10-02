from unittest import mock
import unittest
from unittest.mock import patch,MagicMock
from primer_parcial import tri_from_file


class testMockPrimerParcial(unittest.TestCase):
    
    def test_equilatero(self):
        read_data='3 3 3'
        mock_open=mock.mock_open(read_data=read_data)
        with mock.patch('builtins.open',mock_open):
            result=tri_from_file('filename')
        self.assertEqual('Equilátero',result)

    def test_equilateroDos(self):
        read_data='5 5 5'
        mock_open=mock.mock_open(read_data=read_data)
        with mock.patch('builtins.open',mock_open):
            result=tri_from_file('filename')
        self.assertEqual('Equilátero',result)

    def test_isoceles(self):
        read_data='10 7 7'
        mock_open=mock.mock_open(read_data=read_data)
        with mock.patch('builtins.open',mock_open):
            result=tri_from_file('filename')
        self.assertEqual('Isóceles',result)

    def test_isocelesDos(self):
        read_data='4 5 4'
        mock_open=mock.mock_open(read_data=read_data)
        with mock.patch('builtins.open',mock_open):
            result=tri_from_file('filename')
        self.assertEqual('Isóceles',result)

    def test_noTriangulo(self):
        read_data='0 0 0'
        mock_open=mock.mock_open(read_data=read_data)
        with mock.patch('builtins.open',mock_open):
            result=tri_from_file('filename')
        self.assertEqual('No triángulo',result)

    def test_noTrianguloDos(self):
        read_data='0 5 7'
        mock_open=mock.mock_open(read_data=read_data)
        with mock.patch('builtins.open',mock_open):
            result=tri_from_file('filename')
        self.assertEqual('No triángulo',result)

    def test_escaleno(self):
        read_data='8 6 5'
        mock_open=mock.mock_open(read_data=read_data)
        with mock.patch('builtins.open',mock_open):
            result=tri_from_file('filename')
        self.assertEqual('Escaleno',result)

          

        
        

        
      

        

        


if __name__ == "__main__":
    unittest.main()

