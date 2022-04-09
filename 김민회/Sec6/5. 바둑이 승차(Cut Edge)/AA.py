
# 바둑이 승차 (DFS) (Cut Edge Tech.) ******* 
'''강의에 시간 줄이는 법 나옴 (Cut Edge)''' 

import sys 
sys.stdin = open('/Users/kimmh/Desktop/Algorithm/Sec6/5. 바둑이 승차/in5.txt', 'rt') 

#--------------------------------------------------------------------------------# 
# 1. 바둑이들 트럭에 태우려 함, 트럭은 C키로 넘게 태울 수 없다 
# 2. C를 넘지 않으면서 가장 무겁게 태우고자 
# 3. N마리 바둑이와 각 바둑이의 무게 W > 가장 무거운 무게를 출력 
# 
# 입력1) C (1 이상 1억 이하), N (1 이상 30 이하) 
# 입력2) 각 줄에 N마리의 무게 
# 출력) 가장 무거운 무게 
#--------------------------------------------------------------------------------# 

# 그냥 4번과 똑같이 하면 in4, in5에서 시간초과 뜸 
# 모든 가지를 다 끝까지 봐야하기 때문 ! 

# 그렇다면 내려가다가 중간에 끊을 순 없을까 ? 

# 지금 레벨까지의 sum에 밑에 레벨 모두 다 태워도 result 갱신 불가하다면, 함수 종료 !!! 

# tsum : 지금 레벨까지 총합 
# total - tsum : 남은 레벨들의 총합 
# if (total - tsum) + sum < result : 
#     return 


def DFS(L, sum, tsum):        # L : 인덱스 번호 / sum : 누적합 / tsum : 지금 레벨까지 총합 
    global result 

    if (total - tsum) + sum < result: 
        return 

    if sum > C: 
        return 

    if L == N: 
        if sum > result: 
            result = sum 
        
    else: 
        DFS(L+1, sum + weight[L], tsum + weight[L]) 
        DFS(L+1, sum, tsum + weight[L]) 

if __name__ == '__main__': 
    C, N = map(int, input().split()) 
    result = -1 
    total = 0 

    weight = [0] * N 
    for i in range(N): 
        weight[i] = int(input()) 
        total += weight[i] 

    DFS(0, 0, 0) 
    print(result) 