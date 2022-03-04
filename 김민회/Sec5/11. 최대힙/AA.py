
# 최대힙 *** 

import sys 
sys.stdin = open('/Users/kimmh/Desktop/Algorithm/Sec5/11. 최대힙/in5.txt', 'rt') 

#--------------------------------------------------------------------------------# 
# 1. 최대힙 자료를 이용하여 다음과 같은 연산을 하는 프로그램 작성  
# 2. 자연수가 입력되면 최대힙에 입력 
# 3. 0이 입력되면 최대힙에서 최대값을 꺼내 출력 (출력할 자료 없으면 -1 출력) 
# 4. -1 입력되면 프로그램 종료 
# 
# 입력) 각 줄에 걸쳐 숫자가 입력됨 (100,000개 이하) 
# 출력) 연산 결과 
#--------------------------------------------------------------------------------# 

import heapq 

heap = [] 

while True: 
    num = int(input()) 

    if num > 0: 
        heapq.heappush( heap, (-num, num) )     # (우선순위, 값) 
    
    elif num == 0: 
        if len(heap) == 0: 
            print(-1) 
        else: 
            print( heapq.heappop( heap )[1] )   # index 1 
    
    elif num == -1: 
        break 
