#Práctica 3. Función principal

def Get_Data():
    file = open("archivito.txt", "r")
    Lines=file.readlines()
    Data=[]
    for i in Lines:
        Data.append(i.strip())
    return Data

def calc_prom():
    data=Get_Data()
    total = 0
    for linea in data:
        total += int(linea)
    return total/len(data)

if __name__ == "__main__":
    print(calc_prom())