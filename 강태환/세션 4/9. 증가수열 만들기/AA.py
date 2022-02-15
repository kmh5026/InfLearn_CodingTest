import sys
#sys.stdin=open("input.txt", "r")
n = int(input())
a = list(map(int, input().split()))
num = 0
cnt = 0
alp = list()
while a:
    if (len(a) == 1) & (a[0]>num):
        alp.append('L')
        cnt+=1
        break
    elif (a[0]>a[-1]) & (a[-1] > num):
        alp.append('R')
        num = a[-1]
        cnt+=1
        a.pop(-1)
    elif (a[0]<a[-1]) & (a[0] > num):
        alp.append('L')
        num = a[0]
        cnt+=1
        a.pop(0)
    elif (a[0]>a[-1]) & (a[0] > num):
        alp.append('L')
        num = a[0]
        cnt+=1
        a.pop(0)
    elif (a[0]<a[-1]) & (a[-1] > num):
        alp.append('R')
        num = a[-1]
        cnt+=1
        a.pop(-1)
    else:
        break
print(cnt)
for x in alp:
    print(x,end='')