import sys
#sys.stdin = open('input.txt', 'rt')
n,k = map(int, input().split())
a = list()
for i in range(n):
    a.append(int(input()))
lt = 0
rt = max(a)
while lt <= rt:
    mid = (lt+rt)//2
    cnt = 0
    for i in range(n):
        cnt += a[i]//mid
    if cnt >= k:
        tval = mid
        lt = mid+1
    else:
        rt = mid-1
print(tval)