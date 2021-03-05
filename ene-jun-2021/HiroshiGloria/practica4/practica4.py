import requests

def Shouter(content):
    data = {"INPUT":content}
    url = "HTTP://API.SHOUTCLOUD.IO/V1/SHOUT"
    respuesta = requests.post(url,json = data).json()

    return respuesta["OUTPUT"]