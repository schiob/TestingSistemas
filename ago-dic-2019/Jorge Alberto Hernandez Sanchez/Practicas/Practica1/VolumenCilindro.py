import math
Radio = int (input("Dame el radio: "))
Altura = int(input("Dame la altura: "))

def VolumenCilindro(num1, num2):
 Resultado = float(math.pi *(math.pow(num1, 2)) * (num2))
 return Resultado


print("El Volumen del cilindro es: ", VolumenCilindro(Radio, Altura))