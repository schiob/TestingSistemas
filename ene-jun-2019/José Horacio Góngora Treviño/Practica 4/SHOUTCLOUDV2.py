import requests

def mayus(x):
    response = requests.post("HTTP://API.SHOUTCLOUD.IO/V1/SHOUT", json={"INPUT": x})

    if response.status_code != 200:
        return (f"error, mensaje: {response.text}")

    return response.text.split('"')[-2]

    #data = response.json()

    #return data["OUTPUT"]

if __name__ == '__main__':
    x = input()
    print(mayus(x))