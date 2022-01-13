
# 정다면체 

import sys 
sys.stdin = open('/Users/kimmh/Desktop/Algorithm/Sec2/5.정다면체/in5.txt', 'rt')

#--------------------------------------------------------------------------------# 
# 1. 두 개의 주사위 : 정N면체, 정M면체  
# 2. 나올 수 있는 '눈의 합' 중 가장 '확률이 높은' 숫자 출력  
# 3. 정답 여러개일 경우 오름차순으로 
# 4. N과 M은 4, 6, 8, 12, 20 중의 하나 
#--------------------------------------------------------------------------------# 

N, M = map(int, input().split()) 

sum_ = []
for i in range(1, N+1):
    for j in range(1, M+1): 
        sum_.append(i+j)        # 눈의 합들 나열한 리스트 sum_ (중복 O, 범위 = 2 ~ N+M) 

cnt = []
for k in range(2, N+M+1):
    cnt.append(sum_.count(k))   # sum_에서 (2부터 N+M까지) 모든 합의 등장 횟수 count  

max_ = 0 
for i in cnt:
    if i > max_: 
        max_ = i                # 최다 등장 횟수 구함 (max_) 

for idx, val in enumerate(cnt):
    if val == max_: 
        print(idx+2, end=' ')   # 나올 수 있는 '눈의 합' 중 가장 '확률이 높은' 숫자

print()

#--------------------------------------------------------------------------------# 

### 소스코드 참고 
# 앞의 for문 두개를 하나로 줄일 수 있음 

cnt = [0] * (N+M-1)   # 2부터 N+M까지 합 경우의 수 (N+M-1가지) 

for i in range(1, N+1):
    for j in range(1, M+1):
        cnt[i+j-2] += 1      # 합 count 

max_ = 0 
for i in range(len(cnt)): 
    if cnt[i] > max_: 
        max_ = cnt[i]        # 최다 등장 횟수 구함 (max_) 

for i in range(len(cnt)):
    if cnt[i] == max_: 
        print(i+2, end=' ')  # 나올 수 있는 '눈의 합' 중 가장 '확률이 높은' 숫자 




