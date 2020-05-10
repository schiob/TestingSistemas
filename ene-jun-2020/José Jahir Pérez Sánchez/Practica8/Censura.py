def censura(malas,frase,buena):
   for elemento in malas:
       nfrase=frase.replace(elemento,buena)
       frase=nfrase
   return nfrase

def censura2(malas,frase,buena,diferencia):
    if((len(frase) - len(censura(malas,frase,buena))*+1 >= diferencia)):
        res=print("Es valido")
    else: 
        res=print("No es valido")
    return res

if __name__ == "__main__":
    print(censura(["popo", "sangre", "muerte", "maldito"], "El animal maldito se acercó con una mirada de muerte. Manchas de sangre cubrían el suelo", "kawai"))
    print(censura2(["popo", "sangre", "muerte", "maldito"], "El animal maldito se acercó con una mirada de muerte. Manchas de sangre cubrían el suelo", "kawaii",4))
    
    malas = ["popo", "sangre", "muerte", "maldito"]
    frase = input("Dame la frase: ")
    buena = input("Dame la palabra buena: ")
    dife = input("Numero de diferencia: ")
    print(censura2(malas,frase,buena,int(dife)))
    