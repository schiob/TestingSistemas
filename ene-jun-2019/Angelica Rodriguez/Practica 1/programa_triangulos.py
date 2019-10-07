"""
Programa que lee tres números enteros y a partir de ellos,
define si éstos forman un triángulo, en caso de ser así,
indica el tipo de triángulo según sus lados.
"""
# Leer tres números enteros
#num1, num2, num3 = list(map(int, input().strip().split()))

def ladosTriangulo(num1, num2, num3):
    try:
        # No se puede formar un triángulo si la suma de dos de sus lados es
        # menor o igual al tercer lado

        if num1 >= (num2 + num3) or num2 >= (num1 + num3) or num3 >= (num1 + num2):
            return "No triángulo"
        elif num1 == num2 == num3:    # tres lados iguales
            return "Equilátero"
        elif num1 == num2 or num2 == num3 or num1 == num3:    # dos lados iguales
            return "Isósceles"
        else:
            return "Escaleno"   # si no es isosceles, ni equilátero, es escaleno :D
    except:
        return "Entrada incorrecta"

if __name__ == '__main__':
    num1, num2, num3 = list(map(int, input().strip().split()))
    print(ladosTriangulo(num1,num2,num3))
