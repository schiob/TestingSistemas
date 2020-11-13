def triangulo(path):
    f = open(path)
    #return f.read()
    lados = list(map(int, f.read().strip().split(' ')))

    
    lado1 = lados[0]
    lado2 = lados[1]
    lado3 = lados[2]


    if (lado1 + lado2) > lado3 and (lado1 + lado3) > lado2 and (lado2 + lado3) > lado1:

        if (lado1 == lado2 == lado3):
            return 'Equilatero'

        elif (lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
            return 'Isosceles'

        else:
            return 'Escaleno'

    else:
        return 'No es triangulo'
    f.close()




if __name__ == '__main__':
    print (triangulo("prueba.txt") )