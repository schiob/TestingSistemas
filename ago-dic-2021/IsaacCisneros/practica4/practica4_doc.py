def cp():
    file = open("ago-dic-2021\Isaac Cisneros\practica4\aarchivo.txt", "r")
    total = 0
    
    for linea in file:
        total += int(linea)
        total2 = (total/int(linea))

    return total2

if __name__ == "__main__":
    print(cp()) 