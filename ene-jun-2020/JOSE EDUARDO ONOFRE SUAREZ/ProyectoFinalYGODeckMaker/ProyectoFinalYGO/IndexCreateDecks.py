import DBDecks
import MainDeck

def opcionCrearDecks():

    print("\n******************************")
    print("*****BIENVENIDO AL SISTEMA*****")
    print("*****DE CREACION DE DECKS*****")
    print("******************************\n")

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
 
        print ("1. Insertar Cartas a MainDeck")
        print ("2. Insertar Cartas a ExtraDeck")
        print ("3. Insertar Cartas a SideDeck")
        print ("4. Salir al Menu Principal")
        
      
     
        print ("Elige una opcion")

        opcion = pedirNumeroEntero()
 
        if opcion == 1:
            try:
                print ("Insrtar Cartas al MainDeck\n")
                print("")
                MainDeck.InsertaMainDeck()
                print("")
                print("----- End -----")
            except:
                print("Nombre incorrecto o caracteres no aceptados")
        elif opcion == 2:
            try:    
                print ("Insertar Cartas a ExtraDeck\n")
                print("")
                
                print("")
                print("----- End -----")
            except:
                print("Parece ser que algo salió mal")
        elif opcion == 3:
            try:    
                print ("Insertar Cartas a SideDeck\n")
                print("")
               
                print("")
                print("----- End -----")
            except:
                print("Parece ser que algo salió mal")
        elif opcion == 4:
            salir = True
        
        else:
            print ("Introduce un numero entre 1 y 4")
    
    print ("\nSalió de la construccion de Decks")