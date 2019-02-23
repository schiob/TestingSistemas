import requests

def mayusculas(x):
    x = list(map(str, x.split()))
    m = list()
    for i in x:
        response = requests.post("HTTP://API.SHOUTCLOUD.IO/V1/SHOUT", json={"INPUT": i})
        m.append(response.text)
    return m

if __name__ == '__main__':
    m = input()
    print(mayusculas(m))
