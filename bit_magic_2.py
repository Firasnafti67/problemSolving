def kthbit(n, k):
	print(str(bin(n))[2:])
	if n & (1 << (k-1)):
		print("SET")
	else:
		print("NOT SET")


def findsingleocc(arr):
	res = arr[0]
	for i in range(1, len(arr)):
		res = res ^ arr[i]
	return res


t = int(input())
while t:
	#n, k = map(int, input().split())
	arr = list(map(int, input().split()))
	kthbit(n,k)
	t = t-1


#[5,3,2,3,2,2,1,5]