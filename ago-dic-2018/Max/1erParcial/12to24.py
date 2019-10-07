def reloj(rj):
    i = 0
    hrs =[] #guardare el string en una lista para poder recorrer sus caracteres
    ########## para am
    if rj[6] == 'a' and rj[7] == 'm': #el quinto caracter de la lista horas|Posicion de los caracteres
        while i < len(rj): #empezare a recorrer el string, caracter por caracter                           01234567
            if  rj[i] != '.' and rj[i]!='a' and rj[i]!='m': #al recorrer el string buscare " . , a , m" de 10:00.am
                hrs.append(rj[i]) #agregare a la lista los caracteres
            i = i + 1 #contador para recorrer el string
        Hora = print(''.join(hrs)+'hrs') #imprimo la hora agregando "hrs"

    if rj[6] == 'a' and rj[7] == 'm' and rj[0] == '1' and rj[1] =='2':
        while i < len(rj):
            if  rj[i] != '.' and rj[i]!='a' and rj[i]!='m':
                hrs.append(rj[i])
            i = i + 1
        Hora = print('00:00hrs')
############################################################################ para pm

    if rj[0] == '' and rj[1] == '' and rj[6] == 'p' and rj[7] == 'm':
        Hora = print('13' + ''.join() + 'hrs')

    return Hora

if __name__ == '__main__':
    hrs = []
    rj = str(input('Hora: '))
    reloj(rj)
