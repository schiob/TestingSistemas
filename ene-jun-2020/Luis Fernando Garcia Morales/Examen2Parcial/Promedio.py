from unittest.mock import MagicMock
def get_cal(archivo):   
    f = open(archivo,"r")
    data = []
    f1 = f.readlines()
    for i in f1:
        i = i.rstrip()
        data.append(i.split(" "))
    return data

def prom(datos):
    data = []
    for i in datos:
        dicc = {"Nombre": i[0], "Materia": i[1], "Calificacion": i[2]}
        data.append(dicc)
    
    Nombre = data[0].get("Nombre")
    count = 0
    res = []
    for i in data:
        if Nombre == i.get("Nombre"):
            count += float(i.get("Calificacion"))
        else:
            prom= count/2
            res.append([Nombre, prom])
            count = 0
            Nombre = i.get("Nombre")
    return res

print (prom(get_cal("Calificaciones.txt")))
