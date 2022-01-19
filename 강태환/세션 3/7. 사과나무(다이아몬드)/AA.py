import sys
#sys.stdin = open('input.txt', 'rt')
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
b = n//2
c = n//2
tot = 0
for i in range(n):
    for j in range(b,c+1):
        tot += a[i][j]
    if i < n//2:
        b -= 1
        c += 1
    else:
        b += 1
        c -= 1
print(tot)
    