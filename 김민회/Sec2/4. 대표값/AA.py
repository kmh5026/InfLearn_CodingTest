
# 대표값 

import sys 
sys.stdin = open('/Users/kimmh/Desktop/Algorithm/Sec2/4.대표값/in4.txt', 'rt')

#--------------------------------------------------------------------------------# 
# 1. N명의 수학 점수 
# 2. N명의 평균을 출력하고, (소수 첫째자리에서 반올림) 
# 3. 평균에 가장 가까운 학생은 몇번째 학생인지 출력 
# 4. 평균과 가장 가까운 점수가 여러개일 경우 (거리가 같은 경우), 높은 점수의 학생 번호 출력  (=내림차순) 
# 5.    높은 점수의 학생도 여러명일 경우, 빠른 번호의 학생 번호 출력  (=오름차순) 
#--------------------------------------------------------------------------------# 

N = int(input())

score = list(map(int, input().split()))

avg = round(sum(score)/len(score))                    # 평균 점수 첫째자리에서 반올림 

dist = [ abs(x-y) for x,y in zip(score, [avg]*N) ]    # 평균과의 차이 리스트 

minimum = min(dist)         # 차이 최소값 

cand = []  # 후보군 리스트 

for idx, val in enumerate(dist): 
    if val == minimum: 
        cand.append(idx) 

high = 0
for i in cand:
    if score[i] > high: 
        high = score[i] 
        result = i+1 

print(avg, result) 










