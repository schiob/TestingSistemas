def cuentaimpares(input):
    suma = 0
    lista=[int(i) for i in input.split()]
    lista.sort()
    rangoinf = lista[0] + 1
    for i in range(rangoinf,lista[1]):
         if i % 2:
            suma += i
    return suma

if __name__ == '__main__':
    input=input('Teclea 2 numeros para saber la suma de los impares entre ellos (sepáralos con espacios): ')
    print(cuentaimpares(input))
