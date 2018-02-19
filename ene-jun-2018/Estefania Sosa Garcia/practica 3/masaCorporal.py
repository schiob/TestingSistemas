import sys
import os

sys.stdin
class masaCorporal():
	def masaCORP(self):
		self.masa=[]
		mc =float( self.masa[0] / ( self.masa[1] * self.masa[1] ))
		archivo = open("imc.txt","r+")
		archivo.write("%.2f" % mc)
		


if __name__ == '__main__':
	entrada= list(map(float, input().strip().split(' ')))

	main()

