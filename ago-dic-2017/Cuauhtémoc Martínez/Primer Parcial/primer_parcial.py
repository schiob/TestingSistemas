def triangulo(path):
    f = open(path)
    lados = list(map(int, f.read().strip().split(' ')))

    NT = 0
    l1 = lados[0]
    l2 = lados[1]
    l3 = lados[2]


    if (l1 + l2) > l3 and (l1 + l3) > l2 and (l2 + l3) > l1:
        for x in lados:
            if x <= 0:
                NT += 1

        if NT is not 0:
            return "No triangulo"

        elif l1 == l2 and l1 == l3:
            return "Equilatero"

        elif l1 == l2 and l1 is not l3:
            return "Isosceles"
        elif l1 == l3 and l1 is not l2:
            return "Isosceles"
        elif l2 == l3 and l2 is not l1:
            return "Isosceles"

        elif l1 is not l2 and l1 is not l3 and l2 is not l3:
            return "Escaleno"

    else:
        return "No triangulo"
    f.close()



if __name__ == '__main__':
    print (triangulo("Test.txt"))
