def sumatoria(rng):
    suma = 0
    rango=rng
    x= rango[0]
    y= rango[1]
    if (len(rango) > 2):
        print('Error, fuera del rango. Inserte sólo dos valores.')
    else:
        if (x < y):
            for i in range(x+1, y):
                if i%2==0:
                    suma=suma
                else:
                    suma+=i
        elif (x > y):
            for i in range(y+1, x):
                if i%2==0:
                    suma=suma
                else:
                    suma+=i
    return suma

if __name__ == '__main__':
    rng=list(map (int, input('Introduzca el rango X,Y (separado por espacio): ').split(" ")))
    res=sumatoria(rng)
    print(res)
