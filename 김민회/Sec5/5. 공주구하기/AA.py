
# 공주구하기 (큐) *** (큐의 기본개념 문제) 

import sys 
sys.stdin = open('/Users/kimmh/Desktop/Algorithm/Sec5/5. 공주구하기/in5.txt', 'rt') 

#--------------------------------------------------------------------------------# 
# 1. 공주를 구하러 갈 왕자 선정 
# 2. 왕자들 나이순으로 1 ~ N번까지 번호 
# 3. 시계방향으로 동그랗게 앉음 
# 4. K를 외치게 되는 왕자 제외하고 원 밖으로 나옴 
# 5. 다음 왕자부터 다시 1부터 시작, K 외치면 제외 
#
# ex1) N=8, K=3 
#      1, 2, 3 > 3번 제외  > 1, 2 뒤에 붙임 [4 5 6 7 8 1 2]
#      4, 5, 6 > 6번 제외  > 4, 5 뒤에 붙임 [7 8 1 2 4 5]
#      7, 8, 1 > 1번 제외  > 7, 8 뒤에 붙임 [2 4 5 7 8] 
#      2, 4, 5 > 5번 제외  > 2, 4 뒤에 붙임 [7 8 2 4] 
#      7, 8, 2 > 2번 제외  > 7, 8 뒤에 붙임 [4 7 8] 
#      4, 7, 8 > 8번 제외  > 4, 7 뒤에 붙임 [4 7] 
#      4, 7, 4 > 4번 제외  > 7 뒤에 붙임 
#      len( ) == 1 >> print 
# 
# 입력) N, K  (N은 5 이상 1000 이하) (K는 2 이상 9 이하) 
# 출력) 마지막 남은 왕자의 번호 
#--------------------------------------------------------------------------------# 

# FIFO : First in First out 

# K - 1 번은 popleft 하여 뒤로 append 
# 마지막 K번째는 그냥 popleft 

from collections import deque  # Double Ended Queue 

N, K = map(int, input().split()) 

que = list(range(1, N+1)) 

que = deque(que) 


while que: 

    for _ in range(K-1): 
        tmp = que.popleft() 
        que.append(tmp) 
    
    que.popleft() 

    if len(que) == 1: 
        print( que[0] ) 
        break 
