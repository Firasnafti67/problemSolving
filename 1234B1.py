from collections import Counter
def social(n,k, v, l):
	for i in v:
		if i not in l:
			for j in range(len(l)-1):
				l[len(l)-1-j] = l[len(l)-2-j]
			l[0] = i
	print(len(l))
	for c in range(len(l)):
		print(l[c],end =" ")
	#return 0

n,k = map(int, input().split())
v = list(map(int, input().split()))
if k<=len(Counter(v)):
	l = [0 for i in range(k)]
else:
	l = [0 for i in range(len(Counter(v)))]

social(n,k, v, l)

	