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


if __name__ == "__main__":
	main()
