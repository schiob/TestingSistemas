import requests


def pokedx(n):

    r = requests.get("https://pokeapi.co/api/v2/pokemon/{}".format(n))
    return r.json()['name']

if __name__ == "__main__":
    
    n = str(input("Escriba el numero del Pokemon: "))
    print(pokedx(n))

