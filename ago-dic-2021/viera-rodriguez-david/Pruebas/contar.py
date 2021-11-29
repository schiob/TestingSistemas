#Logica

def contar_vocales(linea):
    cont = 0
    for letra in linea:
        if letra in 'aeiou':
            cont += 1
    return cont
 
if __name__ == '__main__':
    linea = input()
    print (contar_vocales(linea))