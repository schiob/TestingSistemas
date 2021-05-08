import requests


######################################################################################################################################################################
def Funcion_1(path):
    try:
        archivo = open(path)
        contenido = archivo.read()
        archivo.close()
        return contenido
    except Exception:
        c = "El archivito no estaba pero mientras ve este bonito perrito:\n"
        c += """
                   ▄              ▄
                  ▌▒█           ▄▀▒▌
                  ▌▒▒█        ▄▀▒▒▒▐
                 ▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐
               ▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐
             ▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌
            ▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌
            ▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐
           ▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌
           ▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌
          ▌▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐
          ▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌
          ▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐
           ▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌
           ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐
            ▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌
              ▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀
                ▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀
                   ▒▒▒▒▒▒▒▒▒▒▀▀ \n"""
        return c
    
if __name__ == '__main__':
    print(Funcion_1("archvo.txt" + "\n"))
    

######################################################################################################################################################################

url = "http://shoutcloud.io/"
def Funcion_2(req):
    response = requests.post("HTTP://API.SHOUTCLOUD.IO/V1/SHOUT",
    json={"INPUT": req})
    return response.text
        
if __name__ == '__main__':
    req = input("Ingrese el texto a modificar: ")
    print(Funcion_2(req) + "\n")


######################################################################################################################################################################

def Funcion_3():
    path=input("ingrese nombre del archivo (con el .txt por favor): ")
    texto=Funcion_1(path)
    return Funcion_2(texto)

if __name__ == '__main__':
    print(Funcion_3() + "\n")


    