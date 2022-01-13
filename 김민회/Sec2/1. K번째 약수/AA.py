
# K번째 약수 

import sys 
sys.stdin = open('/Users/kimmh/Desktop/Algorithm/Sec2/1.k번째 약수/in4.txt', 'rt')

#--------------------------------------------------------------------------------# 

N, K = map(int, input().split())

order = 0 

for i in range(1, N+1): 
    if N%i == 0: 
        order += 1 
    if order == K: 
        print(i)
        break 
else:
    print(-1) 
