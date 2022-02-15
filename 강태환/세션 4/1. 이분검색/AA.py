import sys
#sys.stdin = open('input.txt', 'rt')
n,m = map(int, input().split())
a = list(map(int,input().split()))
a.sort()
cnt = 1
for i in range(n):
    if a[i]<m:
        cnt+=1
print(cnt)