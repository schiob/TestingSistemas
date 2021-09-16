def practica_3(n,num):
    num_pares=0
    num_negativos=0
    num_positivos=0
    num_inpares=0
    #num=str(num).split()
    for i in range(0,int(n), 1):
        if int(num[i]) % 2 == 0:
            num_pares += 1
        elif int(num[i]) % 2 != 0:
            num_inpares+=1
        if int(num[i])<0:
            num_negativos += 1
        elif int(num[i]) > 0:
            num_positivos +=1
    st=str(num_positivos)+' número(s) positivo(s)'+'\n'+str(num_negativos)+ ' número(s) negativo(s)'+'\n'+str(num_pares)+ ' número(s) par(es)'+'\n'+str(num_inpares)+ ' número(s) impar(es)'
    return st

if __name__ =='__main__':
    #numer_1=input()
    #numer_2=input()
    print(practica_3(5, (0, 1, 2, 3, 4)))