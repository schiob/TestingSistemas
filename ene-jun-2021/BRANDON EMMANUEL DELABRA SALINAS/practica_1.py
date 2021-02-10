
num = input('Ingresa 5 números').split()
numeros = list(map(int, num))

negative =0
positive = 0
par = 0 
impar = 0
ceros = 0

print (numeros)

for i in numeros:
        if int (i) < 0:
            negative += 1

        if int (i) > 0:
            positive += 1   

        if (int (i) % 2) == 0:
            par += 1

        if (int (i) % 2) != 0:
            impar += 1

        if i == 0:
            ceros += 1
        
print(f'{negative} número(s) negativo(s)\n'
          f'{positive} número(s) poditivo(s)\n'
          f'{par} número(s) par(es)\n'
          f'{impar} número(s) impa(es)\n'
          f'{ceros} número(s) neutro(s)')