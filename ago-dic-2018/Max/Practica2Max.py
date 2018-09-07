def cal(N):
    Pos = 0
    Neg = 0
    Par = 0
    Impar = 0
    lista = [] #cree esta lista vacia para guardar los valores y poder ver mas tarde
    for n in N:
        if x >= 0:
            Pos= Pos + 1
            if (x%2)== 0:
                Par= Par + 1
            else:
                Impar= Impar + 1
        else:
            Neg= Neg + 1
            if (x%2)== 0:
                Par= Par + 1
            else:
                Impar= Impar + 1
    return Pos, Neg, Par, Impar
if  __name__ == '__main__':
    n = int(input())
    Nums = list(map(int, input().split(" ")))
    Res = calc(Nums)
    print("Par = {}".format(Res[0]))
    print("Impar = {}".format(Res[1]))
    print("Negativos = {}".format(Res[2]))
    print("Positivos = {}".format(Res[3]))
