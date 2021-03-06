import unittest
import csv
from io import StringIO
from Problema_2 import calculo_de_promedio
from unittest.mock import MagicMock, patch

class test_problema_2 (unittest.TestCase):

    
    def creacion_de_archivo():

        #Escritura del archivo en memoria
        w = csv.writer(StringIO)
        campos = ['usuario', 'correo', 'puntos']
        writer = csv.DictWriter(archivo, campos = campos)
        writer.writeheader()
        writer.writerow({'usuario': 'Tom', 'correo': 'tomas@hotmail.com', 'puntos': '85'})
        writer.writerow({'usuario': 'Juan','correo': 'juan@hotmail.com', 'puntos': '75'})
        writer.writerow({'usuario': 'Maria','correo': 'maria84@gmail.com', 'puntos': '90'})
        writer.writerow({'usuario': 'Paco' ,'correo': 'paquito123@outlook.com', 'puntos': '74'})
        writer.writerow({'usuario': 'Ana' ,'correo': 'anaa22@gmail.com', 'puntos': '88'})
        writer.writerow({'usuario': 'Marcos', 'correo': 'marcosss@hotmail.com', 'puntos': '92'})

    @patch('archivo.csv')
    def test_reader(self, mock):

        mock.writer = MagicMock(writerow = MagicMock())

        creacion_de_archivo()

        self.assertSetEqual(calculo_de_promedio(mock.writer()), "
        hotmail.com 84.0
        hotmail.com 84.0
        outlook.com 74.0")