def lectura_archivo(archivo):
    file = open(archivo,'r')
    content = file.readlines()
    newContent= []
    
    for i in content:
        a = i.replace('\n','')
        newContent.append(a)
    
    content= newContent    
    return content

def lectura_materias(lista:list):
    lista_materias=[]
    for i in lista:
        a=i.split()
        dictionary = {'nombre':a[0],'materia': a[1], 'calif':a[2]}
        lista_materias.append(dictionary)
    return lista_materias

def calcular_promedio(lista):
    nombre_anterior = lista[0]['nombre']
    calif_actual = 0
    promedios = []
    cont = 0
    for i in lista:
        nombre_actual=i['nombre']
        #print(nombre_actual)
        if nombre_actual == nombre_anterior:
            calif_actual += float(i['calif'])
            cont += 1
            #print(cont)
        else:
            nombre = nombre_anterior
            promedio = float("{:.2f}".format(calif_actual/cont))
            promedios.append({'nombre':nombre, 'promedio': promedio})
            calif_actual = float(i['calif'])
            cont = 1
            print(nombre_anterior)
        nombre_anterior = nombre_actual 
    promedio = float("{:.2f}".format(calif_actual/cont))
    promedios.append({'nombre':nombre_anterior, 'promedio': promedio})
    return promedios

if __name__ == '__main__':
    print(calcular_promedio(lectura_materias(lectura_archivo("calificaciones.txt"))))