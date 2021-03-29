def censurador(badwords_list,text,remp):
    #Interamos la lista de malas palabras
    for badword in badwords_list:
        #Por cada palabra mala se reemplaza con kawai
        text = text.replace(badword, remp)
    return text
    
def Limite(badwords_list, texto, remp, lim):

    new_texto = censurador (badwords_list, texto, remp)
    #Funcion de censura
    if(len(new_texto)) <= lim:
        return "Valido"
    else: 
        return "No Valido"

if __name__ == "__main__":
    l = ["popo", "sangre", "muerte", "maldito"]
    s = "El animal maldito se acercó con una mirada de muerte. Manchas de sangre cubrían el suelo"
    r = "kawai"
    lim = 88

    print(censurador(l,s,r))
    
    print(Limite(l,s,r,lim))

