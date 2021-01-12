n = int(input())
diffMax = float(input())
if n==1 or n==2:
	c = float(input())
	print(0)
else:
	l=[]
	while n:
		c = float(input())
		l.append(c)
		n = n-1
	k=[]
	t=True
	c=0
	while t:	
		for i in range(len(l)-1):
			if abs(l[i+1]-l[i])<diffMax:
				if (i==len(l)-2):
					t=False
					break
			else:
				break
		if t==False:
			break
		for i in range(1,len(l)-1):
			k.append((l[i-1]+l[i+1])/2)
		c+=1
		l[1:len(l)-1]=k
		k=[]
	print(c)



