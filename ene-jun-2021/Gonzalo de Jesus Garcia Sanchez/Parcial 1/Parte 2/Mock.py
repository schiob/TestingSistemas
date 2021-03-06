import csv
def leer_archivo(path):
    with open(path,'r') as Archivo_para_Leer:
        data = Archivo_para_Leer.read()
    return data
    
def AbrirArchivo():
    #abre el archivo 
    data = open('Usuarios.csv')
    # leyendo cvs 
    csv_data = csv.reader(data)
    return list(csv_data)

def Calif(lista):
    email = []
    _lista = lista
    for line in _lista[1:]:
        email.append(line[1]+' '+line[2])
    return email

def SortCalif(lista):
    slista = []
    _lista = lista
    arroba = 0
    # separa correo y las calificaciones 
    for i in range(len(_lista)):
        arroba = _lista[i].find("@")
        slista.append(_lista[i][(arroba+1):].split())
    slista.sort()
    return slista     
def Promedio(lista):
    _lista = lista
    promm = {}
    calif = int(_lista[0][1])
    count = 1
    prom = 0 
    #promedio calificaciones 
    for i in range((len(_lista)-1)):
        if _lista[i+1][0] == _lista[i][0]:
            count += 1
            calif += int(_lista[(i+1)][1])
        else:
            if(_lista.index(_lista[i+1])+1 == len(_lista)):
                promm[_lista[i+1][0]] = int(_lista[(i+1)][1])
            prom = calif/count
            calif = int(_lista[(i+1)][1])
            count = 1
            promm[_lista[i][0]] = prom
    return promm
    
lista = AbrirArchivo()
califlista = Calif(lista)
slista = SortCalif(califlista)
promm = Promedio(slista)
print(promm)