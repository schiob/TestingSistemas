import math

def volumen_cilindro(radio,altura):
    print("Funcion que calcula el volumen de un cilindro")
    volumen=math.pi*radio**2*altura
    return volumen

if __name__ == '__main__':
   print(volumen_cilindro(3,4))
