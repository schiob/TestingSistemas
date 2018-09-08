def numtriangular(n):
    triangular = (n*(n+1))/2
    return triangular

if __name__ == '__main__':
    n = int(input('Introduce la posición del numero triangular: '))
    resultado = int(numtriangular(n))
    print('El numero tringular es: {}'.format(resultado))
