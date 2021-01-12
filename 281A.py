s = str(input())

l= list(s)
l[0] = l[0].upper()
o=''
for i in l:
	o = o + i

print(o)