import requests
from internet import MessageCreator

class MiApi(MessageCreator):
    def CreateMessage(self, persona: str) -> str:
        headers = {"Accept": "text/plain"}
        response = requests.get("https://foaas.com/awesome/{}".format(persona), headers=headers)

        return response.text
