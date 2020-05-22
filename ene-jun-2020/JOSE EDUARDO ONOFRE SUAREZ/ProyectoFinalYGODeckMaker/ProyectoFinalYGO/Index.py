from APIRequest import start
import APIRequest
import IndexCreateDecks
import VisualizarFullDeck
import time

class Index():

    print("\n****************************************")
    print("**********BIENVENIDO AL SISTEMA**********")
    print("**********MENU PRINCIPAL DE OPCIONES**********")
    print("****************************************\n")


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
                time.sleep(1)
                APIRequest.getAllCards()
                print("")
                print("----- End -----")
            except:
                print("Parece ser que algo salió mal")
        elif opcion == 3:
            try:    
                print ("Construir DECK\n")
                print("")
                IndexCreateDecks.opcionCrearDecks()
                print("")
                print("----- End -----")
            except:
                print("Parece ser que algo salió mal")
        elif opcion == 4:
            try:    
                print ("\n***************MOSTRANDO SU DECK COMPLETO***************\n")
                print("")
                time.sleep(1)
                VisualizarFullDeck.RetrieveAll()
                print("")
                print("----- End -----")
            except:
                print("Parece ser que algo salió mal")
        elif opcion == 5:
            print("Opcion 5")
        elif opcion == 6:
            salir = True
        else:
            print ("Introduce un numero entre 1 y 4")
    
    print("")
    print ("Hasta pronto!")