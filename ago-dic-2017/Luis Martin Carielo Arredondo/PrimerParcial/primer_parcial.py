def triangulo_desde_archivo(nombre_archivo):
	file = open(nombre_archivo)
	separando = file.read().split(" ")
	file.close()
	lado1 = int(separando[0])
	lado2 = int(separando[1])
	lado3 = int(separando[2])
	trian = ""

	if (lado1+lado2 > lado3) and (lado2+lado3 > lado1) and (lado3+lado1 > lado2):
		if lado1==lado2 and lado2==lado3:
			trian += "Equilátero."
		elif lado1==lado2 or lado2==lado3 or lado1==lado3:
			trian += "Isóceles."
		else:
			trian += "Escaleno."
	else:
		trian += "No es triangulo."
	return trian

def main():
	resultado = triangulo_desde_archivo("lados_triangulo.txt")
	print(resultado)


if __name__ == "__main__":
	main()