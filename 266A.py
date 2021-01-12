n = int(input())
l = [] 
s= str(input())
for i in range(len(s)):
	l.append(s[i])
d = dict()
d['R'] =[]
d['G'] =[]
d['B'] =[]
for i in range(len(l)):
	if l[i] in d.keys():
		d[l[i]].append((l[i], i))
#print(d)

x=[]
for i in range(len(d['R'])):
	x.append(d['R'][i][1])
x.sort()
#print(x)
r=0
for i in range(len(x)-1):
	if abs(x[i]-x[i+1]) ==1:
		r+=1

y=[]
for i in range(len(d['G'])):
	y.append(d['G'][i][1])
y.sort()
#print(y)
g=0
for i in range(len(y)-1):
	if abs(y[i]-y[i+1]) ==1:
		g+=1
		
z=[]
for i in range(len(d['B'])):
	z.append(d['B'][i][1])
z.sort()
#print(z)
b=0
for i in range(len(z)-1):
	if abs(z[i]-z[i+1]) ==1:
		b+=1

print(b+g+r)
		


		

		



