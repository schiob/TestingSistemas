def censura(arreglo:list, texto:str, remplazo:str):
    for i in arreglo:
        texto = texto.replace(i,remplazo)
    return texto


def censuraValida(arreglo:list, texto:str, remplazo:str, longitudValida:int):
    resultado = censura(arreglo,texto,remplazo)
    longitudRes = len(resultado)
    if longitudValida > longitudRes:
        return "Es válida"
    else:
        return "No es válida"


if __name__ == '__main__':
    arreglo = ["Manchas", "acercó", "suelo", "maldito"]
    texto = "El animal maldito se acercó con una mirada de muerte. Manchas de sangre cubrían el suelo"
    remplazo = "cristal"
    longitudTexto = len(texto)
    longitudValida = longitudTexto + 10

    print(censuraValida(arreglo,texto,remplazo,longitudValida))