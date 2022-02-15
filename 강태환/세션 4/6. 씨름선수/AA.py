import sys
#sys.stdin=open("input.txt", "r")
n=int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.sort(key = lambda x: [x[0],x[1]], reverse = True)
b = list()
cnt = 0
for c,d in a:
    b.append(d)
    if max(b) == d:
        cnt +=1
print(cnt)        