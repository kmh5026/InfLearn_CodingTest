import sys
#sys.stdin=open("input.txt", "r")
n = int(input())
num = input().split()

def reverse(x):
    x.rstrip('0')
    x = x[::-1]
    x = int(x)
    return x

rev = list()
for i in num:
    rev.append(reverse(i))

def isPrime(x):
    for i in range(2,x):
        if x%i == 0:
            return False
    if x == 1:
        return False
    else:
        return True

for i in rev:
    if isPrime(i):
        print(i, end = ' ')