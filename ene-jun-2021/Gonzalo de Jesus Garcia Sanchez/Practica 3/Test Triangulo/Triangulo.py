def tipo_triangulo(a, b, c):
    
    if isinstance (a, str) or isinstance (b, str) or isinstance (c, str):
        return "No triangulo"
    if a <= 0 or b <= 0 or c <=0:
        return 'No es ningun triángulo, no se permiten numeros negativos o 0'
    elif a > 10000 or b > 10000 or c > 10000:
            return 'Los lados del triangulo no pueden ser tan grandes'
    elif a == b and a == c:
        return 'Equilatero'
    elif a != b :
        return 'Escaleno'
    elif a != c:
        return 'Isósceles'
    
