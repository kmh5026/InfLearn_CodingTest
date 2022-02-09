
# 곳감 (모래시계) ******* 

import sys 
sys.stdin = open('/Users/kimmh/Desktop/Algorithm/Sec3/8. 곳감/in5.txt', 'rt')

#--------------------------------------------------------------------------------# 
# 1. N x N 격자판 형식의 마당에 감을 말리려 함 (N은 홀수) 
# 2. 각 격자 안에는 감의 수
# 3. 격자의 행을 기준으로 왼쪽, 또는 오른쪽으로 회전시켜 위치를 변경해 모든 감이 잘 마르게 
# 
# ex) 회전명령 정보가 2  0  3이면 2번째 행을 왼쪽으로 3만큼 회전 
#     [12 39 30 23 11]  >  [23 11 12 39 30] 
#     첫번째 수 = 행 번호 / 두번째 수 = 방향 (0은 왼, 1은 오른) / 세번째 수 = 회전하는 격자의 수 
#
# 4. M개의 회전 명령을 실행하고 난 후 마당의 모래시계 영역에는 감이 총 몇개가 있는지 출력하는 프로그램 
# 
# 입력1) N (3 이상 20 이하의 홀수) 
# 입력2) N줄에 걸쳐 각 줄에 N개의 자연수 입력 (각 격자의 감 수) (각 수는 100 이하) 
# 입력3) M (1 이상 10 이하) 
# 입력4) M줄에 걸쳐 M개의 회전명령 정보 
# 출력) 총 감의 수 (모래시계꼴 합) 
#--------------------------------------------------------------------------------# 

N = int(input()) 

# 격자판 생성 
xx = [ list(map(int, input().split())) for _ in range(N) ] 

M = int(input()) 

# 회전명령 정보 
# rot = [ list(map(int, input().split())) for _ in range(M) ] 


# 회전명령 실행 ***** 
#  >> 첨에 1,2,5번만 맞음 씨팔..  >>> 회전 횟수가 격자판 크기(N)를 초과했기 때문 >>> 나눗셈 나머지 개념 이용해서 수정 

for i in range(M):           # 총 M번 실행 ( i = [2, 0, 3] ) 
    row, direction, step = map(int, input().split()) 

    if direction == 0:       # 왼쪽 
        xx[ row-1 ] = xx[ row-1 ][ step%N: ] + xx[ row-1 ][ :step%N ]      # step을 N으로 나눈 나머지 지점을 기준으로 잘라서 이어붙임 
        
    else:               # 오른쪽 
        xx[ row-1 ] = xx[ row-1 ][ -step%N: ] + xx[ row-1 ][ :N-step%N]  


''' 
# 소스코드 참고 ***** (Sec0 리스트 관련 함수 활용) 
for i in range(M): 
    row, direction, step = map(int, input().split()) 

    if direction == 0:                              # 왼쪽으로 회전 
        for _ in range(step):                       # : 왼쪽의 원소들을 뽑아내서 오른쪽으로 차례대로 붙이는 개념 = append( _.pop(0) )
            xx[row-1].append(xx[row-1].pop(0)) 
            
    else:                                           # 오른쪽으로 회전 
        for _ in range(step):                       # : 오른쪽의 원소들을 뽑아내서 왼쪽으로 차례대로 붙이는 개념 = insert( 0, _.pop() ) 
            xx[row-1].insert(0, xx[row-1].pop()) 
'''

# 모래시계 꼴 합산 *** 
# (0, 0) (0, 1) (0, 2) (0, 3) (0, 4) 
#        (1, 1) (1, 2) (1, 3) 
#               (2, 2) 
#        (3, 1) (3, 2) (3, 3) 
# (4, 0) (4, 1) (4, 2) (4, 3) (4, 4) 

result = 0 

start = 0 
end = N 

for i in range(N): 
    result += sum( xx[i][start:end] ) 

    if i < N//2: 
        start += 1 
        end -= 1 
    
    else: 
        start -= 1 
        end += 1 

print(result) 