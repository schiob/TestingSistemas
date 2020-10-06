import csv

def extraer_data(filename: str) -> list:
    #Funcion para sacar los datos que nos interesan para la practica del archivo CSV
    cCOLUMNAS = ["usuario","correo","puntos"]

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ",")
        data = [i for i in csv_reader]

    columnas = [i for i in data][0]

    if columnas != cCOLUMNAS:
        raise ValueError("Formato Incorrecto")

    data = [row[1:] for row in data][1:]
    data = [[i[0].split("@")[1], int(i[1])] for i in data]

    return data

def calcular_promedio(filename: str) -> dict:

    data = extract_data(filename)

    dominios = {i: [] for i in {i[0] for i in data}}
    for dominio in dominios.keys():
        for d, p in data:
            if d == dominio:
                dominios[dominio].append(p)

    for k,v in dominios.items():
        dominios[k] = (sum(v)/len(v))

    return dominios


if __name__ == "__main__":
    for k,v in calcular_promedio("Datos.csv").items():
        print(k, v)