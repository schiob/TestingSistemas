def leer_prom_alumno(name:str):
    dicprom={}
    dicCant={}
    dicFinal={}
    f=open(name)
    datos=f.read()
    listaDatos=datos.split('\n')
    #///////////////////////////////Obtiene suma de promedios///////////////////////////////
    for i in listaDatos:
        nombre,materia,calif=i.split()
        if not nombre in dicprom:
            dicprom[nombre]=float(calif)
        else:
            dicprom[nombre]+=float(calif)
    #/////////////////////////////////////////Obtiene materias contadas/////////////////////
    for j in listaDatos:
        nombres,materias,califs=j.split()
        if not nombres in dicCant:
            dicCant[nombres]=1
        else:
            dicCant[nombres]+=1

    for k,v in dicprom.items():
        dicprom[k]=v/dicCant[k]

    
    return dicprom


if __name__ == "__main__":
   print(leer_prom_alumno('/home/bryan/TestingSistemas/ago-dic-2020/Bryan Balderas/segundo parcial/alumnos.txt')) 