import requests

def peticion_api(string):
    req = requests.post("HTTP://API.SHOUTCLOUD.IO/V1/SHOUT",
        json = {"INPUT": string}, 
        headers = {'Content-Type': 'application/json'} )
    
    if req.status_code != 200:
        return "ERROR"
    
    return req.text.split('"')[-2]