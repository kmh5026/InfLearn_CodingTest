
# 응급실 (큐) **** 

import sys 
sys.stdin = open('/Users/kimmh/Desktop/Algorithm/Sec5/6. 응급실/in1.txt', 'rt') 

#--------------------------------------------------------------------------------# 
# 1. 응급실은 환자가 도착한 순서대로 진료 / 위험도 높은 환자는 빨리 응급조치 
# 2. 접수 순서대로의 환자 목록 (N) 중에서 제일 앞에 있는 차트 꺼냄 
# 3. 나머지 환자 중 위험도가 더 높은 환자가 존재하면 맨 뒤로 다시 넣음 
# 4. 그렇지 않은 경우 진료 
# 5. 대기목록 상 M번째 환자는 몇번째로 진료 받는지 출력  (M은 0부터 N-1) 
# 
# 입력1) N, M  (N은 5 이상 100 이하) (M은 0 이상 N 미만) 
# 입력2) N명의 위험도  (50 이상 100 이하) (같은 값 존재 가능) 
# 출력) M번째 환자의 진료 순서 
#--------------------------------------------------------------------------------# 

# FIFO : First in First out 

from collections import deque 

# ex1) 70 
# 60 50 70 80 90  
# 50 70 80 90 60 
# 70 80 90 60 50 
# 80 90 60 50 70 
# 90 60 50 70 80   90 진료 (popleft) 
# 60 50 70 80 
# 50 70 80 60 
# 70 80 60 50 
# 80 60 50 70      80 진료 
# 60 50 70 
# 50 70 60 
# 70 60 50         70 진료  >>> 3번째로 진료받음 

# if tmp < max(que) : 틀린 건 아니지만 연산이 무조건 N번 돌아감 
# if any (tmp < q for q in Q) : 연산이 N 이하 

# ex2) 60_0 
# 60_0 60_1 90 60_2 60_3 60_4   >> 2번 popleft하여 append 
# 90 60_2 60_3 60_4 60_0 60_1   >>  90 진료 (popleft) (+ count) 
# 60_2 60_3 60_4 60_0 60_1      >>> 5번째로 진료받음 


##### 같은 위험도 존재할 수 있기 때문에 인덱스도 같이 저장해야 함 (큐 요소를 튜플로)   (idx, val) in enumerate( ) 

N, M = map(int, input().split()) 

danger = list( map(int, input().split()) ) 

que = [ (idx, val) for idx, val in enumerate(danger) ] 

que = deque(que) 

order = 0 


while True: 

    tmp = que.popleft()     # First out 

    if any (tmp[1] < q[1] for q in que): 
        que.append(tmp) 
    
    else:                   # 진료 
        order += 1 

        if tmp[0] == M:     # 처음 목록에서 M번째 환자라면 
            print(order)      # 몇번째로 진료받는지 출력 
            break 

