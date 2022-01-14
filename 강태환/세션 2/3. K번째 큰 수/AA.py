import sys
#sys.stdin = open('input.txt','rt')
n, k = map(int, input().split())
a = list(map(int, input().split()))
from itertools import permutations
result = list(permutations(a, 3))
b = set()
for i in range(len(result)):
    b.add(sum(result[i]))
b = list(b)
b.sort(reverse=True)
print(b[k-1])