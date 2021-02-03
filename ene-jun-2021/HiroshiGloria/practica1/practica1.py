lista = input().split(" ")
j=False
while j == False:
    try:
        for i in range(len(lista)):
            lista[i]=int(lista[i])
        j=True
    except:
        print("Introduzca un número válido")
        lista = input().split(" ")

cpos=cneg=cpar=cimpar=0

for i in range(len(lista)):
    if lista[i]==0:
        cpar+=1
    else:
        if lista[i]>=0:
            cpos+=1
            if lista[i]%2==0:
                cpar+=1
            else:
                cimpar+=1
        else:
            cneg+=1
            if lista[i]%2==0:
                cpar+=1
            else:
                cimpar+=1

print(cpos," numero(s) positivo(s)")
print(cneg," numero(s) negativo(s)")
print(cpar," numero(s) par(es)")
print(cimpar," numero(s) impar(es)")