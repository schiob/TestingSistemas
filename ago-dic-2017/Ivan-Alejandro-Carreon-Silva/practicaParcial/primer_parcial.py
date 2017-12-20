def tipo_triangulo(path):
    f = open(path)
    #return f.read()
    lados = list(map(int, f.read().strip().split(' ')))

    ntriangulo = 0
    lado1 = lados[0]
    lado2 = lados[1]
    lado3 = lados[2]

    if(lado1 + lado2) > lado3 or (lado1 + lado3) > lado2 or (lado2 + lado3) > lado1:
        for i in lados:
            if i <= 0:

                ntriangulo+=1

        if ntriangulo is not 0:
            return "No triángulo"

        elif lado1 == lado2 and lado1 == lado3:
            return "Equilatero"

        elif lado1 == lado2 and lado1 is not lado3:
            return "Isóceles"
        elif lado1 == lado3 and lado1 is not lado2:
            return "Isóceles"
        elif lado2 == lado3 and lado2 is not lado1:
            return "Isóceles"


        elif lado1 or lado2 or lado3 is not 1 or 2 or 3:
            if lado1 is not lado2 and lado1 is not lado3 and lado2 is not lado3:
                return "Escaleno"
            return "No Triángulo"


    else:
        return "No triángulo"
    f.close()

if __name__ == '__main__':
    print (tipo_triangulo("archivoP1.txt") )
