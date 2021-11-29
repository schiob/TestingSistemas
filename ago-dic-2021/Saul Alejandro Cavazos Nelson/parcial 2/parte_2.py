from abc import ABC, abstractclassmethod


class escribir (ABC):
    @abstractclassmethod
    def Escribir(texto:str):
        pass
    
class tertminal(escribir):
    def Escribir(texto:str):
        return input()


def escribir_a_pantalla(tex:escribir):
    print("dame un texto")
    esc=input()
    mi_texto_en_patalla=tex.Escribir(esc)
    return mi_texto_en_patalla

if __name__ =='__main__':
    mi_terminal=tertminal()
    print(escribir_a_pantalla(tertminal))

