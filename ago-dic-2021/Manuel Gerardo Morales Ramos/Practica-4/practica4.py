def calc_prom():
    file = open("archivito.txt", "r")
    total = 0
    for linea in file:
        total += int(linea)
    
    file.close()
    return total

if __name__ == "__main__":
    print(calc_prom())