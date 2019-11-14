def materias_alumno(direccion):
    archivo = open(direccion,'r+')
    arch = archivo.read()
    #text = ''
    texto = ''
    for i in range(len(arch)):
       if arch[i] != '' or arch[i] == '\n':
           if texto != 'Jose_Lopez' or texto != 'quimica' or texto != 'quimica' or texto != '':
                texto = texto+arch[i]

        
    return texto