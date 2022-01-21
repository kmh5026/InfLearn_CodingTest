import sys
#sys.stdin = open('input.txt', 'rt')
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.insert(0,[0]*(n))
a.append([0]*n)
for i in a:
    i.insert(0,0)
    i.append(0)
cnt = 0
for i in range(1,n+1):
    for j in range(1, n+1):
        if (a[i][j] > a[i-1][j]) and (a[i][j] > a[i+1][j]) and (a[i][j] > a[i][j-1]) and (a[i][j] > a[i][j+1]):
            cnt +=1
print(cnt)