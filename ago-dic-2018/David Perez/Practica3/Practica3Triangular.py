#La fórmula para cálcular el Triangular de un número n es:
# n(n+1) / 2
def Ctriangular(n):
    Triangular = ((n+1)*n)/2
    return Triangular

if __name__ == '__main__':
    n=int(input('Introduzca el número del que desea calcular su Triangular: '))

    res=Ctriangular(n)
    print("El Triangular de: {0} es: {1}".format(n,res))
