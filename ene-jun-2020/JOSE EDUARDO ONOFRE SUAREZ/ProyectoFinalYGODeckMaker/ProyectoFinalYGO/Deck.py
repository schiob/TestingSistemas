import requests
import pprint
from abc import ABC,abstractclassmethod

class Deck:
    def __init__(self, id, name, main, extra, side,price):
        self.Id= id
        self.Name = name
        self.Main = main
        self.Extra = extra
        self.Side = side
        self.Price = price

class MainDeck:
     def __init__(self,nombre,List_cartas)
        self.Nombre = nombre
        self.List_cartas = list()

    def addCardToMain(self, carta, cantidad, card_to_add):
        for i, car in enumerate(self.List_cartas):
            if car["carta"].nombre == carta.nombre:
                self.List_cartas[i]["cantidad"] += cantidad
                return
        

        if len(self.List_cartas) < 40 and len(self.List_cartas) > 60:
            return "Numero de Cartas Permitioos."
        else:
            "Numero de Cartas Invalido"
            contador_cartas = 0
            # Verifica cuántas copias de una carta hay en tu mazo. Puedes tener máximo 3 de la misma tarjeta. Tarjetas limitadas,
            # se agregaran.
            for card in self.List_cartas
                if card == card_to_add:
                    contador_cartas += 1
            if contador_cartas == 3:
                return "Tienes muchas copias de esa carta en tu deck (3)"

class SideDeck:
     def __init__(self,nombre,List_cartas)
        self.Nombre = nombre
        self.List_cartas2 = list()

    def addCardToSide(self, carta, cantidad,card_to_add2):
        for i, car in enumerate(self.List_cartas):
            if car["carta"].nombre == carta.nombre:
                self.List_cartas2[i]["cantidad"] += cantidad
                return
        

        if len(self.List_cartas) < 15
            return "Numero de Cartas Permitioos."
        else:
            "Numero de Cartas Invalido"
            contador_cartas = 0
            # Verifica cuántas copias de una carta hay en tu mazo. Puedes tener máximo 3 de la misma tarjeta. Tarjetas limitadas,
            # se agregaran.
            for card in self.List_cartas2
                if card == card_to_add:
                    contador_cartas += 1
            if contador_cartas == 3:
                return "Tienes muchas copias de esa carta en tu deck (3)"

class ExtraDeck:
     def __init__(self,nombre,List_cartas)
        self.Nombre = nombre
        self.List_cartas3 = list()

    def addCardToExtra(self, carta, cantidad, card_to_add3):
        for i, car in enumerate(self.List_cartas):
            if car["carta"].nombre == carta.nombre:
                self.List_cartas3[i]["cantidad"] += cantidad
                return
        

        if len(self.List_cartas3) < 15
            return "Numero de Cartas Permitioos."
        else:
            "Numero de Cartas Invalido"
            contador_cartas = 0
            # Verifica cuántas copias de una carta hay en tu mazo. Puedes tener máximo 3 de la misma tarjeta. Tarjetas limitadas,
            # se agregaran.
            for card in self.List_cartas3
                if card == card_to_add3|:
                    contador_cartas += 1
            if contador_cartas == 3:
                return "Tienes muchas copias de esa carta en tu deck (3)"


