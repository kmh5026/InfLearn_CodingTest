
# 교육과정 설계 (큐) ***** (경우의 수 생각 잘 해야 함) 

import sys 
sys.stdin = open('/Users/kimmh/Desktop/Algorithm/Sec5/7. 교육과정 설계/in5.txt', 'rt') 

#--------------------------------------------------------------------------------# 
# 1. 1년 과정의 수업계획 작성 
# 2. 필수과목 : 반드시 이수해야 하며 순서도 정해져 있음 
# 3. 수업계획은 순서대로 앞에 수업이 이수되면 다음 수업을 시작하는 것으로 해석 
# 4. 같은 과목을 여러번 이수해도 됨 
# 5. 수업설계가 옳은 경우 'YES', 잘못된 경우 'NO' 출력 
# 
# 입력1) 필수과목의 순서 
# 입력2) N (1 이상 10 이하) 
# 입력3) N개의 수업설계 (각 줄마다) (길이 30 이하) 
# 출력) 'YES' / 'NO' 
#--------------------------------------------------------------------------------# 

# FIFO : First in First out 

# ex1-2) 
# CBA  :  FGCDAB  >> 'NO' 
# F : not in must 
# G : not in must 
# C : == must.popleft() 
# D : not in must 
# A : != must.popleft()  >>> break and print('NO') 

# ex2) 
# AFC  :  AFFDCCFF  >> 'YES' 
# A : == must.popleft() 
# F : == must.popleft() 
# F : not in must 
# D : not in must 
# C : == must.popleft() 
# len(must) == 0 >>> print('YES') 

from collections import deque 

must = input()

N = int(input()) 

for i in range(N): 

    plan = input() 
    must_tmp = deque(must) 

    for lecture in plan: 
        if lecture in must_tmp: 

            # 필수과목 순서가 틀린 경우 
            if lecture != must_tmp.popleft(): 
                print('#%d NO' % (i+1)) 
                break 
                
            # else:  필수과목 순서가 올바른 경우 
            # 아무것도 안함 (popleft 했으므로) 

            # 필수과목 모두 순서대로 이수한 경우 
            if len(must_tmp) == 0: 
                print('#%d YES' % (i+1)) 
                break 
    
    # 필수과목 순서가 맞았지만, 
    else: 
        # 이수하지 않은 필수과목 존재 
        if len(must_tmp) != 0: 
            print('#%d NO' % (i+1)) 
