'''
def fib(n):
	if n<=1:
		return n
	else:
		return fib(n-1) + fib(n-2)
'''
globalfib = [0,1]

def fib(n):

	if n < len(globalfib):
		return globalfib[n]
	else:
		for i in range(len(globalfib),n+1):
			last = globalfib[-1]
			beforelast = globalfib[-2]
			globalfib.append(last+beforelast)
		return globalfib[n]


t = int(input())
for i in range(t):
	n = int(input())
	print(fib(n))