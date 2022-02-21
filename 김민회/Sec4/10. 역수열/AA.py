
# 역수열 (그리디) ******* 개어렵네 ㅅㅂ 

import sys 
sys.stdin = open('/Users/kimmh/Desktop/Algorithm/Sec4/10. 역수열/in5.txt', 'rt') 

#--------------------------------------------------------------------------------# 
# 1. 1 ~ N 까지의 자연수로 된 수열 (순서 랜덤) 
# 2. 1 ~ N 각각의 수 앞에 놓여있는 수들 중 자신보다 큰 수의 개수를 수열로 : 역수열 
# 3. 역수열이 주어졌을 때 원래의 수열을 출력하는 프로그램 작성 
# 
# 입력1) N (3 이상 100 이하) 
# 입력2) 역수열 
# 출력) 원래 수열 
#--------------------------------------------------------------------------------# 

N = int(input()) 

rev = list(map(int, input().split())) 

# ex) 
# 8 
# 5 3 4 0 2 1 1 0 
# 
# 4 8 6 2 5 1 3 7 

### 소스코드 

original = [0] * N      # 원래 수열 

for i in range(N):      # 주어진 역수열에 대해 

    for j in range(N):  # 원래 수열의 어디에 배치되어야 하는가 
        
        if rev[i] == 0 and original[j] == 0: 
            original[j] = i+1 
            break 
        
        elif original[j] == 0: 
            rev[i] -= 1 

for i in original: 
    print(i, end=' ') 
