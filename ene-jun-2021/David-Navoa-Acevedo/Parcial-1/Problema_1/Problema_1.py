
def numero_triangular(dato):

    #Check del tipo de variable
    check = 1
    if type(dato) != type(check):
        return "No se permiten valores distintos al entero"
    #Check de las reglas de los numeros triangulares
    if dato < 0:
        return "No hay numeros triangulares negativos"
    #Formula dada por wikipedia
    n = (dato * (dato + 1) ) / 2

    return int(n)

if __name__ == '__main__':
    print(numero_triangular(1))

