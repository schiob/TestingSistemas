
def funcion_1(arreglo, texto:str ,reemplazar):
    
    #codigo para modificar el texto
    new_text = texto
    for palabra in arreglo:
        if palabra in texto:
            new_text = texto.replace(palabra, reemplazar)
    
    return new_text

def funcion_2(arreglo, texto: str, reemplazar, tamaño):

    new_texto = funcion_1(arreglo, texto, reemplazar)
    #Funcion de censura
    if abs(len(new_texto) - len(texto)) <= tamaño:
        return "Valido"
    else: 
        return "No Valido"
