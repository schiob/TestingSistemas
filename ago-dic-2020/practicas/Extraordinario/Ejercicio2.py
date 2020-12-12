import csv
#Abre el archivo.
def extraer_data(filename: str) -> list:

    cCOLUMNAS = ["regalo","precio"]

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = " ")
        data = [i for i in csv_reader]

    columnas = [i for i in data][0]

    if columnas != cCOLUMNAS:
        raise ValueError("Formato Incorrecto")

    data = [row[1:] for row in data][1:]
    data = [[i[0].split(" ")[1], int(i[1])] for i in data]

    return data

def precio(filename: str) -> dict:

    data = extraer_data(filename)

    price = {i: [] for i in {i[0] for i in data}}
    for price in price.keys():
        for r, p in data:
            if r == price:
                price[price].append(p)

    for k,v in price.items():
        price[k] = max(data)

    return price