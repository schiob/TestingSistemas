import sys

def solve(n, p):
    if p <= n/2:
        return p//2
    else:
        return n//2 - p//2


#n = int(input().strip())
#p = int(input().strip())
#result = solve(n, p)
#print(result)