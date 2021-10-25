from helpers import insertion_sort
from interfaces import IO, File        

def siguiente_usuario(users: list) -> list:
    aux = []
    for x in range(len(users)):
        aux.append(
            users[x].split(' ')
        )
    
    aux = insertion_sort(aux)
    elements_to_del = []
    
    for x in range(0, len(aux), 1):
        for y in range(x+1, len(aux), 1):
            if aux[x][1] == aux[y][1]:
                elements_to_del.append(
                    aux[y]
                )
    for x in range(len(elements_to_del)):
        aux.remove(elements_to_del[x])
                
    return aux

def viajes_disponibles(input: IO) -> list:
    viajes = []
    index = 0
    conductores = extraer_conductores(input)
    
    for conductor in conductores:
        index += 1
        viajes.append(
            [index, calcuar_tarifa(int(conductor[1]))]
        )

    return viajes

def extraer_conductores(input: IO) -> list:
    conductores = []
    for line in input.Read().split('\n'):
        aux = line.split(' ')
        conductores.append(
            [aux[0], aux[1]]
        )

    return conductores

def calcuar_tarifa(antigedad: int) -> int:
    return 20 + (10 * antigedad)

def funcion_principal(user_input: IO, travels_input: IO) -> list:
    users = user_input.Read().split('\n')
    users = siguiente_usuario(users)
    travels = insertion_sort(viajes_disponibles(travels_input))
    final_users_list = []
   
    max_length = len(travels)
    if len(users) > len(travels):
        max_length = len(users)
    
    for i in range(max_length):
        final_users_list.append(
            '{} - viaje {}'.format(users[i][0], travels[i][1])
        )
    
    return final_users_list
    
def main():
    users_file = File('users.txt')
    drivers_file = File('drivers.txt')

    print(funcion_principal(users_file, drivers_file))

if __name__ == '__main__':
    main()
