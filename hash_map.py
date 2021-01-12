def isPalindrome(s):
	return s == s[::-1]



#TC= O(NLOGN)
def isAnagram(s1, s2):
	print(sorted(s1))
	print(sorted(s2))
	return sorted(s1) == sorted(s2)


#TC = O(N)

from collections import Counter

def isAnagram(s1, s2):
	print(Counter(s1))
	print(Counter(s2))
	return Counter(s1) == Counter(s2)
