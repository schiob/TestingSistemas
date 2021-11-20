def calc_prom():
    file = open("archivo.txt", "r")
    total = 0
    contador = 0
    for linea in file:
        total += int(linea)
    
    if contador == 0:
        return 'El archivo está vacío.'

    return total

if __name__ == "__main__":
    print(calc_prom())
