#El nombre de este archivo debia ser 24to10 pero en al importarlo en los test daba un problemita asi que por eso agregue la E de Examen
def Conversor(tiempo):
    #ponemos el string a una variable local con la que trabajaremos quitando posibles espacios en blanco
    textito = tiempo.strip()
    hora=''
    minutos=''
    dia='' #Esto es donde se asigna el 'a.m.' o 'p.m.'
    hora += textito[0]
    hora += textito[1]
    hora = int(hora)
    minutos += textito[3]
    minutos += textito[4]

    if hora > 12:
        hora = hora-12
        dia = 'p.m.'
        
    elif(hora==12):
        dia = 'p.m.'

    elif(hora==00):
        hora = 12
        dia = 'a.m.'

    else:
        dia = 'a.m.'

    hora = str(hora)
    #.zfill ayuda a rellenar con ceros a la izquierda segun lo pidas, sirve mas que nada para la hora, (solo sirve en strings)
    hora = hora.zfill(2)
    minutos = minutos.zfill(2)

    return hora+':'+minutos+dia