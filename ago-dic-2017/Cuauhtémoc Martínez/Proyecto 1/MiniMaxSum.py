import sys

def MinMax(num):
    sumaMin = 999999999999999
    sumaMax = 0
    sumaTotal = sum(num)
    for i in range(5):
        numActual = sumaTotal - num[i]
        if numActual < sumaMin:
            sumaMin = numActual
        if numActual > sumaMax:
            sumaMax = numActual
    return "{0} {1}".format(sumaMin, sumaMax)


if __name__ == '__main__':
    num = list(map(int, input().strip().split(' ')))
    MinMax(num)
