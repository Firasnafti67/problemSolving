s = str(input())
l=[]
for i in s:
	if i not in l:
		l.append(i)

if (len(l)%2==0):
	print('CHAT WITH HER!')
else:
	print('IGNORE HIM!')