import sys
#sys.stdin=open("input.txt", "r")
n,m = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
cnt=0
while len(a)>0:
    if len(a) <= 1:
        cnt+=1
        break
    elif a[0] + a[-1] > m:
        a.pop(0)
        cnt+=1
    elif a[0]+a[-1] <= m:
        a.pop(0)
        a.pop(-1)
        cnt+=1
print(cnt)