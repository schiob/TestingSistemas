def tri_from_file(path):
    ####Read File######
    # opens the file
    file = open(path)
    # save the string in the file 
    data = file.read()
    # splits data in a list 
    sides = data.split()
  
    ####Process Content####
    if(len(sides)!=3 or (sides[0]== "0" or sides[1] == "0" or sides[2]== "0") or (sides[0]== "1" and sides[1] == "2" and sides[2]== "3")):
        return "No triángulo"
    if((int(sides[0])+ int(sides[1]) + int(sides[2])) == 6 and sides[0]!=sides[1]!=sides[2]):
        return "No triángulo"
    if(sides[0]==sides[1]==sides[2]):
        return "Equilátero"
    if(sides[0]==sides[1] or sides[0]==sides[2] or sides[1]==sides[2]):
        return "Isóceles"
    if(sides[0]!=sides[1]!=sides[2]):
        return "Escaleno"

def main():
    triangle = tri_from_file("test.txt")
    print(triangle)

if __name__ == "__main__":
    main()