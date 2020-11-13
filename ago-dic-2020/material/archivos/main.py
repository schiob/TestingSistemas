from api import MiApi
from random_mesage import MiRandomGenerator
from internet import say_hi, Cosa

def main():
    usuario = input("dame tu usuario porfa plis: ")

    mi_message_creator = MiApi()
    
    mi_cosa = Cosa("nombre random", mi_message_creator)
    saludo = mi_cosa.say_hi(usuario)
    print(saludo)

    mi_otro_creator = MiRandomGenerator()
    mi_cosa.set_message_creator(mi_otro_creator)
    saludo = mi_cosa.say_hi(usuario)
    print(saludo)


if __name__ == "__main__":
    main()
