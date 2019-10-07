import requests

def getOutput(text):
    r = requests.post("HTTP://API.SHOUTCLOUD.IO/V1/SHOUT",
    json = {"INPUT": text}, headers = {'Content-Type': 'application/json'})
    if r.status_code != 200:
         return "error"

    return r.text.split('"')[-2]
    #data = r.json()
    #return r.json()["OUTPUT"]

if __name__ == '__main__':
    print(getOutput("hola"))
