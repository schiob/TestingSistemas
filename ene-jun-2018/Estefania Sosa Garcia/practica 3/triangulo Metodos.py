import sys
sys.stdin

def compruebaRango(lados):
    for x in lados:
        if (x>-100) and (x<100):
            i = 1
        else:
            i = 0  
    return i      

def imprime(lados):
    if (l[0]+l[1])>l[2] and (l[0]+l[2])>l[1] and (l[1]+l[2])>l[0]:
        if (l[0]==l[1]==l[2]):
            print("equilatero")
        elif(l[0]==l[1] or l[0]==l[2] or l[1]==l[2]):
            print("isoceles")
        else:
            print("escaleno")
    else:
        print("no triangulo")    

if __name__ == '__main__':
    l= list(map(int, input().strip().split(' ')))
    if compruebaRango(l) == 1:
        imprime(l)
    else:
        print("recuerda Int (-101 < x < 101)")




