# product = lcm * gcd

def gcd(a,b):
    if a == 0:
        return b
    return gcd(b%a,a)

def lcm(a,b):
    prod = a*b
    hcf =gcd(a,b)
    return prod // hcf

t = int(input())

while t:
    n,m = map(int, input().split())
    print("gcd is {} and lcm is {}".format(gcd(n,m),lcm(n,m)))
    t = t-1

