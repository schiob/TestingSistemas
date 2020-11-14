def open_file(path) -> str:
    file = open(path)
    file_info = file.read()
    lista = file_info.splitlines()
    #print(lista)
    return lista

# def testeo(file_info):
#     prom_jose = 0.0
#     cont_jose = 0
#     prom_maria = 0.0
#     cont_maria = 0
#     lista = file_info
#     contador_de_prom = 0
#     alum_prom = []
#     cont_de_alumn =0
#     for lista in file_info:
#        #for  cosa in lista:
#         print(lista[0])
#         alum_prom.append(lista[0])
#         cont_de_alumn += 1
#         if(cont_de_alumn >= 1):
#             for alumno in alum_prom:
#                 if(lista[0] != alumno):
#                     alum_prom.append(alumno)
                    
#     print(alum_prom)
        #   cont_alum +=1
        # if    cont_alum == 1 and len(alum_prom) ==0):
        #     alum_prom.append(cosa)
        # if    cont_alum == 1 ):
        #     alum_prom.append(cosa)
        # if    cont_alum == 1):
        #     alum_prom.append(cosa)   
        #print(cosa)
        # if    cont_alum == 3):
        #       cont_alum =0
        
        # pass
def calcula_promedio(data):
    prom_alum = {}
    cont_alum = 0
    for cosa in data:
        nom,mat,calif=cosa.split()
        if(nom in prom_alum):
            prom_alum[nom]+=float(calif)
        else:
            prom_alum[nom]=float(calif)
            cont_alum +=1

    for a,b in prom_alum.items():
        prom_alum[a]=b/cont_alum
    return prom_alum


if __name__ == "__main__":
    data = open_file("archivo.txt")
    print(calcula_promedio(data))
    