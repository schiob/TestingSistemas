import requests

def get_juegos(consola: str):
    r=requests.get(f"https://api.rawg.io/api/platforms")
    return r


if __name__=="__main__":
  r=get_juegos("PC")
  print(r.text)