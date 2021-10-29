class leer_usuarios ():
    # Lee el archivo y mete cada linea en una lista
    def leer_u(self) -> list:
        usuarios = []
        with open("usuarios.txt") as fname:
            lineas = fname.readlines()
            for linea in lineas:
                usuarios.append(linea.strip('\n'))
        return usuarios


class leer_conductores ():
    # Lee el archivo y mete cada linea en una lista
    def leer_c(self) -> list:
        conductores = []
        with open("conductores.txt") as fname:
            lineas = fname.readlines()
            for linea in lineas:
                conductores.append(linea.strip('\n'))
        return conductores


def extraer_usuarios(usuarios: leer_usuarios) -> list:
    lista_usuarios = []
    #Lee la lista y la convierte en una lista anidada
    for linea in usuarios.leer_u():
        linea = linea.strip()
        p = linea.find(' ')
        lista_usuarios.append([int(linea[p+1:]), linea[0:p]])
        lista_usuarios.sort(reverse=True)    
    return lista_usuarios


def extraer_conductores(conductores: leer_conductores) -> list:
    lista_conductores = []
    #Lee la lista y la convierte en una lista anidada
    for linea in conductores.leer_c():
        linea = linea.strip()
        p = linea.find(' ')
        lista_conductores.append([linea[0:p], int(linea[p+1:])])
    return lista_conductores


def calcular_tarifa(lista_conductores:list, conductor: str) -> int:
    i=0
    antiguedad = 0
    for i in range(len(lista_conductores)):
        #Busca el conductor solo en las posiciones [i][0]
        if conductor in lista_conductores[i][0]:
            antiguedad = lista_conductores[i][1]
    #else:
        #antiguedad = 0
    tarifa = 20 + (10 * antiguedad)
    
    return tarifa


def viajes_disponibles(lista_conductores:list) -> list:
    lista_viajes = []
    i = 0 
    j = 0
    for i in range(len(lista_conductores)):
        j = calcular_tarifa(lista_conductores, lista_conductores[i][0])
        lista_viajes.append([i+1,j])
        #lista_viajes.append([i+1,lista_conductores[i][0]])

    return lista_viajes


def siguiente_usuario(lista_usuarios:list):
    lista_usuarios.sort()
    sig_user = []
    for i in range(len(lista_usuarios)):
        sig_user.append(lista_usuarios[i][1])

    return sig_user


def main(lista_usuarios:list, lista_viajes:list):
    tarifa_minima = []
    viajes = []
    for i in range(len(lista_viajes)):
        tarifa_minima.append([lista_viajes[i][1],lista_viajes[i][0]])
    
    tarifa_minima.sort()
       
    for i in range(len(lista_viajes)):
        viajes.append(lista_usuarios[i]+ ' - viaje ' + str(tarifa_minima[i][1]))
    
    return viajes




'''def siguiente_usuario(lista_usuarios:list) -> str:
    flag = False
    flag = bool(lista_usuarios)
    if flag:
        sig_user = lista_usuarios[len(lista_usuarios)-1][1]
        lista_usuarios.pop()

    # Sobreescribe el archivo con los nuevos datos del diccionario
    archivo = open('usuarios.txt', 'w')
    i = 0
    for i in range(len(lista_usuarios)):
        s = ''
        s += lista_usuarios[i][1] + ' ' + str(lista_usuarios[i][0]) + '\n'
        archivo.write(s)
    archivo.close()

    if len(lista_usuarios) > 0:
        return sig_user
    else:
        archivo = open('usuarios.txt', 'w')
        s = 'Tom 4\nSusana 2\nAndres 10\nPepe 3\nLuis 2'
        archivo.write(s)
        archivo.close()'''

    


if __name__ == "__main__": 
    archivito_user = leer_usuarios()
    archivito_driver = leer_conductores()
    print(extraer_usuarios(archivito_user))
    print(extraer_conductores(archivito_driver))
    print(calcular_tarifa(extraer_conductores(archivito_driver), 'Pedro'))
    print(viajes_disponibles(extraer_conductores(archivito_driver)))
    print(siguiente_usuario(extraer_usuarios(archivito_user)))
    print(main(siguiente_usuario(extraer_usuarios(archivito_user)),viajes_disponibles(extraer_conductores(archivito_driver))))

