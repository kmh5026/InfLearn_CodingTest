
# 침몰하는 타이타닉 (그리디) ***** 

import sys 
sys.stdin = open('/Users/kimmh/Desktop/Algorithm/Sec4/8. 침몰하는 타이타닉/in5.txt', 'rt') 

#--------------------------------------------------------------------------------# 
# 1. 타이타닉에는 N명의 승객 
# 2. 구명보트 : 2명 이하 & M kg 이하 
# 3. 승객 모두가 탈출하기 위해 필요한 구명보트 수 출력하는 프로그램 
# 
# 
# 입력1) N, M (5 이상 1000 이하) (70 이상 250 이하) 
# 입력2) N명의 몸무게 (공백) (50 이상 150 이하)         몸무게가 M을 넘진 않음 (탈출 못하는 경우 X) 
# 출력) 구명보트의 최소 개수 
#--------------------------------------------------------------------------------# 

# ex) 
# 5 140 
# 90 50 70 100 60 

N, M = map(int, input().split()) 

weight = list(map(int, input().split())) 

weight.sort() 
# 50 60 70 90 100 

cnt = 0 

while weight:              # 왜 while True로 하면 에러뜰까...? 
    if len(weight) == 1: 
        cnt += 1 
        break 

    if weight[0] + weight[-1] > M: 
        weight.pop() 
        cnt += 1
    
    else: 
        weight.pop(0) 
        weight.pop() 
        cnt += 1 

print(cnt) 


### 소스코드 : deque 자료구조 활용 >>> from collections import deque 
# deque.append(item): item을 데크의 오른쪽 끝에 삽입한다.
# deque.appendleft(item): item을 데크의 왼쪽 끝에 삽입한다.
# deque.pop(): 데크의 오른쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
# deque.popleft(): 데크의 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
# deque.extend(array): 주어진 배열(array)을 순환하면서 데크의 오른쪽에 추가한다.
# deque.extendleft(array): 주어진 배열(array)을 순환하면서 데크의 왼쪽에 추가한다.
# deque.remove(item): item을 데크에서 찾아 삭제한다.
# deque.rotate(num): 데크를 num만큼 회전한다(양수면 오른쪽, 음수면 왼쪽).

'''
from collections import deque 
N, M = map(int, input().split())
weight = list(map(int, input().split())) 
weight.sort()
weight = deque(weight) 
cnt = 0
while weight:
    if len(weight) == 1:
        cnt += 1
        break
    if weight[0] + weight[-1] > M: 
        weight.pop() 
        cnt += 1 
    else: 
        weight.popleft() 
        weight.pop() 
        cnt += 1 

print(cnt)
'''
