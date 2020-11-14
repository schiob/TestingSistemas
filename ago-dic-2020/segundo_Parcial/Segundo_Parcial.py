def prom(path):
    ####Read File######
    # opens the file
    file = open(path)
    # save the string in the file 
    data = file.read()
    # splits data in a list 
    lista_datos = data.split("\n")
    
    dic_prom={}
    dic_materias={}
####################sacar los alumnos y calificaciones####################
    for i in lista_datos:
        alumno,materia,cali=i.split()
        if not alumno in dic_prom:
            dic_prom[alumno]=round(float(cali),2)
        else:
            dic_prom[alumno]+=round(float(cali),2)     
################### saca el numero de materias de cada alumno ######################
    for i in lista_datos:
        alumno,materias,cali=i.split()
        if not alumno in dic_materias:
            dic_materias[alumno]=1
        else:
            dic_materias[alumno]+=1
################## dividimos el numero de materias por las calificaciones ###############
    for i,j in dic_prom.items():
        dic_prom[i]=j/dic_materias[i]


    return dic_prom

def main():
    promedio = prom("doc_Prac_2.txt")
    print(promedio)

if __name__ == "__main__":
    main()
