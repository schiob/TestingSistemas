#Getting lines from text to a string
def sameFileOpener(path):
    f = open(path, "r")
    lines = f.read()
    f.close()
    return lines

#Returns if a char in question needs to be added or not
def conserve(c):
    if c.isdigit() or c.isalpha() or c is " " or ord(c) is 10:
        return True
    return False

def applyRules(str):
    ret = ""
    #If it has stuff, read char by char and decide wheter to add it or not
    for c in str.lower():
        if conserve(c):
            ret = ret + c

    return ret

def txtSubMain(path, opener):
    str = opener(path)
    return applyRules(str)


if __name__ == '__main__':
    print(txtSubMain("texto2.txt", sameFileOpener))
