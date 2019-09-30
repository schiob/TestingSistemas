
def DeleteChar(path):
    file = open(path,'r')
    lec = file.read()
    new = ''.join(e for e in lec if e.isalnum())
    file.close()
    return new


