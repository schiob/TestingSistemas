from helpers import insertion_sort
from mocks import File

users_list = []

def funcion_principal() -> list:
    users = []
    travels = viajes_disponibles()
    next_user = siguiente_usuario()
    
    index = 0
    while index < len(travels):
        users.append(
            '{} - viaje {}'.format(next_user[index][0], travels[index][0])
        )
        index += 1
    
    return users 

# Función ligeramente cambiada por practicidad. 
# Ahora devuelve un arreglo del cual se obtendrá sólo el nombre.
def siguiente_usuario() -> str:
    try:
        if len(users_list) == 0:
            users_file = File('users.txt').Read()
            users = []
            for line in users_file.split('\n'):
                aux = line.split(' ')
                users.append(
                    [aux[0], aux[1]]
                )
                users = insertion_sort(users)
            users_list.append(users)

        elements_to_del = []
        for i in range(0, len(users_list[0]), 1):
            for j in range(i+1, len(users_list[0]), 1):
                if users_list[0][i][1] == users_list[0][j][1]:
                    elements_to_del.append(
                        users_list[0][j]
                    )
                    
        for x in range(len(elements_to_del)):
            users_list[0].remove(elements_to_del[x])
        
        if len(users_list[0]) >= 1:
            return users_list[0]
        
        return None

    except IndexError:
        raise IndexError

def viajes_disponibles() -> list[list]:
    viajes = []
    index = 0
    conductores = extraer_conductores()
    
    for conductor in conductores:
        index += 1
        viajes.append(
            [index, calcular_tarifa(int(conductor[1]))]
        )

    return viajes

def extraer_conductores() -> list:
    drivers = File('drivers.txt').Read()
    conductores = []
    for line in drivers.split('\n'):
        aux = line.split(' ')
        conductores.append(
            [aux[0], aux[1]]
        )

    return conductores

def calcular_tarifa(antiguedad: int) -> float:
    return 20 + (10*antiguedad)

if __name__ == '__main__':
    print(funcion_principal())
