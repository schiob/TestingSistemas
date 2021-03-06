def Triangulares(numero):
    if numero < 0:
        return "Número inválido."
    else:
        resultado = (numero*(numero+1))/2
        return resultado