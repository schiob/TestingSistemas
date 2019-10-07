import requests

def ToUpper(text):
    response = requests.post("http://API.SHOUTCLOUD.IO/V1/SHOUT",json={"INPUT": text})

    # Check code
    if response.status_code != 200:
        return "error, mensaje: {}".format(response.text)  

    data = response.json()
    
    return data["OUTPUT"]


if __name__ == '__main__':
    up = ToUpper("HOLI")
    print(up)