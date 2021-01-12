nbLettres = int(input())
if nbLettres == 1:
	print("a")
else:
	s='' 
	for i in range(1,nbLettres*2):
		s=s+"a"
	l=[]
	for i in range(97, 123):
		l.append(chr(i))
	t=2
	print(s)
	k=[]
	k.append(s)
	for i in range(1,len(s)+1):
		print(s[:i]+  (len(s)-t)* l[i] + s[-i:])
		s = s[:i]+  (len(s)-t)* l[i] + s[-i:]
		t+=2
		if t == nbLettres*2:
			break
		k.append(s)

	for i in k[::-1]:
		print(i)
