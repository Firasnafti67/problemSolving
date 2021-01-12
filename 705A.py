n = int(input())
if n==1:
	print("I hate it")
s=""
if n>=2:
	i=1
	while i<n:
		if i%2==0:
			s+="I love that "
		else:
			s+="I hate that "
		i=i+1
	if n%2==0:
		s+= "I love it"
	else:
		s+= "I hate it"

	print(s)