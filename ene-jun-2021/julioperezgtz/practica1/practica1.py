nms=input("Escribe 5 numeros seguidos separados por espacios: ").split()
pos=neg=par=imp=0
for i in nms :
    if int(i) >= 0 :
        pos+=1
        if int(i)%2==0:
            par+=1
        else:
            imp+=1
    else :
        neg+=1
        if int(i)%2==0:
            par+=1
        else:
            imp+=1
print("Positivos:",pos,"\nPares:",par,"\nNegativos:",neg,"\nImpares:",imp)