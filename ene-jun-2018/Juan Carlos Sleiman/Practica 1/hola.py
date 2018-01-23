a,b,c,d,e = input('Pon 5 numeros').split(' ')
		
if int(str(a)) > 0:
	pos = pos + 1
elif int(str(a)) < 0:
		neg = neg + 1
if int(str(b)) > 0:
	pos = pos + 1
elif int(str(b)) < 0:
		neg = neg + 1
if int(str(c)) > 0:
	pos = pos + 1
elif int(str(c)) < 0:
		neg = neg + 1
if int(str(d)) > 0:
	pos = pos + 1
elif int(str(d)) < 0:
		neg = neg + 1
if int(str(e)) > 0:
	pos = pos + 1
elif int(str(e)) < 0:
		neg = neg + 1

	
if int(str(a))%2 == 0:
	par = par+1
else:
	imp = imp + 1
if int(str(b))%2 == 0:
	par = par+1
else:
	imp = imp + 1
if int(str(c))%2 == 0:
	par = par+1
else:
	imp = imp + 1
if int(str(d))%2 == 0:
	par = par+1
else:
	imp = imp + 1
if int(str(e))%2 == 0:
	par = par+1
else:
	imp = imp + 1

print (str(pos) + " número(s) positivo(s)" )
print (str(neg) + " número(s) negativos(s)" )
print (str(par) + " número(s) par(es)" )
print (str(imp) + " número(s) impar(es)" )