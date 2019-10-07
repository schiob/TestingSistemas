import sys
sys.stdin
def hora(a,b):
    h=""
    aa=0
    aa=a
    bb=b
    if ( aa > 12 ):
        aa=aa-12
    else:
        aa=aa
    hR=aa+":"+bb

if __name__ == '__main__':
    cadena = list(input().strip().split(':'))
    a=0
    b=0
    c=0
    d=0
    a=cadena[0]
    b=cadena[1]
    c=int(a)
    d=int(b)
    hora(c,d)
