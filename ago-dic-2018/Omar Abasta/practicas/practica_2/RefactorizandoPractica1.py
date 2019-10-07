# RefactorizandoPractica1

"""Codigo que permite la identificacion de numeros enteros, ya sean positivos o
negativos, al igual que saber si son pares o impares"""


def calc(nums):  # Creando funcion
    par = impar = neg = pos = 0
    for i in nums:
        if i % 2 == 0:
            par += 1
        else:
            impar += 1
        if i < 0:
            neg = +1
        elif i > 0:
            pos += 1
    return par, impar, neg, pos


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, -9]
    resultado = calc(nums)
    print("numeros pares=  {}".format(resultado[0]))
    print("numeros impares= {}".format(resultado[1]))
    print("numeros negativos= {}".format(resultado[2]))
    print("numeros positivos= {}".format(resultado[3]))
