import sys
#sys.stdin=open("input.txt", "r")
n = int(input())
a = list(map(int, input().split()))
nj = 0
scr = 0
for i in range(n):
    if a[i] == 1:
        nj += 1
        scr = scr+nj
    else:
        nj = 0
        scr = scr+nj
print(scr)