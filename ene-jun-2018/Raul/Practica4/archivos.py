
def IMCFile(a1,p1):
    
    file = open('c:/test/imc.txt','w')
    c = p1/(a1 ** 2)
    file.write("{0:.2f}".format(c))
    file.close()





if __name__ == '__main__':
    
    a,p =input().split(' ')
    a1 = float(str(a))
    p1 = float(str(p))
    ok = IMCFile(a1,p1)
    
