import requests
from requests.api import get

#Funcion1
def get_Contenido(path):
    try:
        archivo = open(path)
        contenido = archivo.read()
        archivo.close()
        return contenido
    except OSError:
        cadena = "El archivito no estaba pero mientras ve este bonito perrito:\n... el perrito se escapo!!!\n"
        return cadena

#Funcion2
def Shouter(content):
    if content!="":
        data = {"INPUT":content}
        url = "HTTP://API.SHOUTCLOUD.IO/V1/SHOUT"
        respuesta = requests.post(url,json = data).json()
        return respuesta["OUTPUT"]
    else:
        return "No hay texto"

#Funcion3
def Mezcla(path):
    contenido1 = get_Contenido(path)
    if contenido1 == "El archivito no estaba pero mientras ve este bonito perrito:\n... el perrito se escapo!!!\n":
        cadenaFinal = contenido1
        return cadenaFinal
    else:
        contenido2 = Shouter(contenido1)
        if contenido2 == "No hay texto":
            cadenaFinal = contenido2
            return cadenaFinal
        else:
            cadenaFinal = "{}, {}".format(contenido1,contenido2)
            return cadenaFinal
    """
    contenido1 = get_Contenido(path)
    contenido2 = Shouter(contenido1)
    if contenido2 != "No hay texto":
        cadenaFinal = "{}, {}".format(contenido1,contenido2)
        return cadenaFinal
    else:
        cadenaFinal = "{}".format(contenido1)
        return cadenaFinal
    """