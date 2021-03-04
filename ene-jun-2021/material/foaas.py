import requests

def saludar(nombre):
    response = requests.get("https://foaas.herokuapp.com/awesome/{}".format(nombre), headers={"Accept": "text/plain"})

    return response.text

if __name__ == "__main__":
    print(saludar("Chio"))