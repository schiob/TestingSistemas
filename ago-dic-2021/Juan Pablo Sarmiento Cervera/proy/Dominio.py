#Entidades
from abc import ABC


class Partida():
    def __init__(self, nomInvocador, campeonPrincipal, kill, deaths, assistence, enemigos):
        self.JugadorPrincipal= nomInvocador

        self.CampeonPrincipal = campeonPrincipal
        self.JP.Kills = kill
        self.JP.Deaths = deaths
        self.JP.Assistence = assistence

        self.CampeonesEnemigos = enemigos

    def calc_KDA(self):
        return(self.Assistance + self.Kills/ self.Deaths)
        

class Reporte():
    def __init__(self, jugador, partidas):
        self.Partidas = partidas
        self.Jugador = jugador

        
#Interface
class Fuente(ABC):
    def buscarUltimasPartidas(nomInvocador: str, num_partidas : int) -> list[Partida]:
        pass

class Storage(ABC):
    def GuardarReporte(repo : Reporte):
        pass

    def ObtenerReportes(jugador : str) -> list [Reporte]:
        pass
