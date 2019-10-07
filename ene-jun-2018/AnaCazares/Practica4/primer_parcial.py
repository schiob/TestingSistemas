def IMC_desde_archivo(nombre_archivo):
	file = open(nombre_archivo)
	separando = file.read().split(" ")
	file.close()
	altura = float(separando[0])
	peso = float(separando[1])
	trian = ""

	return peso/altura**2


def main():
	resultado = IMC_desde_archivo("IMC.txt")
	print(resultado)
	
def imprimir_archivo(IMCTxt):
	file = open(IMCTxt)	
	return file.read()
	
def escribir_archivo(IMCTxt, contenido):
	file = open(IMCTxt, "w")
	file.write(contenido)

#def main():
	escribir_archivo("IMC.txt", "1.34 65")
	print(imprimir_archivo("IMC.txt"))

if __name__ == "__main__":
	main()
