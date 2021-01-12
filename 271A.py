y= int(input())
y+=1
b= True
while b:
	s = str(y)
	if s[0]!=s[1] and s[1]!= s[2] and s[1]!= s[3] and s[2]!=s[3] and s[0]!=s[2] and s[0]!=s[3]:
		print(y)
		b= False
	else:
		y+=1