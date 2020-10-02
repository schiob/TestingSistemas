def tipo_triangulo(archivo):
    a = open(archivo)
    l = list(map(int, a.read().strip().split(' ')))
    l1 = l[0]
    l2 = l[1]
    l3 = l[2]
    triangulo = 0
    if(l1 + l2) > l3 or (l1+ l3) > l2 or (l2 + l3) > l1:
        for x in l:
            if x <= 0:
                triangulo+=1
        if triangulo != 0:
            return "No triángulo"

        elif l1 == l2 and l1 == l3:
            return "Equilatero"

        elif l1 == l2 and l1 != l3:
            return "Isóceles"
        elif l1 == l3 and l1 != l2:
            return "Isóceles"
        elif l2 == l3 and l2 != l1:
            return "Isóceles"


        elif l1 or l2 or l3 != 1 or 2 or 3:
            if l1 != l2 and l1 != l3 and l2 != l3:
                return "Escaleno"
            return "No Triángulo"
    else:
        return "No triángulo"
    a.close()
if __name__ == '__main__':
    print (tipo_triangulo('C:/Users/Crist/Documents/notri1.txt'))