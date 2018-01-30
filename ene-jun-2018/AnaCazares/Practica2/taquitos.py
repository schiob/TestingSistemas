#creando una variable (string ) de tipo 'lista'
Tacos=list((input("Ingresa la orden de tacos, separado por espacios solo puedes pedir 30 tacos: ").split()))
#imprimiendo la lista 'tacos'
print(Tacos)
#declaracion de tacos

#creando variables acumuladores
cachete=0
lengua=0
tripas=0
pastor=0
machito=0
#usando un ciclo para recorrer las palabras ingresados
for x in Tacos:
    if x == "cachete":
        cachete+=1
    elif x == "lengua":
        lengua+=1
    elif x == "tripas":
        tripas+=1
    elif x == "pastor":
        pastor+=1
    else:
        machito+=1

#print(cachete,"cahete")
#print(lengua,"lengua")
#print(tripas,"tripas")
#print(pastor,"pastor")
#print(machito,"machito")
print("total" , cachete*13 + lengua*10 + tripas*9 + pastor*15 + machito*14 )
