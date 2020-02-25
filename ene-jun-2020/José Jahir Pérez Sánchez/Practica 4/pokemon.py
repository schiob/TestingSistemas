import requests

def pokedex(NumP):
    res = requests.get("https://pokeapi.co/api/v2/pokemon/"+NumP+"/")

    return res.json()["name"]

if __name__ == "__main__":
    print(pokedex("1"))