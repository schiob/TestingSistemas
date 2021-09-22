#Parcial 1 Taquitos.py

def taquitos(orden):
    orden=orden.split()
    #Contador
    c=0
    #Menu
    Menu={
        "cachete": 13,
        "lengua": 10,
        "tripitas": 9,
        "pastor": 15,
        "machito": 14
        }
    for i in orden:
        c+=Menu[i]
    return c

def ordenando():
    E=input()
    taquitos(E)