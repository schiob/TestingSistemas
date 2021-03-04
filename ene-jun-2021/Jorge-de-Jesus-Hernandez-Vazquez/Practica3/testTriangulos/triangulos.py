def tipo_triangulo(a, b, c):
    
    if isinstance(a, str) or isinstance(b, str) or isinstance(c, str):
        return 'Los valores no pueden contener letras'

    elif a <= 0 or b <= 0 or c <=0:
        return 'No es ningun triángulo'

    elif a > 10000 or b > 10000 or c > 10000  :
            return 'Los lados del triangulo no pueden ser tan grandes'

    elif a == b and a == c:
        return 'Equilatero'

    elif a != b :
        return 'Escaleno'
        
    elif a != c:
        return 'Isósceles'
