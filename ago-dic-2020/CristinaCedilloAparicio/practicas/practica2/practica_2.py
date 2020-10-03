def pantalones(N,X,marca,precio):
    ganancia=0
    marca_respaldo=[] #Variable de respaldo para marca
    precio_respaldo=[] #Variable de respaldo para precio
    mayor=0
    posicion=0
    marquita=""
    conteo=0
    vendidos=0
    while(N > X):
        for i in range(0, len(precio)):
            if (precio[i] > mayor):
                mayor = precio[i]
                posicion = i
                marquita = marca[posicion]
        for i in range(0, len(marca)):
            if (marca[i] == marquita):
                conteo += 1
        if(conteo > 1):
            ganancia += precio[posicion]
            del marca[posicion]
            del precio[posicion]
            N -= 1
            vendidos += 1
        else:
            marca_respaldo.append(marca[posicion])
            precio_respaldo.append(precio[posicion])
            del marca[posicion]
            del precio[posicion]
        conteo = 0
        mayor = 0
        if(len(marca) == 0):
            break
    if((len(marca) + len(marca_respaldo)) == X):
        return vendidos, ganancia

if __name__=="__main__":
    print("Por favor, ingresa  el número de pantalones y la cantidad a la que deseas reducir tus pantalones. Separados por un espacio")
    N,X=input().split()
    N=int(N)
    X=int(X) #print(N,X)
    marca=[]
    precio=[]
    print("\nAhora ingresa la marca y precio de tus pantalones: ")
    for i in range(0,N):
        m,p=input().split()
        marca.append(m)
        precio.append(int(p))
        
    print(pantalones(N,X,marca,precio))
    