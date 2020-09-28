import csv

def read_file(path):
    with open(path, 'r') as file_to_read:
        data = file_to_read.read()
    return data
    
def Abrir_Archivo():
    # Open the file 
    data = open('Practica4.csv',encoding = 'utf-8')

    # csv.reader
    csv_data = csv.reader(data)

    # reformat it into a python object
    return list(csv_data)

def Sacar_Correos_Calif(lista):
    email = []
    _lista = lista
    for line in _lista[1:]:
        email.append(line[1]+' '+line[2])
    return email

def Sort_Correos_Calif(lista):
    slista = []
    _lista = lista
    arroba = 0
    # separa los dominios del correo y las calificaciones 
    for i in range(len(_lista)):
        arroba = _lista[i].find("@")
        slista.append(_lista[i][(arroba+1):].split())
    slista.sort()
    return slista     
def Promedio(lista):
    _lista = lista
    dprom = {}
    calif = int(_lista[0][1])
    count = 1
    prom = 0 
    #cuenta los dominios y hace el promedio de las calificaciones 
    for i in range((len(_lista)-1)):
        if _lista[i+1][0] == _lista[i][0]:
            count += 1
            calif += int(_lista[(i+1)][1])
        else:
            if(_lista.index(_lista[i+1])+1 == len(_lista)):
                dprom[_lista[i+1][0]] = int(_lista[(i+1)][1])
           
            prom = calif/count
            calif = int(_lista[(i+1)][1])
            count = 1
            dprom[_lista[i][0]] = prom
       
    return dprom 
    

lista = Abrir_Archivo()
clista = Sacar_Correos_Calif(lista)
slista = Sort_Correos_Calif(clista)
dprom = Promedio(slista)
print(dprom)