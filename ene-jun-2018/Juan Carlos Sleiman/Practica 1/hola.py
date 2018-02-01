a,b,c,d,e = input('Pon 5 numeros').split(' ')
pos = 0
neg = 0
par = 0
imp = 0
		
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

print (str(pos) + " n¨²mero(s) positivo(s)" )
print (str(neg) + " n¨²mero(s) negativos(s)" )
print (str(par) + " n¨²mero(s) par(es)" )
print (str(imp) + " n¨²mero(s) impar(es)" )
=======

>>>>>>> 2dd99c514cf8ed99536dc5d8d8d5ca4bd29f6ab4
