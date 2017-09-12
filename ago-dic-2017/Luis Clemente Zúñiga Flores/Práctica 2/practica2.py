import os
import tempfile

def printFile(ruta):
	with open(ruta,'r+') as f:
		a = f.read()
	return a
	
def writeFile(ruta, texto):
	f = open(ruta,'w')
	f.write(texto)
	f.close()
	return printFile(f.name)
