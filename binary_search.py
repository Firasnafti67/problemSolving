#Sorted Array
# TIME COMP = O(LOG N)

def binSearch(a, left, right, key):
	while left<=right:
		mid = (left+right) // 2
		if a[mid] == key:
			return mid
		elif a[mid] < key:
			left = mid + 1
		else:
			right = mid -1
	return -1


def findTargetPair(A, K):
	st = set()
	for i in range(len(A)):
		complement = K - A[i]
		if complement in st:
			return [complement, A[i]]
		else:
			st.add(A[i])