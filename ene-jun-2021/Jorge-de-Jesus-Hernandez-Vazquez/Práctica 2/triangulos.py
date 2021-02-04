def tipo_triangulo(a, b, c):
    
    if a <= 0 or b <= 0 or b <=0:
        return 'No es ningun triángulo'
    elif a > 10000 or a > 10000 or a > 10000  :
            return 'Los lados del triangulo no pueden ser tan grandes'
    elif a == b and a == c:
        return 'Equilatero'

    elif a != b :
        return 'Escaleno'
        
    elif a != c:
        return 'Isósceles'

print(tipo_triangulo(7, 7, 7))
print(tipo_triangulo(7, 7, 9))
print(tipo_triangulo(7, 8, 10))
print(tipo_triangulo(1, 2, 3))
print(tipo_triangulo(1, -10, 4))
print(tipo_triangulo(10, -10, 10))
print(tipo_triangulo(0, 0, 0))
print(tipo_triangulo(9999999999, 88, 22))

'''trian(10, 77 , 6)
trian(4,  41 , 99)
trian(90, 90 , 90)
trian(9,  3 ,  9)
trian(56, 8 ,  9)
trian(77, 77 , 9)
trian(12, 18 , 9)
trian(5,  5 ,  5)
trian(5,  5 ,  5)
'''