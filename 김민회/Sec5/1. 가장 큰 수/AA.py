
# 가장 큰 수 (스택) *** 

import sys 
sys.stdin = open('/Users/kimmh/Desktop/Algorithm/Sec5/1. 가장 큰 수/in5.txt', 'rt') 

#--------------------------------------------------------------------------------# 
# 1. 주어진 숫자의 자릿수들 중 m개의 숫자를 제거하여 가장 큰 수를 만들고자 
# 2. 숫자의 순서는 유지  
# ex) 5276823 3 >> 7823 
# 
# 입력) 숫자와 제거해야 할 자릿수 (m) 
# 출력) 가장 큰 수 
#--------------------------------------------------------------------------------# 

N, m = map(int, input().split()) 

num = list(map(int, str(N))) 

# print(num, m) 

stack = [] 


# 자릿수 순서대로 비교해가며 stack에 추가 
# 큰 수가 등장할 경우 last in 요소들 pop 

for i in num: 
    # 숫자 제거 가능하다면 다 제거 
    # while stack은 필요한가? >> YES (반복문 시작할 때) 
    while stack and m > 0 and stack[-1] < i:
        stack.pop() 
        m -= 1 
    stack.append(i) 

# 다 지우지 못한 경우 (m이 0이 아님) 
if m != 0: 
    stack = stack[ : -m] 

for i in stack: 
    print(i, end='') 


'''
'구분자'.join( 리스트 ) : 문자열 합치기 

result = ''.join( map(str, stack) ) 
print(result) 
'''
