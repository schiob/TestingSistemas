#Escribe un pequeño programa que tome 2 números de STDIN y muestre el resultado de su suma.

print("Programa que pide dos números y te regresa la suma")

def superfuncionint():
    global suma
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    suma = num1 + num2

def superfuncionfloat():
    global suma
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    suma = num1 + num2

unauotra = input("Su número contiene decimales? (introduzca si o no): ")

if unauotra == "si":
    superfuncionfloat()
else:
    superfuncionint()

print("La suma de los numeros que se introdujeron es: ")
print(suma)