def calc_prom():

    file = open("archivito.txt", "r")
    # file = open("archivito1.txt", "r")
    # file = open("archivito2.txt", "r")
    total = 0
    for linea in file:
        total += int(linea)
        promedio = total/int(linea)

    return promedio

if __name__ == "__main__":
    print(calc_prom())
