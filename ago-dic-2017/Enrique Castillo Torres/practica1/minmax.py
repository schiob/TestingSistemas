import sys

def MinMax(num):
    sumaMin = 9999999999999999
    sumaMax = 0
    sumaTotal = sum(num)
    for i in range(5):
        numActual = sumaTotal - num[i]
        if numActual < sumaMin:
            sumaMin = numActual
        if numActual > sumaMax:
            sumaMax = numActual
    print (sumaMin, sumaMax)

num = list(map(int, input().strip().split(' ')))
MinMax(num)
