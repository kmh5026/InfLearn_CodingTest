import sys
#sys.stdin = open('input.txt','rt')
a,b = map(int, input().split())
a1 = list(range(1,a+1))
b1 = list(range(1,b+1))
c = list()
for x in a1:
    for y in b1:
        c.append(x+y)
c.sort()
d = [0]*(max(c)+1)
for i in c:
    d[i] += 1
for i in range(len(d)):
    if max(d) == d[i]:
        print(i, end = ' ')