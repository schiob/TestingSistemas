#Getting lines from text to a list
def getLines(path):
    f = open(path, "r")
    lines = f.read()
    f.close()
    return lines

#Returns if a char in question needs to be added or not
def conserve(c):
    if c.isdigit() or c.isalpha() or c is " " or c is "\n":
        return True
    return False

def txtSub(path):

    lines = getLines(path)

    #Variable to return after the rules are aplied
    ret = ""

    #If it has stuff, read char by char and decide wheter to add it or not
    for c in lines.lower():
        if conserve(c):
            ret = ret + c

            # for l in lines:
            #     #If its a jump line, add it
            #     if l is "\n":
            #         ret = ret + "\n\n"
            #         continue
            #
            #     #If it has stuff, read char by char and decide wheter to add it or not
            #     for c in l.lower():
            #         if conserve(c):
            #             ret = ret + c

    return ret

print(txtSub("texto2.txt"))
