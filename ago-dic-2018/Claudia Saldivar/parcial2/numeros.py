def numeros_impar(x,y):
    suma = 0

    if x < y:
        i = x
        for i in range(x,y):
            if i%2!=0:
                if i > x:
                    if i < y:
                        suma = suma + i

    elif y < x:
        i = y
        for i in range(y,x):
            if i%2!=0:
                if i > y:
                    if i < x:
                        suma = suma + i
    return suma

if __name__ == '__main__':
    n = list(map(int,input('INGRESA LOS DATOS:  ').split(" ")))
    res=numeros_impar(n[0],n[1])
    print('SUMA DE LOS NUMEROS IMPARES QUE INGRESASTE {}'.format(res))
