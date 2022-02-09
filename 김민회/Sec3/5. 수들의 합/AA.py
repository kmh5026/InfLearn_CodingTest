
# 수들의 합 ***** 

import sys 
sys.stdin = open('/Users/kimmh/Desktop/Algorithm/Sec3/5. 수들의 합/in4.txt', 'rt')

#--------------------------------------------------------------------------------# 
# 1. N개의 수로 된 수열 
# 2. 이 수열의 i번째 수부터 j번째 수까지의 합이 M이 되는 경우의 수를 구하는 프로그램 작성 
# 
# 입력1) N, M (N은 1이상 10,000이하 / M은 1이상 3억 이하) 
# 입력2) N개로 이루어진 수열 (공백으로 분리) (각 수는 30,000 이하의 자연수) 
# 출력) 경우의 수 
#--------------------------------------------------------------------------------# 

N, M = map(int, input().split()) 

num = list(map(int, input().split())) 


### 시도 1 : in4.txt에 대해 너무 오래 걸림 ### 
'''
cnt = 0 

for i in range(N):
    for j in range(N):
        if sum(num[i:j+1]) == M: 
            cnt += 1 

print(cnt) 
''' 

##### 소스코드 참고 ##### 

left = 0         # 수열의 왼쪽 경계 
right = 1        # 수열의 오른쪽 경계 

cnt = 0          # 경우의 수 초기화 

total = num[0]   # 수열의 합 초기화 (=수열의 첫번째 원소) (수열의 합 중 첫번째 경우의 수) 

while True: 
    if total < M:                     # 1. 수열 합이 M 보다 작은 경우 
        if right < N:                 # 1-1) right이 N 미만인 경우 ( = 우측 인덱스가 수열 길이 이하 ) 
            total += num[right]       #      합산에 추가 
            right += 1                #      우측 경계 늘림 (j 늘림) 
        else:                         # 1-2) right이 N 이상인 경우 ( = 우측 인덱스가 수열 길이 초과 ) 
            break 

    elif total == M:                  # 2. 수열 합이 M 인 경우 
        cnt += 1                      #    일단 하나 count 
        total -= num[left]            #    합산에서 좌측 경계 원소 제외 
        left += 1                     #    좌측 경계 줄임 (i 늘림) 
    
    else:                             # 3. 수열 합이 M 을 초과하는 경우 
        total -= num[left]            #    합산에서 좌측 경계 원소 제외 
        left += 1                     #    좌측 경계 줄임 (i 늘림) 

print(cnt) 


    





