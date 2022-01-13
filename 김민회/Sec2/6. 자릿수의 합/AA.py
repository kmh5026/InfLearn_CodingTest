
# 자릿수의 합 

import sys 
sys.stdin = open('/Users/kimmh/Desktop/Algorithm/Sec2/6.자릿수의 합/in5.txt', 'rt')

#--------------------------------------------------------------------------------# 
# 1. def digit_sum(x)  
# 2. N개의 자연수 입력되면 각 자연수의 자릿수의 합 구하고, 
# 3. 그 자릿수 합이 최대인 자연수를 출력 
# 4. 자릿수 합 최대가 같을 경우 먼저 입력된 수를 출력 
#--------------------------------------------------------------------------------# 

N = int(input())

num = list(map(int, input().split())) 

# ex) 297 
# 2 + 9 + 7 = 18 
# 7 : 297을 10으로 나눈 나머지 
# 9 : 29를 10으로 나눈 나머지   (29 = 297을 10으로 나눈 몫)
# 2 : 2를 10으로 나눈 나머지    (2 = 29를 10으로 나눈 몫)     >>>  while문 활용 가능 


def digit_sum(x): 
    x = str(x) 
    sum_ = 0 
    for i in range(len(x)):
        sum_ += int(x[i])
    return sum_ 

max_ = 0 

for i in num:
    dg_sum = digit_sum(i)
    if dg_sum > max_:
        max_ = dg_sum 
        result = i 

print(result) 


