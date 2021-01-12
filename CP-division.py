from math import *

def fun1(n):
	#O(sqrt(n))
	div1 = set()
	for i in range(1, int(sqrt(n))+1):
		if n%i ==0:
			div1.add(i)
			div1.add(n//i)
	return list(div1)
t = int(input())

while t:
	n = int(input())
	div1 = fun1(n)
	print(*div1)
	t = t-1

