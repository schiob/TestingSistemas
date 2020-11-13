def saludo(nombre: str) -> str:
    a = input()

    datos = a.values.tolist()

    return datos

if __name__ == "__main__":
    print(saludo("David"))