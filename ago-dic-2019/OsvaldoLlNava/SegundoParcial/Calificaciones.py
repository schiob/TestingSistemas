def Calcular_promedios(ruta):
    direccion = ruta
    archivo = open(direccion, 'r')
    nombres = []
    promedios = []
    nombre = 'qwerty'
    for linea in archivo:
        texto = str(linea).strip()
        if nombre not in linea:
            nombre=''
            for i in range(0,len(texto)):
                nombre += texto[i] 
                if texto[i] == ' ' or texto[i] == '\n':
                    if nombre not in nombres:
                        nombres.append(nombre.strip())
                        break
                    else:
                        nombre += texto[i] 
    archivo.close()
    espacios=0
    for i in range(0, len(nombres)):
        nombre = nombres[i]
        promedio = 0
        cadena =''
        cantidad = 0
        
        archivo = open(direccion, 'r')
        for linea in archivo:
            texto = str(linea).strip()
            if nombre in linea:
                for j in range(0,len(texto)):
                    if texto[j] == ' ' or texto[j] == '\n':
                        espacios+=1
                    if espacios == 2:
                        cadena += texto[j]
                    if j == (len(texto)-1):
                        promedio += float(cadena)
                        cantidad +=1
                        espacios=0
                        cadena = ''
        promedios.append(promedio/cantidad)
        archivo.close()
    final = []
    for i in range(0,len(nombres)):
        final.append(nombres[i])
        final.append(promedios[i])
    return final

# lista = Calcular_promedios('calificaciones_alumnos.txt')
# print(lista)