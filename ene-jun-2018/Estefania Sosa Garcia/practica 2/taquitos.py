import sys
sys.stdin
cadena = list(input().strip().split(' '))
tacos={"cachete":13,"lengua":10,"tripitas":9,"pastor":15,"machito":14}
suma=0
if (len(cadena) > 30):
    print("solo maximo 30 taquitos")
else:
    for x in cadena:
        if x in tacos:
            suma=suma+tacos[x]
print(suma)