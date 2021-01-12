n = int(input())
l = [i for i in range(1,n+1)]
c = list(map(int,input().split()))
c.remove(c[0])
d = list(map(int, input().split()))
d.remove(d[0])

e = list(set(d) | set(c))
e.sort()

if e==l:
	print("I become the guy.")
else:
	print("Oh, my keyboard!")
