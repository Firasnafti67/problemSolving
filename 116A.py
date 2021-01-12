n = int(input())
s = 0
m = 0
while n:
	n = n-1
	a,b = map(int,input().split())
	m = m+b-a
	s = max(s, m)

print(s)
