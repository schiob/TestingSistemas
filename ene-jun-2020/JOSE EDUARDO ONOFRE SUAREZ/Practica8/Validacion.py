import Censura

class validacion:

    def validar(pal,text,mag,num):

        cantoriginal = len(text)
        print(cantoriginal)
        newtext = (Censura.censura.censored(pal,text,mag)) #Aqui manda a llamar el metodo censored que esta en otro modulo
        print(newtext)
        cantnew  = len(newtext)
        print(cantnew)
        limit = num

        diff = cantoriginal - cantnew

        if abs(diff) <= limit:
            res = "El texto sigue siendo valido"
        else:
            res = "El texto ya no es valido"

        return res



if __name__ == "__main__":
    
    palabras = ["popo","sangre","muerte","maldito"]
    texto = input("Escriba el texto a validar:")
    magicword = input("Escriba la palabra para sustituir las malas palabras:")
    num = int(input("Numero valido de diferencia:"))

    print(validacion.validar(palabras,texto,magicword,num))