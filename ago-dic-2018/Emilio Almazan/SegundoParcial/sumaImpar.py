def sumarImpares(t):
    x=t[0]

    y=t[1]

    sumaimpar=0

    if (x < y):
        for i in range(x+1, y):
            if i % 2 != 0:
                sumaimpar+=i
            else:
                sumaimpar=sumaimpar
    elif (x > y):
        for i in range(y+1, x):
            if i % 2 != 0:
                sumaimpar+=i
            else:
                sumaimpar=sumaimpar
    return sumaimpar

if __name__ == '__main__':

    t=list(map(int,input("Teclea el rango esperado separado en espacios. ").split(" ")))

    resultado=sumarImpares(t)
    
    print("la suma de impares es:", resultado)
