import sys
#sys.stdin = open('input.txt', 'rt')
a = list()
for _ in range(2):
    n = int(input())
    b = list(map(int, input().split()))
    for i in range(n):
        a.append(b[i])
a.sort()
for i in range(len(a)):
    print(a[i], end = ' ')