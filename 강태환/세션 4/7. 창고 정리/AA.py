import sys
#sys.stdin=open("input.txt", "r")
n = int(input())
a = list(map(int, input().split()))
b = int(input())
for i in range(b):
    a.sort()
    a[0]+=1
    a[n-1]-=1
a.sort()
print(a[n-1]-a[0])