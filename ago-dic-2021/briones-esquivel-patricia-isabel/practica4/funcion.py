class leer_archivo (): 
    def leer(self) -> list: 
        datos = []
        with open("archivito.txt") as fname:
            lineas = fname.readlines()
            for linea in lineas:
                datos.append(linea.strip('\n'))
        return datos

def calc_prom(entrada):
    total = 0
    n = 0
    for linea in entrada.leer():
        #if linea[0].isnumeric():
        #if linea.split():
        total += int(linea)
        n += 1
    return total / n

if __name__ == "__main__": 
    archivito = leer_archivo() 
    print(calc_prom (archivito))
    