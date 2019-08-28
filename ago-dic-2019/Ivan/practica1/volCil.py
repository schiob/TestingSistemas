import math

def volCil(radio, altura):
    vol=math.pi*(radio*radio)*altura
    return vol


if __name__ == "__main__":
    
	print("VOLUMEN DEL CILINDRO ")
	radio=input("Radio: ")
	altura=input("Altura: ")
	v=volCil(radio, altura)
	print("Volumen : "+str(v))