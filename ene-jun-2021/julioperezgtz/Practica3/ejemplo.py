def clasnums(lista):
    pos=neg=par=imp=0
    for i in lista:
        if i>=0:
            pos+=1
            if i%2==0:
                par+=1
            else:
                imp+=1
        else:
            neg+=1
            if i%2==0:
                par+=1
            else:
                imp+=1
    return [pos, neg, par, imp]

print(clasnums([2,2,2,2,2]))