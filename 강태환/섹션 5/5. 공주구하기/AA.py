import sys
#sys.stdin=open("input.txt", "r")
n,k = map(int, input().split())
a = list(range(1,n+1))
from collections import deque
a = deque(a)
while len(a)>=1:
    a.rotate(-(k-1))
    a.popleft()
    if len(a) == 1:
        print(a[0])