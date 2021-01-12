n = int(input())
s=0
while n:
	n=n-1
	p,q = map(int, input().split())
	if abs(p-q) >=2:
		s+=1

print(s)

