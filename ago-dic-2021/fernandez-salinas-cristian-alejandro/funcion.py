def calc_prom():
    file = open("archivito.txt", "r")
    total = 0
    cantidad = 0
    for linea in file:
        total += int(linea)
        cantidad += 1

    if cantidad == 0:
        return 'Porfavor ingresa datos'
    
    return round(total / cantidad, 2)

if __name__ == "__main__":
    print(calc_prom())