def impar(a,b):
    suma = 0
    if a < b:
        i = a
        for i in range(a,b):
            if i%2!=0:
                if i > a:
                    if i < b:
                        suma = suma + i
    elif b < a:
        i = b
        for i in range(b,a):
            if i%2!=0:
                if i > b:
                    if i < a:
                        suma = suma + i
    return suma


if __name__ == '__main__':
    n = list(map(int,input('Dame los extremos del rango inferior  y superior(separados por espacio):').split(" ")))
    res=impar(n[0],n[1])
    print('La suma de los numeros impares es {}'.format(res))
