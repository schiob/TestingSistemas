
def convertir(numero):
    prueba1=prueba2=prueba3=prueba4=prueba5=0
    for num in numero:
            if(num==1):
                prueba1=(num*(num +1))/2
            elif(num==3):
                prueba2=(num*(num +1))/2
            elif(num==4):
                prueba3=(num*(num +1))/2
            elif(num==56):
                prueba4=(num*(num +1))/2
            elif(num==400):
                prueba5=(num*(num +1))/2

    return prueba1,prueba2,prueba3,prueba4,prueba5

if __name__ == '__main__':

    resultado=covertir(numero)

    print("  = {}".format(resultado[0]))
    print("  = {}".format(resultado[1]))
    print("  = {}".format(resultado[2]))
    print("  = {}".format(resultado[3]))
    print("  = {}".format(resultado[4]))
