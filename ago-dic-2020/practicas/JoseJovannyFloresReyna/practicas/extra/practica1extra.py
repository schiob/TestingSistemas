
def sumImpares(x, y):
    sum = 0
    y2 = x
    x2 = y
    if x<y:
        for i in range(x+1, y):
            if i%2!=0:
               sum +=i
        print(sum)
        return sum
    else:
        for i in range(x2+1, y2):
            if i%2!=0:
               sum += i
        print(sum)
        return sum


entrada = input("Extremos del rango: ")
separador = entrada.split(" ")
x = int(separador[0])
y = int(separador[1])
sumImpares(x, y)
