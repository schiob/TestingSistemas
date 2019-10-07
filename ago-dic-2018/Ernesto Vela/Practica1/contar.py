pos = 0
neg = 0
par = 0
imp = 0
list = []
import sys

tot = int(input('¿Con cuántos números vamos a trabajar? '))
num = input('Escribe los números separados por un espacio: ')
list=[int(tot) for tot in num.split(" ")]
for i in range(0,tot):
    n = list[i]
    if len(list) > tot:
        print('Escribiste números de mas!!!')
        sys.exit()
    if len(list) < tot:
        print('Te faltaron números por escribir!!!')
        sys.exit()
    if n % 2 == 0:
            par = par + 1
    if n % 2 != 0:
            imp = imp + 1
    if n > 0:
            pos = pos + 1
    if n < 0:
            neg = neg + 1

print(str(par) + " Numero(s) Par" + '\n' + str(imp) + " Numero(s) Impar" + '\n' + str(pos) + " Numero(s) Positivos" + '\n' + str(neg) + " Numero(s) Negativos")
