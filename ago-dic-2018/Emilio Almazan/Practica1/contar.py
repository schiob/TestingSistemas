positivos=0
negativos= 0
impar=0
par= 0
lista=[]

while True:
    try:
        n=int(input("Escribe la cantidad de numeros en la lista: "))
        numeros=input("Escribe los numeros de la lista separados por espacio: ")
        lista=[int(n) for n in numeros.split()]
        for i in range(0,n):
            num=lista[i]
            if num > 0:
                positivos+=1
            else:
                negativos+=1
            if num % 2 == 0 :
                par +=1
            else:
                impar+=1
        break
    except:
        print("ingrese SOLAMENTE numeros")
        pass
print(str(positivos) + " Numero(s) Positivo(s)")
print(str(negativos) + " Numero(s) Negativo(s)")
print(str(par) + " Numero(s) Par(es)")
print(str(impar) + " Numero(s) Impar(es)")
 


