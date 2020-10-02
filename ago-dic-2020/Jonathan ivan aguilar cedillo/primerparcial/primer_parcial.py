def tipo_triangulo(path):
    f = open(path)
    lados = list(map(int, f.read().strip().split(' ')))
    nt= 0
    l1 = lados[0]
    l2 = lados[1]
    l3 = lados[2]

    if(l1 + l2)>l3 and (l1+l3)>l2 and (l2+l3)>l1: #teorema de la desigualdad del triángulo
        for i in lados:
            if i <= 0:
                nt+=1

        if nt is not 0:
            return "No triángulo"

        elif l1 == l2 and l1 == l3: 
            return "Equilatero"

        elif l1 == l2 and l1 is not l3:
            return "Isóceles"
        elif l1 == l3 and l1 is not l2:
            return "Isóceles"
        elif l2 == l3 and l2 is not l1:
            return "Isóceles"

        elif l1 or l2 or l3 is not 1 or 2 or 3:
            if l1 is not l2 and l1 is not l3 and l2 is not l3:
                return "Escaleno"
            return "No Triángulo"


    else:
        return "No triángulo"
    f.close()

if __name__ == '__main__':
    print (tipo_triangulo("triangulos.txt") )