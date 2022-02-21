
# 증가수열 만들기 (그리디) ***** 

import sys 
sys.stdin = open('/Users/kimmh/Desktop/Algorithm/Sec4/9. 증가수열 만들기/in1.txt', 'rt') 

#--------------------------------------------------------------------------------# 
# 1. 1 ~ N 까지의 자연수로 된 수열 (순서 랜덤) 
# 2. 양 끝 숫자 중 하나를 가져와 나열하여 가장 긴 증가수열을 만듦 
# 3. 최대 증가수열의 길이 / 가져온 방향을 순서대로 나열 (L/R)
# 
# 입력1) N (3 이상 100 이하) 
# 입력2) 길이 N인 수열 
# 출력1) 최대 증가수열의 길이 
# 출력2) 가져온 방향 문자열 (단, 마지막에 남은 값은 왼쪽으로 생각함) 
#--------------------------------------------------------------------------------# 

N = int(input()) 

num = list(map(int, input().split())) 

last_num = 0 
direction = '' 

# 좌한이 우한 이하일 때까지 반복, 추가 안되는 경우 break 
# 한 쪽만 뽑힌 경우 > last_num에 저장 / direction 저장 
# 양 쪽 다 뽑힌 경우 > 정렬 후 last_num에 저장 / direction 저장 

# 4, ... 3, 2
# (2, R) >> 저장 
# (4, L) 

while num: 

    tmp = []                            # 증가수열 후보 리스트 

    if num[0] > last_num:               # 좌측 후보 
        tmp.append( (num[0], 'L') ) 
    if num[-1] > last_num:              # 우측 후보 
        tmp.append( (num[-1], 'R') ) 

    if len(tmp) == 0:                   # 후보가 0개일 때 break (증가수열 만들 수 없을 때) 
        break 

    tmp.sort()                          # 오름차순 정렬 (최종 후보 결정을 위해) 


    if tmp[0][1] == 'L':                # 좌측이 더 작다면, 
        last_num = num.pop(0)           # 좌측 값을 수열에 추가 
        direction += 'L'                # 방향 추가 
    
    else:                               # 우측이 더 작다면, 
        last_num = num.pop()            # 우측 값을 수열에 추가 
        direction += 'R'                # 방향 추가 

print(len(direction)) 
print(direction) 


### 소스코드 

# 좌한 / 우한 개념 (이분탐색에서처럼) 
'''
N = int(input())
num = list(map(int, input().split())) 

lt = 0
rt = N-1 

last = 0 
res = '' 

tmp = [] 

while lt <= rt: 

    if num[lt] > last: 
        tmp.append( (num[lt], 'L') ) 
    if num[rt] > last: 
        tmp.append( (num[rt], 'R') ) 

    tmp.sort() 

    if len(tmp) == 0: 
        break 

    else: 
        res += tmp[0][1] 
        last = tmp[0][0] 
        if tmp[0][1] == 'L':
            lt += 1
        else: 
            rt -= 1 

    tmp.clear() 


print(len(res))
print(res)
'''