import requests

def get_url(dato):
    response = requests.post("http://API.SHOUTCLOUD.IO/V1/SHOUT",json={"INPUT": dato})
    if response.status_code != 200:
        return "error, mensaje: {}".format(response.text)  

    data = response.json()
    return data["OUTPUT"] 

if __name__ == "__main__":
      prueba=get_url('no pues esta cul su vestido')
      print(prueba)

