n = int(input())
l = list(map(int, input().split()))
s = "EASY"
for i in l:
	if i==1:
		s = "HARD"

print(s)
