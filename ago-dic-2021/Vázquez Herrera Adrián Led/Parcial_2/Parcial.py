#CyPdS Parcial 2 pt1--Código

def Promedios():
    f=open("Calificaciones.txt",'r')
    rawdata=f.readlines()
    f.close()
    data=[]
    for i in rawdata:
        data.append(i.split(' '))
        
    Alumnos={}
    Promedios=""
    
    for line in data:
        if line[0] in Alumnos:
            Alumnos[line[0]][line[1]]=float(line[-1])
        else:
            Alumnos[line[0]]={line[1]:float(line[-1])}
    
    for alumno in Alumnos:
        x=Alumnos[alumno].values()
        suma=0
        materias=len(Alumnos[alumno].items())
        promedio=0
        for i in x:
            suma+=i
            promedio=(suma/materias)
            
        Promedios+=alumno+" "+str(round(promedio,2))+"\n"
        
    return Promedios