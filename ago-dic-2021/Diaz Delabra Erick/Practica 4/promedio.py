def calc_prom():
    file = open("ago-dic-2021\Diaz Delabra Erick\Practica 4\sarchivito.txt", "r")
    total = 0
    total2= 0
    x = 0
    '''Le cambie el nombre a archivito porque no me dejaba abrirlo, habia un conflicto con la diagonal y la primer letra (/archivito)'''

    for linea in file:
        x = x + 1
        total += int(linea)
        
    total2 = (total/x)
    return total2

if __name__ == "__main__":
    print(calc_prom())