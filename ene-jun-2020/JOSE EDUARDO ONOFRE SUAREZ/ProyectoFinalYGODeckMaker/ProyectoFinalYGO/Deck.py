class Deck(object):
    def __init__(self, main_deck):
        self.main_deck = main_deck

    def add_normal_cards(self, card_to_add, all_cards):
        "Agrega monstruos, hechizos y trampas al deck"
        "La función len() devuelve la longitud de una cadena de caracteres o el número de elementos de una lista."
        
        if len(self.main_deck) > 60:
            return "Tienes mas cartas de las permitidas en tu Deck (60)."
        else:
            contador_cartas = 0
            # Verifica cuántas copias de una carta hay en tu mazo. Puedes tener máximo 3 de la misma tarjeta. Tarjetas limitadas,
            # se agregaran.
            for card in self.main_deck:
                if card == card_to_add:
                    contador_cartas += 1
            if contador_cartas == 3:
                return "Tienes muchas copias de esa carta en tu deck (3)"
            else:
                if card_to_add not in all_cards:
                    return "Esa carta aún no se ha agregado al juego  (" + card_to_add + ")."
                else:
                    self.main_deck.append(card_to_add)

    def BuildExtraDeck(self, card_to_add, all_cards):
            "Agrega monstruos, hechizos y trampas al deck"
        
            if len(self.main_deck) > 15:
                return "Tienes mas cartas de lo permitido en tu extra deck (15)."
            else:
                contador_carta = 0
                # Verifica cuántas copias de una carta hay en tu mazo. Puedes tener máximo 3 de la misma tarjeta. Tarjetas limitadas,
                # se agregaran.
                for card in self.main_deck:
                    if card == card_to_add:
                        contador_carta += 1
                if contador_carta == 3:
                    return "Tienes muchas copias de esa carta en tu deck (3)."
                else:
                    if card_to_add not in all_cards:
                        return "Esa carta aún no se ha agregado al juego (" + card_to_add + ")."
                    else:
                        self.main_deck.append(card_to_add)

    def BuildSideDeck():
            pass
    
    def DeckValue():
        pass
    


class SearchInDeck(ABC):
    @abstractclassmethod
    def Search(id):
        pass
    
    def getCard(id, bibliotec):# Metodo para obtener el nombre o algo en especifico 
    yugih = bibliotec.Search(id)

    return yugih.name
