import unittest
from parte1 import clean_file
import os.path as path


def thereSpecials(text):
    for x in text:
        if not (unicode(x).isnumeric() or x.isalpha() or x==" " or x=="\n"):
            return True
    return False

def openMock(file):
	return file

def closeMock(file):
	file=None

file1=" "

file2=""
file2+="HOLA MUNDO"
file2+="ESTA Y LA ANTERIOR LINEA ERAN MAYUSCULAS"
file2+="menos las siguientes lineas"
file2+="ahora probemos los simbolos"
file2+="@!#$%&/()=?"
file2+="por cierto!!! se guardaron los" 
file2+="espacio y saltos de lineas."
file2+="se removieron algunos caracteres"


file3=""
file3+="HOLA MUNDO"
file3+="ESTA Y LA ANTERIOR LINEA ERAN MAYUSCULAS"
file3+="menos estas lineas"
file3+="por los simbolos no te preocupes no le puse"
file3+="por cierto se guardaron los "
file3+="espacio y saltos de lineas"
file3+="asi que no hay nada que remover"





class TestSum(unittest.TestCase):




	def test_list_int(self):
		print "Prueba A, el archivo esta vacio..."
		self.prueba(file1)
		self.prueba(file2)
		self.prueba(file3)

		

		# filename="./pruebaA.txt"

	def prueba(self,filename):

		print "*"*50
		textfile=openMock(filename)
		result = clean_file(textfile)#modulo a probar
		#print result
		self.assertTrue(result.islower() or result==" ") #hay mayusculas
		self.assertFalse(thereSpecials(result)) #caracteres especiales aparte de espacio y salto de linea?
		self.assertTrue(textfile) #existe archivo?
		self.assertFalse(textfile==None) #esta vacio
		closeMock(filename)
		print "*"*50+"\n"

if __name__ == '__main__':
	unittest.main()
	#filename="./pruebaA.txt"
	#textfile=open(filename,'r')
	#result = clean_file(text)
	#print(thereSpecials(result))
