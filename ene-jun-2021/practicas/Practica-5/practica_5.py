
def funcion_1(arreglo: list[str], texto:str ,reemplazar: str):
    
    #codigo de Censura
    new_text = texto
    for palabra in arreglo:
        if palabra in texto:
            new_text = texto.replace(palabra, reemplazar)
    
    return new_text

def funcion_2(arreglo: list[str], texto: str, reemplazar: str, tamaño):

    new_texto = funcion_1(arreglo, texto, reemplazar)
    #codigo de Validacion
    try:
        if abs(len(new_texto) - len(texto)) <= tamaño:
            return "Valido"
        else: 
            return "No Valido"
    except:
        return "No Valido"

