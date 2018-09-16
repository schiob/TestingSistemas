import random
print("ingrese cuantos numeros aleatorios desea obtener")
n=int(input())

aleatorio=[random.randint(-100,100) for _ in range(n)]
print(aleatorio)

ContadorPar=int(0);
ContadorImpar=int(0);
ContadorPositivo=int(0);
ContadorNegativo=int(0);

le = len(aleatorio)
control = 0

while(control < le):
    valor = aleatorio[control]

    if(valor%2==0):
        ContadorPar=ContadorPar+1;
    else:
        ContadorImpar=ContadorImpar+1;

    if (valor>0):
        ContadorPositivo=ContadorPositivo+1;
    else:
        ContadorNegativo=ContadorNegativo+1;

    control = control + 1

print("cantidad de numeros pares: "+str(ContadorPar));
print("cantidad de numeros impares " +str(ContadorImpar));
print("cantidad de numeros positivos: " +str(ContadorPositivo));
print("cantidad de numeros negativos "+str(ContadorNegativo));
