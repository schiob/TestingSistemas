#logica
def calculo(numero1, numero2):
    suma = numero1 + numero2
    return suma 

if __name__ == '__main__':
    numero1 = int(input("Primer numero: "))
    numero2 = int(input("Segundo numero: "))
    print(calculo(numero1, numero2))    
