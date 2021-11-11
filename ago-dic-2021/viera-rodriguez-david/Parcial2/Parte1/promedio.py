def calc_prom ()-> str:
    archivo=open("calificaciones.txt","r")
    alumnos=archivo.read()
    estudiante=alumnos.split('\n')
    calif=0
    promedios=""
    prom=0
    for i in range(0,len(estudiante),1):
        temp=estudiante[i].split(' ')
        if i==0:
            temp2=temp[0]
            cont=0
        if temp2 != temp[0]:
            promedios=promedios+temp2+""+str(prom)+"\n"
            prom=calif/float(cont)
            calif=0
            cont=0
            temp2=temp[0]
        if temp2 == temp[0]:
            cont+=1
            calif=calif+float(temp[2])
    prom=calif/float(cont)
    promedios=promedios+temp2+""+str(prom)
    return promedios 