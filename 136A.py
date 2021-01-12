n = int(input())
l = list(map(int, input().split()))
c = []
for i in range(len(l)):
	c.append(0)
for i in range(len(l)):
	c[l[i]-1] = i+1
s = str(c[0])
for i in range(1, len(c)):
	s = s+ " "+ str(c[i])
print(s)
