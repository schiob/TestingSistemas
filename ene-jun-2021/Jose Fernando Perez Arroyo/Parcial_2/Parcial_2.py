import requests
import os.path

def check(path):
    if os.path.isfile(path) == True: 
        data=open(path,"r")
        d1=data.read()
        data.close()
        return d1
    else:
        datas ="El archivito no estaba pero mientras ve este bonito perrito:"
        datas += "no se que onda con el perro jajaj"

        return datas

def get_url(dato):
    response = requests.post("http://API.SHOUTCLOUD.IO/V1/SHOUT",json={"INPUT": dato})
    if response.status_code != 200:
        return "error, mensaje: {}".format(response.text)  
    data = response.json()
    return data["OUTPUT"] 

def compilado(nombre):
    
    data= check(nombre)
    data1= get_url(data)
    print(data1)

if __name__ == "__main__":
      dato= "doge.txt"
      compilado(dato)






