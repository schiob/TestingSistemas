def numTriang(num):

    tn=int((num*(num+1))/2)
    return tn

if __name__ == '__main__':
    n=int(input("Posicion: "))

    resultado=numTriang(n)

    print("{}".format(resultado))
