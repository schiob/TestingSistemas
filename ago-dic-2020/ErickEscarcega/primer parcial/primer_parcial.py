def tri_from_file(path):
### Reads file and saves the string in the file as a variable ###
    file = open(path)
    sides = file.read()
    l1, l2, l3 = sides.split()
### Process Content ###
    #Checks to see if its a triangle
    if (l1 + l2 ) > l3 and (l1 + l3) > l2 and (l2 + l3) > l1:
        #Three equal sides
        if(l1==l2==l3):
            #Returning string
            return("Equilátero")
        #Two equl sides
        if(l1==l2 or l1==l3 or l2==l3):
            #Returning string
            return("Isóceles")
        #No equal sides
        if(l1 != l2 != l3):
            #Returning string
            return("Escaleno")
    #Not a triangle at all
    else:
        #Returning string
        return("No triángulo")
    # close the damn file!
    file.close()
### Main Function ###
if __name__ == '__main__':
    print (tri_from_file("equi1.txt"))