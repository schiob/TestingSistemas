class leer_archivo (): 
    def leer(self) -> str: 
        with open("archivito.txt", "r") as f:
            return f.read()

def calc_prom(entrada):
    total = 0
    n = 0
    for linea in entrada.leer():
        #if linea[0].isnumeric():
        if linea.split():
            total += int(linea)
            n += 1
    return total / n

if __name__ == "__main__": 
    archivito = leer_archivo() 
    print(calc_prom (archivito))