nbLivres, nbJours = map(int,input().split())
d=dict()
for i in range(nbLivres):
	d[i]=0
i=1
l = []
while i<=nbJours:
	nbClients = int(input())	
	while nbClients:
		ind,dur = map(int,input().split())
		if i>= d[ind]:
			d[ind]=i+dur
			l.append(1)
		else:
			l.append(0)
		nbClients = nbClients-1
	i = i+1		
	
for i in l:
	print(i)