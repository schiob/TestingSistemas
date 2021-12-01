from types import TracebackType


class leer_archivo():
    archivo = open('calificaciones.txt', 'r')
    message = archivo.read()
    archivo.close()
    
    nuevo_mensaje=message.replace('\n', ' ')
    print(nuevo_mensaje)
    lista = list(nuevo_mensaje.split(' '))

    contador = 0
    cali_temp = 0
    nombre_temp = lista[0]
    temp = True
    nombre_igual = False
    calificacion = ''
    for index in lista:

        for i in index:
            if str.isupper(i):
                temp = True

                if contador != 0:
                    calificacion = f"{nombre_temp} {cali_temp/contador}"
                    print(calificacion)
                    contador = 0
                    cali_temp = 0

                nombre_temp = index
                break
            if str.islower(i):
                temp = False
                break
            
        if temp == False:  
            continue
        
        if str.isnumeric(index) and contador == 0:
            cali_temp = int(index)
            contador = contador + 1
            continue

        if str.isnumeric(index) and contador != 0:
            cali_temp = cali_temp + int(index)
            contador = contador + 1
            continue

if __name__ == '__main__':
    calificaciones = leer_archivo()