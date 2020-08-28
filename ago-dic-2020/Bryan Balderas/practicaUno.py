import sys


sys.stdout.write("Escribe los numeros a sumar")
sys.stdout.flush()
n=sys.stdin.readline()
m=list(map(float,n.split()))
if len(m) > 2:
    print('inserta solo dos numeros')
else:
    print(sum(m))

