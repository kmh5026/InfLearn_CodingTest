import sys
#sys.stdin=open("input.txt", "r")
tmp = input()
from collections import deque
est = []
for i in range(len(tmp)):
    est.append(tmp[i])
est = deque(est)
n = int(input())

for _ in range(n):
    a = input()
    sub = []
    for i in range(len(a)):
        sub.append(a[i])
    est1 = est.copy()
    sub = deque(sub)
    for x in sub:
       if x in est1:
           if x != est1.popleft():
               print('#%d NO' %(_+1))
               break
    else:        
        if len(est1) > 0:
            print('#%d NO' %(_+1))
        else:
            print('#%d YES' %(_+1))