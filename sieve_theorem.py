from math import *


def generate_primes(n):
	primes= [True]*(n+1)
	primes[0] = False
	primes[1] = False
	for p in range(2,int(sqrt(n))+1):
		if primes[p]==True:
			for i in range(p*p,n+1,p):
				primes[i]=False
	for i in range(0,len(primes)):
		if primes[i]==True:
			print(i, end=" ")


t = int(input())
while t:
	n = int(input())
	generate_primes(n)
	t = t-1