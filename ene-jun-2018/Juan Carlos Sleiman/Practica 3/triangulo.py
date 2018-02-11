def tipo_triang(a,b,c):
    if -100 <= a <= 100 and -100 <= b <= 100 and -100 <= c <= 100:
        if  a!=0 and b!=0 and c!=0 and a + b > c and a + c > b and b + c > a:
            if a == b and b == c:
                return 'Equilatero'
            elif a == b or a == c or b == c:
                return 'Isósceles'
            elif a != b and a != c and c != b:
                return 'Escaleno'
        else:
            return 'No es triangulo'
    else:
        print("Los lados deben estar en este rango de -100 a 100")

if __name__ == '__main__':

    a,b,c = input('Pon 3 y comprobemos el tipo de triángulo:\n').split(' ')
    a = int(a)
    b = int(b)
    c = int(c)
    olakace = tipo_triang(a, b, c)
    print(olakace)
