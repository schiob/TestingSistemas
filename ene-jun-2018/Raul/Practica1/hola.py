pares=0
impares=0
positivo=0
negativo=0
a,b,c,d,e = input().split(' ')

if int(str(a))>0:
    positivo=positivo + 1
elif int(str(a))<0:
    negativo=negativo + 1

if int(str(a))%2==0:
    pares= pares + 1
else:
    impares=impares + 1

if int(str(b))>0:
    positivo=positivo + 1
elif int(str(b))<0:
    negativo=negativo + 1

if (-1)**int(str(b)) == 1:
    pares= pares + 1
else:
    impares=impares + 1

if int(str(c))>0:
    positivo=positivo + 1
elif int(str(c))<0:
    negativo=negativo + 1

if (-1)**int(str(c)) == 1:
    pares= pares + 1
else:
    impares=impares + 1

if int(str(d))>0:
    positivo=positivo + 1
elif int(str(d))<0:
    negativo=negativo + 1

if (-1)**int(str(d)) == 1:
    pares= pares + 1
else:
    impares=impares + 1

if int(str(e))>0:
    positivo=positivo + 1
elif int(str(e))<0:
    negativo=negativo + 1

if (-1)**int(str(e)) == 1:
    pares= pares + 1
else:
    impares=impares + 1

print(positivo,'numero(s)', 'positivo(s)')
print(negativo,'numero(s)', 'negativo(s)')
print(pares,'numero(s)', 'par(es)')
print(impares,'numero(s)', 'impar(es)')



    
    
    
