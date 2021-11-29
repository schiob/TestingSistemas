
def calc_prom(myfile):
    miArchivo = open(myfile)
    total = 0
    for linea in miArchivo:

        total += int(linea)

    return total
