import unittest
import Alfanumericos
"""
def Quitar_especiales(direccion):
    archivo = open(direccion, "r")
    texto = archivo.read()
    archivo.close()
    cadena=''

    for i in range(0,len(texto)):
        if texto[i].isalnum() or texto[i]=='\n' or texto[i]==' ':
            cadena = cadena + texto[i]

    cadena = cadena.lower()

    return cadena
    """

class test(unittest.TestCase):

    def test_vacio(self):
        ruta='C:\\Users\\Osvaldo Nava\\Desktop\\uni\\7-Semestre\\calidad\\Practica4\\vacio.txt'
        self.assertEqual(Alfanumericos.Quitar_especiales(ruta),'')

    def test_sinquitar(self):
        ruta='C:\\Users\\Osvaldo Nava\\Desktop\\uni\\7-Semestre\\calidad\\Practica4\\sinquitar.txt'
        self.assertEqual(Alfanumericos.Quitar_especiales(ruta),'fuego123 y arroz')

    def test_quitar(self):
        ruta='C:\\Users\\Osvaldo Nava\\Desktop\\uni\\7-Semestre\\calidad\\Practica4\\quitar.txt'
        self.assertEqual(Alfanumericos.Quitar_especiales(ruta),'fuego123 y arroz')

if __name__ == '__main__':
    unittest.main()