import math

r=input("Escribe el radio del cilindro: ")
h=input("Escribe la altura del cilindro: ")
def my_volumen(r, h):
    return str(math.pi*math.pow(float(r), 2)*float(h))

print("El volumen del cilindro es "+my_volumen(r,h))
