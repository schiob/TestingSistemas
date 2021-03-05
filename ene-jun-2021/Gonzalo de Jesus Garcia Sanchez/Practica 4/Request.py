import requests
url = "http://shoutcloud.io/"
def pag(req):
    response = requests.post("HTTP://API.SHOUTCLOUD.IO/V1/SHOUT",
    json={"INPUT": req})
    
    return response.text
    
if __name__ == '__main__':
    req = input("Ingrese el texto: ")
    print(pag(req))