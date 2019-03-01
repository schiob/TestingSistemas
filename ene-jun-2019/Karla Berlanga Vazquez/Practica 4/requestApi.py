import requests
import json

def makePost(input):
    cabecera =  {'Content-type': 'application/json'}
    parameters = {
    "INPUT": str(input)
    }
    solicitud = requests.post(url = "HTTP://API.SHOUTCLOUD.IO/V1/SHOUT", headers = cabecera, data = json.dumps(parameters))
    if solicitud.status_code != 200:
        return "error :("
    else:
        #return solicitud.text.split('"')[-2]
        data = solicitud.json()
        return data["OUTPUT"]
    #return solicitud.json()["OUTPUT"]



if __name__ == '__main__':
    print(makePost("hola mundo"))
