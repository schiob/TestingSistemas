def practica3(n,num):

    pares=0
    negativos=0
    positivos=0
    inpares=0

    for i in range(0,int(n), 1):

        if int(num[i])<0:
            negativos += 1

        elif int(num[i]) > 0:
            positivos +=1
    
        if int(num[i]) % 2 == 0:
            pares += 1

        elif int(num[i]) % 2 != 0:
            inpares+=1
        
    st=str(positivos)+'número(s) positivo(s)'+'\n'+str(negativos)+ 'número(s) negativo(s)'+'\n'+str(pares)+'número(s) par(es)'+'\n'+str(inpares)+ 'número(s) impar(es)'
    return st

if __name__ =='__main__':
    print(practica3(5, (0, 1, 2, 3, 4)))