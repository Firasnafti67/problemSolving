#bitwise operator and-&
#bitwise operator or - |
#bitwise operator not - ~
#bitwise operator xor - ^
#bitwise operator right shift - >>
#bitwise operator left shift - <<

#right shift is divide in power of 2
#left shift is multiply in power of 2
def evenodd(n):
	if n&1==1:
		print("odd")
	else:
		print("even")

def mulpow2(n, y):
	return n << y

def divpow2(n, y):
	return n >> y

def ispowerof2(n):
	if n<=0:
		return False
	x = n
	y = not(n & (n-1))
	return x and y

def bruteforcecntbits(n):
	#T.C: O(n)
	s = str(bin(n))[2:]
	print("{}".format(s))
	return s.count('1')
def cntbits(n):
	#T.C: O(logn)
	cnt=0
	while n:
		cnt+=1
		n = n & (n-1)
	return cnt

t = int(input())
while t:
	#n,y = map(int, input().split())
	n = int(input())
	#print(ispowerof2(n))
	print(bruteforcecntbits(n))
	print(cntbits(n))
	#evenodd(n)
	#print(divpow2(n,y))
	#print(mulpow2(n,y))
	t = t-1