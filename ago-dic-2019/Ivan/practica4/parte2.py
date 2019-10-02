import unittest
from parte1 import clean_file
import os.path as path


def thereSpecials(text):
        for x in text:
            if not (unicode(x).isnumeric() or x.isalpha() or x==" " or x=="\n"):
                return True
        return False


class TestSum(unittest.TestCase):

    def prueba(self,filename):

        print "*"*50
        textfile=open(filename,'r')
        result = clean_file(textfile)#modulo a probar
        #print result
        self.assertTrue(result.islower() or result=="") #hay mayusculas
        self.assertFalse(thereSpecials(result)) #caracteres especiales aparte de espacio y salto de linea?
        self.assertTrue(textfile) #existe aror result==" "chivo?
        self.assertFalse(textfile==None) #esta vacio
        textfile.close()
        print "*"*50+"\n"



    def test_list_int(self):
        "PRUEBA A, EL ARCHIVO ESTA VACIO..."
        self.prueba("./pruebaA.txt")
        "PREUBA B, EL ARCHIVO NECESITA LIMPIARSE"
        self.prueba("./pruebaB.txt")
        "PRUEBA C, EL ARCHIVO NO NECESITA MODIFICARSE"
        self.prueba("./pruebaC.txt")




if __name__ == '__main__':
	unittest.main()
	#filename="./pruebaA.txt"
	#textfile=open(filename,'r')
	#result = clean_file(text)
	#print(thereSpecials(result))
