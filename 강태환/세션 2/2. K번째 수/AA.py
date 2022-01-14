#미안합니다 이건 답지 봤습니다 답답해서
import sys
#sys.stdin = open('input.txt','rt')
T = int(input())
for t in range(T):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[s-1:e]
    a.sort()
    print("#%d %d" %(t+1, a[k-1]))