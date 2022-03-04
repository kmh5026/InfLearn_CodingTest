
# 후위표기식 만들기 ******* 후위표기법 자체가 헷갈림 + 문제도 개어려움 (사칙연산 우선순위 이용) 

import sys 
sys.stdin = open('/Users/kimmh/Desktop/Algorithm/Sec5/3. 후위표기식 만들기/in5.txt', 'rt') 

#--------------------------------------------------------------------------------# 
# 1. 중위표기식 입력 > 후위표기식으로 변환 
# 2. 중위표기식 : 연산자가 피연산자 사이에 존재 (3 + 5) 
# 3. 후위표기식 : 연산자가 피연산자 뒤에 있는 표기식 (3 5 +) 
#
# ex1) 3 + 5 * 2    =  3 5 2 * + 
# ex2) (3 + 5) * 2  =  3 5 + 2 * 
# ex3) 3 + 5 * 2 / (7 - 2) =  3 5 2 * 7 2 - / + 
# ex4) 3 * (5 + 2) - 9     =  3 5 2 + * 9 - 
# 
# 입력) 중위표기식 (길이 100 이하) 
# 출력) 후위표기식 
#--------------------------------------------------------------------------------# 

# 괄호가 필요없음 
# 인간과 달리 컴퓨터는 내부에서 원래 스택을 활용해 중위표기법을 후위표기법으로 반환하여 연산을 한다고 한다. 
# 이 과정에서 괄호표기가 없는 후위표기법을 이용하는것이 중위표기법 보다 속도가 빠르다고 한다. 
#  ( https://velog.io/@jin0106/Python-%ED%9B%84%EC%9C%84%ED%91%9C%EA%B8%B0%EB%B2%95-%EB%B0%8F-%EA%B3%84%EC%82%B0%EB%B2%95 ) 


# 숫자 2개 나오면 바로 뒤의 연산 수행 
# 3 5 2 * 7 2 - / +  ==  3 10 5 / +  ==  3 2 +  ==  5 

# 후위표기와 스택: 연산자의 우선순위에 따라 스택에 연산자를 push/pop한다. 

# ( : 나오면 바로 스택에 push한다.
# ) : 우선순위가 가장 높은 괄호연산자가 끝난다는 뜻이므로, 괄호 안에 남아있는 연산자를 전부 pop하고 ( 도 pop해줌. ) 는 처음부터 스택에 넣지 않는다.
# * / : 스택에 * / 가 있다면 그것들을 먼저 없어질 때까지 pop해주고 끝나면 push한다. (+, -은 우선순위가 낮으므로 pop안함) 
# + - : 스택에 다른 사칙연산자가 있다면 그것들을 먼저 없어질 때까지 (괄호연산자 직전가지)pop해주고 끝나면 push한다. 


### ex3) 3 + 5 * 2 / (7 - 2)  =  3 5 2 * 7 2 - / + 

# 3 : result에 붙임 
# + : stack에 push                          result = '3' ,  stack = [+] 
# 5 : result에 붙임                          result = '35' ,  stack = [+] 
# * : stack에 push                          result = '35' ,  stack = [+, *] 
# 2 : result에 붙임                          result = '352' ,  stack = [+, *] 
# / : 일단 stack의 마지막이 * / 인지 확인 
#     * 이므로 pop하여 result에 붙임            result = '352*' ,  stack = [+, /] 
# ( : stack에 push                          result = '352*' ,  stack = [+, /, (] 
# 7 : result에 붙임                          result = '352*7' ,  stack = [+, /, (] 
# - : stack에 push                          result = '352*7' ,  stack = [+, /, (, -] 
# 2 : result에 붙임                          result = '352*72' ,  stack = [+, /, (, -] 
# ) : ( 아니라면 계속 stack에서 pop하여 result에 붙임 
#     반복문 종료하고 ( 도 pop                  result = '352*72-' ,  stack = [+, /] 

# stack 빌 때까지 stack에서 pop하여 result에 붙임 



### ex4) 3 * (5 + 2) - 9  =  3 5 2 + * 9 - 

# 3 : result에 붙임 
# * : stack에 push                          result = '3' ,  stack = [*] 
# ( : stack에 push                          result = '3' ,  stack = [*, (] 
# 5 : result에 붙임                          result = '35' ,  stack = [*, (] 
# + : stack에 push                          result = '35' ,  stack = [*, (, +] 
# 2 : result에 붙임                          result = '352' ,  stack = [*, (, +] 
# ) : ( 아니라면 계속 stack에서 pop하여 result에 붙임  
#     반복문 종료하고 ( 도 pop                  result = '352+' ,  stack = [*] 
# - : ( 아니라면 계속 stack에서 pop하여 result에 붙임  
#     반복문 종료하고 stack에 push              result = '352+*' ,  stack = [-] 
# 9 : result에 붙임                          result = '352+*9' ,  stack = [-] 

# stack 빌 때까지 stack에서 pop하여 result에 붙임 


infix = input() 

result = '' 

stack = [] 

for i in infix: 

    if i.isdecimal(): 
        result += i 
    
    else: 

        if i == '(': 
            stack.append(i) 
        
        elif i == ')': 
            while stack and stack[-1] != '(': 
                result += stack.pop() 
            stack.pop() 
        
        elif i == '*' or i == '/': 
            while stack and (stack[-1]=='*' or stack[-1]=='/'): 
                result += stack.pop() 
            stack.append(i) 
        
        elif i == '+' or i == '-': 
            while stack and stack[-1] != '(': 
                result += stack.pop() 
            stack.append(i) 

while stack: 
    result += stack.pop() 

print(result) 

