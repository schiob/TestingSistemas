import requests
import time

def joke(URL):
    if URL:
        r1=requests.get(url=URL,headers={'Connection':'close'})
        resp1=r1.json()
        return resp1
    else:
        print "INGRESA URL"


if __name__ == '__main__':
    URL="https://sv443.net/jokeapi/category/Programming"
    print(joke(URL))
