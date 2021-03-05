import requests as req

from requests.models import Response

data = {"INPUT":"asdfgheqwtgsfasda"}
url = "HTTP://API.SHOUTCLOUD.IO/V1/SHOUT"
respuesta = req.post(url,json = data).json()

print(respuesta["OUTPUT"])