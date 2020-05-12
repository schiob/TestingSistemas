import unittest
import os
from unittest.mock import MagicMock
from Promedio import prom

class Test_Promedio(unittest.TestCase):
    def setup(self):
        f = open("Calificaciones.txt","w+")
        f.write('''
        Jose_Lopez quimica 89.00\n
        Jose_Lopez matematicas 85.34\n
        Maria_Martinez fisica 95.50\n
        Maria_Martinez español 90.00\n
        ''')
    def tearDown(self):
        os.remove("Calificaciones.txt")
    
    def Read(self):
        entrada = "Calificaciones.txt"
        salida = [['Jose_Lopez', 'quimica', '89.00'], ['Jose_Lopez', 'matematicas', '85.34'], ['Maria_Martinez', 'fisica', '95.50'], ['Maria_Martinez', 'espaÃ±ol', '90.00']]
    def promedio(self):
        entrada= [['Jose_Lopez', 'quimica', '89.00'], ['Jose_Lopez', 'matematicas', '85.34'], ['Maria_Martinez', 'fisica', '95.50'], ['Maria_Martinez', 'espaÃ±ol', '90.00']]
        salida_esperada =[['Jose_Lopez', 87.17],['Maria_Martinez', 92.75]]

if __name__ == '__main__':
    unittest.main()