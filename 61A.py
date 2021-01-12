a = str(input())
b = str(input())
y = int(a,2) ^ int(b,2)
print(bin(y)[2:].zfill(len(a)))