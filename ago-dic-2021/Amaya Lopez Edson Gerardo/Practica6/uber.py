user_priority = {
    'Tom':    4,
    'Susana': 2,
    'Andres':10,
    'Pepe':   3,
    'Luis':   2
}
conductores = {
    'Juan' :  3,
    'Jesus': 2,
    'Maria': 3,
    'Toño' : 1
}
viajes= {}
def siguiente_usuario():
    next_user = min(user_priority,key=user_priority.get)
    user_priority.pop(next_user)
    return next_user

def extraer_conductores():
    return conductores

def calcular_tarifa(conductor):
    antiguedad = conductores.get(conductor)
    tarifa = 20 + (10* antiguedad)
    return tarifa

def viajes_disponibles():
    y=1
    for x in extraer_conductores():
        tarifa= calcular_tarifa(x)
        viajes[y] =tarifa
        y +=1
    return viajes

contador = len(user_priority)
user_viaje = {}
def principal():
    viaje = viajes_disponibles()
    # print(user_priority)
    # print(f'viajes disponobles {viajes}')
    # print('='.center(50,"="))
    for x in range(contador-1):
        usuario = siguiente_usuario()
        id_viaje = min(viaje,key=viaje.get)
        # print(f'El usuario: "{usuario}" tiene el viaje con el ID: {id_viaje}')
        user_viaje[id_viaje] =usuario
        del viaje[id_viaje]
    return user_viaje

print('='.center(50,"="))
print(calcular_tarifa('Juan'))
if __name__ == "__main__":
    principal()