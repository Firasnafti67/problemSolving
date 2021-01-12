n = int(input())
l = []
while n:
	n = n-1
	s = str(input())
	l.append(s)

s=1
for i in range(len(l)-1):
	if l[i][1] == l[i+1][0]:
		s+=1
print(s)