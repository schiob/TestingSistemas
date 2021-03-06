import requests


def mayus(x):
    response = requests.post("HTTP://API.SHOUTCLOUD.IO/V1/SHOUT", json={"INPUT": x})

    # return response.status_code

    if response.status_code != 200:
        return f"error, mensaje: {response.text}"

    # return type(response.text)
    #return response.text.split('"')[-2]

    data = response.json()

    # return type(data)

    return data["OUTPUT"]


def main():
    x = input('Dime las cosas que me vas a gritar :( -> ')
    print(mayus(x))


if __name__ == '__main__':
    main()
