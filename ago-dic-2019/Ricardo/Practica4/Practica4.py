import re
def leerarchivo(lugar):
    archivo = open(lugar,'r+')
    arch=archivo.read()
    texto=''
    #arch.lower()
    #arch=re.compile(r'\W+', re.UNICODE).split(arch)
    for i in range(len(arch)):
        if arch[i].isalnum() or arch[i].isalpha() or arch[i].isdigit() or arch[i] == ' ' or arch[i] == '\n':
            #arch[i].lower()
            if arch[i] != '':
                texto = texto+arch[i]
                texto.lower()
    return texto
