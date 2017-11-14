def imprimir_archivo(puntoTxt):
	file = open(puntoTxt)	
	return file.read()

def escribir_archivo(puntoTxt, contenido):
	file = open(puntoTxt, "w")
	file.write(contenido)

def main():
	escribir_archivo("test.txt", "LuCa")
	print(imprimir_archivo("test.txt"))

if __name__ == "__main__":
	main()