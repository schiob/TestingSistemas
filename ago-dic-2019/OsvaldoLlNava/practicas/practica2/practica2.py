ganancia = 0
marca = []
precio = []
entrada = input()
separador = entrada.split(" ")
N = int(separador[0])
x = int(separador[1])
respaldo1 = [] #Variable de respaldo para marca
respaldo2 = [] #Variable de respaldo para precio
mayor = 0
posicion = 0
marquita = ""
conteo=0
vendidos = 0
for i in range(0,N):
    entrada = input()
    separador =  entrada.split(" ")
    marca.append(separador[0])
    precio.append(int(separador[1]))


#print(marca, precio, N, x)


while(N > x):
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
        respaldo1.append(marca[posicion])
        respaldo2.append(precio[posicion])
        del marca[posicion]
        del precio[posicion]
    
    
    conteo = 0
    mayor = 0
    if(len(marca) == 0):
        break

if((len(marca) + len(respaldo1)) == x):
    print(vendidos, ganancia)
#print("Marca",marca, respaldo1) 
#print("Precio",precio, respaldo2) 
#print("N =", N, "x =", x,"ganancia", ganancia)