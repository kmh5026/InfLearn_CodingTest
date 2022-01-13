
import sys 
sys.stdin = open('/Users/kimmh/Desktop/Algorithm/Sec2/2.K번째 수/in1.txt', 'rt')

T = int(input())

for i in range(T):
    N, s, e, k = map(int, input().split())
    ls = list(map(int, input().split()))
    ls = ls[s-1:e] 
    ls.sort() 
    print('#{}'.format(i+1), ls[k-1])









