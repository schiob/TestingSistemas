def contar(num):
	positivos = negativos = par = impar = 0
	for i in num:
		if i > 0:
			positivos +=1
		elif i < 0:
			negativos +=1
		if i % 2:
			par +=1
		else:
			impar +=1
	return positivos,negativos,impar,par

if __name__ == '__main__':
	lista=[1,2,3,4,-6]	
	r=int(contar(lista))
print("Numero(s) Positivo(s)= {}".format(r[0]))
print("Numero(s) Negativo(s)= {}".format(r[1]))
print("Numero(s) Par(es)= {}".format(r[2]))
print("Numero(s) Impar(es)= {}".format(r[3]))