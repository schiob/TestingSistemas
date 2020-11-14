import unittest
from segundoparcialapp import leer_prom_alumno
import tempfile

class test_Segundo_Parcial(unittest.TestCase):
    def test_uno(self):
        f=tempfile.NamedTemporaryFile(mode='w+')
        f.write('pepito mate 34.65\nmaria mate 88.34\npepito quimica 89.34\nmaria espanol 78.99')
        resultadoEsperado={'pepito': 61.995000000000005, 'maria': 83.66499999999999}
        f.seek(0)
        self.assertEqual(leer_prom_alumno(f.name),resultadoEsperado)
        f.close()

    def test_dos(self):
        f=tempfile.NamedTemporaryFile(mode='w+')
        f.write('juanito mate -56.77\npedrito espanol -99.99\njuanito quimica -67.88\npedrito mate -66.98')
        resultadoEsperado={'juanito': -62.325, 'pedrito': -83.485}
        f.seek(0)
        self.assertEqual(leer_prom_alumno(f.name),resultadoEsperado)
        f.close()

    def test_Tres(self):
        f=tempfile.NamedTemporaryFile(mode='w+')
        f.write('juanito mate 0\npedrito espanol 0\njuanito quimica 0\npedrito mate 0')
        resultadoEsperado={'juanito': 0, 'pedrito': 0}
        f.seek(0)
        self.assertEqual(leer_prom_alumno(f.name),resultadoEsperado)
        f.close()

if __name__ == "__main__":
    unittest.main()
    
