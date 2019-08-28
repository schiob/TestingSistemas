import math

def volCil(radio, altura):
    vol=math.pi*(radio*radio)*altura
    return vol

print("VOLUMEN DEL CILINDRO ")
radio=input("Radio: ")
altura=input("Altura: ")
v=volCil(radio, altura)
print("Volumen : "+v)