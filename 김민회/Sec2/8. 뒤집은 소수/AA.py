
# 뒤집은 소수 

import sys 
sys.stdin = open('/Users/kimmh/Desktop/Algorithm/Sec2/8.뒤집은 소수/in5.txt', 'rt')

#--------------------------------------------------------------------------------# 
# 1. N개의 자연수 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수일 경우 그것을 출력 (뒤집은 수)
# 2. def reverse(x) 
# 3. def isPrime(x) 
# 4. N : 3 이상 100 이하 
# 5. 각 자연수는 100,000 이하 
# 
# ex) 32 > 23 == 소수 > 출력 
#     910 > 19 == 소수 > 출력 (첫자리 0은 무시) 즉, 10으로 나눠 나머지 0인 경우 
#--------------------------------------------------------------------------------# 

N = int(input())

num = list(map(int, input().split())) 


# *** Slicing 
#     [ start : stop : step ] 을 의미 (디폴트로 step = 1) 

def reverse(x): 
    x = str(x)         # 문자열로 
    x = x.rstrip('0')  # 우측의 '0'들 다 제거 
    x = x[::-1]        # slicing 이용하여 순서 뒤집기 
    x = int(x)         # 다시 정수형으로 
    return x 

def isPrime(x): 
    if x == 1:
        return False 

    for i in range(2, x):
        if x % i == 0:
            return False 

    return True 

for i in num:
    res = reverse(i)
    if isPrime(res): 
        print(res, end=' ') 


