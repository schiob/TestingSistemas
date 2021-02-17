### solo para tener algo que hacer commit
def contador(linea):
    lista = linea.split(" ")
    j = False
    while j == False:
        try:
            for i in range(len(lista)):
                lista[i] = int(lista[i])
            j = True
        except:
            return "Introduzca un número válido"
    
    cpos=cneg=cpar=cimpar=0

    for i in range(len(lista)):
        if lista[i]==0:
            cpar +=1
        else:
            if lista[i]>=0:
                cpos+=1
                if lista[i]%2==0:
                    cpar+=1
                else:
                    cimpar+=1
            else:
                cneg+=1
                if lista[i]%2==0:
                    cpar+=1
                else: cimpar+=1
    cadena = cpos," numero(s) positivo(s).\n",cneg," numero(s) negativo(s).\n",cpar," numero(s) par(es).\n",cimpar," numero(s) impar(es)."
    return cadena