def Quitar_especiales(direccion):
    archivo = open(direccion, "r")
    texto = archivo.read()
    archivo.close()
    cadena=''

    for i in range(0,len(texto)):
        if texto[i].isalnum() or texto[i]=='\n' or texto[i]==' ':
            cadena = cadena + texto[i]

    cadena = cadena.lower()
    return cadena


"""
lugar = 'C:\\Users\\Osvaldo Nava\\Desktop\\uni\\7-Semestre\\calidad\\Practica4\\' 
# ^----Esta es la carpeta donde estan los archivos para asi solo agregar el nombre del archivo en cada ruta
print("prueba principal")
ruta= lugar +'pp.txt'
print(Quitar_especiales(ruta))
print("\nTeniendo un archivo vacio")
ruta= lugar +'vacio.txt'
print(Quitar_especiales(ruta))
print("\nTeniendo un archivo con texto para eliminar")
ruta= lugar +'remover.txt'
print(Quitar_especiales(ruta))
print("\nTeniendo un archivo sin texto para eliminar")
ruta= lugar +'sinRemo.txt'
print(Quitar_especiales(ruta))
"""
