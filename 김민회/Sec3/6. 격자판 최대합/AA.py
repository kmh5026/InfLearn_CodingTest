
# 격자판 최대합 

import sys 
sys.stdin = open('/Users/kimmh/Desktop/Algorithm/Sec3/6. 격자판 최대합/in5.txt', 'rt')

#--------------------------------------------------------------------------------# 
# 1. N x N 격자판 
# 2. 각 행의 합, 각 열의 합, 두 대각선의 합 중 가장 큰 합을 출력  
# 
# 입력1) N (1 이상 50 이하) 
# 입력2) N줄에 걸쳐 각 줄에 N개의 자연수 입력 (격자판 생성) (각 수는 100 이하) 
# 출력) 최대 합 출력  
#--------------------------------------------------------------------------------# 

N = int(input()) 

xx = []                 # 격자판 

# 2차원 리스트로 격자판 생성 
for _ in range(N):
    tmp = list(map(int, input().split())) 
    xx.append(tmp) 

# 격자판 확인 
# for i in range(N): 
#     print(xx[i]) 
# 
# 격자판 원소 확인 
# print(xx[7][1]) 

max_sum = 0 


for i in range(N): 

    ### 1. 열 합 확인 
    ver_sum = 0 
    for j in range(N): 
        ver_sum += xx[j][i] 
    if ver_sum > max_sum:
        max_sum = ver_sum 

    ### 2. 행 합 확인 
    if sum(xx[i]) > max_sum:
        max_sum = sum(xx[i]) 
    

# ex) (0, 4) (1, 3) (2, 2) (3, 1) (4, 0) : 역 대각선 

### 3. 대각선 합 확인 
diag1 = diag2 = 0            # 대각선 합 초기화 

for i in range(N): 
    diag1 += xx[i][i]        # 정 대각선 
    diag2 += xx[i][N-1 - i]  # 역 대각선 

if diag1 > max_sum:
    max_sum = diag1 
if diag2 > max_sum: 
    max_sum = diag2 


print(max_sum) 
 