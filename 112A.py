def compare(s1,s2):
	a = 0
	b = 0
	for i in range(len(s1)):
		a = a + ord(s1[i].lower()) 
		b = b + ord(s2[i].lower())
		if a==b:
			continue
		elif a<b:
			return -1
		else:
			return 1
	return 0



s1 = str(input())
s2 = str(input())

print(compare(s1,s2))