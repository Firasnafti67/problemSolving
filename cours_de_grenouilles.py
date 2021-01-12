nbGrenouilles = int(input())
nbTours = int(input())
d=dict()
k = [0]*nbGrenouilles
if nbTours == 1:
	num, dist = map(int,input().split())
	print(num)
else:
	while nbTours:
		if k.count(max(k))==1:
			d[k.index(max(k))+1]=d[k.index(max(k))+1] + 1
		num, dist = map(int,input().split())
		if nbTours ==1:
			break
		if num not in d.keys():
			d[num]=0
		k[num-1]+=dist
		nbTours = nbTours - 1

	m = 0
	t = nbGrenouilles
	for i in d.keys():
		if d[i]==m and i<=t:
			t = i 
			m = d[i]
		elif d[i]>m:
			t = i 
			m = d[i]	

	print(t)

