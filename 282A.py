t = int(input())
l = []
while t:
	t = t-1
	s = str(input())
	l.append(s)
x = 0
for i in range(len(l)):
	if l[i][0]=='-' or l[i][1]=='-':
		x = x-1
	else:
		x = x+1
print(x)