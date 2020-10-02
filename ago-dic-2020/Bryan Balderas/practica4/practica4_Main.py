class personas:
    def __init__(self,nombre,correo,puntos):
     self.nombre=nombre
     self.correo=correo
     self.puntos=puntos


import csv
from collections import defaultdict

def abrirArchivo(nombreArchivo:str)->list:
    i=0
    persona=personas
    lista=[]
    listaCorreos=[]
    diccionario={}
    with open(nombreArchivo,newline='',encoding='utf-8') as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
            correo=row['correo']
            x,y=correo.split('@')
            lista.append(personas(row['usuario'],y,row['puntos']))
            i=i+1
    
    return lista

def obtenerPromedios(archivoName:str)->dict:
    listaCorreos=[]
    diccionario={}
    lista=abrirArchivo(archivoName)
    correos=[c.correo for c in lista]
    numCorreos={i:correos.count(i) for i in correos}
 #########################################obtener correos############################
    for r in lista:
        cor=r.correo
        if cor not in listaCorreos:
            listaCorreos.append(cor)
 ######################################inicializar diccionario#################################
    for elementos in listaCorreos:
        diccionario[elementos]=0
  ########################################sumatoria###########################################
    for a in listaCorreos:
        for nrow in lista:
            if nrow.correo==a:
                if diccionario[a]==0:
                    diccionario[a]=float(nrow.puntos)
                else:
                    diccionario[a]+=float(nrow.puntos)

     ######################################promedios###################################3
    for prom in listaCorreos:
        cantidad=numCorreos[prom]
        cantidadDos=diccionario[prom]
        diccionario[prom]=cantidadDos/cantidad
    
    return diccionario


     

if __name__ == "__main__":
   #print(abrirArchivo('testtexto.csv'))
   for k,v in obtenerPromedios('testdos.csv').items():
       print(k,v)

    