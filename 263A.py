r=[]
j =0
for i in range(5):
	l = list(map(int, input().split()))
	if 1 in l:
		c=i+1
		j=l.index(1) + 1
	r.append(l)

print(abs(3-j)+abs(3-c))
