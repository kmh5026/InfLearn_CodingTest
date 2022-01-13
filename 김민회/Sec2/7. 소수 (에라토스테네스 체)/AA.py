
# 소수 (에라토스테네스 체) 

import sys 
sys.stdin = open('/Users/kimmh/Desktop/Algorithm/Sec2/7.소수(에라토스테네스 체)/in5.txt', 'rt')

#--------------------------------------------------------------------------------# 
# 1. 자연수 N 입력되면, 1부터 N까지 중 소수의 개수를 출력 
# 2. 제한시간 1초 *** 
# 
# ex) N = 20 >> 8개 (2, 3, 5, 7, 11, 13, 17, 19) 
#--------------------------------------------------------------------------------# 

N = int(input()) 

cnt = 0 
ls = []
for i in range(2, N+1): 
    if any(i % j == 0 for j in range(2, i)): 
        cnt += 0  
    else: 
        cnt += 1 


print(cnt) 
    
# any문을 사용해서인지 존나 오래 걸림 


cnt = 0 
ls = []
for i in range(2, N+1): 
    tmp = 0 
    for j in range(2, i):
        if i % j == 0: 
            tmp = 1 
            break 
    if tmp == 0:
        cnt += 1 

print(cnt) 

# 이것도 시발... 

