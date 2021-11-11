def numbers(expected):
    positive = 0
    negative = 0
    even = 0
    odd = 0
    for i in expected:
        if i > 0:
            positive = positive + 1
            if i % 2 == 0:
                even = even + 1
            else:
                odd = odd + 1
        elif i < 0:
            negative = negative + 1
            if i % 2 == 0:
                even = even + 1
            else:
                odd = odd + 1
        elif i == 0:
            even = even + 1

    return(f'{positive} positivos, {negative} negativos, {even} pares, {odd} impares')

if __name__ == '__main__':
    num = int(input('Tamaño de la lista:'))
    expected = []
    for i in range(num):
        i = int(input("Ingrese el numero:"))
        expected.append(i)