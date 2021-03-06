import pandas

def get_info(parcialcsv):
    archivo = pandas.read_csv(parcialcsv)
    data = archivo.values.tolist()
    data = [[i[1].split("@")[1], int(i[2])] for i in data]
    return data
promedio = []

def promediacion():
    completeinfo = get_info('parcial.csv')
    while len(completeinfo) > 0:
        dom = []
        ind = []
        ultimodom = completeinfo[0][0]
        ind = 0
        cont = 0
        suma = 0
        for d in completeinfo:
            dominio, puntos = d[0], d[1]
            if ultimodom == dominio:
                dom.append([dominio, puntos])
                ind.append(ind)
            ind +=1
        while cont < len(ind):
            completeinfo.pop(ind[cont] - cont)
            cont += 1
        for i in dom:
            suma+= i[1]
        valores = [dom[0][0], suma/len(dom)]
        promedio.append(valores)
    return promedio

if __name__ == "__main__":
    dominiosypromedios = promediacion()
    print(dominiosypromedios)