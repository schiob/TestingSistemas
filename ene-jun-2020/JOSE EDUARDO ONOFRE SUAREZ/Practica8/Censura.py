
class censura:

    def __init__(self,palabra,texto,magicword):
        self.pal = palabra
        self.text = texto
        self.mag = magicword


    def censored(pal,text,mag):

        palabras = pal
        magicword = mag

        for i in range(0,4):
            text = text.replace(palabras[i],magicword)
            #print(text)

        return text
        


if __name__ == "__main__":

    palabras = ["popo","sangre","muerte","maldito"]

    #for i in range(0,4):
    #    word = input("Mala palabra:")
    #    palabras.append(word)

    texto = input("Escriba el texto a censurar:")
    magicword = input("Escriba la palabra para sustituir las malas palabras:")
    print("----- Su texto Censurado -----\n")

    print(censura.censored(palabras,texto,magicword))

