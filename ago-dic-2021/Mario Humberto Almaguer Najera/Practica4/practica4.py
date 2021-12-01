def calc_prom():
    file = open("datos.txt", "r")
    total = 0
    lineas = 0
    for linea in file:
        total += int(linea)
        lineas += 1

    if lineas == 0:
        return 'No hay datos'

    return round(total / lineas, 2)

if __name__ == "__main__":
    print(calc_prom())
