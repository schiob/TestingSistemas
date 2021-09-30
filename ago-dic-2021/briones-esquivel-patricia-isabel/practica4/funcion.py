class leer_archivo (): 
    def leer(self) -> str: 
        with open("archivito.txt", "r") as f:
            return f.read()

def calc_prom(entrada):
    total = 0
    for linea in entrada.leer():
        if linea.strip():
            total += int(linea)
    return total

if __name__ == "__main__": 
    archivito = leer_archivo() 
    print(calc_prom (archivito))