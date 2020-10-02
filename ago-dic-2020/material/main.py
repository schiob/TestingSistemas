from api import MiApi
from random_mesage import MiRandomGenerator
from internet import say_hi

def main():
    usuario = input("dame tu usuario porfa plis: ")

    mi_message_creator = MiApi()
    saludo = say_hi(usuario, mi_message_creator)

    print(saludo)

    mi_otro_creator = MiRandomGenerator()
    saludo = say_hi(usuario, mi_otro_creator)

    print(saludo)


if __name__ == "__main__":
    main()
