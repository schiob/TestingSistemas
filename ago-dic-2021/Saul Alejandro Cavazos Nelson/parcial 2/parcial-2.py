
def leer_calificaciones ()-> str:
    file_alumno=open("calificaciones.txt", "r")
    alumnos=file_alumno.read()
    alumno= alumnos.split('\n')
    calificacion=0
    promedios=""
    promedio=0
    for i in range(0,len(alumno), 1 ):
        aux=alumno[i].split(' ')
        if i==0:
            aux2=aux[0]
            cont=0
        if aux2 != aux[0]:
            promedio= calificacion / float(cont)
            promedios= promedios +aux2 + " " + str(promedio) +"\n" 
            calificacion=0
            cont=0
            aux2=aux[0]
        if aux2 == aux[0]:
            cont+=1
            calificacion= calificacion + float(aux[2])
    promedio= calificacion / float(cont)
    promedios= promedios +aux2 + " " + str(promedio)
       
    return promedios
            
         


    
if __name__ == "__main__":
   print( leer_calificaciones())