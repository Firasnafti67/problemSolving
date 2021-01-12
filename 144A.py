n = int(input())
l = list(map(int,input().split()))
c = l.index(max(l))
d =len(l)-1-l[::-1].index(min(l))
if c!=0:
	if d<c:
		d=d+1
	print(c+abs(d+1-len(l)))
else:
	print(abs(d+1-len(l)))
