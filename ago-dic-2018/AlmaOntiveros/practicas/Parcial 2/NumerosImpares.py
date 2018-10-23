def calc(x , y):
    impares = 0

    if x > y:
        for num in range((y + 1), x):
            if num % 2:
                impares+= num

    for num in range((x + 1), (y - 1)):
        if num % 2:
            impares+= num
    return impares

if __name__ == '__main__':
    x , y = list(map(int,input('Escribe los números a evaluar (separados con un espacio entre ellos): ').split(" ")))
    resultado= calc(x , y)
    print("La suma de los números impares es = {}".format(resultado))