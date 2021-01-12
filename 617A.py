x = int(input())
n = 0
while x:
	if(x>=5):
		x = x-5
		n+=1
	elif(x==4):
		x = x-4
		n+=1
	elif (x==3):
		x = x-3
		n+=1
	elif (x==2):
		x = x-2
		n+=1
	else:
		x = x-1
		n+=1
print(n)