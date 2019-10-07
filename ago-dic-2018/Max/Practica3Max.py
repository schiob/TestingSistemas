def calc(n): #Un numero triangular es aquel que se puede reacomodar para formar un triangulo equilatero
        NumTtri = ((n*(n+1)))/2 #La formula de obtene run numer triangular es "Tn = (n(n+1))/2"
        return NumTtri

if __name__ == '__main__':
    n = int(input('Dame el numero: '))
    resultado = int(calc(n))
    print('El resultado del numero triangular " {} ", es el " {} "'.format(n, resultado))
