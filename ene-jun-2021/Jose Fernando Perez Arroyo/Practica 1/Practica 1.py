cadena= input("Dame una lista de numeros: ").split(" ")
d=list(cadena)
tam=len(cadena)
d= list(map(int, d))
print(d)
cpo, cne, cim, cpar=0, 0, 0, 0
for x in d:
    if x <0:
       cne = cne+1
    if x>0:
       cpo=cpo+1
    if x % 2==0:
        cpar=cpar+1
    else:
        cim=cim+1
print (cpo, 'número(s) positivo(s)')
print (cne, 'número(s) negativos(s)')
print (cpar, 'número(s) pares(s)')
print (cim, 'número(s) impares(s)')

