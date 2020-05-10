
def censura(black_list,sentence,new_word):
    new_blacklist=[]
    for i in black_list:
        new_blacklist.append(i.lower())
    black_list=new_blacklist
    a=sentence.split(" ")
    rvalue=""
    for i in a:
        if((',' in i) or ('.' in i) or (';' in i)):
            special=i[len(i)-1]
            #print(special)
            d=i.replace(",", "")
            #print(d)
            d=d.replace(".", "")
            #print(d)
            d=d.replace(";", "")
            #print(d)
            if d.lower() in black_list:
                if new_word =='*':
                    rvalue = rvalue + ('*'*len(d)) + special + " "
                else:
                    rvalue = rvalue + new_word + special + " "
            else: 
                    rvalue = rvalue + d + special + " "
        elif i.lower() in black_list:
            if new_word =='*':
                rvalue = rvalue + ('*'*len(i)) + " "
            else:
                rvalue = rvalue + new_word + " "
        else:
            rvalue = rvalue + i + " "
    
    return rvalue[:-1] #Para que no salga el ultimo espacio


def validar(sentence1,function,maxlen):
    if(abs(len(sentence1)-len(function))>maxlen):
        return False
    return True

if __name__ == '__main__':
    black_list = ['popo','sangre','muerte','maldito']
    sentence = "El animal maldito se acerco con una mirada de muerte. Manchas de sangre cubrian el suelo"
    new_word = "*"
    print(sentence)
    print(censura(black_list,sentence,new_word))
    print(validar(sentence,censura(black_list,sentence,new_word),2))
