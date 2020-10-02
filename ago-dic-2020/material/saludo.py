def saludo(nombre: str) -> str:
    a = input("apellido: ")

    return "hola {} {}".format(nombre, a)

if __name__ == "__main__":
    print(saludo("David"))