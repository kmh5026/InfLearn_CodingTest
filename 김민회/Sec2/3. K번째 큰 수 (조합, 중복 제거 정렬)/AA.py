
# K번째 큰 수 

import sys 
sys.stdin = open('/Users/kimmh/Desktop/Algorithm/Sec2/3.k번째 큰 수/in5.txt', 'rt')

#--------------------------------------------------------------------------------# 
# 1. 1부터 100 사이 자연수 적힌 N장의 카드 (숫자 중복 가능) 
# 2. 이 중 3장을 뽑아 합을 기록 (모든 경우의 수에 대해) 
# 3. 기록된 값들 중 K번째로 큰 수 출력 (내림차순) 
# 
# ex) 25 25 23 21 21 18 ... 에서 K=4이면 18 출력 
#--------------------------------------------------------------------------------#


N, K = map(int, input().split())   # N과 K 입력 

card = list(map(int, input().split()))  # N장의 카드 입력 

comb = []   # 빈 조합 리스트 생성 


'''
*** 1차 시도 *** 

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            comb.append(card[i] + card[j] + card[k])
# 가능한 모든 조합 생성 

comb.sort(reverse=True)  # 조합 내림차순 정렬 

print(comb[K-1])         # K번째로 큰 수 출력 

   - 문제점: 내림차순 정렬할 때 중복 제거 안 됨 
   - 해결책: list를 다시 set으로 만들거나, (https://blockdmask.tistory.com/543) 
           for문 이용 (not in 구문으로 새 리스트에 append) 
           => 값 순서가 중요한 경우 for문 이용 
'''

#--------------------------------------------------------------------------------# 

### 해결책 1 ### 

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            comb.append(card[i] + card[j] + card[k]) 
# 가능한 모든 조합 생성 
# 내가 작성한 for문은 조합 생성 단계에 있어서는 중복이 없으나, 소스코드의 for문은 조합 생성할 때도 중복적으로 조합함 

comb = list(set(comb))   # 중복 제거 (자동으로 오름차순 정렬) 
comb.sort(reverse=True)  # 조합 내림차순 정렬 

print(comb[K-1])         # K번째로 큰 수 출력 



#--------------------------------------------------------------------------------# 

'''
# 해결책 2 # 
comb = []   # 빈 조합 리스트 생성 

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            comb.append(card[i] + card[j] + card[k])
# 가능한 모든 조합 생성 

res = [] 
for i in comb:
    if i not in res:
        res.append(i)

res.sort(reverse=True)  # 조합 내림차순 정렬 

print(res[K-1])         # K번째로 큰 수 출력 
'''
