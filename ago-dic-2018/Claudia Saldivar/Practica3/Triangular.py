def numero_triangular(n):
    triangular = (n*(n+1))/2
    return triangular

if __name__ == '__main__':
    n = int(input('Introduce la posición del numero triangular: '))
    res = int(numero_triangular(n))
print('El numero tringular es: {}'.format(res))
