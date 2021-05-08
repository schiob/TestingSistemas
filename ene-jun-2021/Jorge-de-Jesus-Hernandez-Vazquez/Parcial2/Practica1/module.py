import requests

def file_method(file_name:str):
    
    try:
        with open(file_name, "r") as fl:
            #new = fl.read()
            print(fl.readlines())
            fl.close()

    except:
        return """ 
    El archivito no estaba pero mientras ve este bonito perrito:
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
                   ▒▒▒▒▒▒▒▒▒▒▀▀     
        """
        
    
def upper_case(strings:str):
    req = requests.post("HTTP://API.SHOUTCLOUD.IO/V1/SHOUT",
        json = {"INPUT": strings}, 
        headers = {'Content-Type': 'application/json'} )
    
    if req.status_code != 200:
         return "****ERROR****"

    else:

        return req.text.split('"')[-2]
    

#La tercera función debe de pedirle al usuario el nombre de un archivo 
# y usar las dos funciones anteriores para el contenido del
# archivo transformarlo en mayúsculas.
def main_method(file_name:str, strings:str):
    
    print(file_method(file_name))
    print(upper_case(strings))
     

if __name__ == '__main__':
    
    name   = input("Ingresa el nombre del archivo: \n")
    mayusc =  input("\nPalabras a convertir a mayusculas: \n\n")
    print(main_method(name, mayusc))
