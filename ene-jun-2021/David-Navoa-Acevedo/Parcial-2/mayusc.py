import os
import requests
#Funcion 3
class Conversor:
    def validador_de_existencia(self, nombre_archivo):

        if(os.path.isfile(nombre_archivo)):
            archivo = open(nombre_archivo, "r") 
            return archivo.read() 
        else:
            return """El archivito no estaba pero mientras ve este bonito perrito:
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
                   ▒▒▒▒▒▒▒▒▒▒▀▀"""
        

    #Funcion 2
    def conversor_a_mayusculas(self, a: str):
        b = requests.post("HTTP://API.SHOUTCLOUD.IO/V1/SHOUT",json={"INPUT": a})
        return b.text.split('"')[-2]
    #Funcion 1
    def funcion_principal(self):
        
        archivo = str(input("Escribe el nombre del archivo (con su extension) que deseas transformar a mayusculas:  "))
        #Llamado de la funcion 1
        texto = self.validador_de_existencia(archivo)

        #llamado de la funcion 2
        texto_en_mayusculas = self.conversor_a_mayusculas(texto)

        return "Resultado: ",texto_en_mayusculas

if __name__ == "__main__":
    #path que se usa "ene-jun-2021/David-Navoa-Acevedo/Parcial-2/archivo_de_texto.txt"
    print(Conversor().funcion_principal())