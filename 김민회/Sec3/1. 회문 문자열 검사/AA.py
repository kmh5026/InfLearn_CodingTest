
# 회문 문자열 검사 

import sys 
sys.stdin = open('/Users/kimmh/Desktop/Algorithm/Sec3/1. 회문 문자열 검사/in5.txt', 'rt')

#--------------------------------------------------------------------------------# 
# 1. N개의 문자열 입력 
# 2. 각 문자열에 대해 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우 YES를 출력, 아니면 NO를 출력 
# 3. 회문 검사 시 대소문자 구분 X 
# 
# ex) level > YES 
#     moon  > NO 
#     gooG  > YES 
# 
# 입력 1) N (1이상 20이하)
# 입력 2) N개의 단어 (줄바꿈하여) (100자 이하)  
#--------------------------------------------------------------------------------# 

N = int(input()) 

for i in range(N):
    string = input() 
    string = string.lower() 
    if string == string[::-1]:
        print('#{} YES'.format(i+1))
    else: 
        print('#{} NO'.format(i+1)) 
