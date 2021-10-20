
def Principal ()-> list:
    viajes=viajes_disponibles()
    viajes_usuarios=[]
    usuario=""
    for i in range(0,len(viajes),1):
        if  usuario!="vacio":
            usuario=siguiente_usuario()
            id_conductor=int(viajes[i][0])
            viajes_usuarios+=[[usuario,"viaje " +str(id_conductor) ]]
        else:
            break
        
    return viajes_usuarios

def siguiente_usuario()-> str:
    file_usuarios = open("usuario.txt", "r+")
    usuarios=file_usuarios.read()
    if usuarios!='':
        usuario=usuarios.split('\n')
        prioridad=11
        numero_de_usuario=0
        nombre_de_usuario=""
        for i in range(0,len(usuario), 1 ):
            Usario_p=usuario[i].split(' ')
            if prioridad>int(Usario_p[1]):
                prioridad=int(Usario_p[1])
                numero_de_usuario = int(i)
                nombre_de_usuario=str(Usario_p[0])
        usuario.pop(numero_de_usuario)
        stri=""
        file_usuarios.truncate(0)
        for i in range(0,len(usuario), 1 ):
            if i<len(usuario)-1:
                stri += str(usuario[i])+"\n"
            else:
                stri += str(usuario[i])
        file_usuarios.seek(0)
        file_usuarios.write(str(stri))
        file_usuarios.close()
        return nombre_de_usuario
    return "vacio"

def viajes_disponibles()->list:
    conductores=extraer_conductores()
    id_conductor=1
    viajes =[]
    for i in range(0,len(conductores),1):
        viajes +=[[id_conductor,calcular_tarifa(conductores[i][1])]]
        id_conductor+=1
    return viajes


def extraer_conductores()-> list:
    file_conductores=open("conductores.txt",'r')
    conductores=file_conductores.read()
    file_conductores.close()
    conductores=conductores.split("\n")
    conductores_list=[]
    for i in range(0,len(conductores), 1 ):
        aux=conductores[i].split(' ')
        conductores_list+=[[str(aux[0]),int(aux[1])]]
    return conductores_list

def calcular_tarifa(antiguedad_conductor)-> int:
    antiguedad=antiguedad_conductor
    tarifa=20+(10*antiguedad)
    return tarifa


if __name__ == "__main__":
    print(viajes_disponibles())