import sys
#sys.stdin=open("input.txt", "r")
n = int(input())
cnt = 0
c = [0]*(n+1)
for i in range(2,n+1):
    if c[i] == 0:
        cnt +=1
        for j in range(i, n+1, i):
            c[j] = 1
print(cnt)