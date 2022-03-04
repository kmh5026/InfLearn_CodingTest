
# 후위표기식 연산 *** 후위표기법 이해하면 쉬움 

import sys 
sys.stdin = open('/Users/kimmh/Desktop/Algorithm/Sec5/4. 후위식 연산/in5.txt', 'rt') 

#--------------------------------------------------------------------------------# 
# 1. 후위표기식 입력 > 연산 결과 출력 
# 2. 중위표기식 : 연산자가 피연산자 사이에 존재 (3 + 5) 
# 3. 후위표기식 : 연산자가 피연산자 뒤에 있는 표기식 (3 5 +) 
#
# ex1) 3 5 2 + * 9 -  ==  21 
# 
# 입력) 중위표기식 (길이 100 이하) 
# 출력) 후위표기식 
#--------------------------------------------------------------------------------# 

# 숫자 2개 나오면 바로 뒤의 연산 수행 
# 3 5 2 * 7 2 - / +  ==  3 10 5 / +  ==  3 2 +  ==  5 

# 후위표기와 스택: 연산자의 우선순위에 따라 스택에 연산자를 push/pop한다. 


# ex1) 3 5 2 * 7 2 - / + 

# 3 : stack에 push      stack = [3] 
# 5 : stack에 push      stack = [3, 5] 
# 2 : stack에 push      stack = [3, 5, 2] 
# * : stack 마지막 2개 pop하여 연산 후 stack에 push     stack = [3, 10] 
# 7 : stack에 push      stack = [3, 10, 7] 
# 2 : stack에 push      stack = [3, 10, 7, 2] 
# - : stack 마지막 2개 pop하여 연산 후 stack에 push     stack = [3, 10, 5] 
# / : stack 마지막 2개 pop하여 연산 후 stack에 push     stack = [3, 2]   (나눗셈 순서 유의) 
# + : stack 마지막 2개 pop하여 연산 후 stack에 push     stack = [5] 

post_fix = input() 

stack = [] 

for i in post_fix: 

    if i.isdecimal(): 
        stack.append(int(i)) 

    else: 
        if i == '+': 
            n2 = stack.pop() 
            n1 = stack.pop() 

            stack.append(n1 + n2) 
        
        elif i == '-': 
            n2 = stack.pop() 
            n1 = stack.pop() 

            stack.append(n1 - n2) 
        
        elif i == '*': 
            n2 = stack.pop() 
            n1 = stack.pop() 

            stack.append(n1 * n2) 
        
        elif i == '/': 
            n2 = stack.pop() 
            n1 = stack.pop() 

            stack.append(n1 / n2) 

print(stack[0]) 
