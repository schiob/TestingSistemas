def calc(nums): #Creando funcion
    par=impar=neg=pos=0
    for i in nums:
        if i%2==0:
            par=+1
        else: impar+=1

        if i<0:
            neg=+1
        elif i>0:
            pos+=1
    return par, impar,neg,pos
if __name__=='__main__':
    n=int(input("CUANTOS NUMEROS QUIERES?"))
    nums=lista(map(int,input().split("  ")))#map--- aplica la conversion a todos los elementos
    resultado=calc(nums)
    print("par=  {}".format(0))
    print("impar= {}".format(1))
    print("pos= {}".format(2))
    print("neg= {}".format(3))
