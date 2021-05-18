

def bad_words(badwords_list, text, remp):
    
    #iteramos la lista de las malas palabras:
    for badword in badwords_list:
        #Por cada mala palabra en la lista de malas palabras
        #Remplazamos la mala palabra en el string
        text = text.replace(badword, remp)
        #print(text)
     
    return text


def check_badwords(badwords_list, text, remp, n):
    texto = bad_words(badwords_list, text, remp)
    if len(text) == n:
        return "Es válido"
    else:
        return "No es valido"


if __name__ == "__main__":
    l = ["popo", "sangre", "muerte", "maldito"]
    s = "El animal maldito se acercó con una mirada de muerte. Manchas de sangre cubrían el suelo"
    r = "kawai"
    n = 88
    
    print(bad_words(l, s, r))
    print(check_badwords(l, s, r, n))

     