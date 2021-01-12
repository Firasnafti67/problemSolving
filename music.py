s = str(input())
l=[]
l.append(s[0])
if len(s)<=1:
	print(s)
else:
	for i in range(1,len(s)):
		if len(l)==0:
			l.append(s[i])
		if s[i]==l[-1]:
			l.pop()
			continue
		l.append(s[i])

	t=''
	for i in l:
		t+=i
	print(t)

