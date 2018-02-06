def tipo_triang(a,b,c):
    if -100 <= int(a) <= 100 and -100 <= int(b) <= 100 and -100 <= int(c) <= 100  :
        if  int(a)!=0 and int(b)!=0 and int(c)!=0 and int(a) + int(b) > int(c) and int(a) + int(c) > int(b) and int(b) + int(c) > int(a):
            if a == b and b == c:
                print("El triángulo es Equilatero\n")
                return 'Equilatero'
            elif a == b or a == c or b == c:
                print("El triángulo es Isósceles\n")
                return 'Isósceles'
            elif a != b and a != c and c != b:
                print("El triángulo es Escaleno")
                return 'Escaleno'
        else:
            print("No es triángulo")
    else:
        print("Los lados deben estar en este rango de -100 a 100")
if __name__ == '__main__':
    a,b,c = input('Pon 3 y comprobemos el tipo de triángulo:\n').split(' ')
    olakace = tipo_triang(a, b, c)
