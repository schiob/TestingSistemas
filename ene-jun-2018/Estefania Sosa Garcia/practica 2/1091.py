import sys
sys.stdin
while k!=0:
	k=sys.stdin.readline()
	if k>0 and K<=1000:
		n,m=list(map(int, input().split(' ')))
		if n>-10000 or m<10000:
			for x in range(k):
				X,Y=list(map(int, input().split(' ')))
				if X>=-10000 or Y<=10000:
					if X>N and Y>M:
						print("NE")
					elif X<N and Y>M:
						print("NO")
					elif X<N and Y<M:
						print("SO")
					elif X>N and Y<M:
						print("SE")
					elif X==N or Y==M:
						print("divisa")