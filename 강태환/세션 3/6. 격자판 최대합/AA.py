import sys
#sys.stdin = open('input.txt', 'rt')
n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
tot = 0
for i in range(n):
    ims = list()
    ims.append(a[i][i])
    if sum(ims) > tot:
        tot = sum(ims)
    ims = list()
    ims.append(a[i][n-i-1])
    if sum(ims) > tot:
        tot = sum(ims)
    ims = list()
    for j in range(n):
        ims.append(a[i][j])
        if tot < sum(ims):
            tot = sum(ims)
    ims = list()
    for j in range(n):
        ims.append(a[j][i])
        if tot < sum(ims):
            tot = sum(ims)
print(tot)