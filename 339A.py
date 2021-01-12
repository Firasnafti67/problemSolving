s= str(input())
l = s.split('+')
for i in range(len(l)):
	l[i] = int(l[i])

l.sort()
c=''
for i in l:
	if c=="":
		c =str(i)
	else:
		c = c + '+'+str(i)
print(c)

