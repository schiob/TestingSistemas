#Este archivo sirve pare probar el sistema desde la terminal
#Lleva un switch case para testear que el CRUD se haga correctamente
#NO CONFUNDIR ESTE ARCHIVO CON EL TEST !!!
from twitter_ap import AppTwitter
from Tweet import *
from baseladvd import basedb

print("Bienvenido al Sistema, elija una opción: ")
option= int(input("Buscar Usuario: 1 \nCrear Usuario: 2 \nActualizar Usuario: 3 \nBorrar Usuario: 4 \n"))
cont = 0
db = basedb()
y = AppTwitter()
while cont == 0:
    if option == 1:

        usr = input("Introduzca un Usuario:")
        res = basedb.selectUsuario(db,usr)
        print(res)
    elif option == 2:
        usuario = input("Introduzca un Usuario:")
        t=AppTwitter.getUsuario(y,usuario)
        res1 = basedb.insert_db(db,t)
        print(res1)
    elif option == 3:
        usuario = input("Introduzca el Usuario a actualizar:")
        rank = input("Puesto en el Ranking:")
        categ = input("Categoria:")
        v = input("Número de Victorias:")
        d = input("Número de Derrotas:")

        res = basedb.updateUsuario(db,usuario,rank,categ,v,d)
        print(res)
    elif option == 4:
        usuario = input("Introduzca el Usuario a eliminar:")
        res = basedb.deleteUsuario(db,usuario)
        print(res)
    else:
        print("Introduzca una opción válida.\n")
    cont= 1
