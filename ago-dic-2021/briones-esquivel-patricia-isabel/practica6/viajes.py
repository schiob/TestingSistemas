import operator

def siguiente_usuario(): 
    usuarios = {}
    count = 0
    flag = False
    # Lee archivo y lo pasa a un diccionario
    with open('usuarios.txt', 'r') as archivo:
        for linea in archivo:
            count += 1
            key, value = linea.split(' ')
            usuarios[key.strip()] = int(value.strip())

    # Verifica que el diccionario está lleno
    flag = bool(usuarios)
    if flag:
        # Detecta la prioridad y la borra del diccionario
        sig_user_key = min(usuarios.items(), key = operator.itemgetter(1))[0]
        sig_user = sig_user_key
        usuarios.pop(sig_user_key, min(usuarios.items(), key = operator.itemgetter(1))[1])

    # Pasa el diccionario a listas
    keyL = list(usuarios.keys())
    valueL = list(usuarios.values())

    # Sobreescribe el archivo con los nuevos datos del diccionario
    archivo = open('usuarios.txt', 'w')
    i = 0
    for i in range(len(keyL)):
        s = ''
        s += str(keyL[i]) + ' ' + str(valueL[i]) + '\n'
        archivo.write(s)
    archivo.close()
    
    if count > 0:
        return sig_user
    return 'No hay más usuarios'


def extraer_conductores():
    conductores = {}
    # Lee archivo y lo pasa a un diccionario
    with open('conductores.txt', 'r') as archivo:
        for linea in archivo:
            key, value = linea.split(' ')
            conductores[key.strip()] = int(value.strip()) 

    return conductores 



def calcular_tarifa(conductor):
    ec = extraer_conductores()
    antiguedad = ec.get(conductor)
    tarifa = 20 + (10 * antiguedad)
    
    return tarifa


def viajes_disponibles():
    ec = extraer_conductores()
    viajes = []
    i = 0

    # Envia como párametro el nombre de cada conductor para que calcule la tarifa de cada uno
    for i in range(len(ec.items())):
        viajes.append(calcular_tarifa(list(ec.keys())[i]))    
    vd = dict (enumerate(viajes, 1))

    return vd


def main ():
    usuarios = {}
    viajes_dados = {}
    vd = viajes_disponibles()

    # Lee archivo y lo pasa a un diccionario
    with open('usuarios.txt', 'r') as archivo:
        for linea in archivo:
            key, value = linea.split(' ')
            usuarios[key.strip()] = int(value.strip())

    for i in range(len(usuarios.items())):
        # Verifica que el diccionario está lleno
        flag = bool(vd)
        if flag:
            tarifa_minima = min(vd.items(), key = operator.itemgetter(1))[0]
            viajes_dados[siguiente_usuario()] = tarifa_minima
            vd.pop(tarifa_minima)

    return viajes_dados


if __name__ == "__main__": 
    #print (siguiente_usuario())
    #print (extraer_conductores())
    #print (calcular_tarifa('Maria'))
    print (viajes_disponibles())
    print (main())