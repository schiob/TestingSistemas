class File():
    def __init__(self, ruta):
        self.ruta = ruta

    def reader(self):
        dic = {}
        lista= []
        with open(self.ruta, "r") as f:
            return f.readlines()


def promedio(file):
    lista = file.reader()
    dic = {}
    promedios = {}
    for linea in lista:
        if linea.split(' ')[0] not in dic.keys():
            dic[linea.split(' ')[0]] = [float(linea.split(' ')[2])]
        else:
            dic[linea.split(' ')[0]].append(float(linea.split(' ')[2]))

    for clave, elemento in dic.items():
        suma = 0
        for x in elemento:
            suma +=x
        promedios[clave] = suma/len(elemento)

    return promedios


if __name__ == '__main__':
    ruta = 'C:/Users/Skynet-Gold/Desktop/mi_repo/TestingSistemas/ago-dic-2020/mariacastro/practicas/segundoParcial/calificaciones.txt'
   
    r = File(ruta)
    prueba = promedio(r)
    print(prueba)