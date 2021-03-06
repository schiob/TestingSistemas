import requests


def reQst(t):
    req = requests.post("HTTP://API.SHOUTCLOUD.IO/V1/SHOUT",
        json = {"INPUT": t}, 
        headers = {'Content-Type': 'application/json'} )
    
    if req.status_code != 200:
         return "****ERROR****"

    return req.text.split('"')[-2]
    

if __name__ == '__main__':
    print(reQst("waasaaaaaaa"))
 