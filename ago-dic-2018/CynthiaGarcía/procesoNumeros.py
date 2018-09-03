print("Cuántos números quieres procesar?")
cantidad=int(input())
print("ingresa los números")
#lista=[]
par=0
impar=0
npos=0
neg=0
for i in range(0, cantidad):
	nums=float(input())
	if nums%2==0:
		par=par+1
	else:
		impar=impar+1

	if nums>=0:
		npos=npos+1
	elif nums<0:
		neg=neg+1

#print(lista[0:cantidad-1])
print (npos, "numero(s)", "positivos")
print (neg, "numero(s)", "negativos")
print (par, "numero(s)", "pares")
print (impar,"numero(s)", "impares")