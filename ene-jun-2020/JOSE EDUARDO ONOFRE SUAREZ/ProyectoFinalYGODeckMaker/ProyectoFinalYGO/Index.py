from APIRequest import start
import APIRequest

class Index():

    def pedirNumeroEntero():
 
        correcto=False
        num=0
        while(not correcto):
            try:
                num = int(input("Introduce un numero entero: "))
                correcto=True
            except ValueError:
                print('Error, introduce un numero entero')
     
        return num
 
    salir = False
    opcion = 0
 
    while not salir:
 
        print ("1. Checar efecto de una carta")
        print ("2. Ver todas las cartas disponibles")
        print ("3. Crear Deck")
        print ("4. Ver Deck")
        print ("5. Valorar Deck")
        print ("6. Salir de la App")
     
        print ("Elige una opcion")

        opcion = pedirNumeroEntero()
 
        if opcion == 1:
            try:
                print ("Ver descripción de la carta\n")
                print("")
                APIRequest.start()
                print("")
                print("----- End -----")
            except:
                print("Nombre incorrecto o caracteres no aceptados")
        elif opcion == 2:
            try:    
                print ("Obtener todas las cartas\n")
                print("")
                APIRequest.getAllCards()
                print("")
                print("----- End -----")
            except:
                print("Parece ser que algo salió mal")
        elif opcion == 3:
            print("Opcion 3")
        elif opcion == 4:
            print("Opcion 4")
        elif opcion == 5:
            print("Opcion 5")
        elif opcion == 6:
            salir = True
        else:
            print ("Introduce un numero entre 1 y 4")
    
    print("")
    print ("Hasta pronto!")