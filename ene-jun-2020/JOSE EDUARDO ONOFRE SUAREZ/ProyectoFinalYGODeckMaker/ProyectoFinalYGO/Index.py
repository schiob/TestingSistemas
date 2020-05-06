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
 
        print ("1. Checar efecto de carta")
        print ("2. Exportar desde API")
        print ("3. Crear Deck")
        print ("4. Ver Deck")
        print ("5. Valorar Deck")
        print ("6. Salir de la App")
     
        print ("Elige una opcion")

        opcion = pedirNumeroEntero()
 
        if opcion == 1:
            print ("Ver descripción de la carta\n")
            print("")
            APIRequest.start()
            print("")
            print("----- End -----")
        elif opcion == 2:
            print ("Opcion 2")
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