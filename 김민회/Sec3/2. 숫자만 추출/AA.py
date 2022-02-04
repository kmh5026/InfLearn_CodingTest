
# 숫자만 추출 

import sys 
sys.stdin = open('/Users/kimmh/Desktop/Algorithm/Sec3/2. 숫자만 추출/in5.txt', 'rt')

#--------------------------------------------------------------------------------# 
# 1. 문자와 숫자가 섞인 문자열 입력 
# 2. 숫자만 추출하여 순서대로 자연수를 만들고 출력  (100,000,000 이하) 
# 3. 다음 줄에는 그 자연수의 약수의 개수 출력 
# 
# ex) 입력: t0e0a1c2h0er 
#     출력1: 120 
#     출력2: 120의 약수 개수 
#--------------------------------------------------------------------------------# 

string = input()

num = '' 
for i in string: 
    if i.isdigit():
        num += i 

num.lstrip('0') 
num = int(num) 

print(num) 

cnt = 0 
for i in range(1, num + 1): 
    if num % i == 0: 
        cnt += 1 

print(cnt) 


    

