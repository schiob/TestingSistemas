import csv
from os import close

#Leo el archivo csv, lo recorro y guardo la info en diccionarios 
#dentro de una lista que retorno.
def read_csv() -> list:
    lista =[]
    with open('usuarios.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            lista.append(row)
    
    return lista

def calculating_average(list):
    userss = list
    hotmail = 0
    gmail = 0
    outlook = 0
    count_hotm = 0
    count_gmail = 0
    count_outl = 0
    #print(userss)

    #Recorro la lista de diccionarios y guardo el valor de los puntos 
    #dependiendo de la terminación del correo.
    for i in userss:
        
        a = i["correo"].split("@")
        
        if a[1] == "hotmail.com":
            hotmail += float(i["puntos"])
            count_hotm += 1
            
        if a[1] == "gmail.com":
            gmail += float(i["puntos"])
            count_gmail += 1

        if a[1] == "outlook.com":
            outlook += float(i["puntos"])
            count_outl += 1

    return "hotmail "+ str(hotmail/count_hotm)+"\n" "gmail "+ str(gmail/count_gmail)+"\n"+ "outlook "+ str(outlook/count_outl)

if __name__ == "__main__":
    #Guardo en una variable la lista con la info
    data = read_csv()

    #Mandamos los datos a calcular e imprimimos
    print(calculating_average(data))