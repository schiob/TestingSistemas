import requests

def pedido (a):
    
    b = requests.post("HTTP://API.SHOUTCLOUD.IO/V1/SHOUT",json={"INPUT": a})

    return b.text

if __name__ == '__main__':
    print(pedido("quionda"))
    
