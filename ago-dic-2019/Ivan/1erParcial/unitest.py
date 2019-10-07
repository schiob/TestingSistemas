import unittest
from ok24to12 import timestr

class TestSum(unittest.TestCase):

	def test_list_int(self):
    
		lista_entradas=[]
		lista_entradas.append("14:23hrs")
		lista_entradas.append("23:42hrs")
		lista_entradas.append("11:42hrs")
		lista_entradas.append("00:00hrs")
		lista_entradas.append("12:00hrs")
		lista_entradas.append("01:05hrs")
		lista_entradas.append("23:59hrs")

		salidas_esperadas=[]
		salidas_esperadas.append("02:23p.m.")
		salidas_esperadas.append("11:42p.m.")
		salidas_esperadas.append("11:42a.m.")
		salidas_esperadas.append("12:00p.m.")
		salidas_esperadas.append("12:00p.m.")
		salidas_esperadas.append("01:05p.m.")
		salidas_esperadas.append("11:59p.m.")




		#lista_salidas_esperadas.append("<\"14:23hrs\",\"02:23p.m.\">")	
		i=0
		for x in lista_entradas:
			print("<\"{},{}\">".format(x,timestr(salidas_esperadas[i])))
			i=i+1


		print(lista_entradas[0])
		print(salidas_esperadas[0])
		self.assertTrue(salidas_esperadas[0],timestr(lista_entradas[0]))
		self.assertTrue(salidas_esperadas[1],timestr(lista_entradas[1]))
		self.assertTrue(salidas_esperadas[2],timestr(lista_entradas[2]))
		self.assertTrue(salidas_esperadas[3],timestr(lista_entradas[3]))
		self.assertTrue(salidas_esperadas[4],timestr(lista_entradas[4]))
		self.assertTrue(salidas_esperadas[5],timestr(lista_entradas[5]))
		self.assertTrue(salidas_esperadas[6],timestr(lista_entradas[6]))




		
if __name__ == '__main__':
	unittest.main()