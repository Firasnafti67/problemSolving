import math
t = int(input())
while t:
	t = t-1
	x, y, k = map(int ,input().split())
	a = k + k*y
	if ((a-1)%(x-1)):
		print(k+((a-1)//(x-1))+1)
	else:
		print(k+((a-1)//(x-1)))	
