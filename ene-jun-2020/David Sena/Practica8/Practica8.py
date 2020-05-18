
def censura(texto, palabras_malas, reemplazo):
    for elemento in palabras_malas :
        # checamos si la palabra es el texto principal
        if elemento in texto :
            #Reemplazamos las palabras
            texto = texto.replace(elemento, reemplazo)
    
    return  texto   

def censura2(texto,palabras_malas,reemplazo,diferencia):
    if((len(texto) - len(censura(texto, palabras_malas, reemplazo))*+1 >= diferencia)):
        res=print("Es valido")
    else: 
        res=print("No es valido")
    return res 
 
def main():
    
    texto = "El animal maldito lleno de popo se acercó con una mirada de muerte. Manchas de sangre cubrían el suelo"
 
   
    nuevo_texto = censura(texto, ['popo','sangre', 'muerte', 'maldito'] , "kawai")
    
    print(nuevo_texto)
           
if __name__ == '__main__':
    main()