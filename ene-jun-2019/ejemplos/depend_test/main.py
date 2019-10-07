from molecule import Molecule
from element import Element
from static_storage import StaticStorage

def find_element(name, storage):
    e = storage.search_element(name)
    if e == None:
        return "no se encontró el elemento :("
    return str(e)

def create_molecule(storage, molecule_name, *names):
    elements = []
    for name in names:
        e = storage.search_element(name)
        if e == None:
            return "no se encontró el elemento {} :(".format(name)
        elements.append(e)
    
    molecule = Molecule(molecule_name, *elements)

    return str(molecule)

def main():
    staticS = StaticStorage()
    option = input("1. buscar un elemento\n 2. crear una molécula")

    if option == "1":
        name = input("dame el nombre del elemento que estás buscando: ")
        print(find_element(name, staticS))
    elif option == "2":
        mole_name = input("cómo se llama tu nueva molécula: ")
        n = int(input("cuántos elementos tiene tu molécula: "))
        names = []
        for x in range(n):
            name = input("nombre del elemento {}: ".format(x))
            names.append(name)
        print(create_molecule(staticS, mole_name, *names))

if __name__ == "__main__":
    main()