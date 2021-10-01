def calc_prom():
    file = open("archivito.txt", "r")
    total = 0
    cantidad=0


    for linea in file:

        total += int(linea)
        cantidad+=1


    if cantidad == 0:
        return 'no existen datos en el archivo'


    return (total/cantidad)



if __name__ == "__main__":
    print(calc_prom())
