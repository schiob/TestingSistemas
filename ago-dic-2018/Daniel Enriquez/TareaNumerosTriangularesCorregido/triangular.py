
def convertir(numero):
    prueba1=prueba2=prueba3=prueba4=prueba5=0

    prueba1 = (numero[0]*(numero[0]+1))/2
    prueba2 = (numero[1]*(numero[1]+1))/2
    prueba3 = (numero[2]*(numero[2]+1))/2
    prueba4 = (numero[3]*(numero[3]+1))/2
    prueba5 = (numero[4]*(numero[4]+1))/2
    return prueba1,prueba2,prueba3,prueba4,prueba5

if __name__ == '__main__':

    resultado=covertir(numero)

    print("  = {}".format(resultado[0]))
    print("  = {}".format(resultado[1]))
    print("  = {}".format(resultado[2]))
    print("  = {}".format(resultado[3]))
    print("  = {}".format(resultado[4]))
