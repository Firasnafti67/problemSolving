s = str(input())
l = []
for i in s:
	if i =='{' or i =='}' or i ==',' or i ==' ':
		continue
	else:
		l.append(i)

print(len(set(l)))