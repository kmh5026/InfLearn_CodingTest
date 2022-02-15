import sys
#sys.stdin=open("input.txt", "r")
n=int(input())
a = [list(map(int,input().split())) for _ in range(n)]
a.sort(key=lambda x:(x[1],x[0]))
b = 0
cnt = 0
for c,d in a:
    if c >= b:
        cnt +=1
        b = d
print(cnt)