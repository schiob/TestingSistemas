def censurar(list, str, rem):
    for palabra in list:
        str=str.replace(palabra, rem)
    return str

def validar(list, str, rem, lim): # limite que puede exceder el str censurado con el original
    censura=censurar(list, str, rem)
    if len(censura) <= len(str)+lim:
        return 'Es valido'
    return 'No es valido'