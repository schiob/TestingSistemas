import sys
def calc(n, nums):
    pos = neg = par = imp = 0

    if len(nums) > n:
        print('Escribiste números de mas!!!')
        sys.exit()
    if len(nums) < n:
        print('Te faltaron números por escribir!!!')
        sys.exit()

    for i in nums:

        if i % 2 == 0:
                par = par + 1
        if i % 2 != 0:
                imp = imp + 1
        if i >= 0:
                pos = pos + 1
        if i < 0:
                neg = neg + 1

    return par, imp, pos, neg

if __name__ == '__main__':

    n = int(input('¿Con cuántos números vamos a trabajar? '))
    nums = list(map(int, input('Escribe los números separados por un espacio: ').split(" ")))
    res=calc(n, nums)

    print("Numero(s) Pares = {}".format(res[0]))
    print("Numero(s) Impares = {}".format(res[1]))
    print("Numero(s) Positivos = {}".format(res[2]))
    print("Numero(s) Negativos = {}".format(res[3]))
