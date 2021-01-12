n,k = map(int,input().split())
while k:
	k = k-1
	if str(n)[len(str(n))-1]=='0':
		n = n//10	
	else:
		n = n-1

print(n)
