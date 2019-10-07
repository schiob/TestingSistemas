import sys
sys.stdin
class triangulo ():
    def compruebaRango(self):
        for x in lados:
            if (x>-100) and (x<100):
                i = 1
            else:
                i = 0  
        return i      

    def imprime(l):
        if (l[0]+l[1])>l[2] and (l[0]+l[2])>l[1] and (l[1]+l[2])>l[0]:
            if (l[0]==l[1]==l[2]):
                return("equilatero")
            elif(l[0]==l[1] or l[0]==l[2] or l[1]==l[2]):
                return("isoceles")
            else:
                return("escaleno")
        else:
            return("no triangulo")    

if __name__ == '__main__':
    lados= list(map(int, input().strip().split(' ')))
    if triangulo.compruebaRango(lados) == 1 :
        triangulo.imprime(lados)
    else:
        print("recuerda Int (-101 < x < 101)")
