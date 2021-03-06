def abrir(archivo):
    a=open(archivo, 'r')
    linea_lista=[]
    suma=0
    for linea in a:
        linea_lista=linea.split(',')
        suma+=int(linea[2])
        print (suma)
    #a.close()
#abrir('cvs.txt')