def Ntriangular(n):
    NTriangular = (n*(n+1))/2
    return NTriangular

if __name__ == '__main__':
    n=int(input('Introduzca el número del que desea calcular su Triangular: '))

    res=Ntriangular(n)
    print("{1} es el {0} número triangular".format(n,res))
