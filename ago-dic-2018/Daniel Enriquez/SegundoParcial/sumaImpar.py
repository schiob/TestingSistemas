lista=[]
guardaPar1,guardaPar2,guardaImpar1,guardaImpar2 =0,0,0,0
suma1=0
suma2=0
numeros = input('Dime los numeros: ')
for num in [int(n) for n in numeros.split(" ")]:
    lista.append(num)

primerElemento=lista[0]
UltimoElemento=lista[1]
inicio1=0
fin1=0

if(primerElemento>UltimoElemento):
    inicio1=UltimoElemento+1
    fin1=primerElemento-1
    for x in range(inicio1,fin1):
        if(x%2!=0):
            suma1=suma1+x
    print(suma1)

if(primerElemento<UltimoElemento):
    inicio2=primerElemento+1
    fin2=UltimoElemento-1
    for x in range(inicio2,fin2):
        if(x%2!=0):
            suma2=suma2+x
    print(suma2)

if(primerElemento==UltimoElemento):
    print('0')
