
# 최소힙 (힙 개념문제) 

import sys 
sys.stdin = open('/Users/kimmh/Desktop/Algorithm/Sec5/10. 최소힙/in5.txt', 'rt') 

#--------------------------------------------------------------------------------# 
# 1. 최소힙 자료를 이용하여 다음과 같은 연산을 하는 프로그램 작성  
# 2. 자연수가 입력되면 최소힙에 입력 
# 3. 0이 입력되면 최소힙에서 최소값을 꺼내 출력 (출력할 자료 없으면 -1 출력) 
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
        heapq.heappush( heap, num ) 
    
    elif num == 0: 
        if len(heap) == 0: 
            print(-1) 
        else: 
            print(heapq.heappop( heap )) 
    
    elif num == -1: 
        break 
