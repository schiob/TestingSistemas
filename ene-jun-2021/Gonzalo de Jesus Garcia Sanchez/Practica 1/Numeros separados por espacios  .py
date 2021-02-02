#   51 -12 -3 0 2
#   Gonchologon
def practica1(lista):
    pares, impares, positivo, negativo = 0, 0, 0, 0 #CREAMOS UN CONTADOS DE PAR IMPAR POSI NEGAT INICIALIZANDOLOS EN 0
   
    for n in lista: #Pasamos por cada numero que hay en la lista
        if n % 2 == 0:      #PARES
            pares += 1
        else:               #IMPARES
             impares += 1
        if n >0:            #POSOTIVO
            positivo += 1
        if n < 0:           #NEGATIVO
            negativo += 1
    return pares, impares, positivo, negativo #RETORNAMOS LA LISTA PRIMER LUGAR PARES 2DO IMPARE ETC ETC

Entrada_de_Numeros = input("Ingrese 5 numeros separados por un espacio:  ").split(" ") #INGRECION DE NUMEROS SEPARADOS POR UN ESPACIO
numero0= int(Entrada_de_Numeros[0]) #VUELVO  LOS NUMEROS QUE VOY METIENDO A LA LISTA SEPARADOS POR UN ESPACIO A ENTEROS RESPECTIVAMENTE EN SU ESPACIO
numero1= int(Entrada_de_Numeros[1])
numero2= int(Entrada_de_Numeros[2]) 
numero3= int(Entrada_de_Numeros[3])
numero4= int(Entrada_de_Numeros[4]) 

numeros = [numero0,numero1,numero2,numero3,numero4]#LOS NUMEROS QUE SAQUE PREVIAMENTE UNO POR UNO RESPECTO A SU POCICION LOS PONGO EN UNA LISTA
resultado = practica1(numeros) #SE LLAMA A LA FUNCION PRACTICA1 Y  LA [ASAMOS COMO ARGUMENTO A LA LISTA DE NUMEROS

print('La Cantidad de Numeros Positivos son: %i' % resultado[2])  #INSPECCIONAMOS TERCERA POCICION DE RESULTADO POSITIVOS
print('La Cantidad de Numeros Negativos son: %i' % resultado[3])  #INSPECCIONAMOS CUARTA  POCICION DE RESULTADO NEGATIVOS
print('La Cantidad de Numeros Pares son: %i' % resultado[0])      #INSPECCIONAMOS PRIMERA POCICION DE RESULTADO PARES
print('La Cantidad de Numeros Impares son: %i' % resultado[1])    #INSPECCIONAMOS SEGUNDA POCICION DE RESULTADO IMPARES