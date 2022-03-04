import sys
#sys.stdin=open("input.txt", "r")
n,m = map(int, input().split())
dan = list(map(int, input().split()))
from collections import deque
dan = deque(dan)
seq = deque(list(range(n)))
cnt = 0
while True:
    num = int(dan.popleft())
    seq1 = int(seq.popleft())
    if num < max(dan):
        dan.append(num)
        seq.append(seq1)
    elif num >= max(dan):
        cnt+=1
        if seq1 == m:
            break
print(cnt)
