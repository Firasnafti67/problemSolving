n,k = map(int, input().split())
l = list(map(int, input().split()))
c=0
b = False
while 0 in l:
	l.remove(0)

for i in range(k-1,len(l)):
	if l[i]<l[k-1]:
		c=i-1
		b = True
		break

if b == True:
	print(len(l[:c+1]))
else:
	print(len(l))


