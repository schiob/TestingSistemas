import sys
sys.stdin
def hora(a,b):
    hR=[]
    y=b
    aa=a
    if ( aa > 0 and aa<13  ):
        aa=a
    else:
        aa=aa+12
    hR=aa,y,"hrs"
    return hR
    

if __name__ == '__main__':
    cadena = list(input().strip().split(':'))
    y=""
    w=""
    a=0
    b=0
    c=0
    d=0
    a=cadena[0]
    b=cadena[1]
    c=b.split("p.m")
    d=int(a)
    e=c[0]
    a=int(e)
    hora(d,a)
	
