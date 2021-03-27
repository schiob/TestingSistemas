import requests

def MensajeBonito() -> str:
    response = requests.get("https://foaas.herokuapp.com/because/escuelita", headers={"Accept": "text/plain"})

    return response.text