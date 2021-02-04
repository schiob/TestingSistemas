
def tipo_triangulo(a, b, c):

    if a <= 0 or b <= 0 or b <=0:
      return 'No es ningun triángulo'
    elif a > 10000 or a > 10000 or a > 10000:
            return 'Los lados del triangulo no pueden ser tan grandes'
    elif a == b and a == c:
        return 'Equilatero'
    elif a != b :
        return 'Escaleno'
    elif a != c:
        return 'Isósceles'
    else:
        return 'Ingrese un numero valido'

    
print(tipo_triangulo(7, 7, 7))
print(tipo_triangulo(7, 7, 9))
print(tipo_triangulo(7, 8, 10))
print(tipo_triangulo(1, 2, 3))
print(tipo_triangulo(8, -10, 5))
print(tipo_triangulo(9999999999, 88, 22))


