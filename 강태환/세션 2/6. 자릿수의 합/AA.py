import sys
#sys.stdin = open('input.txt','rt')
n = int(input())
b = list(input().split())
c = list()
def digit_sum(x):
    for i in x:
        c.append(sum(int(j) for j in i))
    return c
digit_sum(b)
maxx = 0
for i in range(n):
    if c[i] > maxx:
        maxx = c[i]
        idx = i
    else:
        continue
print(int(b[idx]))